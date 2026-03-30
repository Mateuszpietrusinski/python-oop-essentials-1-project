# CHECKLIST — Mechanizmy OOP

## Podstawy klas (5 pozycji)

- [x] **Klasy i obiekty** — definicja klas, tworzenie obiektów
  - Lokalizacja: `src/zoo/animals.py: Animal`, `src/zoo/zoo.py: Zoo`

- [x] **Konstruktor `__init__`** — inicjalizacja atrybutów
  - Lokalizacja: `src/zoo/animals.py: Animal.__init__`, `src/zoo/enclosure.py: Enclosure.__init__`

- [x] **Atrybuty instancji** — unikalne dla każdego obiektu
  - Lokalizacja: `src/zoo/animals.py: Animal.__init__` (`self._id`, `self._name`, `self._health`)

- [x] **Atrybuty klasy** — współdzielone między instancjami (`_next_id`)
  - Lokalizacja: `src/zoo/animals.py: Animal._next_id`, `src/zoo/employees.py: Employee._next_id`

- [x] **Metody instancji** — operacje na obiektach
  - Lokalizacja: `src/zoo/animals.py: Animal.feed`, `src/zoo/enclosure.py: Enclosure.add_animal`

---

## Enkapsulacja i metody specjalne (7 pozycji)

- [x] **Prywatne atrybuty** — konwencja `_protected`
  - Lokalizacja: `src/zoo/animals.py` (`_name`, `_health`, `_id`), `src/zoo/enclosure.py` (`_animals`)

- [x] **`@property`** — gettery
  - Lokalizacja: `src/zoo/animals.py: Animal.id`, `Animal.name`, `Animal.health`, `Animal.age`

- [x] **`@property.setter`** — settery z walidacją
  - Lokalizacja: `src/zoo/animals.py: Animal.name.setter` (walidacja pusta nazwa), `Animal.health.setter` (clamping 0–100)

- [x] **`__str__()`** — reprezentacja dla użytkownika
  - Lokalizacja: `src/zoo/animals.py: Animal.__str__`

- [x] **`__repr__()`** — reprezentacja dla debugowania
  - Lokalizacja: `src/zoo/animals.py: Animal.__repr__`, `src/zoo/enclosure.py: Enclosure.__repr__`

- [x] **`__eq__()`** — porównywanie obiektów
  - Lokalizacja: `src/zoo/animals.py: Animal.__eq__` (po `_id`), `src/zoo/enclosure.py: Enclosure.__eq__` (po `name`)

- [x] **Dodatkowe metody specjalne** (`__lt__`, `__len__`, `__contains__`, `__iter__`, `__getitem__`)
  - Lokalizacja: `Animal.__lt__` (sortowanie po nazwie), `Enclosure.__len__`, `Enclosure.__contains__`, `Enclosure.__iter__`, `Zoo.__getitem__`

---

## Dziedziczenie (5 pozycji)

- [x] **Klasa bazowa**
  - Lokalizacja: `src/zoo/animals.py: Animal (ABC)`, `src/zoo/employees.py: Employee (ABC)`

- [x] **Klasy pochodne** — 3 dla Animal, 3 dla Employee
  - Lokalizacja: `animals.py: Mammal, Bird, Reptile`; `employees.py: Zookeeper, Veterinarian, Guide`

- [x] **`super()`** — wywołanie konstruktora rodzica
  - Lokalizacja: `animals.py: Mammal.__init__`, `Bird.__init__`, `Reptile.__init__`, `Lion.__init__` (i pozostałe gatunki)

- [x] **Nadpisywanie metod (override)**
  - Lokalizacja: `animals.py: Lion.diet()` (nadpisuje `Mammal.diet()`), `Elephant.diet()` (nadpisuje `Mammal.diet()`)

- [x] **`isinstance()` i `issubclass()`**
  - Lokalizacja: `src/zoo/zoo.py: Zoo.__contains__`, `tests/test_zoo.py: test_isinstance_issubclass`

---

## Polimorfizm (2 pozycje)

- [x] **Polimorfizm** — ta sama metoda, różne implementacje
  - Lokalizacja: `animals.py: make_sound()` — Lion, Elephant, Monkey, Eagle, Penguin, Crocodile mają różne implementacje

- [x] **Duck typing** — lista różnych obiektów, wspólny interfejs
  - Lokalizacja: `demo.py` (linia ~107): `for animal in all_animals: animal.make_sound()`; `tests/test_zoo.py: test_polymorphism_make_sound_diet`

---

## Kompozycja i agregacja (2 pozycje)

- [x] **Kompozycja** — has-a, silne powiązanie
  - Lokalizacja: `src/zoo/zoo.py: Zoo.create_enclosure()` — wybiegi tworzone przez zoo, `src/zoo/feeding.py: FeedingSchedule` własne `FeedingEntry`

- [x] **Agregacja** — has-a, słabsze powiązanie
  - Lokalizacja: `src/zoo/enclosure.py: Enclosure.add_animal()` — zwierzęta mogą istnieć poza wybiegiem; `src/zoo/zoo.py: Zoo.hire_employee()` — pracownicy mogą istnieć poza zoo

---

## Klasy abstrakcyjne i operatory (3 pozycje)

- [x] **Klasa abstrakcyjna (ABC)**
  - Lokalizacja: `src/zoo/animals.py: class Animal(ABC)`, `src/zoo/employees.py: class Employee(ABC)`

- [x] **`@abstractmethod`** — wymuszenie implementacji
  - Lokalizacja: `animals.py: Animal.make_sound`, `Animal.diet`; `employees.py: Employee.work`, `Employee.role`

- [x] **Przeciążanie operatorów**
  - Lokalizacja: `animals.py: Animal.__lt__` (operator `<`), `Animal.__eq__` (operator `==`)

---

## Wyjątki (4 pozycje)

- [x] **Własny wyjątek bazowy**
  - Lokalizacja: `src/zoo/exceptions.py: class ZooError(Exception)`

- [x] **Hierarchia wyjątków** — 2 specjalizowane
  - Lokalizacja: `exceptions.py: EnclosureFullError(ZooError)`, `AnimalNotFoundError(ZooError)`, `InvalidAnimalDataError(ZooError)`

- [x] **Zgłaszanie wyjątków** — `raise` w metodach
  - Lokalizacja: `enclosure.py: Enclosure.add_animal` (EnclosureFullError), `Enclosure.remove_animal` (AnimalNotFoundError), `animals.py: Animal.name.setter` (InvalidAnimalDataError)

- [x] **Obsługa wyjątków** — `try-except`
  - Lokalizacja: `demo.py` (scenario 3): `try: savanna.add_animal(extra_lion) except EnclosureFullError as e:`

---

## Testowanie i dokumentacja (3 pozycje)

- [x] **Testy pytest** — dokładnie 15 testów
  - Lokalizacja: `tests/test_zoo.py` (15 funkcji `test_*`)

- [x] **Docstringi** — dla wszystkich klas i metod publicznych (format Google)
  - Lokalizacja: wszystkie pliki w `src/zoo/`

- [x] **Type hints** — dla głównych metod
  - Lokalizacja: wszystkie metody publiczne w `src/zoo/`
