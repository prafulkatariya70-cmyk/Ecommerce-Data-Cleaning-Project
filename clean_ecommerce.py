import pandas as pd

df = pd.read_csv("messy_ecommerce_data.csv")

print(df.head())

df = df.drop_duplicates()

df["Customer"].fillna("Unknown",inplace=True)
df["Country"].fillna("Unknown",inplace=True)
df["Product"].fillna("Not Specified",inplace=True)
df["Category"].fillna("Not SPecified",inplace=True)

df["Country"] = df["Country"].str.strip().str.title()
df["Category"] = df["Category"].str.title()


df["Date"] = pd.to_datetime(df["Date"],errors="coerce")

df["Amount"].fillna(df["Amount"].mean(), inplace=True)


print("Total Revenue:", df["Amount"].sum())
print("\nRevenue by Country:")
print(df.groupby("Country")["Amount"].sum())

print("\nTop Products:")
print(df.groupby("Product")["Amount"].sum().sort_values(ascending=False))

df.to_csv("clean_ecommerce_data.csv", index=False)

print("File saved successfully!")