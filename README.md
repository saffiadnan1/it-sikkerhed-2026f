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




## Kryptering og hashing
Valg af krypterings- og hashing-algoritmer

Til hashing af passwords er bcrypt valgt. Bcrypt er designet specifikt til passwords og er langsom, hvilket beskytter mod brute-force angreb. Passwords kan ikke dekrypteres og gemmes aldrig i klartekst, hvilket er vigtigt for GDPR og datasikkerhed.

Til kryptering af følsomme data er AES via Fernet (cryptography-biblioteket) valgt. AES er en udbredt og sikker standard, og Fernet sikrer korrekt brug af kryptering og dekryptering.

## Hvornår krypteres data

Data krypteres, når de gemmes i databasen (db.json). Det betyder, at følsomme oplysninger som adresse aldrig lagres i klartekst, men altid i krypteret form.

## Hvornår dekrypteres data

Data dekrypteres kun når de skal bruges, for eksempel når en bruger hentes fra databasen. Dekryptering sker midlertidigt og kun i det øjeblik, data skal vises eller behandles.

## Hvornår fjernes dekrypteret data fra hukommelsen

Dekrypteret data fjernes igen straks efter brug. Når funktionen afsluttes, fjernes data automatisk fra hukommelsen, så følsomme oplysninger ikke opbevares unødigt i klartekst.

## Tests af kryptering og hashing

Der er lavet unit tests, som tester:

at passwords bliver hashet og ikke gemt i klartekst

at krypterede data ikke gemmes som læsbar tekst

at data kan dekrypteres korrekt, når det er nødvendigt

Hvis disse tests fejler, kan det betyde, at følsomme data ikke er beskyttet korrekt.

## Yderligere hensyn

Der bør også tages hensyn til:

at krypteringsnøglen opbevares separat fra databasen

at adgang til databasen er begrænset

at der kun dekrypteres data, når det er nødvendigt

at logs ikke indeholder følsomme oplysninger

## screenshot




## REST API

Der er implementeret et REST API med FastAPI.
API’et kan testes via Swagger UI på http://127.0.0.1:8000/docs.

API’et understøtter:
- Create: Opret bruger
- Read: Hent bruger
- Update: Deaktivér bruger
- Delete: Slet bruger
- List: Vis alle brugere

API’et bruger den eksisterende flat_file_db som datalager.

## screenshoot




## REST API

Der er implementeret et REST API med FastAPI.
API’et kan testes via Swagger UI på http://127.0.0.1:8000/docs.

API’et understøtter:
- Create: Opret bruger
- Read: Hent bruger
- Update: Deaktivér bruger
- Delete: Slet bruger
- List: Vis alle brugere

API’et bruger den eksisterende flat_file_db som datalager.

## screenshoot

<img width="1890" height="958" alt="image" src="https://github.com/user-attachments/assets/eea81ce6-12fc-4cd1-bb57-d88ac6399506" />
