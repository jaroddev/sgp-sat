class Socialisation:

    # correction applied ???
    def add_constraint(self, data):
        for week_id in range(1, data.week):
            for next_week_id in range(week_id + 1, data.week + 1):
                for group_id in range(1, data.group + 1):
                    for other_group_id in range(1, data.group + 1):
                        for player_id in range(1, data.players):
                            for next_player_id in range(player_id + 1, data.players + 1):
                                
                                variable = data.generate_minimal_variable(player_id, group_id, week_id)
                                next_variable = data.generate_minimal_variable(next_player_id, group_id, week_id)

                                variable_other_week = data.generate_minimal_variable(player_id, other_group_id, next_week_id)
                                variable_next_other_week = data.generate_minimal_variable(next_player_id, other_group_id, next_week_id)

                                data.formula.append([
                                    -variable,
                                    -next_variable,
                                    -variable_other_week,
                                    -variable_next_other_week,
                                ])