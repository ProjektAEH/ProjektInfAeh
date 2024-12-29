```markdown
# Optymalizacja Tras Dostaw - Kolonia Mrówek (ACO)

Program służy do optymalizacji tras dostaw przy użyciu algorytmu Kolonii Mrówek (ACO - Ant Colony Optimization). Celem jest wyznaczenie najlepszej trasy, która minimalizuje całkowity koszt dostaw, biorąc pod uwagę odległości między punktami dostaw oraz koszty podróży pojazdów.

## Spis treści

1. [Opis programu](#opis-programu)
2. [Wymagania](#wymagania)
3. [Instalacja](#instalacja)
4. [Użycie](#użycie)
5. [Struktura plików](#struktura-plików)
6. [Przykład danych](#przykład-danych)

## Opis programu

Program wczytuje dane o punktach dostaw i flocie pojazdów, generuje macierz odległości między punktami dostaw, a następnie wykonuje optymalizację tras za pomocą algorytmu Kolonii Mrówek (ACO). Algorytm znajduje najlepszą trasę, która minimalizuje koszt dostaw, biorąc pod uwagę odległości i koszty podróży pojazdów.

### Główne funkcje:

- Wczytywanie danych z plików CSV i JSON.
- Generowanie macierzy odległości między punktami dostaw.
- Optymalizacja tras dostaw za pomocą algorytmu Kolonii Mrówek (ACO).
- Wyświetlanie najlepszej trasy i kosztu.

## Wymagania

Aby uruchomić program, musisz mieć zainstalowane następujące biblioteki:

- Python 3.x
- numpy
- pandas
- json

Możesz zainstalować wymagane biblioteki za pomocą poniższego polecenia:

```bash
pip install numpy pandas
```

## Instalacja

1. Sklonuj to repozytorium:

   ```bash
   git clone https://github.com/ProjektAEH/ProjektInfAeh.git
   cd ProjektInfAeh
   ```

2. Upewnij się, że masz zainstalowane wszystkie wymagane zależności, wykonując polecenie:

   ```bash
   pip install -r requirements.txt
   ```

## Użycie

1. Przygotuj pliki wejściowe:
   - **`deliveries.csv`**: Plik CSV z danymi o punktach dostaw. Przykład:
   
     ```
     ID,Latitude,Longitude,TimeWindow,Priority
     1,52.2297,21.0122,8:00-12:00,High
     2,50.0647,19.9450,9:00-13:00,Medium
     3,52.4064,16.9252,10:00-14:00,Low
     ```
   
   - **`fleet.json`**: Plik JSON z danymi o flocie pojazdów. Przykład:

     ```json
     [
       {"ID": "V001", "Capacity": 100, "CostPerKm": 0.5},
       {"ID": "V002", "Capacity": 50, "CostPerKm": 0.2}
     ]
     ```

2. Uruchom program:

   ```bash
   python3 program.py
   ```

3. Program wczyta dane z plików, wygeneruje macierz odległości między punktami dostaw, a następnie uruchomi algorytm Kolonii Mrówek (ACO), który znajdzie najlepszą trasę i obliczy jej koszt.

4. Program wyświetli wynik:
   - Najlepsza trasa (kolejność odwiedzanych punktów).
   - Najlepszy koszt (całkowity koszt podróży).

## Struktura plików

- `program.py`: Główny plik programu, który implementuje algorytm ACO.
- `deliveries.csv`: Plik CSV z danymi o punktach dostaw.
- `fleet.json`: Plik JSON z danymi o flocie pojazdów.
- `requirements.txt`: Plik z wymaganymi zależnościami (np. numpy, pandas).

## Przykład danych

### Przykładowa zawartość pliku `deliveries.csv`:

```
ID,Latitude,Longitude,TimeWindow,Priority
1,52.2297,21.0122,8:00-12:00,High
2,50.0647,19.9450,9:00-13:00,Medium
3,52.4064,16.9252,10:00-14:00,Low
```

### Przykładowa zawartość pliku `fleet.json`:

```json
[
  {"ID": "V001", "Capacity": 100, "CostPerKm": 0.5},
  {"ID": "V002", "Capacity": 50, "CostPerKm": 0.2}
]
```
