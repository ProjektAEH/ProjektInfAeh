import pytest
import pandas as pd
import numpy as np
from program import load_data, generate_distance_matrix, AntColonyOptimization  # Zaimportuj odpowiednie funkcje

# Testy, które wcześniej podałem

def test_load_deliveries():
    deliveries, _ = load_data()
    assert deliveries.shape == (3, 5)
    assert deliveries['ID'][0] == 1
    assert deliveries['Priority'][2] == 'Low'

def test_load_fleet():
    _, fleet = load_data()
    assert len(fleet) == 2
    assert fleet[0]['ID'] == 'V001'
    assert fleet[1]['CostPerKm'] == 0.2

def test_generate_distance_matrix():
    deliveries = pd.DataFrame({
        'ID': [1, 2, 3],
        'Latitude': [52.2297, 50.0647, 52.4064],
        'Longitude': [21.0122, 19.9450, 16.9252]
    })
    distance_matrix = generate_distance_matrix(deliveries)
    assert distance_matrix.shape == (3, 3)
    assert np.all(np.diagonal(distance_matrix) == 0)

def test_full_integration():
    deliveries, fleet = load_data()
    distance_matrix = generate_distance_matrix(deliveries)
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
    assert len(best_route) == len(deliveries) + 1
    assert best_cost > 0
