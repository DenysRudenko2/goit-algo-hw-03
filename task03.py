def console_output(rods):
    max_height = max(len(rod) for rod in rods.values())
    for level in range(max_height, 0, -1):
        for rod in ['A', 'B', 'C']:
            if len(rods[rod]) >= level:
                print(f"|{rods[rod][level-1]}|", end=" ")
            else:
                print("   ", end=" ")
        print()
    print("-" * 10)


def hanoi_tower(n, first, second, third, rods):
    if n == 1:
        rods[third].append(rods[first].pop())
        console_output(rods)
        return

    hanoi_tower(n - 1, first, third, second, rods)
    rods[third].append(rods[first].pop())
    console_output(rods)
    hanoi_tower(n - 1, second, first, third, rods)

# Number of disks
n = 3
rods = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
console_output(rods)
hanoi_tower(n, 'A', 'B', 'C', rods)