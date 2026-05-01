# Zoo Garden — Projekt Semestralny OOP I

System symulacji ogrodu zoologicznego implementujący kluczowe mechanizmy programowania obiektowego w Pythonie.

---

## Opis projektu

Zoo Garden to system zarządzania ogrodem zoologicznym przeznaczony dla pracowników administracji oraz personelu opiekującego się zwierzętami. Użytkownik może zakładać wybiegi o określonej pojemności, dodawać do nich zwierzęta różnych gatunków, zatrudniać pracowników (opiekunów, weterynarzy, przewodników) oraz planować codzienne karmienia. System pilnuje, aby liczba zwierząt nie przekroczyła pojemności wybiegu, sygnalizuje błędy w postaci czytelnych wyjątków oraz potrafi wygenerować zbiorczy raport stanu zoo. Celem systemu jest uporządkowanie pracy operacyjnej w zoo i zmniejszenie ryzyka pomyłek, takich jak pominięcie karmienia czy przepełnienie wybiegu.

---

## Autorzy


| Imię i nazwisko      |
| ----------------------- |
| Mateusz Pietrusiński |
| Jan Fałek            |
| Bartłomiej Stasiak   |

---

## Lista klas z opisami

### Hierarchia zwierząt


| Klasa                        | Opis                                                                                                                       | Najważniejsze atrybuty                                   | Najważniejsze metody                                                                            |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `Animal` (ABC)               | Abstrakcyjna klasa bazowa wszystkich zwierząt. Definiuje wspólne API i niezmienniki (np.`health` w zakresie `[0, 100]`). | `_id`, `_name`, `_species`, `_age`, `_health`, `_next_id` | `make_sound()` (abstrakcyjna), `diet()` (abstrakcyjna), `feed()`, `__eq__`, `__hash__`, `__lt__` |
| `Mammal`                     | Pośrednia klasa dla ssaków, dodaje cechy charakterystyczne dla ssaków.                                                  | `fur_color`                                               | `give_birth()`, domyślne `diet()`                                                               |
| `Bird`                       | Pośrednia klasa dla ptaków, opisuje rozpiętość skrzydeł i zdolność lotu.                                           | `wingspan`, `can_fly`                                     | `fly()`, domyślne `diet()`                                                                      |
| `Reptile`                    | Pośrednia klasa dla gadów, opisuje cechę jadowitości.                                                                  | `is_venomous`                                             | `bask()`, domyślne `diet()`                                                                     |
| `Lion`, `Elephant`, `Monkey` | Konkretne gatunki ssaków (lew, słoń, szympans).                                                                         | np.`mane`, `tusk_length`                                  | nadpisane`make_sound()` i `diet()`                                                               |
| `Eagle`, `Penguin`           | Konkretne gatunki ptaków (orzeł, pingwin — pingwin nie lata).                                                           | dziedziczone                                              | nadpisane`make_sound()`                                                                          |
| `Crocodile`                  | Konkretny gatunek gada (krokodyl nilowy).                                                                                  | `length`                                                  | nadpisane`make_sound()`                                                                          |

### Hierarchia pracowników


| Klasa            | Opis                                                            | Najważniejsze atrybuty               | Najważniejsze metody                            |
| ------------------ | ----------------------------------------------------------------- | --------------------------------------- | -------------------------------------------------- |
| `Employee` (ABC) | Abstrakcyjna klasa bazowa wszystkich pracowników zoo.          | `_id`, `_name`, `_salary`, `_next_id` | `work()` (abstrakcyjna), `role()` (abstrakcyjna) |
| `Zookeeper`      | Opiekun zwierząt przypisany do konkretnego wybiegu.            | `_assigned_enclosure`                 | `assign_to(enclosure)`, `feed_animals()`         |
| `Veterinarian`   | Weterynarz o określonej specjalizacji (`general` / `exotic`).  | `_specialization`                     | `work()`, `role()`                               |
| `Guide`          | Przewodnik prowadzący zwiedzanie w jednym lub kilku językach. | `_languages`                          | `work()`, `role()`                               |

### Wybiegi, zoo i karmienia


| Klasa                         | Opis                                                               | Najważniejsze atrybuty                        | Najważniejsze metody                                                                                                  |
| ------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `Enclosure`                   | Wybieg w zoo, przechowuje zwierzęta i pilnuje pojemności.        | `_name`, `_capacity`, `_animals`               | `add_animal()`, `remove_animal()`, `find_animal()`, `feed_all()`, `__iter__`, `__contains__`, `__len__`                |
| `Zoo`                         | Cały ogród zoologiczny. Tworzy wybiegi i zatrudnia pracowników. | `_name`, `_city`, `_enclosures`, `_employees`  | `create_enclosure()`, `hire_employee()`, `total_animals()`, `find_animal()`, `report()`, `__getitem__`, `__contains__` |
| `FeedingEntry` (`@dataclass`) | Pojedynczy wpis w harmonogramie karmień.                          | `enclosure_name`, `time`, `food_type`, `notes` | (auto-generowane przez`@dataclass`)                                                                                    |
| `FeedingSchedule`             | Harmonogram karmień na dany dzień, agreguje wpisy`FeedingEntry`. | `_day`, `_entries`                             | `add_entry()`, `remove_entry()`, `get_by_enclosure()`, `__len__`                                                       |

### Wyjątki


| Klasa                    | Opis                                                                                      |
| -------------------------- | ------------------------------------------------------------------------------------------- |
| `ZooError`               | Bazowa klasa wyjątków systemu. Pozwala złapać dowolny błąd domenowy jednym`except`. |
| `EnclosureFullError`     | Próba dodania zwierzęcia do wybiegu, który osiągnął pojemność.                    |
| `AnimalNotFoundError`    | Operacja odwołuje się do zwierzęcia, którego nie ma na wybiegu.                       |
| `InvalidAnimalDataError` | Dane zwierzęcia nie przeszły walidacji (np. puste imię).                               |

---

## Hierarchia klas

```
Animal (ABC)
├── Mammal   → Lion, Elephant, Monkey
├── Bird     → Eagle, Penguin
└── Reptile  → Crocodile

Employee (ABC)
├── Zookeeper
├── Veterinarian
└── Guide

Enclosure
Zoo
FeedingSchedule / FeedingEntry (@dataclass)

ZooError (Exception)
├── EnclosureFullError
├── AnimalNotFoundError
└── InvalidAnimalDataError
```

---

## Relacje między klasami

Notacja: `◆──` kompozycja, `◇──` agregacja, `──` asocjacja, `▲──` dziedziczenie.


| Relacja                                                                         | Typ           | Co się dzieje, gdy obiekt nadrzędny zostanie usunięty                                                                                                                                         | Uzasadnienie                                                                                                                 |
| --------------------------------------------------------------------------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `Zoo ◆── Enclosure`                                                          | Kompozycja    | Po usunięciu`Zoo` jego wybiegi również znikają — są tworzone wyłącznie przez `zoo.create_enclosure()` i nie istnieją poza zoo.                                                          | Wybieg jest częścią zoo i nie ma sensu w oderwaniu od konkretnego ogrodu, dlatego cykl życia jest powiązany.            |
| `FeedingSchedule ◆── FeedingEntry`                                           | Kompozycja    | Po usunięciu`FeedingSchedule` wszystkie wpisy `FeedingEntry` przestają istnieć — są tworzone tylko przez `add_entry()`.                                                                     | Wpis o karmieniu jest fragmentem konkretnego harmonogramu i nie ma własnej tożsamości.                                    |
| `Enclosure ◇── Animal`                                                       | Agregacja     | Po usunięciu`Enclosure` zwierzęta nadal istnieją jako niezależne obiekty `Animal` i mogą zostać przeniesione do innego wybiegu.                                                            | Zwierzę jest bytem niezależnym — może zmieniać wybieg, trafić do kwarantanny lub na transport bez utraty tożsamości. |
| `Zoo ◇── Employee`                                                           | Agregacja     | Po zwolnieniu pracownika lub usunięciu`Zoo` obiekt `Employee` nadal istnieje i może zostać zatrudniony gdzie indziej.                                                                         | Pracownik istnieje niezależnie od zoo (ma własne ID, pensję, kompetencje) — zoo tylko go zatrudnia.                      |
| `Zookeeper ── Enclosure`                                                      | Asocjacja     | Po usunięciu wybiegu opiekun nadal istnieje, ale traci przypisanie (`_assigned_enclosure` powinno wskazywać na nieaktualny obiekt — w praktyce wymaga ręcznego wyzerowania lub przepięcia). | Opiekun i wybieg są bytami równorzędnymi; przypisanie to luźne powiązanie, które może się zmieniać w czasie.        |
| `Animal ▲── Mammal/Bird/Reptile ▲── Lion/Eagle/...`                       | Dziedziczenie | n/d — relacja typów, nie obiektów.                                                                                                                                                            | Wspólne API (`make_sound()`, `diet()`, `health`) oraz polimorfizm na liście mieszanych zwierząt.                          |
| `Employee ▲── Zookeeper/Veterinarian/Guide`                                  | Dziedziczenie | n/d — relacja typów, nie obiektów.                                                                                                                                                            | Wspólne API (`work()`, `role()`, ID, pensja) dla wszystkich pracowników.                                                   |
| `ZooError ▲── EnclosureFullError/AnimalNotFoundError/InvalidAnimalDataError` | Dziedziczenie | n/d — relacja typów, nie obiektów.                                                                                                                                                            | Pozwala wyłapać dowolny błąd domenowy jednym`except ZooError`.                                                           |

---

## Planowane funkcjonalności

- Tworzenie zoo o określonej nazwie i lokalizacji.
- Tworzenie wybiegów o zdefiniowanej pojemności wewnątrz zoo (kompozycja).
- Dodawanie zwierząt do wybiegu z walidacją pojemności (`EnclosureFullError`).
- Usuwanie zwierząt z wybiegu z walidacją obecności (`AnimalNotFoundError`).
- Walidacja danych zwierzęcia przy tworzeniu (`InvalidAnimalDataError` przy pustym imieniu).
- Polimorficzne wywołania `make_sound()` i `diet()` na liście mieszanych zwierząt.
- Nakarmienie wszystkich zwierząt na wybiegu jednym poleceniem (`feed_all()`).
- Wyszukiwanie zwierzęcia po imieniu w obrębie wybiegu lub całego zoo.
- Iteracja po zwierzętach w wybiegu, sprawdzanie obecności (`in`), liczność (`len()`).
- Zatrudnianie pracowników (opiekunów, weterynarzy, przewodników) — agregacja.
- Przypisywanie opiekuna do wybiegu (asocjacja) i karmienie wszystkich jego zwierząt.
- Tworzenie dziennego harmonogramu karmień z wpisami `FeedingEntry` (kompozycja).
- Filtrowanie wpisów harmonogramu po nazwie wybiegu.
- Generowanie tekstowego raportu stanu zoo (`report()`): wybiegi, zwierzęta, personel.
- Bezpieczna walidacja zdrowia zwierzęcia (clamping do zakresu `[0, 100]`).
- Sortowanie zwierząt po imieniu (`sorted()` dzięki `__lt__`).
- Dostęp do wybiegu po nazwie z `Zoo` w stylu słownikowym (`zoo["Savanna"]`).

---

## Przykłady wykonania — scenariusze

Pełna demonstracja znajduje się w pliku [`demo.py`](demo.py) i pokrywa siedem scenariuszy.

### Scenariusz 1 — Utworzenie zoo i wybiegów

```python
from zoo import Zoo

zoo = Zoo("Łódź Zoo", city="Łódź")
savanna = zoo.create_enclosure("Savanna", capacity=3)
aviary  = zoo.create_enclosure("Aviary", capacity=2)
```

### Scenariusz 2 — Dodanie zwierząt do wybiegów

```python
from zoo import Lion, Elephant, Monkey, Eagle, Penguin

savanna.add_animal(Lion("Simba", age=5))
savanna.add_animal(Elephant("Dumbo", age=10, tusk_length=1.2))
savanna.add_animal(Monkey("George", age=4))

aviary.add_animal(Eagle("Sam", age=3))
aviary.add_animal(Penguin("Pete", age=2))
```

### Scenariusz 3 — Próba przepełnienia wybiegu (`EnclosureFullError`)

```python
from zoo import Lion, EnclosureFullError

try:
    savanna.add_animal(Lion("Mufasa", age=7))   # Savanna ma już 3/3
except EnclosureFullError as e:
    print(f"Caught: {e}")
# → Caught: Enclosure 'Savanna' is full (capacity=3).
```

### Scenariusz 4 — Karmienie wszystkich zwierząt na wybiegu

```python
for msg in savanna.feed_all():
    print(msg)
# → Simba has been fed.
# → Dumbo has been fed.
# → George has been fed.
```

### Scenariusz 5 — Przypisanie opiekuna i karmienie z poziomu pracownika

```python
from zoo import Zookeeper

keeper = Zookeeper("Anna Kowalska", salary=4800.0)
keeper.assign_to(savanna)
zoo.hire_employee(keeper)

print(keeper.feed_animals())
```

### Scenariusz 6 — Raport stanu zoo

```python
print(zoo.report())
# === Łódź Zoo — Zoo Report ===
# City: Łódź
# Enclosures: 3
# Total animals: 6
# Employees: 3
# ...
```

### Scenariusz 7 — Polimorfizm na liście mieszanych zwierząt

```python
animals = [Lion("Simba", 5), Eagle("Sam", 3), Penguin("Pete", 2)]
for a in animals:
    print(a.make_sound())
# → Simba roars loudly: ROARRR!
# → Sam screeches: KREE-EEE-AR!
# → Pete squawks: BRAP BRAP!
```

---

## User Stories

**US-1 — Opiekun zwierząt:**
Jako opiekun chcę przypisać się do wybiegu i nakarmić wszystkie zwierzęta jednym poleceniem (`feed_animals()`), żeby zaoszczędzić czas i mieć pewność, że żadne zwierzę nie zostanie pominięte.

**US-2 — Dyrektor zoo:**
Jako dyrektor chcę wygenerować raport stanu zoo (`zoo.report()`), żeby szybko zobaczyć liczbę wybiegów, całkowitą liczbę zwierząt i pełną listę pracowników.

**US-3 — Weterynarz:**
Jako weterynarz chcę sprawdzić stan zdrowia zwierzęcia (`animal.health`) z gwarancją, że wartość mieści się w zakresie `[0, 100]`, żeby wyniki były zawsze interpretowalne i porównywalne między zwierzętami.

---

## Mechanizmy OOP


| Mechanizm                    | Lokalizacja                                                                   |
| ------------------------------ | ------------------------------------------------------------------------------- |
| Klasy abstrakcyjne (ABC)     | `animals.py: Animal`, `employees.py: Employee`                                |
| Dziedziczenie wielopoziomowe | `Mammal → Lion`, `Bird → Penguin`                                           |
| `@abstractmethod`            | `Animal.make_sound`, `Animal.diet`, `Employee.work`, `Employee.role`          |
| `@property` z walidacją     | `Animal.health` (clamping), `Animal.name` (walidacja)                         |
| Atrybut klasy`_next_id`      | `Animal._next_id`, `Employee._next_id`                                        |
| Enkapsulacja                 | atrybuty`_name`, `_health`, `_animals`, `_enclosures`                         |
| `__str__` / `__repr__`       | `Animal`, `Enclosure`, `Employee`                                             |
| `__eq__` / `__hash__`        | `Animal` (po ID), `Enclosure` (po nazwie)                                     |
| `__lt__` (sortowanie)        | `Animal` (po nazwie)                                                          |
| `__len__`                    | `Enclosure`, `FeedingSchedule`, `Zoo`                                         |
| `__contains__`               | `Enclosure`, `Zoo`                                                            |
| `__iter__`                   | `Enclosure`                                                                   |
| `__getitem__`                | `Zoo`                                                                         |
| Polimorfizm                  | `make_sound()`, `diet()` na liście różnych zwierząt                       |
| Duck typing                  | iteracja po liście`Animal` z wywołaniem `make_sound()`                      |
| Kompozycja                   | `Zoo ◆── Enclosure`, `FeedingSchedule ◆── FeedingEntry`                 |
| Agregacja                    | `Enclosure ◇── Animal`, `Zoo ◇── Employee`                              |
| Asocjacja                    | `Zookeeper ── Enclosure` (`assign_to`)                                      |
| `@dataclass`                 | `FeedingEntry`                                                                |
| Własne wyjątki             | `ZooError → EnclosureFullError, AnimalNotFoundError, InvalidAnimalDataError` |
| `super()`                    | we wszystkich konstruktorach klas pochodnych                                  |
| Type hints                   | wszystkie metody publiczne                                                    |
| Docstringi (Google)          | wszystkie klasy i metody publiczne                                            |
| `isinstance` / `issubclass`  | testy jednostkowe,`Zoo.__contains__`                                          |

---

## Struktura projektu

```
projekt/
├── src/
│   └── zoo/
│       ├── __init__.py       # eksport publicznego API
│       ├── exceptions.py     # hierarchia wyjątków
│       ├── animals.py        # klasy zwierząt
│       ├── enclosure.py      # klasa Enclosure
│       ├── feeding.py        # FeedingEntry, FeedingSchedule
│       ├── employees.py      # klasy pracowników
│       └── zoo.py            # klasa Zoo
├── tests/
│   ├── conftest.py           # fixtures pytest
│   └── test_zoo.py           # testy jednostkowe
├── demo.py                   # demonstracja działania
├── README.md
├── CHECKLIST.md
├── JUSTIFICATION.md
└── requirements.txt
```

---

## Wymagania i uruchomienie

### Wymagania

- Python 3.10+
- pytest >= 7.0.0

### Instalacja zależności

```bash
pip3 install -r requirements.txt
```

### Uruchomienie demonstracji

```bash
python3 demo.py
```

### Uruchomienie testów

```bash
python3 -m pytest tests/ -v
```

---

## Historia zmian

- **2026-05-01** — Uzupełniono README zgodnie z uwagami wykładowcy: dodano sekcję *Autorzy i podział pracy*, *Lista klas z opisami*, *Relacje między klasami* (z opisem cyklu życia obiektów zależnych — kompozycja vs. agregacja), *Planowane funkcjonalności* oraz *Przykłady wykonania — scenariusze*. Zaktualizowano również tabelę mechanizmów OOP, dopisując kompozycję `FeedingSchedule ◆── FeedingEntry`.
