def print_grid(grid: list[list[str]]):
    for row in grid:
        print("".join(row))
    print()


def make_grid(input: list[str], to_int=False):
    if to_int:
        return [[int(cell) for cell in row] for row in input]
    return [list(row) for row in input]

def is_out_of_bounds(grid, r, c):
    return r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0])
