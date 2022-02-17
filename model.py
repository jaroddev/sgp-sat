from constraints.onceperweek import AtLeastOncePerWeek
from constraints.atmost import AtMostOncePerGroupPerWeek
from constraints.onegroupeachweek import OneGroupEachWeek
from constraints.eachposoneplayer import EachPosOnePlayer
from constraints.atmostoneplayerpergroupperpos import OnePlayerForEachGroupAndPos
from constraints.equivalence import Equivalence
from constraints.socialisation import Socialisation

class Data():

    def __init__(self, formula, group, group_size, week):
        """
            formula is the conjunction of clauses
            group is the number of group
            group_size is the number of position in a group
            number of golfer = group * groupe_size
            week = number of week
        """
    
        # should check if week, group, groupe_size is invalid
        # should check if formula is nil ??
        
        self.formula = formula

        self.group = group
        self.group_size = group_size

        self.players = self.group * self.group_size

        self.week = week

    @staticmethod
    def generate_variable(player_id, pos_id, group_id, week_id):
        # player can be higher than anything
        # pos cannot be higher than 10
        # group cannot be higher than 10
        # week cannot be higher than 10
        return player_id * 1000 + pos_id * 100 + group_id * 10 + week_id

    @staticmethod
    def generate_minimal_variable(player_id, group_id, week_id):
        # player can be higher than anything
        # group cannot be higher than 10
        # week cannot be higher than 10
        return player_id * 100 + group_id * 10 + week_id


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

        for constraint in constraints:
            constraint.add_constraint(self)

    def decode_results(self, res):
        pos = [ value for value in res if value > 0 ]
        return pos