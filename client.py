import subprocess
from time import sleep, time

BENCH_REPO: str = "bench"
CMD: str = "python3 run.py"

MAX_GROUP_SIZE = 2
MAX_POS = 2
MAX_WEEK = 9


def shell_command(group_size, position, week):
    return f"{CMD} -g {group_size} -s {position} -w {week} >> ./{BENCH_REPO}/{group_size}-{position}-{week}.out"


def echo_csv(records):
    filename = f"./{BENCH_REPO}/times.csv"
    header = "group_size;position;week;elapsed\n"
    
    with open(filename, 'w') as file:
        file.write(header)
        for record in records:
            file.write(record)
        


def time_record(group_size, position, week, time):
    return f"{group_size};{position};{week};{time}\n"



# Tests
if __name__ == "__main__":
    time_records = ""

    for group_size in range(1,MAX_GROUP_SIZE + 1):
        for position in range(1,MAX_POS + 1):
            for week in range(1,MAX_WEEK + 1):

                cmd = shell_command(group_size, position, week)

                start = time()
                subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
                end = time()

                record = time_record(group_size, position, week, end-start)

                time_records = f"{time_records}{record}"
    
    echo_csv(time_records)

