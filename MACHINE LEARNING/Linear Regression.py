
import pandas as pd
houses = {
    "Size (sq ft)": [1500, 2000, 2500, 3000, 1800, 2200],
    "Rooms": [3, 4, 3, 5, 3, 4],
    "Price": [300000, 400000, 350000, 500000, 320000, 420000],
}
df = pd.DataFrame(houses)
print("Available Houses Dataset:")
print(df)
try:
    rooms = int(input("\nEnter the number of rooms you want: "))
    min_size = int(input("Enter the minimum size of the house in square feet: "))
except ValueError:
    print("Please enter valid numbers for rooms and size.")
    exit()
filtered_houses = df[(df["Rooms"] == rooms) & (df["Size (sq ft)"] >= min_size)]
if not filtered_houses.empty:
    avg_price = filtered_houses["Price"].mean()
    max_price = filtered_houses["Price"].max()
    print("\nMatching Houses:")
    print(filtered_houses)
    print(f"\nAverage Price of Matching Houses: ${avg_price:.2f}")
    print(f"Maximum Price of Matching Houses: ${max_price:.2f}")
else:
    print("\nNo houses meet your criteria. Please adjust your preferences.")
