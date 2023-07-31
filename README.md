# PDBcheck
The general algorith consist of three different parts. Dowload, Resolution check and sequence lenght check. The algorithm first downloads PDB files as extension of 
cif. and it creates a folder called PDB. After the initialization occur the algorithm check the protein structures by creating a threshold on two different 
endpoints: 
Protein resolution and sequence lenght. 

The threshold for the 'Resolution' (Å) is determined to be 3.00, for particular reasons. A protein with a resolution above 2.7 Å is considered to be low-resolution
structure, while proteins with a resolution between 2.7 and 1.8 Å are classified as medium resolution structures, and those below 1.8 Å resolution are typically 
classified as high-resolution structures (Minor 2007; Wlodawer et al. 2008). After 3.00 Å errors are very likely and many sidechains placed with wrong rotamer.
(Blow, 2002).

Sequence lenght can be interchangable according to the research. In the case of superimposing experimental structures to Alphafold structure, the threshold is
determined to be 100 aminoacids as seq lenght.
