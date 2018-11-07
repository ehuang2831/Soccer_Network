
"""
    feature vector for a single player
"""

def get_single_player_features(match_id = None, player_id = None):
    # u indexes a player

    # z_u is their feature vector

    # z_u = [role (Midfielder, striker etc), 
    #        Passing Rate summed over neighbors
    #        Self Loss Rate
    #        Self Gain Rate
    #        1-hop Neighbor Passing Rates? [can be for all possible players]
    #        ]

    return z_u

"""
    concatenate feature vectors across home, away teams for a single match, 

    input to logistic regression
"""

def get_match_aggregated_feature_vectors(match_id = None, home_team_id = None, away_team_id = None):

    z_u_list = []
    for player_u in home_team:
        
        z_u = get_single_player_features()

        z_u_list.append(z_u)

    # same for z_v for players v in away_team

    home_team_average = np.mean(z_u_list)
    
    away_team_average = np.mean(z_v_list)

    concat_match_feature_vector = [home_team_average, away_team_average]    

    return concat_match_feature_vector


