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

if __name__ == '__main__':
    print 'ROOT_SOCCER_DIR: ', ROOT_SOCCER_DIR

    league_list = ['epl']

    for league in league_list:
        csv_fname = '/'.join([GAME_CSV_DIR, league,  league + '.csv'])

        df = pandas.read_csv(csv_fname)

        print 'COLUMNS: ', list(df)

        # COLUMNS:  ['season_id', 'match_id', 'home_team_id', 'home_team_name', 'away_team_id', 'away_team_name', 'id', 'event_id', 'date', 'time', 'period_id', 'min', 'sec', 'team_id', 'player_id', 'playerName', 'playerPosition', 'x', 'y', 'type', 'description', 'outcome']

        columns_of_interest = ['season_id', 'match_id', 'home_team_id', 'home_team_name', 'away_team_id', 'away_team_name', 'id', 'event_id', 'period_id', 'team_id', 'player_id', 'playerName', 'playerPosition', 'type', 'description', 'outcome']

        for column_name in columns_of_interest:
            unique_set = set(df[column_name])

            print column_name, ' , : ', len(unique_set)

            if len(unique_set) < 10:
                print column_name, ' , : ', unique_set
            print ' ' 
            print '## ' 

