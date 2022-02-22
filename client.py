import subprocess
from time import sleep, time

BENCH_REPO: str = "bench"
CMD: str = "python3 run.py"

MAX_GROUP_SIZE = 2
MAX_POS = 2
MAX_WEEK = 9


def shell_command(group_size, position, week):
    return f"{CMD} -g {group_size} -s {position} -w {week} > ./{BENCH_REPO}/{group_size}-{position}-{week}.out"


def echo_csv(group_size, position, records):
    filename = f"./{BENCH_REPO}/{group_size}-{position}-times.csv"
    header = "week;elapsed\n"
    
    with open(filename, 'w') as file:
        file.write(header)
        for record in records:
            file.write(record)
        


def record_time(group_size, position, week, time):
    return f"{week};{time}\n"


def fixed_config(fixed_group_size, fixed_pos):
    time_records = ""

    for week in range(1,MAX_WEEK + 1):

        cmd = shell_command(fixed_group_size, fixed_pos, week)

        start = time()
        subprocess.run(cmd, timeout=10 ,shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
        end = time()

        record = record_time(fixed_group_size, fixed_pos, week, end-start)

        time_records = f"{time_records}{record}"

    echo_csv(fixed_group_size, fixed_pos, time_records)


# Tests
if __name__ == "__main__":

    # fixed_config(3, 3)
    # fixed_config(5, 3)
    # fixed_config(6, 4)
    # fixed_config(7, 5)

    # fixed_config(8, 4)
    # fixed_config(9, 4)