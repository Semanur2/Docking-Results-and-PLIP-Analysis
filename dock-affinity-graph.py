import pandas as pd
import matplotlib.pyplot as plt

# Load the affinity values data with explicit header columns
affinity_df = pd.read_csv('C:/Users/139sa/Desktop/blac/affinity_values.csv', names=["Ligand", "Affinity"])

# Load the hydrogen bond data with explicit header columns
hbonds_df = pd.read_csv('C:/Users/139sa/Desktop/blac/hydrogen_bonds_results.txt', header=None, names=["Ligand", "H-bond"])

# Strip any leading/trailing spaces from the 'Ligand' columns in both dataframes
affinity_df['Ligand'] = affinity_df['Ligand'].str.strip()
hbonds_df['Ligand'] = hbonds_df['Ligand'].str.strip()

# Convert Affinity and H-bond columns to numeric (in case they are not already)
affinity_df['Affinity'] = pd.to_numeric(affinity_df['Affinity'], errors='coerce')
hbonds_df['H-bond'] = pd.to_numeric(hbonds_df['H-bond'], errors='coerce')

# Merge the dataframes on the "Ligand" column
merged_df = pd.merge(affinity_df, hbonds_df, on="Ligand")

# Drop rows with any missing values (if any exist)
merged_df.dropna(inplace=True)

# Sort by H-bond or Affinity to keep data consistent for plotting
merged_df = merged_df.sort_values(by=['H-bond'], ascending=False)

# Print the first few rows to confirm the merge worked correctly
print(merged_df.head())

# Plot the data
plt.figure(figsize=(10, 6))
plt.scatter(merged_df['H-bond'], merged_df['Affinity'], color='blue', label='Data points')

# Label the axes and title
plt.xlabel('Hydrogen Bonds')
plt.ylabel('Affinity (kcal/mol)')
plt.title('Hydrogen Bonds vs Affinity Values')

# Remove the grid
plt.grid(False)

# Display the plot
plt.legend()
plt.show()
