

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


def next_coord(r, c, dr, dc):
    return r + dr, c + dc


def connected_regions(
    grid,
) -> dict[str, list[tuple[set[tuple[int, int]], int, int]]]:
    R, C = len(grid), len(grid[0])
    visited = [[False] * C for _ in range(R)]
    regions = {}

    def dfs(r, c, type):
        if is_out_of_bounds(grid, r, c) or visited[r][c] or grid[r][c] != type:
            return set(), set()
        visited[r][c] = True
        region_plots = {(r, c)}
        perimeter = set()

        directions = [RIGHT, DOWN, LEFT, UP]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if is_out_of_bounds(grid, nr, nc) or grid[nr][nc] != type:
                perimeter.add((r, c, dr, dc))
                continue

            if not visited[nr][nc]:
                new_plots, new_perimeter = dfs(nr, nc, type)
                region_plots.update(new_plots)
                perimeter.update(new_perimeter)
        return region_plots, perimeter

    for r in range(R):
        for c in range(C):
            if visited[r][c]:
                continue
            type = grid[r][c]
            plots, perimeter = dfs(r, c, type)
            if plots:
                sides = {}
                for x, y, dr, dc in perimeter:
                    if (dr, dc) in {UP, DOWN}:
                        key = (x, (dr, dc))
                        if key not in sides:
                            sides[key] = []
                        sides[key].append(y)
                    elif (dr, dc) in {LEFT, RIGHT}:
                        key = (y, (dr, dc))
                        if key not in sides:
                            sides[key] = []
                        sides[key].append(x)
                total_sides = 0
                for v in sides.values():
                    total_sides += 1
                    v.sort()
                    i = v.pop()
                    while v:
                        n = v.pop()
                        if i - n > 1:
                            total_sides += 1
                        i = n

                if type not in regions:
                    regions[type] = []
                regions[type].append((plots, len(perimeter), total_sides))
    return regions


def next_directions_by_degree(d, deg=90) -> tuple[int, int]:
    if deg == 90:
        return (d + 1) % 4, (d + 3) % 4
    if deg == 180:
        return (d + 2) % 4, (d + 2) % 4
    return (d + 1) % 4, (d + 3) % 4


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

DIRECTIONS = [UP, RIGHT, DOWN, LEFT]
