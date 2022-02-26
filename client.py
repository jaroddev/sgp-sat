import subprocess
from time import sleep, time

BENCH_REPO: str = "bench"
CMD: str = "python3 main.py search"

MAX_WEEK = 9

MODEL_WITHOUT_SYM = "basic"
MODEL_WITH_SYM = "sym"

def shell_command(group_size, position, name=MODEL_WITHOUT_SYM):
    if name != "":
        fullname = f"-n {name}"
    else:
        fullname=""

    return f"{CMD} -g {group_size} -s {position} {fullname} -o ./{BENCH_REPO}/{name}-{group_size}-{position}.csv"


def fixed_config(fixed_group_size, fixed_pos, name=""):
    cmd = shell_command(fixed_group_size, fixed_pos, name)
    subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)


# Tests
if __name__ == "__main__":
    
    configs = [
        [3, 3],
        [5, 3],
        [6, 4],
        [7, 5],
        [8, 4],
        [9, 4],
    ]

    for config in configs:
        fixed_config(config[0], config[1], MODEL_WITHOUT_SYM)
        fixed_config(config[0], config[1], MODEL_WITH_SYM)
