import csv

def write_bench(filename, metrics):
    print(filename)
    
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        
        header = __generate_header()
        rows = __generate_rows(metrics)

        writer.writerow(header)
        writer.writerows(rows)


def __generate_header():
    return ["instance", "clauses", "variables", "time"]


def __generate_rows(metrics):
    rows = []
    
    for metric in metrics:
        rows.append([
            metric.name, 
            metric.cl, 
            metric.var, 
            metric.time
        ])
    
    return rows