import pandas as pd  # pandas kütüphanesini yükleyin

# Affinity verisini doğru bir şekilde oku
affinity_df = pd.read_csv('C:/Users/139sa/Desktop/blac/affinity_values.csv', sep='\t', header=0, names=["Ligand", "Affinity"])

# H-bond verisini doğru bir şekilde oku
hbonds_df = pd.read_csv('C:/Users/139sa/Desktop/blac/hydrogen_bonds_results.txt', sep=',', header=0, names=["Ligand", "H-bond"])

# Affinity verisini yazdır
print("Affinity Data:")
print(affinity_df.head())

# H-bond verisini yazdır
print("\nHydrogen Bonds Data:")
print(hbonds_df.head())

# Eğer boşluk varsa temizleyelim
affinity_df['Ligand'] = affinity_df['Ligand'].str.strip()
hbonds_df['Ligand'] = hbonds_df['Ligand'].str.strip()

# Affinity ve H-bond verilerini birleştirelim
merged_df = pd.merge(affinity_df, hbonds_df, on="Ligand")

# Eksik değerleri (NaN) temizleyelim
merged_df.dropna(inplace=True)

# Birleştirilen veriyi görelim
print("\nMerged Data:")
print(merged_df.head())


import matplotlib.pyplot as plt

# Veriyi sıralayalım
merged_df = merged_df.sort_values(by=['H-bond'], ascending=False)

# Grafik boyutlarını ayarlayalım
plt.figure(figsize=(12, 8))

# Renkli noktalar, Affinity'ye göre renk değişimi ve boyut değişimi
scatter = plt.scatter(merged_df['H-bond'], merged_df['Affinity'], 
                      c=merged_df['Affinity'], cmap='viridis', s=100, edgecolors='k', alpha=0.7)

# Eksen etiketlerini ve başlıkları ekleyelim
plt.xlabel('Hydrogen Bonds', fontsize=14)
plt.ylabel('Affinity (kcal/mol)', fontsize=14)
plt.title('Hydrogen Bonds vs Affinity Values', fontsize=16)

# Grafik üzerine her veri noktasının ismini ekleyelim
for i, row in merged_df.iterrows():
    plt.text(row['H-bond'], row['Affinity'], row['Ligand'], fontsize=9, ha='right', va='bottom')

# Grid'i kaldırıp, rengini değiştirelim
plt.grid(True, linestyle='--', alpha=0.7)

# Renk barı ekleyelim
cbar = plt.colorbar(scatter)
cbar.set_label('Affinity (kcal/mol)', fontsize=12)

# X ve Y eksenleri için sınırları ayarlayalım
plt.xlim(0, merged_df['H-bond'].max() + 1)
plt.ylim(merged_df['Affinity'].min() - 1, merged_df['Affinity'].max() + 1)

# Grafiği gösterelim
plt.legend(['Data points'], loc='upper right')
plt.tight_layout()

# Yüksek çözünürlükte kaydedelim
plt.savefig('hydrogen_bonds_affinity_plot.png', dpi=300)

# Grafiği gösterelim
plt.show()
