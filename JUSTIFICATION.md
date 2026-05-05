# JUSTIFICATION — Uzasadnienia decyzji projektowych

## J1. Dlaczego `Animal` jest klasą abstrakcyjną?

Klasa `Animal` jest abstrakcyjna (dziedziczy po `ABC`), ponieważ nie ma sensu tworzyć „ogólnego zwierzęcia" bez konkretnego gatunku. Metody `make_sound()` i `diet()` muszą być zaimplementowane przez każdy konkretny gatunek — `@abstractmethod` wymusza tę implementację na poziomie języka. Bez ABC można by przypadkowo pominąć te metody w podklasie i nie otrzymać błędu do momentu wywołania.

## J2. Jeden `_next_id` współdzielony dla wszystkich podklas `Animal`

Zdecydowaliśmy się na jeden licznik `_next_id` na poziomie klasy `Animal`, a nie osobny licznik per gatunek. Dzięki temu każde zwierzę w systemie ma globalnie unikalny identyfikator, co upraszcza porównania (`__eq__`) i hashowanie (`__hash__`). Minusem jest to, że ID nie są przewidywalne per-gatunek, ale w tym projekcie nie ma takiej potrzeby.

## J3. Dlaczego `health` stosuje clamping zamiast wyjątku?

Specyfikacja jasno definiuje mechanizm jako „clamping (max(0, min(100, value)))". Rzucenie wyjątku dla wartości poza zakresem byłoby niezgodne ze specyfikacją i zmuszałoby kod wywołujący do obsługi wyjątku przy każdej zmianie zdrowia. Clamping jest bezpieczniejszy i bardziej intuicyjny w kontekście symulacji — zdrowie po prostu nie może wyjść poza fizyczne limity.

## J4. Kompozycja `Zoo ◆── Enclosure` vs agregacja `Enclosure ◇── Animal`

- `Zoo` tworzy `Enclosure` przez fabrykę `create_enclosure()` — wybiegi nie mają sensu bez zoo, są zarządzane przez słownik `_enclosures`. To kompozycja.
- `Enclosure` przyjmuje istniejące obiekty `Animal` przez `add_animal()` — zwierzęta mogą istnieć przed przypisaniem do wybiegu i po usunięciu z niego. To agregacja.

Różnica jest ważna dydaktycznie: w kompozycji czas życia obiektu zależnego jest związany z właścicielem; w agregacji — nie.

## J5. Dlaczego `animals` property w `Enclosure` zwraca kopię listy?

```python
return list(self._animals)
```

Zwrócenie referencji do wewnętrznej listy pozwoliłoby zewnętrznemu kodu na modyfikację stanu bez przejścia przez `add_animal()`/`remove_animal()`, co obchodziłoby walidację pojemności. Kopia chroni niezmienność wewnętrznego stanu (zasada enkapsulacji).

## J6. Dlaczego `__eq__` w `Animal` porównuje po `_id`, a nie po nazwie?

Dwie instancje `Lion` o imieniu "Simba" to dwa różne zwierzęta — powinny być różne obiektowo. Porównanie po ID gwarantuje unikalność per-instancja. Porównanie po nazwie prowadziłoby do błędów w kolekcjach (`set`, `dict`) jeśli dwa różne zwierzęta miałyby to samo imię.

## J7. Dlaczego `FeedingEntry` jest `@dataclass`?

Specyfikacja wymaga `@dataclass`. Dataclass automatycznie generuje `__init__`, `__repr__` i `__eq__` na podstawie zadeklarowanych pól, eliminując boilerplate. Jest to idiomatyczny Python dla prostych klas danych bez logiki biznesowej.

## J8. Dlaczego `Zookeeper._assigned_enclosure` jest `Optional[Enclosure]`?

Opiekun może istnieć w systemie zanim zostanie przypisany do wybiegu. `None` jako wartość domyślna sygnalizuje brak przypisania. Metoda `feed_animals()` obsługuje ten przypadek zwracając czytelny komunikat zamiast rzucać wyjątek — jest to bezpieczniejsze w kontekście demo i testów.

## J9. Dlaczego testy są podzielone na pliki wg capability?

Specyfikacja wymaga dokładnie 15 testów — i nadal mamy ich 15. Po refaktoryzacji zostały rozdzielone na cztery pliki odpowiadające obszarom funkcjonalnym (capability):

- `tests/test_animals.py` — 8 testów (hierarchia zwierząt, walidacja, polimorfizm)
- `tests/test_enclosure.py` — 4 testy (zarządzanie wybiegiem, wyjątki pojemności)
- `tests/test_feeding.py` — 1 test (`FeedingSchedule`)
- `tests/test_zoo.py` — 2 testy (`isinstance/issubclass`, raport `Zoo`)

Zalety podziału:
- każdy plik testowy mapuje się na jedną sekcję `openspec/specs/*/spec.md`, co ułatwia audyt pokrycia,
- mniejsze pliki są łatwiejsze do czytania i nawigacji w IDE,
- diff przy modyfikacji jednej grupy testów nie miesza się z innymi.

Liczba testów pozostaje weryfikowalna jednym poleceniem: `grep -rE '^def test_' tests/ | wc -l` zwraca `15`. Fixtures dalej żyją w `tests/conftest.py` i są współdzielone między wszystkimi czterema plikami — pytest wykrywa je automatycznie dzięki konwencji `conftest.py`.

## J10. Struktura modułów — jedna klasa, jeden plik

Import order: `exceptions/ → animals/ → enclosure.py → feeding/ → employees/ → zoo.py`

Pakiet `src/zoo/` jest zorganizowany według zasady **one class per file** — każda klasa publiczna mieszka w osobnym pliku, zgrupowana w sub-pakiecie odpowiadającym jej domenie:

- `exceptions/` — cztery wyjątki, każdy w osobnym pliku (`zoo_error.py`, `enclosure_full_error.py`, `animal_not_found_error.py`, `invalid_animal_data_error.py`).
- `animals/` — bazowa `animal.py`, klasy pośrednie (`mammal.py`, `bird.py`, `reptile.py`) i sześć konkretnych gatunków (`lion.py`, `elephant.py`, `monkey.py`, `eagle.py`, `penguin.py`, `crocodile.py`).
- `feeding/` — `feeding_entry.py` (dataclass) i `feeding_schedule.py` (kompozycja).
- `employees/` — `employee.py` (ABC) plus trzy role w osobnych plikach (`zookeeper.py`, `veterinarian.py`, `guide.py`).
- `enclosure.py` i `zoo.py` pozostają płaskimi modułami — zawierają po jednej klasie, więc opakowanie ich w folder byłoby zbędną ceremonią.

Każdy sub-pakiet posiada własny `__init__.py` re-eksportujący swoje klasy. Główny `src/zoo/__init__.py` re-eksportuje cały publiczny API, więc `from zoo import Lion, Zookeeper, …` działa identycznie jak przed refaktoryzacją.

Dlaczego ten porządek eliminuje cykle:
- `exceptions/` nie zależy od niczego w pakiecie zoo,
- `animals/animal.py` importuje tylko `InvalidAnimalDataError` z `..exceptions`,
- klasy pośrednie i gatunki w `animals/` importują w głąb tego samego sub-pakietu (`from .animal import Animal`, `from .mammal import Mammal`),
- `enclosure.py` importuje `Animal` z `.animals` i wybrane wyjątki,
- `feeding/feeding_schedule.py` importuje `FeedingEntry` z `.feeding_entry`,
- `employees/zookeeper.py` importuje `Enclosure` z `..enclosure`,
- `zoo.py` jest ostatnim ogniwem i importuje ze wszystkich sub-pakietów.
