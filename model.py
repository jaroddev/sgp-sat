from numpy import array

from constraints.onceperweek import AtLeastOncePerWeek
from constraints.atmost import AtMostOncePerGroupPerWeek
from constraints.onegroupeachweek import OneGroupEachWeek
from constraints.eachposoneplayer import EachPosOnePlayer
from constraints.atmostoneplayerpergroupperpos import OnePlayerForEachGroupAndPos
from constraints.equivalence import Equivalence
from constraints.socialisation import Socialisation

from constraints.sym1 import Sym1
from constraints.sym2 import Sym2
from constraints.sym4 import Sym4

class Model():

    def __init__(self, formula, group, group_size, week, name="basic",):
        """
            formula is the conjunction of clauses
            group is the number of group
            group_size is the number of position in a group
            number of golfer = group * groupe_size
            week = number of week
        """
    
        self.name = name

        self.formula = formula

        self.group = group
        self.group_size = group_size

        self.players = self.group * self.group_size

        self.week = week

        # might be better to just keep this as a temporaru variable
        self.number_of_var = self.players * group * group_size * week
        self.number_of_minimal_var = self.players * group * week

        var_range = range(1, 1 + self.number_of_var)
        variables = array(var_range)
        self.variables = variables.reshape(self.players, group_size, group, week)

        minimal_var_range = range(1 + self.number_of_var, 1 + self.number_of_var + self.number_of_minimal_var)
        minimal_variables = array(minimal_var_range)
        self.minimal_variables = minimal_variables.reshape(self.players, group, week)

    def display(self, solution):
        message = ""
               
        for week in range(len(solution)):
            message += f"////////////////////////////// week: {week + 1} //////////////////////////////\n"
            
            for group in range(len(solution[week])):
                message += f"------------------- group : {group + 1} -------------------\n"

                for pos in range(len(solution[week][group])):
                    message += f"pos {pos + 1}: player {solution[week][group][pos]}\n"


        return message

    def get_solution(self, result):
        schedule = []
    
        for week_id in range(self.week):
            week = []
            for group_id in range(self.group):
                group = []
                for pos_id in range(self.group_size):
                    for player_id in range(self.players):                        
                        variable = self.variables[player_id, pos_id, group_id, week_id]
                        if variable in result:
                            group.append(player_id + 1)

                week.append(group)
            schedule.append(week)

        return schedule

    def generate_variable(self, player_id, pos_id, group_id, week_id):
        variable = self.variables[player_id - 1, pos_id - 1, group_id - 1, week_id - 1]
        return int(variable)
        
    def generate_minimal_variable(self, player_id, group_id, week_id):
        variable =  self.minimal_variables[player_id - 1, group_id - 1, week_id - 1]
        return int(variable)

    def generate_formula(self):
        constraints = [
            AtLeastOncePerWeek(),
            AtMostOncePerGroupPerWeek(),
            OneGroupEachWeek(),
            EachPosOnePlayer(),
            OnePlayerForEachGroupAndPos(),
            Equivalence(),
            Socialisation(),
        ]

        if self.name == "symup":
            constraints.append(Sym1())
            constraints.append(Sym2())
            constraints.append(Sym4())

        for constraint in constraints:
            constraint.add_constraint(self)

    def decode_results(self, res):
        highest_possible_variable = self.players * self.group * self.group_size * self.week
        return [ 
            value for value in res 
            if value > 0 
            and value < highest_possible_variable + 1 
        ]
