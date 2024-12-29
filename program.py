import numpy as np
import pandas as pd
import json

# Wczytywanie danych z plików
def load_data():
    deliveries = pd.read_csv("deliveries.csv")
    with open("fleet.json", "r") as f:
        fleet = json.load(f)

    return deliveries, fleet

# Przetwarzanie macierzy odległości
def generate_distance_matrix(deliveries):
    num_locations = len(deliveries)
    matrix = np.random.randint(100, 500, size=(num_locations, num_locations))
    np.fill_diagonal(matrix, 0)  # Odległość do siebie samego = 0
    return matrix

if __name__ == "__main__":
    deliveries, fleet = load_data()
    print("Punkty dostaw:\n", deliveries)
    print("Flota pojazdów:\n", fleet)

    # Generowanie macierzy odległości
    distance_matrix = generate_distance_matrix(deliveries)
    print("Macierz odległości:\n", distance_matrix)

    # Wykonanie algorytmu
    aco = AntColonyOptimization(
        distances=distance_matrix,
        n_ants=10,
        n_iterations=100,
        alpha=1.0,
        beta=2.0,
        evaporation_rate=0.5,
        q=100
    )

    best_route, best_cost = aco.optimize()
    print("Najlepsza trasa:", best_route)
    print("Najlepszy koszt:", best_cost)
