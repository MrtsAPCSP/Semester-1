def make_part1(type):
    print("Part 1:", type)
    return 2.5  # cost

def make_part2(type):
    print("Part 2:", type)
    return 3.0  # cost

def assemble_product(p1, p2):
    print("Product assembled with", p1, "and", p2)

def total_cost(cost1, cost2):
    return cost1 + cost2

# Sample Run
cost_a = make_part1("Metal Frame")
cost_b = make_part2("Sensor Chip")
assemble_product("Metal Frame", "Sensor Chip")
final = total_cost(cost_a, cost_b)
print("Total Cost: $", final)


