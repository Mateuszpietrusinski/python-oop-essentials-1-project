"""Zoo Garden — demonstration script.

Covers all 7 required scenarios:
  1. Create zoo with enclosures
  2. Add animals (Mammal, Bird, Reptile)
  3. Attempt to add animal to full enclosure (EnclosureFullError)
  4. Feed all animals (feed_all)
  5. Assign zookeeper to enclosure (association)
  6. Generate zoo report
  7. Polymorphic make_sound() and diet() calls
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from zoo import (
    Zoo,
    Lion,
    Elephant,
    Monkey,
    Eagle,
    Penguin,
    Crocodile,
    Zookeeper,
    Veterinarian,
    Guide,
    FeedingSchedule,
    EnclosureFullError,
)


def separator(title: str) -> None:
    print(f"\n{'='*60}")
    print(f"  {title}")
    print("="*60)


# ---------------------------------------------------------------------------
# Scenario 1 — Create zoo with enclosures
# ---------------------------------------------------------------------------
separator("Scenario 1: Create zoo with enclosures")

zoo = Zoo("Łódź Zoo", city="Łódź")
savanna = zoo.create_enclosure("Savanna", capacity=3)
aviary = zoo.create_enclosure("Aviary", capacity=2)
reptile_house = zoo.create_enclosure("Reptile House", capacity=2)

print(f"Created zoo: {zoo.name} in {zoo.city}")
print(f"Enclosures created: {len(zoo)}")
print(f"  - {savanna.name} (capacity {savanna.capacity})")
print(f"  - {aviary.name} (capacity {aviary.capacity})")
print(f"  - {reptile_house.name} (capacity {reptile_house.capacity})")


# ---------------------------------------------------------------------------
# Scenario 2 — Add animals to enclosures
# ---------------------------------------------------------------------------
separator("Scenario 2: Add animals to enclosures")

# Mammals → Savanna
simba = Lion("Simba", age=5, mane=True)
dumbo = Elephant("Dumbo", age=10, tusk_length=1.2)
george = Monkey("George", age=4)

savanna.add_animal(simba)
savanna.add_animal(dumbo)
savanna.add_animal(george)
print(f"Added to Savanna: {[a.name for a in savanna]}")

# Birds → Aviary
sam = Eagle("Sam", age=3)
pete = Penguin("Pete", age=2)

aviary.add_animal(sam)
aviary.add_animal(pete)
print(f"Added to Aviary: {[a.name for a in aviary]}")

# Reptile → Reptile House
rex = Crocodile("Rex", age=8, length=4.2)
reptile_house.add_animal(rex)
print(f"Added to Reptile House: {[a.name for a in reptile_house]}")


# ---------------------------------------------------------------------------
# Scenario 3 — Attempt to add animal to full enclosure (EnclosureFullError)
# ---------------------------------------------------------------------------
separator("Scenario 3: EnclosureFullError on full enclosure")

extra_lion = Lion("Mufasa", age=7)
try:
    savanna.add_animal(extra_lion)  # Savanna capacity=3 is already full
except EnclosureFullError as e:
    print(f"Caught EnclosureFullError: {e}")


# ---------------------------------------------------------------------------
# Scenario 4 — Feed all animals in an enclosure (feed_all)
# ---------------------------------------------------------------------------
separator("Scenario 4: Feeding all animals in Savanna")

feed_results = savanna.feed_all()
for msg in feed_results:
    print(f"  {msg}")


# ---------------------------------------------------------------------------
# Scenario 5 — Assign zookeeper to enclosure (association)
# ---------------------------------------------------------------------------
separator("Scenario 5: Zookeeper assigns to enclosure and feeds")

keeper = Zookeeper("Anna Kowalska", salary=4800.0)
keeper.assign_to(savanna)
zoo.hire_employee(keeper)

vet = Veterinarian("Dr. Wiśniewski", specialization="exotic", salary=7500.0)
guide = Guide("Piotr Nowak", languages=["Polish", "English", "German"], salary=3600.0)
zoo.hire_employee(vet)
zoo.hire_employee(guide)

print(keeper.work())
print()
print(keeper.feed_animals())
print()
print(vet.work())
print(guide.work())


# ---------------------------------------------------------------------------
# Scenario 6 — Generate zoo report
# ---------------------------------------------------------------------------
separator("Scenario 6: Zoo report")

print(zoo.report())


# ---------------------------------------------------------------------------
# Scenario 7 — Polymorphic make_sound() and diet() calls
# ---------------------------------------------------------------------------
separator("Scenario 7: Polymorphic method calls on mixed animal list")

all_animals = [simba, dumbo, george, sam, pete, rex]
for animal in all_animals:
    print(f"{animal.name:>10} | {animal.make_sound()}")
    print(f"{'':>10} | {animal.diet()}")
    print()


separator("Demo complete — all scenarios executed successfully!")
