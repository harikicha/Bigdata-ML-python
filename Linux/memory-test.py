import numpy as np 

instance_size_gib_advertised = 20 # CHANGE THIS VALUE 

# Usable memory scaling factor - accounts for system and numpy overhead. 
# Change this to 1.00 to force a MemoryError. 
# 0.90 is slightly lower than necessary, the actual value is somewhere around 0.95. 
scaling_factor = 0.90
memory_to_fill_gib = instance_size_gib_advertised * scaling_factor 

np.empty(int(memory_to_fill_gib * ((1024) ** 3) * 8 / 32), dtype=np.float32)