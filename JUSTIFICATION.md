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

## J9. Dlaczego testy są w jednym pliku `test_zoo.py`?

Specyfikacja wymaga dokładnie 15 testów. Jeden plik ułatwia audyt liczby testów i zapewnia czytelną strukturę. Fixtures współdzielone są przez `conftest.py`, co jest standardową praktyką pytest.

## J10. Struktura modułów — podział na pliki

Import order: `exceptions → animals → enclosure → feeding → employees → zoo`

Ten porządek eliminuje importy cykliczne. `animals.py` nie zależy od żadnego innego modułu zoo. `enclosure.py` importuje tylko `animals` i `exceptions`. `employees.py` importuje `enclosure`. `zoo.py` importuje wszystkie pozostałe.
