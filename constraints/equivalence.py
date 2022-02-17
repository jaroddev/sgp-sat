class Equivalence:

    def add_constraint(self, data):
        for player_id in range(1, data.players + 1):
            for group_id in range(1, data.group + 1):
                for week_id in range(1, data.week + 1):
                    
                    minimal_variable = data.generate_minimal_variable(player_id, group_id, week_id)

                    implication = [ -minimal_variable ]
                    sufficience = [ minimal_variable ]
                                       
                    for pos in range(1, data.group_size + 1):
                        
                        variable = data.generate_variable(player_id, pos, group_id, week_id)

                        implication.append(variable)    
                        sufficience.append(-variable)
                    
                    data.formula.append(implication)
                    data.formula.append(sufficience)