from itertools import permutations, combinations


l = input("Enter elements separated by spaces: ").split()


print("Permutations:")
print(list(permutations(l)))

# Display combinations
print("\nCombinations:")
for r in range(1, len(l) + 1):
    print(f"Length {r}: {list(combinations(l, r))}")
