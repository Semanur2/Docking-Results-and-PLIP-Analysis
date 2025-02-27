import pandas as pd  # Load the pandas library

# Read the affinity data correctly
affinity_df = pd.read_csv('C:/Users/139sa/Desktop/blac/affinity_values.csv', sep='\t', header=0, names=["Ligand", "Affinity"])

# Read the hydrogen bond data correctly
hbonds_df = pd.read_csv('C:/Users/139sa/Desktop/blac/hydrogen_bonds_results.txt', sep=',', header=0, names=["Ligand", "H-bond"])

# Print the affinity data
print("Affinity Data:")
print(affinity_df.head())

# Print the hydrogen bond data
print("\nHydrogen Bonds Data:")
print(hbonds_df.head())

# Remove any leading or trailing spaces if present
affinity_df['Ligand'] = affinity_df['Ligand'].str.strip()
hbonds_df['Ligand'] = hbonds_df['Ligand'].str.strip()

# Merge the affinity and hydrogen bond data based on the Ligand column
merged_df = pd.merge(affinity_df, hbonds_df, on="Ligand")

# Remove missing values (NaN) if any
merged_df.dropna(inplace=True)

# Display the merged dataset
print("\nMerged Data:")
print(merged_df.head())


import matplotlib.pyplot as plt

# Sort the dataset based on the number of hydrogen bonds in descending order
merged_df = merged_df.sort_values(by=['H-bond'], ascending=False)

# Set figure size
plt.figure(figsize=(12, 8))

# Create a scatter plot with colored points, where color and size vary by affinity values
scatter = plt.scatter(merged_df['H-bond'], merged_df['Affinity'], 
                      c=merged_df['Affinity'], cmap='viridis', s=100, edgecolors='k', alpha=0.7)

# Add axis labels and title
plt.xlabel('Hydrogen Bonds', fontsize=14)
plt.ylabel('Affinity (kcal/mol)', fontsize=14)
plt.title('Hydrogen Bonds vs Affinity Values', fontsize=16)

# Annotate each data point with the corresponding ligand name
for i, row in merged_df.iterrows():
    plt.text(row['H-bond'], row['Affinity'], row['Ligand'], fontsize=9, ha='right', va='bottom')

# Enable grid with a customized style
plt.grid(True, linestyle='--', alpha=0.7)

# Add a color bar to indicate affinity values
cbar = plt.colorbar(scatter)
cbar.set_label('Affinity (kcal/mol)', fontsize=12)

# Set limits for X and Y axes
plt.xlim(0, merged_df['H-bond'].max() + 1)
plt.ylim(merged_df['Affinity'].min() - 1, merged_df['Affinity'].max() + 1)

# Add legend
plt.legend(['Data points'], loc='upper right')
plt.tight_layout()

# Save the plot in high resolution
plt.savefig('hydrogen_bonds_affinity_plot.png', dpi=300)

# Show the plot
plt.show()
