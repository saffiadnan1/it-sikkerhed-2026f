# it-sikkerhed-2026f


Teststrategier – Login (IT-sikkerhed)
Emne

Login til et website (brugernavn og adgangskode)

Ækvivalensklasser

Korrekt brugernavn og korrekt adgangskode → login godkendt

Forkert brugernavn → login afvist

Forkert adgangskode → login afvist

Grænseværditest

Regel: Adgangskode skal være mellem 8 og 12 tegn.

7 tegn (for kort) → fejl

8 tegn (mindste gyldige) → OK

12 tegn (største gyldige) → OK

13 tegn (for langt) → fejl

CRUD(L)

Create: Opret ny bruger

Read: Se brugerprofil

Update: Skift adgangskode

Delete: Slet bruger

List: Vis alle brugere (admin)

Cycle Process Test

Bruger åbner login-side

Bruger indtaster brugernavn og adgangskode

System validerer oplysninger

Login gennemføres eller fejl vises

Bruger logger ind eller prøver igen

Testpyramiden

Unit test: Tjek længde på adgangskode

Integration test: Tjek login-API mod database

UI test: Tjek login-knap og fejlbesked i browser

Decision Table Test

Korrekt brugernavn + korrekt adgangskode → login OK

Korrekt brugernavn + forkert adgangskode → fejl

Forkert brugernavn + korrekt adgangskode → fejl

Forkert brugernavn + forkert adgangskode → fejl

Security Gate

Under udvikling: Unit test og grænseværditest

Før deployment: Integration test og decision table test

Før release: UI test og cycle process test


## Testresultater af unittest

### Bestået test
### Fejlet test
### Skippet test

![alt text](image.png)



# Flat File Database

## Hvad er en flat_file_db?
En flat file database gemmer data i én JSON-fil.
Det er smart til små systemer, fordi det er simpelt og nemt at vedligeholde.

## Funktioner i databasen
- Opret bruger
- Hent bruger via person_id
- Deaktivér bruger

## Tests
Der er lavet unit tests, som tester:
- at en bruger kan oprettes korrekt
- at en bruger der ikke findes returnerer None
- at en bruger kan deaktiveres

## Risici
Hvis testene fejler, kan det betyde:
- at brugere ikke bliver gemt korrekt
- at forkerte brugere bliver hentet
- at deaktiverede brugere stadig kan være aktive

## Screenshots
<img width="1310" height="296" alt="image" src="https://github.com/user-attachments/assets/54723125-1a86-4743-8c31-9987f15ae175" />


