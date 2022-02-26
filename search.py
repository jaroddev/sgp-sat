from time import time

from pysat.formula import CNF
from pysat.solvers import Lingeling

from model import Model
from writer import write_bench
from custom_timeout import timeout, TimeoutError


class UNSAT(Exception):
    pass


class Metric:

    def __init__(self):
        self.name = ""
        self.cl = 0
        self.var = 0
        self.time = 0

    def __str__(self):
        message = ""

        message += f"Model name: {self.name}\n"
        message += f"CL: {self.cl}\n"
        message += f"Variables: {self.var}\n"
        message += f"Time: {self.time}\n"

        return message


    def name_from_model(self, model):
        self.name = f"{model.group}-{model.group_size}-{model.week}"


def search(args):
    metrics = []
    week = 1
    
    while(True):
        try:
            args.week = week
            model = create_model(args)
            metric = Metric()
            metric.name_from_model(model)

            start = time()
            model.generate_formula()
            solve_instance(model, metric)
            end = time()

            metric.time = end - start

            metric.cl = len(model.formula.clauses)
            metric.var = model.formula.nv

            metrics.append(metric)
            week+=1
        except TimeoutError:
            print("too long !!")
            break
        except UNSAT:
            print("UNSAT")
            break
    
    write_bench(args.file, metrics)
    

def create_model(args):
    formula = CNF()

    group = args.group
    group_size = args.group_size
    week = args.week
    name = args.name

    return Model(formula, group, group_size, week, name)

@timeout(10, use_signals=False)
def solve_instance(model, metric):
    with Lingeling(bootstrap_with=model.formula.clauses, with_proof=True) as solver:
        is_sat = solver.solve()
                
        if not is_sat:
            raise UNSAT