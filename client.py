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



# Tests
if __name__ == "__main__":

    for group_size in range(1,MAX_GROUP_SIZE + 1):
        for position in range(1,MAX_POS + 1):
            time_records = ""
            
            for week in range(1,MAX_WEEK + 1):

                cmd = shell_command(group_size, position, week)

                start = time()
                subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
                end = time()

                record = record_time(group_size, position, week, end-start)

                time_records = f"{time_records}{record}"
    
            echo_csv(group_size, position, time_records)

