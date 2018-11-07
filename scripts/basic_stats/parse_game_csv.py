from __future__ import division
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import snap
import numpy as np
import sys,os
from scipy.sparse import *
import itertools
import pandas

# configure paths
####################
ROOT_SOCCER_DIR=os.environ['ROOT_SOCCER_DIR']
sys.path.append(ROOT_SOCCER_DIR)

UTILS_DIR = ROOT_SOCCER_DIR + '/utils/'
sys.path.append(UTILS_DIR)

DATA_DIR = ROOT_SOCCER_DIR + '/data/'
EXAMPLE_GRAPH_DIR = DATA_DIR + '/example_graphs/'

GAME_CSV_DIR = DATA_DIR + '/raw_soccer_csv/'

####################

from basic_snap_utils import *
from textfile_utils import *

if __name__ == '__main__':
    print 'ROOT_SOCCER_DIR: ', ROOT_SOCCER_DIR

    league_list = ['epl']


    for league in league_list:
        csv_fname = '/'.join([GAME_CSV_DIR, league,  league + '.csv'])

        df = pandas.read_csv(csv_fname)

        print 'COLUMNS: ', list(df)

        # COLUMNS:  ['season_id', 'match_id', 'home_team_id', 'home_team_name', 'away_team_id', 'away_team_name', 'id', 'event_id', 'date', 'time', 'period_id', 'min', 'sec', 'team_id', 'player_id', 'playerName', 'playerPosition', 'x', 'y', 'type', 'description', 'outcome']

        columns_of_interest = ['season_id', 'match_id', 'home_team_id', 'home_team_name', 'away_team_id', 'away_team_name', 'id', 'event_id', 'period_id', 'team_id', 'player_id', 'playerName', 'playerPosition', 'type', 'description', 'outcome']

        COLUMN_INFO_PARSED = True

        if not COLUMN_INFO_PARSED:

            for column_name in columns_of_interest:
                unique_set = set(df[column_name])

                print column_name, ' , : ', len(unique_set)
                
                if len(unique_set) < 10:
                    print column_name, ' , FULL: ', unique_set
                else:
                    print column_name, ' , PARTIAL: ', list(unique_set)[0:10]

                print ' ' 
                print '## ' 
        else:
            pass

        PER_PLAYER_GOAL_DICT_CREATED = True

        if not PER_PLAYER_GOAL_DICT_CREATED:

            per_player_goal_dict = {}

            for idx, row in df.iterrows():

                if row['description'] == 'Goal':
                    player_name = row['playerName']
                    player_id = row['player_id']
                    team_id = row['team_id']
                    playerPosition = row['playerPosition']

                    success = False
                    if row['outcome'] == 1:
                        success = True
                    else:
                        success = False

                    if player_id not in per_player_goal_dict.keys():
                        goal_results_dict = {}
                        goal_results_dict['playerName'] = player_name
                        goal_results_dict['team_id'] = team_id
                        goal_results_dict['playerPosition'] = playerPosition

                        if success:
                            goal_results_dict['success_goals'] = 1
                            goal_results_dict['fail_goals'] = 0
                        else:
                            goal_results_dict['success_goals'] = 0
                            goal_results_dict['fail_goals'] = 1

                        per_player_goal_dict[player_id] = goal_results_dict
                    else:
                        goal_results_dict  = per_player_goal_dict[player_id]
                       
                        if success:
                            goal_results_dict['success_goals'] += 1
                        else:
                            goal_results_dict['fail_goals'] += 1
                    
                    print ' '
                    print goal_results_dict
                    print ' '

            per_player_goal_dict_fname = 'results/' + league + '_per_player_goal_dict.pkl'
            write_pkl(fname = per_player_goal_dict_fname, input_dict = per_player_goal_dict)

        else: 
            per_player_goal_dict_fname = 'results/' + league + '_per_player_goal_dict.pkl'
            per_player_goal_dict = load_pkl(fname = per_player_goal_dict_fname)

        MATCH_GOAL_DICT_CREATED = False

        if not MATCH_GOAL_DICT_CREATED:

            match_goal_dict = {}

            match_id_list = list(set(df['match_id']))

            for match_id in match_id_list: 
                match_df = df[df['match_id'] == match_id]

                home_team_id = list(set(match_df['home_team_id']))[0]
                home_team_name = list(set(match_df['home_team_name']))[0]

                away_team_id = list(set(match_df['away_team_id']))[0]
                away_team_name = list(set(match_df['away_team_name']))[0]

                home_team_goal_list = []
                away_team_goal_list = []
                team_id_goal_list = []

                for i, row in match_df.iterrows():
                    if row['description'] == 'Goal':
                       team_id = row['team_id']
                       team_id_goal_list.append(team_id)

                       if team_id == home_team_id:
                           home_team_goal_list.append(row['playerName'])
                       elif team_id == away_team_id:
                           away_team_goal_list.append(row['playerName'])
                       else:
                           pass
                
                single_match_results_dict = {}
                
                single_match_results_dict['home_team_goal_list'] = home_team_goal_list

                single_match_results_dict['away_team_goal_list'] = away_team_goal_list

                single_match_results_dict['team_id_goal_list'] = team_id_goal_list
                
                single_match_results_dict['home_team_id'] = home_team_id
                
                single_match_results_dict['home_team_name'] = home_team_name

                single_match_results_dict['away_team_id'] = away_team_id
                
                single_match_results_dict['away_team_name'] = away_team_name

                match_goal_dict[match_id] = single_match_results_dict 
            
            match_goal_dict_fname = 'results/' + league + '_match_goal_dict.pkl'
            write_pkl(fname = match_goal_dict_fname, input_dict = match_goal_dict)
