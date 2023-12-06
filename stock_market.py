import json
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import covariance, cluster
from urllib.error import URLError

def load_symbols(symbol_file):
    with open(symbol_file, 'r') as file:
        symbol_dict = json.load(file)
    return np.array(sorted(symbol_dict.items())).T

def fetch_financial_data(symbols):
    quotes = []
    for symbol in symbols:
        print(f'Fetching quote history for {symbol}', file=sys.stderr)
        url = (f'https://raw.githubusercontent.com/scikit-learn/examples-data/'
               f'master/financial-data/{symbol}.csv')
        try:
            quotes.append(pd.read_csv(url))
        except URLError as e:
            print(f"Error fetching data for {symbol}: {e}", file=sys.stderr)
    return quotes

def calculate_fluctuations(quotes):
    closing_quotes = np.vstack([q['close'] for q in quotes])
    opening_quotes = np.vstack([q['open'] for q in quotes])
    return closing_quotes - opening_quotes

def build_graph_model(delta_quotes):
    edge_model = covariance.GraphicalLassoCV(cv=3)
    X = delta_quotes.copy().T
    X /= X.std(axis=0)
    with np.errstate(invalid='ignore'):
        edge_model.fit(X)
    return edge_model

def perform_clustering(edge_model, names):
    _, labels = cluster.affinity_propagation(edge_model.covariance_)
    num_labels = labels.max()
    for i in range(num_labels + 1):
        print("Cluster", i + 1, "-->", ', '.join(names[labels == i]))
    return labels

def visualize_clusters(labels, names):
    plt.figure(figsize=(12, 8))  # Adjust the figure size
    for i in range(labels.max() + 1):
        plt.scatter(names[labels == i], [i]*np.sum(labels == i), label=f"Cluster {i+1}")

    plt.title("Financial Data Clustering")
    plt.xlabel("Company Names")
    plt.ylabel("Cluster")
    plt.xticks(rotation=90)  # Rotate the x-tick labels
    plt.legend()
    plt.tight_layout()  # Adjust the layout
    plt.show()

def main():
    symbol_file = 'symbol_map.json'
    symbols, names = load_symbols(symbol_file)
    quotes = fetch_financial_data(symbols)
    if not quotes:
        print("No data fetched. Exiting.", file=sys.stderr)
        return
    delta_quotes = calculate_fluctuations(quotes)
    edge_model = build_graph_model(delta_quotes)
    labels = perform_clustering(edge_model, names)
    visualize_clusters(labels, names)

if __name__ == "__main__":
    main()
