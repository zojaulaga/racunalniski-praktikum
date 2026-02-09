import pandas as pd
import numpy as np
from itertools import product

dates = pd.date_range(start="2023-01-01", end="2023-03-31", freq="D")
regions = ["Celje", "Ptuj", "Nova Gorica", "Škofja Loka"]
products = ["Vino", "Sir", "Sadje"]
combinations = list(product(regions, products, dates))

data = {
    "Regija": [combo[0] for combo in combinations],
    "Datum": [combo[2] for combo in combinations],
    "Izdelek": [combo[1] for combo in combinations],
    "Količina (kg/l)": np.random.randint(3, 30, size=len(combinations)),
    "Cena na enoto (€)": np.round(np.random.uniform(5, 20, size=len(combinations)), 2),
}

df = pd.DataFrame(data)
df.to_csv("vhodni-podatki.csv", index=False)
