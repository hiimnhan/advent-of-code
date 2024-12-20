import heapq
from math import inf


def print_grid(grid: list[list[str]] | list[list[int]]):
    for row in grid:
        print("".join(str(cell) for cell in row))
    print()


def make_grid(input: list[str], to_int=False):
    if to_int:
        return [[int(cell) for cell in row] for row in input]
    return [list(row) for row in input]


def is_out_of_bounds(grid, r, c):
    return r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0])


def is_out_of_bounds_w_h(w, h, r, c):
    return r < 0 or c < 0 or r >= h or c >= w


def next_coord(r, c, dr, dc):
    return r + dr, c + dc


def get_valid_adj(w, h, r, c):
    return [
        (r + dr, c + dc)
        for dr, dc in DIRECTIONS
        if not is_out_of_bounds_w_h(w, h, r + dr, c + dc)
    ]


def get_adj(r, c):
    return [(r + dr, c + dc) for dr, dc in DIRECTIONS]


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


def make_grid_with_obstacles(w, h, obstacles):
    grid = []
    for r in range(h):
        row = []
        for c in range(w):
            row.append("#" if (r, c) in obstacles else ".")
        grid.append(row)
    return grid


def dijkstra(w, h, start, end, obstacles=set(), include_end=False):
    pq = []
    heapq.heappush(pq, (0, start))

    visited = set()

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node == end:
            return current_distance - include_end

        if current_node in visited:
            continue

        visited.add(current_node)

        x, y = current_node
        for dx, dy in DIRECTIONS:
            neighbor = (x + dx, y + dy)

            if (
                0 <= neighbor[0] < w
                and 0 <= neighbor[1] < h
                and neighbor not in obstacles
            ):
                if neighbor not in visited:
                    heapq.heappush(pq, (current_distance + 1, neighbor))

    return inf


def dijkstra_and_path(w, h, start, end, obstacles=set(), include_end=False):
    pq = []
    heapq.heappush(pq, (0, start, [start]))

    visited = set()

    while pq:
        current_distance, current_node, path = heapq.heappop(pq)

        if current_node == end:
            if include_end:
                return current_distance, path
            else:
                return current_distance - 1, path[:-1]

        if current_node in visited:
            continue

        visited.add(current_node)

        x, y = current_node
        for dx, dy in DIRECTIONS:
            neighbor = (x + dx, y + dy)

            if (
                0 <= neighbor[0] < w
                and 0 <= neighbor[1] < h
                and neighbor not in obstacles
            ):
                if neighbor not in visited:
                    heapq.heappush(
                        pq, (current_distance + 1, neighbor, path + [neighbor])
                    )

    return inf, []


def find_turning_points(path):
    if len(path) < 3:
        return []
    turning_points = []
    for i in range(1, len(path) - 1):
        prev = path[i - 1]
        curr = path[i]
        next = path[i + 1]
        # Check if direction changes
        if (curr[0] - prev[0], curr[1] - prev[1]) != (
            next[0] - curr[0],
            next[1] - curr[1],
        ):
            turning_points.append(curr)
    return turning_points


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

DIRECTIONS = [UP, RIGHT, DOWN, LEFT]
