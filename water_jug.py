from collections import deque

a = int(input("Enter capacity of Jug A: "))
b = int(input("Enter capacity of Jug B: "))
target = int(input("Enter target amount: "))

start = (0, 0)
queue = deque([(start, [])])
visited = {start}
solution = None

while queue:
    (x, y), path = queue.popleft()

    if x == target or y == target:
        solution = path
        break

    moves = [
        ("Fill Jug A", a, y),
        ("Fill Jug B", x, b),
        ("Empty Jug A", 0, y),
        ("Empty Jug B", x, 0),
        ("Pour A into B",
         x - min(x, b-y), y + min(x, b-y)),
        ("Pour B into A",
         x + min(y, a-x), y - min(y, a-x))
    ]

    for action, nx, ny in moves:
        state = (nx, ny)

        if state != (x, y) and state not in visited:
            visited.add(state)
            queue.append((state, path + [(action, nx, ny)]))

if solution is None:
    print("No solution found.")
else:
    print("Step 0: Start -> A = 0, B = 0")

    for i, (action, x, y) in enumerate(solution, 1):
        print(f"Step {i}: {action} -> A = {x}, B = {y}")

    print("Target achieved:", target, "litre(s)")