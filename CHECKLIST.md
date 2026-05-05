# CHECKLIST — Mechanizmy OOP

## Podstawy klas (5 pozycji)

- [x] **Klasy i obiekty** — definicja klas, tworzenie obiektów
  - Lokalizacja: `src/zoo/animals/animal.py: Animal`, `src/zoo/zoo.py: Zoo`

- [x] **Konstruktor `__init__`** — inicjalizacja atrybutów
  - Lokalizacja: `src/zoo/animals/animal.py: Animal.__init__`, `src/zoo/enclosure.py: Enclosure.__init__`

- [x] **Atrybuty instancji** — unikalne dla każdego obiektu
  - Lokalizacja: `src/zoo/animals/animal.py: Animal.__init__` (`self._id`, `self._name`, `self._health`)

- [x] **Atrybuty klasy** — współdzielone między instancjami (`_next_id`)
  - Lokalizacja: `src/zoo/animals/animal.py: Animal._next_id`, `src/zoo/employees/employee.py: Employee._next_id`

- [x] **Metody instancji** — operacje na obiektach
  - Lokalizacja: `src/zoo/animals/animal.py: Animal.feed`, `src/zoo/enclosure.py: Enclosure.add_animal`

---

## Enkapsulacja i metody specjalne (7 pozycji)

- [x] **Prywatne atrybuty** — konwencja `_protected`
  - Lokalizacja: `src/zoo/animals/animal.py` (`_name`, `_health`, `_id`), `src/zoo/enclosure.py` (`_animals`)

- [x] **`@property`** — gettery
  - Lokalizacja: `src/zoo/animals/animal.py: Animal.id`, `Animal.name`, `Animal.health`, `Animal.age`

- [x] **`@property.setter`** — settery z walidacją
  - Lokalizacja: `src/zoo/animals/animal.py: Animal.name.setter` (walidacja pusta nazwa), `Animal.health.setter` (clamping 0–100)

- [x] **`__str__()`** — reprezentacja dla użytkownika
  - Lokalizacja: `src/zoo/animals/animal.py: Animal.__str__`

- [x] **`__repr__()`** — reprezentacja dla debugowania
  - Lokalizacja: `src/zoo/animals/animal.py: Animal.__repr__`, `src/zoo/enclosure.py: Enclosure.__repr__`

- [x] **`__eq__()`** — porównywanie obiektów
  - Lokalizacja: `src/zoo/animals/animal.py: Animal.__eq__` (po `_id`), `src/zoo/enclosure.py: Enclosure.__eq__` (po `name`)

- [x] **Dodatkowe metody specjalne** (`__lt__`, `__len__`, `__contains__`, `__iter__`, `__getitem__`)
  - Lokalizacja: `Animal.__lt__` (sortowanie po nazwie), `Enclosure.__len__`, `Enclosure.__contains__`, `Enclosure.__iter__`, `Zoo.__getitem__`

---

## Dziedziczenie (5 pozycji)

- [x] **Klasa bazowa**
  - Lokalizacja: `src/zoo/animals/animal.py: Animal (ABC)`, `src/zoo/employees/employee.py: Employee (ABC)`

- [x] **Klasy pochodne** — 3 dla Animal, 3 dla Employee
  - Lokalizacja: `animals/mammal.py`, `animals/bird.py`, `animals/reptile.py`; `employees/zookeeper.py`, `employees/veterinarian.py`, `employees/guide.py`

- [x] **`super()`** — wywołanie konstruktora rodzica
  - Lokalizacja: `animals/mammal.py: Mammal.__init__`, `animals/bird.py: Bird.__init__`, `animals/reptile.py: Reptile.__init__`, `animals/lion.py: Lion.__init__` (i pozostałe gatunki w `animals/<species>.py`)

- [x] **Nadpisywanie metod (override)**
  - Lokalizacja: `animals/lion.py: Lion.diet()` (nadpisuje `Mammal.diet()`), `animals/elephant.py: Elephant.diet()` (nadpisuje `Mammal.diet()`)

- [x] **`isinstance()` i `issubclass()`**
  - Lokalizacja: `src/zoo/zoo.py: Zoo.__contains__`, `tests/test_zoo.py: test_isinstance_issubclass`  <!-- test żyje w pliku zoo-core po podziale -->


---

## Polimorfizm (2 pozycje)

- [x] **Polimorfizm** — ta sama metoda, różne implementacje
  - Lokalizacja: `animals/<species>.py: make_sound()` — Lion, Elephant, Monkey, Eagle, Penguin, Crocodile mają różne implementacje (każdy w osobnym pliku)

- [x] **Duck typing** — lista różnych obiektów, wspólny interfejs
  - Lokalizacja: `demo.py` (linia ~107): `for animal in all_animals: animal.make_sound()`; `tests/test_animals.py: test_polymorphism_make_sound_diet`

---

## Kompozycja i agregacja (2 pozycje)

- [x] **Kompozycja** — has-a, silne powiązanie
  - Lokalizacja: `src/zoo/zoo.py: Zoo.create_enclosure()` — wybiegi tworzone przez zoo, `src/zoo/feeding/feeding_schedule.py: FeedingSchedule` własne `FeedingEntry`

- [x] **Agregacja** — has-a, słabsze powiązanie
  - Lokalizacja: `src/zoo/enclosure.py: Enclosure.add_animal()` — zwierzęta mogą istnieć poza wybiegiem; `src/zoo/zoo.py: Zoo.hire_employee()` — pracownicy mogą istnieć poza zoo

---

## Klasy abstrakcyjne i operatory (3 pozycje)

- [x] **Klasa abstrakcyjna (ABC)**
  - Lokalizacja: `src/zoo/animals/animal.py: class Animal(ABC)`, `src/zoo/employees/employee.py: class Employee(ABC)`

- [x] **`@abstractmethod`** — wymuszenie implementacji
  - Lokalizacja: `animals/animal.py: Animal.make_sound`, `Animal.diet`; `employees/employee.py: Employee.work`, `Employee.role`

- [x] **Przeciążanie operatorów**
  - Lokalizacja: `animals/animal.py: Animal.__lt__` (operator `<`), `Animal.__eq__` (operator `==`)

---

## Wyjątki (4 pozycje)

- [x] **Własny wyjątek bazowy**
  - Lokalizacja: `src/zoo/exceptions/zoo_error.py: class ZooError(Exception)`

- [x] **Hierarchia wyjątków** — 2 specjalizowane
  - Lokalizacja: `exceptions/enclosure_full_error.py: EnclosureFullError(ZooError)`, `exceptions/animal_not_found_error.py: AnimalNotFoundError(ZooError)`, `exceptions/invalid_animal_data_error.py: InvalidAnimalDataError(ZooError)`

- [x] **Zgłaszanie wyjątków** — `raise` w metodach
  - Lokalizacja: `enclosure.py: Enclosure.add_animal` (EnclosureFullError), `Enclosure.remove_animal` (AnimalNotFoundError), `animals/animal.py: Animal.name.setter` (InvalidAnimalDataError)

- [x] **Obsługa wyjątków** — `try-except`
  - Lokalizacja: `demo.py` (scenario 3): `try: savanna.add_animal(extra_lion) except EnclosureFullError as e:`

---

## Testowanie i dokumentacja (3 pozycje)

- [x] **Testy pytest** — dokładnie 15 testów (rozdzielone wg capability)
  - Lokalizacja: `tests/test_animals.py` (8), `tests/test_enclosure.py` (4), `tests/test_feeding.py` (1), `tests/test_zoo.py` (2) — łącznie 15 funkcji `test_*` (audyt: `grep -rE '^def test_' tests/ | wc -l`)

- [x] **Docstringi** — dla wszystkich klas i metod publicznych (format Google)
  - Lokalizacja: wszystkie pliki w `src/zoo/`

- [x] **Type hints** — dla głównych metod
  - Lokalizacja: wszystkie metody publiczne w `src/zoo/`
