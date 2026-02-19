import os
import subprocess

def run_cmd(cmd):
    subprocess.run(cmd, shell=True)

# 1. Initialize Git
run_cmd("git init")

# 2. Generate initial noise (Fake files)
for i in range(1, 4):
    with open(f"decoy_module_{i}.py", "w") as f:
        f.write(f"print('This is useless decoy file {i}')\n")
    run_cmd(f"git add decoy_module_{i}.py")
    run_cmd(f'git commit -m "Added initial decoy modules batch {i}"')

# 3. Create the Real Clue (UPDATE THIS PART)
with open("debug_config.json", "w") as f:
    f.write('{\n  "target_ip": "10.142.244.239",\n  "network": "Codex_Node_5",\n  "password": "hacktheplanet",\n  "hidden_terminal_port": 65000\n}')
run_cmd("git add debug_config.json")
run_cmd('git commit -m "Testing new terminal connection on port 65000"')

# 4. Delete the Clue
run_cmd("git rm debug_config.json")
run_cmd('git commit -m "SECURITY FIX: Removed debug config file!!"')

# 5. More noise
for i in range(4, 8):
    with open(f"decoy_module_{i}.py", "w") as f:
        f.write(f"print('This is useless decoy file {i}')\n")
    run_cmd(f"git add decoy_module_{i}.py")
    run_cmd(f'git commit -m "WIP: refactoring codebase part {i}"')

print("Messy Git Repo Created!")
