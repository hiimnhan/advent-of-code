from collections import defaultdict


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
            print("----")
            print(type)
            plots, perimeter = dfs(r, c, type)
            if plots:
                corners = 0
                for x, y in plots:
                    top = next_coord(x, y, *UP)
                    left = next_coord(x, y, *LEFT)
                    right = next_coord(x, y, *RIGHT)
                    bottom = next_coord(x, y, *DOWN)

                    tr = top not in plots and right not in plots
                    tl = top not in plots and left not in plots
                    br = bottom not in plots and right not in plots
                    bl = bottom not in plots and left not in plots

                    print(
                        f"x: {x}, y: {y}, corners: {tl, tr, bl, br} -> {tl + tr + bl + br}"
                    )

                    corners += tl + tr + bl + br

                if type not in regions:
                    regions[type] = []
                regions[type].append((plots, len(perimeter), corners))
    return regions


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
