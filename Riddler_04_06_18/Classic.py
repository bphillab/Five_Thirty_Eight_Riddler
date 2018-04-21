import pandas as pd
import numpy as np


games_data = pd.read_fwf('./game_comparison.txt', header=None)
games_data.columns = [0,"Winner",2,"Loser",4,5,6,7]
games_data = games_data[['Winner','Loser']]
games_data['Winner'] = games_data.Winner.apply(lambda x: x.lstrip('@'))
games_data['Loser'] = games_data.Loser.apply(lambda x: x.lstrip('@'))

team_names = pd.DataFrame(games_data.Winner.append(games_data.Loser).unique())
team_names.columns = ['team_name']
team_names['trans_champ'] = 0
team_names['champ_level'] = 9999
team_names.loc[team_names.team_name == 'Villanova', 'trans_champ'] = 1
team_names.loc[team_names.team_name == 'Villanova', 'champ_level'] = 0

last_winners = ['Villanova']
games_data.loc[games_data.Loser.isin(last_winners),'Winner']

num_winners = 0
last_round = 0

while team_names.trans_champ.sum() != num_winners:
    num_winners = team_names.trans_champ.sum()
    last_winners = np.array(team_names[team_names.champ_level == last_round]['team_name'])
    last_round = last_round+1
    winners = np.array(games_data.loc[games_data.Loser.isin(last_winners), 'Winner'])
    team_names.loc[team_names.team_name.isin(winners), 'trans_champ'] = 1
    team_names.loc[team_names.team_name.isin(winners), 'champ_level'] = team_names.loc[team_names.team_name.isin(winners), 'champ_level'].apply(lambda x: min(last_round,x))


