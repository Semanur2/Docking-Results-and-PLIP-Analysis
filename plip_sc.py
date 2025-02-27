import os
import subprocess

# Folder containing the complex structures
complex_folder = "C:/Users/139sa/Desktop/blac/complexes"
output_folder = "C:/Users/139sa/Desktop/blac/output_folder"

# Create the output folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Define the path to the PLIP executable (plip.exe)
plip_path = "C:/Users/139sa/miniconda3/envs/myenv36/Scripts/plip.exe"

# Iterate through all files in the complex folder and run PLIP analysis for each complex
for complex_file in os.listdir(complex_folder):
    if complex_file.endswith(".pdb"):
        complex_path = os.path.join(complex_folder, complex_file)
        
        # Set the output file name to match the complex file name
        output_file = os.path.join(output_folder, complex_file.replace(".pdb", "_report"))
        
        # Execute the PLIP command
        subprocess.run([plip_path, '-f', complex_path, '-o', output_file, '-t', '-x'])

print("✅ Interaction analysis for all complexes is complete.")
