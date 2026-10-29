from collections import deque

start = (3, 3, 0)
goal = (0, 0, 1)

moves = [
    (1, 0), (2, 0),
    (0, 1), (0, 2),
    (1, 1)
]

def safe(m, c):
    return (
        0 <= m <= 3 and 0 <= c <= 3
        and (m == 0 or m >= c)
        and (3-m == 0 or 3-m >= 3-c)
    )

queue = deque([(start, [])])
visited = {start}
solution = None

while queue:
    state, path = queue.popleft()
    m, c, boat = state

    if state == goal:
        solution = path
        break

    for dm, dc in moves:
        if boat == 0:
            new_state = (m-dm, c-dc, 1)
        else:
            new_state = (m+dm, c+dc, 0)

        nm, nc, nb = new_state

        if (
            0 <= nm <= 3 and 0 <= nc <= 3
            and safe(nm, nc)
            and new_state not in visited
        ):
            visited.add(new_state)
            queue.append(
                (new_state, path + [(dm, dc, new_state)])
            )

if solution is None:
    print("No solution found.")
else:
    print("Step 0: All are on the left bank.")

    for i, (dm, dc, state) in enumerate(solution, 1):
        m, c, boat = state
        side = "right" if boat == 1 else "left"

        print(
            f"Step {i}: Move {dm} missionary(s) "
            f"and {dc} cannibal(s) to the {side} bank."
        )
        print(f"Left: {m} missionaries, {c} cannibals")
        print(f"Right: {3-m} missionaries, {3-c} cannibals")

    print("Everyone crossed safely!")