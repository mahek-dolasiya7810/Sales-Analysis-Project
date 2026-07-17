import pandas as pd
import matplotlib.pyplot as plt

# Read Excel file
df = pd.read_excel("Sales Data.xlsx")

print(df.head())
print(df.shape)
print(df.columns)

# Display the Revenue column
print("\n Revenue column:")
print(df["Revenue"])

# Calculate the  Total Revenue
total_rev = df["Revenue"].sum()

print("\nTotal Revenue:")
print(total_rev)

# Calculate Average Revenue
avg_rev = df["Revenue"].mean()

print("\n Average Revenue:")
print(avg_rev)

# Total Quantity sold
total_quant = df["Quantity"].sum()

print("\n Total Quantity sold:")
print(total_quant)

# Basic Analysis
print("\n Total Revenue:")
print(df["Revenue"].sum())

print("\nAverage Revenue:")
print(df["Revenue"].mean())

print("\nHighest Revenue:")
print(df["Revenue"].max())

print("\nLowest Revenue:")
print(df["Revenue"].min())

print("\n Revenue by Category:")
print(df.groupby("Category")["Revenue"].sum())

print("\n Orders By City:")
print(df["City"].value_counts())

print("\n Top 10 products:")
print(df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(10))

# Revenue By Category (Bar chart)
cat_rev = df.groupby("Category")["Revenue"].sum()

plt.figure(figsize=(8,5))

cat_rev.plot(
    kind="bar",
    color="skyblue",
    edgecolor="black"
)

plt.title("Revenue by Category", fontsize=16)
plt.xlabel("Category", fontsize=12)
plt.ylabel("Revenue", fontsize=12)

plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig("Revenue_By_Category.png")

plt.show()

# Pie chart 
plt.figure(figsize=(7,7))

cat_rev.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Revenue Distribution by Category")

plt.ylabel("")

plt.tight_layout()

plt.savefig("Revenue_Distribution.png")

plt.show()


top_products = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(9,5))

top_products.plot(
    kind="bar",
    color="green",
    edgecolor="black"
)

plt.title("Top 10 Products by Revenue")

plt.xlabel("Product")

plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig("Top_10_Products.png")

plt.show()


city_orders = df["City"].value_counts()

plt.figure(figsize=(8,5))

city_orders.plot(
    kind="bar",
    color="orange",
    edgecolor="black"
)

plt.title("Orders by City")

plt.xlabel("City")

plt.ylabel("Number of Orders")

plt.xticks(rotation=45)

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig("Orders_by_City.png")

plt.show()

print("Excel files saved successfully!")