# Docking-Results-and-PLIP-Analysis
# Docking Results and PLIP Analysis

This repository contains the docking results of ligand-protein interactions, as well as the Protein-Ligand Interaction Profiler (PLIP) analysis of these interactions. The goal is to explore the binding modes, interactions, and affinity values of various ligands with the receptor.

## Docking Results

The docking results for various ligands are stored in the `docking_results/` directory. These results include the binding affinities, poses, and detailed docking parameters. The ligand-protein interactions are evaluated using AutoDock Vina.

- **Ligands Used:** The ligands for the docking simulations are stored in the `ligands/` directory and are in `.pdbqt` format.
- **Docking Parameters:** The docking was carried out using a predefined configuration file (`config.txt`).

## PLIP Analysis

The Protein-Ligand Interaction Profiler (PLIP) tool was used to analyze the interactions between the ligands and the protein. PLIP identifies and classifies various molecular interactions such as hydrogen bonds, hydrophobic interactions, salt bridges, and metal coordination.

### PLIP Results

The results of the PLIP analysis are stored in the `plip_results/` directory. These files contain detailed interaction profiles for each ligand-protein complex. The interactions include:

- **Hydrogen Bonds**
- **Hydrophobic Interactions**
- **Salt Bridges**
- **π-π Stacking**
- **π-cation Interactions**

You can check the interaction details for each ligand in the corresponding files.

### Example

Here is an example of the PLIP analysis output for one ligand:

- **Ligand:** `lig_1.pdbqt`
- **Binding Affinity:** -7.2 kcal/mol
- **Interactions:**
  - Hydrogen bonds with residues: TYR (A:211), ASP (A:224)
  - Hydrophobic interactions with residues: LEU (A:236), MET (A:239)
  - π-π stacking with residue: PHE (A:160)

## How to Reproduce

1. Clone the repository:
   ```bash
   git clone https://github.com/Semanur2/molecular_docking.git
