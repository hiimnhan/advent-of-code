def print_grid(grid: list[list[str]]):
    for row in grid:
        print("".join(row))
    print()


def make_grid(input: list[str]):
    return [list(row) for row in input]
