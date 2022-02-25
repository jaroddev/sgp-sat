class Sym2:
    
    def add_constraint(self, data):
        for player_id in range(1,  data.players + 1):
            for group_id in range(1, data.group):
                for week_id in range(1, data.week + 1):
                    for other_player_id in range(1, player_id):
                    
                        variable = data.generate_variable(player_id, 1, group_id + 1, week_id)
                        next_variable = data.generate_variable(other_player_id, 1, group_id, week_id)

                        data.formula.append([
                            -variable,
                            -next_variable
                        ])