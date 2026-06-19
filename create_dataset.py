import pandas as pd
import random

data = {
    "CustomerID": range(1, 101),
    "Name": [f"Customer{i}" for i in range(1, 101)],
    "Age": [random.randint(18, 60) for _ in range(100)],
    "City": [random.choice(["Delhi", "Mumbai", "Kanpur", "Lucknow", "Pune"]) for _ in range(100)],
    "Salary": [random.randint(20000, 100000) for _ in range(100)]
}

df = pd.DataFrame(data)

df.to_csv("datasets/raw_dataset.csv", index=False)

print("raw_dataset.csv created successfully")