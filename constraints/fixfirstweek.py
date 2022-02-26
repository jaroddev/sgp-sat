
class FixFirstWeek:
    def add_constraint(self, data):
        pos_id = 1
        group_id = 1
        
        for player_id in range(1,  data.players + 1):

            if pos_id == data.group_size:
                pos_id = 1
                group_id +=1
                continue

            variable = data.generate_variable(player_id, pos_id, group_id, 1)

            data.formula.append([
                variable,
            ])

            pos_id+=1