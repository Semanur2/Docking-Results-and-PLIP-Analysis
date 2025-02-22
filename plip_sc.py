import os
import subprocess

# Komplekslerin bulunduğu klasör
complex_folder = "C:/Users/139sa/Desktop/blac/complexes"
output_folder = "C:/Users/139sa/Desktop/blac/output_folder"

# Çıktı klasörü yoksa oluştur
os.makedirs(output_folder, exist_ok=True)

# PLIP'in komut satırı yolunu belirleyin (plip.exe)
plip_path = "C:/Users/139sa/miniconda3/envs/myenv36/Scripts/plip.exe"

# Komplekslerin üzerinden geçerek her biri için PLIP analizini çalıştır
for complex_file in os.listdir(complex_folder):
    if complex_file.endswith(".pdb"):
        complex_path = os.path.join(complex_folder, complex_file)
        
        # Çıktı dosyasının adını kompleks dosyasının adıyla aynı yap
        output_file = os.path.join(output_folder, complex_file.replace(".pdb", "_report"))
        
        # PLIP komutunu çalıştır
        subprocess.run([plip_path, '-f', complex_path, '-o', output_file, '-t', '-x'])

print("✅ Tüm komplekslerin etkileşim analizleri tamamlandı.")
