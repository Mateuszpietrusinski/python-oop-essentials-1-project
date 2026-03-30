# Zoo Garden — Projekt Semestralny OOP I

System symulacji ogrodu zoologicznego implementujący kluczowe mechanizmy programowania obiektowego w Pythonie.

---

## Opis projektu

System Zoo Garden umożliwia zarządzanie ogrodem zoologicznym: tworzenie wybiegów, dodawanie zwierząt, zarządzanie pracownikami oraz planowanie karmień. Projekt demonstruje dziedziczenie, kompozycję, agregację, polimorfizm, klasy abstrakcyjne, enkapsulację oraz własne wyjątki.

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
│   └── test_zoo.py           # 15 testów jednostkowych
├── demo.py                   # demonstracja działania
├── README.md
├── CHECKLIST.md
├── JUSTIFICATION.md
└── requirements.txt
```

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

## Lista mechanizmów OOP

| Mechanizm | Lokalizacja |
|-----------|-------------|
| Klasy abstrakcyjne (ABC) | `animals.py: Animal`, `employees.py: Employee` |
| Dziedziczenie wielopoziomowe | `Mammal → Lion`, `Bird → Penguin` |
| `@abstractmethod` | `Animal.make_sound`, `Animal.diet`, `Employee.work`, `Employee.role` |
| `@property` z walidacją | `Animal.health` (clamping), `Animal.name` (walidacja) |
| Atrybut klasy `_next_id` | `Animal._next_id`, `Employee._next_id` |
| Enkapsulacja | atrybuty `_name`, `_health`, `_animals`, `_enclosures` |
| `__str__` / `__repr__` | `Animal`, `Enclosure`, `Employee` |
| `__eq__` / `__hash__` | `Animal` (po ID), `Enclosure` (po nazwie) |
| `__lt__` (sortowanie) | `Animal` (po nazwie) |
| `__len__` | `Enclosure`, `FeedingSchedule`, `Zoo` |
| `__contains__` | `Enclosure`, `Zoo` |
| `__iter__` | `Enclosure` |
| `__getitem__` | `Zoo` |
| Polimorfizm | `make_sound()`, `diet()` na liście różnych zwierząt |
| Duck typing | iteracja po liście `Animal` z wywołaniem `make_sound()` |
| Kompozycja | `Zoo ◆── Enclosure` (create_enclosure) |
| Agregacja | `Enclosure ◇── Animal`, `Zoo ◇── Employee` |
| Asocjacja | `Zookeeper ── Enclosure` (assign_to) |
| `@dataclass` | `FeedingEntry` |
| Własne wyjątki | `ZooError → EnclosureFullError, AnimalNotFoundError, InvalidAnimalDataError` |
| `super()` | we wszystkich konstruktorach klas pochodnych |
| Type hints | wszystkie metody publiczne |
| Docstringi (Google) | wszystkie klasy i metody publiczne |
| `isinstance` / `issubclass` | testy 13, `Zoo.__contains__` |

---

## 3 User Stories

**US-1 — Opiekun zwierząt:**
Jako opiekun chcę przypisać się do wybiegu i nakarmić wszystkie zwierzęta jednym poleceniem (`feed_animals()`), aby zaoszczędzić czas i mieć pewność, że żadne zwierzę nie zostanie pominięte.

**US-2 — Dyrektor zoo:**
Jako dyrektor chcę wygenerować raport stanu zoo (`zoo.report()`), aby szybko zobaczyć liczbę wybiegów, całkowitą liczbę zwierząt i pełną listę pracowników.

**US-3 — Weterynarz:**
Jako weterynarz chcę mieć możliwość sprawdzenia stanu zdrowia zwierzęcia (`animal.health`) i wiedzieć, że wartość będzie zawsze w zakresie [0, 100], aby wyniki były zawsze interpretowalne.
