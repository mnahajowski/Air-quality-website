## 1. Opis

Aplikacja wizualizuje wykonanie metody IDW na danych o jakości powietrza.

Składa się z 4 kontenerów:
1. Kontener z API
2. Kontener z bazą danych w PostgreSQL
3. Kontener z modułem do pobierania danych z API rządowego
4. Kontener z frontendem

Kontener z API odpowiedzialny jest za wykonanie obliczeń na danych oraz zawiera algorytm z metodą IDW. 
Obliczone w określony sposób wartości prezentowane są na podzielonej na segmenty mapie.
Jeżeli w danym segmencie znajduje się jeden czujnik lub więcej, to segmentowi zostaje przypisana średnia 
wartości z wszystkich czujników w danym segmencie. W przypadku
braku czujnika w danym segmencie, wartość dla tego segmentu jest interpelowana ze wskazań z pobliskich 
czujników (znajdujących się w innych segmentach) zgodnie z opisaną
poniżej metodą IDW.

Kontener z bazą danych w PostgreSQL przechowuje zmagazynowane dane. Składają się na nie dane o stacjach pomiarowych pobierane z API rządowego (kontener 3) oraz dane
z tych stacji pomiarowych. Na podstawie danych zawartych w bazie danej możliwe jest później wyświetlenie mapy
wizualizującej pomiary na danym obszarze w danym terminie.

Kontener z modułem do pobieranie danych z API rządowych pobiera dane o stacjach pomiarowych co 24h oraz dane pomiarowe co 1h.

Kontener z frontendem zawiera prezentację graficzną całego systemu i ułatwia generowanie map i przeglądanie danych.

### Przykład użycia API


Użytkownik może podać datę, godzinę, współrzędne A, B, C, D (na podstawie których obliczany jest wyświetlany obszar) oraz rodzaj zanieczyszczenia. Wygenerowana zostanie wówczas 
wspomniana podzielona na segmenty mapa w formacie .png . 

Parametry podawane są po znaku "?" oddzielone od siebie "&" w formacie nazwa=wartość.

### Dostępne parametry:

- rect - współrzędne geograficzne (wymagane, brak wartości domyślnej) - w formacie X1,Y1,X2,Y2, gdzie współrzędne X to szerokość
  geograficzna, a Y to długość geograficzna podane w stopniach, punkty 1 i 2 określają
  prostokąt (obszar), na którym generowana jest mapa jaokści powietrza, 
  np. 51.05,17,51.15,17.12
- width - szerokość mapy w pikselach (opcjonalne, domyślna wartość 800), np. 1600,
wysokość mapy jest kalkulowana, aby zachować format współrzędnych
- param - rodzaj mierzonego zanieczyszczenia (opcjonalne, domyślna wartość pm2.5),
 jedna z wartości ze zbioru ('no2', 'o3', 'pm25', 'so2', 'pm10', 'co', 'c6h6')
- date - data i czas pomiaru (opcjonalne, domyślna wartość "latest" - dane z ostatniej
  godziny) - w formacie YYYY-MM-DDTHH:00:00, np. 2021-04-06T16:00:00
- segments_x - liczba segmentów mapy w poziomie, na które podzielona zostanie mapa
  (opcjonalne, domyślna wartość 8) - segmenty w pionie są kalkulowane automatycznie, np. 10


Przykładowy URL dla danych z 6 kwietnia 2021r. godz 16:00, Wrocław, 
parametr domyślny PM2.5, domyślne 8 segmentów:

`localhost:80/map/?&rect=51.05,17,51.15,17.12&width=1600&date=2021-04-06T16:00:00`

### Zastosowany algorytm

Metoda IDW (ang. Inverse Distance Weighted) nazywana również metodą średniej ważonej odległością opiera się na tym, że wartość dla szacowanego punktu jest bardziej 
skorelowana z bliższymi punktami pomiarowymi niż z dalszymi. Algorytm działania metody IDW opiera się na tym, że dla każdego szacowanego punktu wykonywane są czynności: 
1. Obranie punktu o współrzędnych (x,y), który jest środkiem komórki, w której ma być obliczona wartość. 
2. Założenie, że punkt (x,y) jest środkiem koła o promieniu równym r. 
3. Wskazanie punktów pomiarowych (xi, yi) leżących w kole wyznaczonym w poprzednim kroku. 
4. Zmierzenie odległości pomiędzy każdym punktem pomiarowym (xi, yi) a środkiem koła (x,y) i obliczenie wag według wzorów (2) i (3). 
5. Obliczenie wartości F w punkcie (x,y) według wzoru (1) dla całej komórki.



## 2. Źródła
[1] https://powietrze.gios.gov.pl/pjp/current, 2021


## 3. Uruchomienie kontenera z usługą

Aby uruchomić aplikację należy sklonować repozytorium, a następnie w głównym katalogu wywołać 
`docker-compose up`. Frontend jest dostępny na porcie 8080 a API na 80.

## 4. Pozyskanie danych testowych
Aplikacja nastawiona jest na zbieranie danych przez cały czas jej uruchomienia. W związku z tym
w momencie pierwszego uruchomienie baza danych jest pusta. Możliwe jest jednak ręczne uzyskanie
danych testowych poprzez wywołanie na kontenerze data_source (id do pobrania przez `docker ps`)
`docker exec [id_kontenera] "python /app/get_stations.py"`, 
by uzyskać aktualne dane o aktywnych stacjach pomiarowych oraz wywołanie 
`docker exec [id_kontenera] "python /app/get_pollution_data.py"` 
celem uzyskania aktualnych danych z aktywnych stacji pomiarowych. Można to również wykonać przez Docker Desktop z CLI 
danego kontenera. Dostępne są wówczas dane z godziny obecnej.