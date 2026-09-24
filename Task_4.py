import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset
df = pd.read_csv("Data_set 2 - Copy.csv")

# Step 2: Display the column names
print("Column Names:")
print(df.columns)

# Step 3: Count the frequency of each Investment Avenue
investment_counts = df["Investment_Avenues"].value_counts()

print("\nInvestment_Avenues Frequency:")
print(investment_counts)

# Step 4: Find the most preferred investment avenue
most_preferred = investment_counts.idxmax()
highest_frequency = investment_counts.max()

print("\nMost Preferred Investment_Avenues:")
print(most_preferred)

print("Number of People:")
print(highest_frequency)

# Step 5: Display percentage of preference
total_people = investment_counts.sum()
percentage = (highest_frequency / total_people) * 100

print(f"Percentage of Preference: {percentage:.2f}%")

# Step 6: Create a bar chart
plt.figure(figsize=(8, 5))

investment_counts.plot(kind="bar")

plt.title("Most Preferred Investment_Avenues")
plt.xlabel("Investment_Avenues")
plt.ylabel("Number of People")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()