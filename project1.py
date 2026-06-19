import pandas as pd

df = pd.read_csv("datasets/raw_dataset.csv")

print("Original Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

for col in df.select_dtypes(include=['number']).columns:
    df[col] = df[col].fillna(df[col].median())

for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

duplicates = df.duplicated().sum()
print("\nDuplicates Found:", duplicates)

df = df.drop_duplicates()

for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].str.strip()

df.to_csv("datasets/cleaned_dataset.csv", index=False)

print("\nData Cleaning Completed Successfully")
print("Final Shape:", df.shape)