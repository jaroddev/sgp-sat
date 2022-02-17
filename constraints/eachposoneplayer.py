class EachPosOnePlayer:

    def add_constraint(self, data):
        for week_id in range(1, data.week + 1):
            for group_id in range(1, data.group + 1):
                for pos_id in range(1, data.group_size + 1):
                    clause = []
            
                    for player_id in range(1,  data.players + 1):
                        variable = data.generate_variable(player_id, pos_id, group_id, week_id)
                        clause.append(variable)

                    data.formula.append(clause)
