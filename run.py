from pysat.formula import CNF
from pysat.solvers import Lingeling

from model import Data

# g - p - w
def read_parameters():
    formula = CNF()

    group = 4
    group_size = 2
    week = 2

    return Data(formula, group, group_size, week)


def run(data):

    with Lingeling(bootstrap_with=data.formula.clauses, with_proof=True) as solver:
        res = solver.solve()
        print(res)
        
        if not res:
            print(solver.get_proof())
        else:
            pos = data.decode_results(solver.get_model())
            print(pos)


if __name__ == "__main__":
    data = read_parameters()
    data.generate_formula()

    print(len(data.formula.clauses))
    run(data)