def rabbits(n, k):
    # Initial rabbit pairs
    f1 = 1
    f2 = 1

    # Generate sequence up to month n
    for i in range(3, n + 1):
        fn = f2 + k * f1
        f1 = f2
        f2 = fn

    return f2

# Example
n = 29
k = 5

print(rabbits(n, k))

