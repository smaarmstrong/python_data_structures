#!/usr/bin/env python3
import pyhash

bit_vector = [0] * 20
print(bit_vector)

# Non cryptographic hash functions (Murmur and FNV)
fnv = pyhash.fnv1_32()
murmur = pyhash.murmur3_32()

# Calculate the output of FNV and Murmur hash functions for Ricky and Julian
fnv_ricky = fnv("Ricky") % 20
murmur_ricky = murmur("Ricky") % 20
fnv_julian = fnv("Julian") % 20
murmur_julian = murmur("Julian") % 20

print(f"fnv ricky {fnv_ricky}")
print(f"fnv julian {fnv_julian}")

print(f"murmur ricky {murmur_ricky}")
print(f"murmur julian {murmur_julian}")

bit_vector[fnv_ricky] = 1
bit_vector[fnv_julian] = 1

bit_vector[murmur_ricky] = 1
bit_vector[murmur_julian] = 1

print(bit_vector)

# Is Bubbles on the scene?
fnv_bubbles = fnv("Bubbles") % 20
murmur_bubbles = murmur("Bubbles") % 20

print(f"fnv bubbles {fnv_bubbles}")
print(f"murmur bubbles {murmur_bubbles}")

if bit_vector[fnv_bubbles] == 1 or bit_vector[murmur_bubbles] == 1:
    print("Bubbles might already be on the scene.")
else:
    print("Bubbles is definitely not on the scene.")
