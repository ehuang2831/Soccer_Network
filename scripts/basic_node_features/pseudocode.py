
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

    return home_team_average, away_team_average, concat_match_feature_vector

"""
    cluster the team feature vectors using T-SNE or K-MEANS

    color by win, loss or cluster_id

    can also cluster concat_match_feature_vector

    generate 
    FEATURE_VECTOR_DICT = {}

    keys: match_id

    values: list of dicts
        v[0] = [home_team_id, away_team_id] 

        v[1] = [home_team_average, away_team_average]

        v[2] = [home_team_sum, away_team_sum]
        
        v[3] = z_u_list = [(player_u_id, z_u), ...] [HOME player feature vectors]
        
        v[4] = z_v_list = [(player_v_id, z_v), ...] [AWAY player feature vectors]



"""

def cluster_team_feature_vectors(all_match_id_list = None)

    vectors_to_cluster = []

    feature_vector_dict = {}

    for match_id in all_match_id_list:

        concat_match_feature_vector = get_match_aggregated_feature_vectors(match_id = None, home_team_id = None, away_team_id = None)

        # add to feature_vector_dict

        vectors_to_cluster.append(concat_match_feature_vector)

    STANDARD_CLUSTER_ROUTINE(vectors_to_cluster)
    
    visualize_clustering()

