# System wizualizujący dane o jakości powietrza 

## Opis 

Projekt składa się z 4 modułów. Każdy z nich uruchamiany jest w osobnym kontenerze, spiętym z pozostałymi za pomocą docker-compose. 
Moduł API pozwala na pobieranie danych i generowanie mapy, oraz zawiera zaimplementowany w języku Python algorytm 
interpolacji przestrzennej IDW. Moduł pobierania danych pozyskuje je w formacie JSON z rządowego 
[API](https://powietrze.gios.gov.pl/pjp/content/api) oraz ze strony https://powietrze.gios.gov.pl/pjp/current.
Trzeci moduł odpowiedzialny jest za utrzymywanie bazy danych pomiarowych w PostgreSQL. 
Czwarty zawiera frontend aplikacji.