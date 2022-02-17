class UncorrectOnePlayerForEachGroupAndPos:
    """
        Problem in indexes ???
        I had to code the incorrect version cause i coded the correct one without knowing it...
    """

    def add_constraint(self, data):
        for week_id in range(1, data.week + 1):
            for group_id in range(1, data.group + 1):
                for pos_id in range(1, data.group_size + 1):
                    for player_id in range(1,  data.players):
                        for next_player_id in range(player_id + 1, data.players + 1):
                            variable = data.generate_variable(player_id, pos_id, group_id, week_id)
                            next_variable = data.generate_variable(player_id, next_player_id, group_id, week_id)

                            data.formula.append([
                                -variable,
                                -next_variable
                            ])


class OnePlayerForEachGroupAndPos:

    def add_constraint(self, data):
        for week_id in range(1, data.week + 1):
            for group_id in range(1, data.group + 1):
                for pos_id in range(1, data.group_size + 1):
                    for player_id in range(1,  data.players):
                        for next_player_id in range(player_id + 1, data.players + 1):
                            variable = data.generate_variable(player_id, pos_id, group_id, week_id)
                            next_variable = data.generate_variable(next_player_id, pos_id, group_id, week_id)

                            data.formula.append([
                                -variable,
                                -next_variable
                            ])