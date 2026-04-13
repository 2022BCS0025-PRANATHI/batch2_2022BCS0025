import pandas as pd
import json
import sys
import os

def train(data_path):
    df = pd.read_csv(data_path, sep=';')

    size = len(df)
    accuracy = 0.6 + size * 0.0001

    metrics = {
        "data_size": size,
        "accuracy": round(accuracy, 3)
    }

    os.makedirs("metrics", exist_ok=True)

    with open("metrics/metrics.json", "w") as f:
        json.dump(metrics, f)

if __name__ == "__main__":
    train(sys.argv[1])