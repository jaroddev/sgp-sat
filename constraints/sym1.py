class Sym1:
    
    def add_constraint(self, data):
        for player_id in range(1,  data.players + 1):
            for other_player_id in range(1, player_id):
                for pos_id in range(1, data.group_size):
                    for group_id in range(1, data.group + 1):
                        for week_id in range(1, data.week + 1):
                            
                                variable = data.generate_variable(player_id, pos_id, group_id, week_id)
                                next_variable = data.generate_variable(other_player_id, pos_id + 1, group_id, week_id)

                                data.formula.append([
                                    -variable,
                                    -next_variable
                                ])