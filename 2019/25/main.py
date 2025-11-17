import re
import sys
from collections import defaultdict, deque
from itertools import combinations
from pathlib import Path


# --- Intcode Computer ---
class IntcodeComputer:
    def __init__(self, program):
        self.memory = defaultdict(int)
        for i, val in enumerate(program):
            self.memory[i] = val
        self.ip = 0
        self.relative_base = 0
        self.inputs = deque()
        self.halted = False

    def add_input(self, ascii_str):
        for char in ascii_str:
            self.inputs.append(ord(char))

    def run(self):
        out = []
        while True:
            opcode = self.memory[self.ip] % 100
            modes = [int(x) for x in str(self.memory[self.ip] // 100)[::-1]]

            def get_param(index):
                mode = modes[index] if index < len(modes) else 0
                val = self.memory[self.ip + 1 + index]
                if mode == 0: return self.memory[val]
                if mode == 1: return val
                if mode == 2: return self.memory[self.relative_base + val]
                return 0

            def set_param(index, val):
                mode = modes[index] if index < len(modes) else 0
                addr = self.memory[self.ip + 1 + index]
                if mode == 2: addr += self.relative_base
                self.memory[addr] = val

            if opcode == 99:
                self.halted = True
                return "".join(chr(o) for o in out)

            if opcode == 1: # Add
                set_param(2, get_param(0) + get_param(1))
                self.ip += 4
            elif opcode == 2: # Multiply
                set_param(2, get_param(0) * get_param(1))
                self.ip += 4
            elif opcode == 3: # Input
                if not self.inputs:
                    return "".join(chr(o) for o in out)
                set_param(0, self.inputs.popleft())
                self.ip += 2
            elif opcode == 4: # Output
                out.append(get_param(0))
                self.ip += 2
            elif opcode == 5: # Jump-if-true
                self.ip = get_param(1) if get_param(0) != 0 else self.ip + 3
            elif opcode == 6: # Jump-if-false
                self.ip = get_param(1) if get_param(0) == 0 else self.ip + 3
            elif opcode == 7: # Less than
                set_param(2, 1 if get_param(0) < get_param(1) else 0)
                self.ip += 4
            elif opcode == 8: # Equals
                set_param(2, 1 if get_param(0) == get_param(1) else 0)
                self.ip += 4
            elif opcode == 9: # Adjust relative base
                self.relative_base += get_param(0)
                self.ip += 2

# --- Game Logic ---

FORBIDDEN_ITEMS = {
    "giant electromagnet", "infinite loop", "escape pod",
    "molten lava", "photons"
}

REVERSE_DIR = {'north': 'south', 'south': 'north', 'east': 'west', 'west': 'east'}

def parse_output(output):
    """
    Parses the output from the Droid.
    Returns (room_name, doors, items, raw_lines).
    Returns (None, ...) if no room header is found.
    """
    if "== " not in output:
        return None, [], [], output

    # Get the LAST room description in the buffer
    last_block_index = output.rfind("== ")
    relevant_text = output[last_block_index:]

    lines = relevant_text.strip().split('\n')
    room_name = ""
    doors = []
    items = []

    mode = None
    for line in lines:
        if line.startswith('== '):
            room_name = line.strip(' =')
        elif line == "Doors here lead:":
            mode = "doors"
        elif line == "Items here:":
            mode = "items"
        elif line.startswith('- '):
            if mode == "doors":
                doors.append(line[2:])
            elif mode == "items":
                items.append(line[2:])
        elif line == "":
            mode = None

    return room_name, doors, items, lines

def solve_day_25(lines):
    program = [int(x) for x in lines[0].split(',')]
    computer = IntcodeComputer(program)

    # Initial Boot
    output = computer.run()

    adj = defaultdict(dict)
    visited = set()
    all_items = []

    checkpoint_room = "Security Checkpoint"
    sensor_dir = None

    # Parse Initial Room
    current_room, doors, items, _ = parse_output(output)
    if current_room is None:
        # If start fails, force a look (unlikely)
        computer.add_input("look\n")
        output = computer.run()
        current_room, doors, items, _ = parse_output(output)

    visited.add(current_room)

    # Helper: Loot logic
    def take_available_items(out_text):
        nonlocal output
        _, _, cur_items, _ = parse_output(out_text)
        for it in cur_items:
            if it not in FORBIDDEN_ITEMS:
                computer.add_input(f"take {it}\n")
                res = computer.run()
                all_items.append(it)
                output = res # Update global last output

    take_available_items(output)

    # DFS Initialization
    stack = [iter(doors)]
    path_rooms = [current_room]
    path_dirs = []

    print("--- Exploring Ship ---")

    while stack:
        parent_room = path_rooms[-1]

        # Get next door
        try:
            move_dir = next(stack[-1])
        except StopIteration:
            # Backtrack
            stack.pop()
            path_rooms.pop()
            if path_dirs:
                back = REVERSE_DIR[path_dirs.pop()]
                computer.add_input(f"{back}\n")
                computer.run() # consume output
            continue

        # ATTEMPT MOVE
        computer.add_input(f"{move_dir}\n")
        res = computer.run()

        # --- ROBUSTNESS CHECK ---
        # If response doesn't have "== ", we might have slipped or hit a wall without description.
        # Force a "look" to be sure where we are.
        if "== " not in res:
            computer.add_input("look\n")
            res += computer.run()

        new_room, new_doors, new_items, _ = parse_output(res)

        # Handle Parsing Failures (e.g., "You can't go that way")
        if new_room is None:
            # Treat as a wall/dead-end
            continue

        # CHECK FOR SENSOR
        hit_sensor = (new_room == "Pressure-Sensitive Floor") or \
                     ("Alert!" in res) or \
                     ("lighter" in res) or \
                     ("heavier" in res)

        if hit_sensor:
            print(f"  > Found Sensor Direction: {move_dir} (from {parent_room})")
            sensor_dir = move_dir
            # If we hit sensor, we are effectively blocked (wall).
            # The game usually resets us to the previous room automatically.
            continue

        # STANDARD TRAVERSAL
        if new_room in visited:
            # Backtrack immediately physically
            computer.add_input(f"{REVERSE_DIR[move_dir]}\n")
            computer.run()

            # Map connection
            adj[parent_room][move_dir] = new_room
            adj[new_room][REVERSE_DIR[move_dir]] = parent_room
        else:
            # New Room
            visited.add(new_room)
            adj[parent_room][move_dir] = new_room
            adj[new_room][REVERSE_DIR[move_dir]] = parent_room

            path_rooms.append(new_room)
            path_dirs.append(move_dir)
            stack.append(iter(new_doors))

            take_available_items(res)

    print(f"Mapping Complete. Items: {all_items}")

    # --- Pathfinding to Checkpoint ---
    # Reset view to confirm start room
    computer.add_input("look\n")
    start_out = computer.run()
    start_room_name, _, _, _ = parse_output(start_out)

    if start_room_name is None:
        start_room_name = current_room # Fallback

    q = deque([(start_room_name, [])])
    seen = {start_room_name}
    path_to_cp = None

    while q:
        r, p = q.popleft()
        if r == checkpoint_room:
            path_to_cp = p
            break
        for d, n in adj[r].items():
            if n not in seen:
                seen.add(n)
                q.append((n, p + [d]))

    if path_to_cp is None:
        return f"Error: Could not find path to '{checkpoint_room}'. Rooms mapped: {len(adj)}"

    print(f"Walking to Checkpoint: {path_to_cp}")
    for m in path_to_cp:
        computer.add_input(f"{m}\n")
        computer.run()

    # --- Brute Force ---
    if not sensor_dir:
        # Fallback heuristic
        computer.add_input("look\n")
        _, cp_doors, _, _ = parse_output(computer.run())
        way_back = REVERSE_DIR[path_to_cp[-1]] if path_to_cp else None
        candidates = [d for d in cp_doors if d != way_back]
        sensor_dir = candidates[0] if candidates else 'north'

    print(f"Brute forcing... (Sensor: {sensor_dir})")

    inv = set(all_items)

    # Gray Code-ish Iteration
    for i in range(len(all_items) + 1):
        for combo in combinations(all_items, i):
            target = set(combo)

            to_drop = inv - target
            for item in to_drop:
                computer.add_input(f"drop {item}\n")
                while not computer.run().endswith("Command?\n"): pass

            to_take = target - inv
            for item in to_take:
                computer.add_input(f"take {item}\n")
                while not computer.run().endswith("Command?\n"): pass

            inv = target

            # Try Sensor
            computer.add_input(f"{sensor_dir}\n")
            res = computer.run()

            if "Alert" in res or "lighter" in res or "heavier" in res:
                continue

            if "Analysis complete" in res or "get in by typing" in res:
                print("\n--- ACCESS GRANTED ---")
                match = re.search(r'\d{5,}', res)
                if match:
                    return match.group(0)
                else:
                    return res

    return "Password not found."

def part2(lines):
    return "Click the star!"

if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print("Part 1 Answer:", solve_day_25(lines))
    print("Part 2:", part2(lines))
