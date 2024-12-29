import numpy as np
import pandas as pd
import json
import random

class AntColonyOptimization:
    def __init__(self, distances, n_ants, n_iterations, alpha, beta, evaporation_rate, q):
        self.distances = distances
        self.pheromone = np.ones(self.distances.shape) / len(distances)
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.alpha = alpha  # wpływ feromonów
        self.beta = beta    # wpływ heurystyki (odwrotności odległości)
        self.evaporation_rate = evaporation_rate
        self.q = q  # intensywność feromonów
        self.all_nodes = range(len(distances))

    def _select_next_node(self, current_node, unvisited_nodes):
        pheromone = self.pheromone[current_node][unvisited_nodes]
        heuristic = 1 / self.distances[current_node][unvisited_nodes]
        probabilities = (pheromone ** self.alpha) * (heuristic ** self.beta)
        probabilities /= probabilities.sum()
        return np.random.choice(unvisited_nodes, p=probabilities)

    def _update_pheromones(self, all_routes, all_costs):
        self.pheromone *= (1 - self.evaporation_rate)
        for route, cost in zip(all_routes, all_costs):
            for i in range(len(route) - 1):
                self.pheromone[route[i], route[i + 1]] += self.q / cost

    def optimize(self):
        best_cost = float('inf')
        best_route = None

        for iteration in range(self.n_iterations):
            all_routes = []
            all_costs = []

            for ant in range(self.n_ants):
                current_node = random.choice(self.all_nodes)
                unvisited_nodes = list(self.all_nodes)
                unvisited_nodes.remove(current_node)
                route = [current_node]

                while unvisited_nodes:
                    next_node = self._select_next_node(current_node, unvisited_nodes)
                    route.append(next_node)
                    unvisited_nodes.remove(next_node)
                    current_node = next_node

                route.append(route[0])  # wracamy do początkowego punktu
                cost = sum(self.distances[route[i], route[i + 1]] for i in range(len(route) - 1))
                all_routes.append(route)
                all_costs.append(cost)

                if cost < best_cost:
                    best_cost = cost
                    best_route = route

            self._update_pheromones(all_routes, all_costs)

        return best_route, best_cost

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
    # Wczytanie danych
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
