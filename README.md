# Usługa wizualizująca dane o jakości powietrza 

## Opis 

Projekt składa się z 3 modułów. Każdy z nich uruchamiany jest na osobnym kontenerze, spiętym z pozostałymi za pomocą docker-compose. 
Zawierają zaimplementowany w języku Python algorytm interpolacji przestrzennej IDW na podstawie danych o jakości powietrza. Dane o jakości powietrza, 
na których uruchamiany jest algorytm pobierane są w formacie JSON z rządowego [API](https://powietrze.gios.gov.pl/pjp/content/api)
oraz ze strony https://powietrze.gios.gov.pl/pjp/current.
Trzeci moduł odpowiedzialny jest za utrzymywanie bazy danych pomiarowych w PostgreSQL. 
Po wykonaniu algorytmu prezentacja danych wykonywana jest na podzielonej na segmenty mapie. 
Szczegółowy opis można znaleźć w wiki tego projektu.