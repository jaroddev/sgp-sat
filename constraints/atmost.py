class AtMostOncePerGroupPerWeek:
    
    def add_constraint(self, data):
        for player_id in range(1,  data.players + 1):
            for week_id in range(1, data.week + 1):
                for group_id in range(1, data.group + 1):
                    for pos_id in range(1, data.group_size):
                        for next_pos_id in range(pos_id + 1, data.group_size + 1):
                            variable = data.generate_variable(player_id, pos_id, group_id, week_id)
                            next_variable = data.generate_variable(player_id, next_pos_id, group_id, week_id)

                            data.formula.append([
                                -variable,
                                -next_variable
                            ])