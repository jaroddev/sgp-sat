class Sym4:
    
    def add_constraint(self, data):
        for player_id in range(1,  data.players + 1):
            for week_id in range(1, data.week):
                for other_player_id in range(1, player_id + 1):
                    variable = data.generate_variable(player_id, 2, 1, week_id)
                    next_variable = data.generate_variable(other_player_id, 2, 1, week_id + 1)

                    data.formula.append([
                        -variable,
                        -next_variable
                    ])