from src.data.data_utils import pdb_to_tensor
import os

filename = "1A9N_1_Q.pdb"
sequence, coords, sec_struct, sasa = pdb_to_tensor(os.path.join("/Users/marinafranca/Desktop/inverse-folding-problem/src/data/", "raw", filename))
print(sequence)
print(coords)
print(sasa)