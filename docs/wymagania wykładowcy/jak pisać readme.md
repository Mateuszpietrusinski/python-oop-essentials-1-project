Przed napisaniem jakiegokolwiek kodu proszę przygotować plik README.md, który będzie pełnił rolę specyfikacji projektu. Specyfikacja powinna być na tyle precyzyjna, aby inna osoba mogła na jej podstawie zaimplementować system bez dodatkowych pytań. Plik README.md powinien zawierać poniższe sekcje.

1. Opis projektu. W 3-5 zdaniach proszę opisać, czym jest system i jaki problem rozwiązuje. Proszę pisać z perspektywy użytkownika systemu, nie programisty.

2. Autorzy i podział pracy. Tabela z imionami i nazwiskami członków zespołu oraz zakresem odpowiedzialności każdej osoby.

3. Lista klas z opisami. Dla każdej planowanej klasy proszę podać: nazwę, krótki opis (1-2 zdania) wyjaśniający jej rolę w systemie oraz najważniejsze atrybuty i metody.

4. Relacje między klasami. Proszę opisać, jakie relacje łączą poszczególne klasy (kompozycja, agregacja, asocjacja, dziedziczenie). Dla każdej relacji proszę wyjaśnić w 1-2 zdaniach, dlaczego wybrano właśnie ten typ powiązania - co się stanie z obiektem zależnym, jeśli obiekt nadrzędny zostanie usunięty?

5. Planowane funkcjonalności. Lista konkretnych operacji, które system będzie udostępniał (np. "dodawanie zwierzęcia do wybiegu z walidacją pojemności").

6. User Stories (dokładnie 3).

User story to krótki opis jednej funkcjonalności systemu napisany z perspektywy konkretnego użytkownika. Nie opisujemy w nim kodu ani implementacji - opisujemy kto chce co zrobić i po co. Dzięki temu łatwiej jest zrozumieć, jakie zachowanie system powinien oferować, zanim zaczniemy go programować.

Każde user story ma stały format:

"Jako [rola użytkownika] chcę [wykonać akcję], żeby [osiągnąć cel]."

Na przykład (z innej domeny):

"Jako klient sklepu internetowego chcę filtrować produkty po cenie, żeby szybko znaleźć rzeczy w moim budżecie."
"Jako administrator systemu chcę blokować konta nieaktywne dłużej niż 90 dni, żeby zwiększyć bezpieczeństwo platformy."
Proszę zwrócić uwagę, że dobre user story opisuje jeden konkretny scenariusz, a nie całą funkcjonalność systemu. "Jako użytkownik chcę korzystać z systemu" to za mało - trzeba wskazać konkretną akcję i jej uzasadnienie.

Proszę napisać dokładnie 3 user stories. Każde powinno dotyczyć innego aspektu systemu.

7. Mechanizmy OOP. Tabela lub lista mechanizmów programowania obiektowego, które Państwo planują zastosować, ze wskazaniem gdzie w projekcie (która klasa, która metoda) dany mechanizm się pojawi.


Formatowanie pliku README.md
Plik README.md jest pisany w składni Markdown i jego forma ma znaczenie. Proszę zadbać o to, żeby dokument był czytelny i spójny wizualnie.

Hierarchia nagłówków. Tytuł projektu powinien być nagłówkiem pierwszego poziomu (#). Główne sekcje (opis, klasy, relacje itd.) powinny używać drugiego poziomu (##). Podsekcje - trzeciego (###). Proszę nie przeskakiwać poziomów (np. z ## od razu do ####).

Nazwy klas, metod i atrybutów. Wszystkie elementy kodu - nazwy klas (Animal), metod (make_sound()), atrybutów (_next_id) - proszę zapisywać w backtickach: `Animal`, `make_sound()`. Dzięki temu czytelnik od razu widzi, co jest kodem, a co opisem.

Tabele. Tam, gdzie porównujecie wiele elementów (np. lista klas, mechanizmy OOP), proszę użyć tabel Markdown zamiast długich akapitów. Tabela jest czytelniejsza, gdy informacja ma powtarzalną strukturę.

Bloki kodu. Jeśli pokazujecie hierarchię klas lub przykładowy fragment kodu, proszę używać bloków kodu z potrójnym backtickiem i oznaczeniem języka (np. ```python).

Ogólna zasada. Dokument powinien wyglądać profesjonalnie. Proszę nie pisać wszystkiego jednym ciągłym tekstem - używajcie nagłówków, list i tabel, żeby informację dało się szybko przeskanować wzrokiem.



Wskazówki:

Proszę traktować README.md jako dokument, do którego będą Państwo wracać podczas implementacji - to plan pracy na kolejne etapy.
Jeśli podczas implementacji okaże się, że coś w specyfikacji wymaga zmiany, proszę ją zaktualizować. Każda zmiana musi być opatrzona krótkim komentarzem na końcu pliku README.md w sekcji "Historia zmian" - proszę zapisać co zostało zmienione, z czego na co i dlaczego. Na przykład: "Zmieniono relację Zoo-Employee z kompozycji na agregację, ponieważ pracownik może istnieć niezależnie od zoo."
Proszę nie opisywać instrukcji uruchomienia ani struktury katalogów - te sekcje uzupełnią Państwo w późniejszych etapach, gdy kod będzie gotowy.
Wgrywają Państwo: README.md

Specyfikację omawiamy i oceniamy na najbliższym zjeździe.