def parse_input(input_file):
    list1, list2 = [], []
    with open(input_file, 'r') as file:
        for line in file:
            loc1, loc2 = list(map(int, line.split()))
            list1.append(loc1)
            list2.append(loc2)
    return list1, list2

def solve_part_one(list1, list2):
    total_distance = 0
    for l1, l2 in zip(sorted(list1), sorted(list2)):
        total_distance += abs(l1 - l2)

    return total_distance

def solve_part_two(list1, list2):
    freqs = {}
    for n in list2:
        freqs[n] = 1 + freqs.get(n, 0)

    similarity = 0
    for n in list1:
        f = freqs.get(n, 0)
        similarity += (n * f)
    
    return similarity


list1, list2 = parse_input("./input.txt")

print(f"Part One: {solve_part_one(list1, list2)}")
print(f"Part Two: {solve_part_two(list1, list2)}")
