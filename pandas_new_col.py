# 根据条件创建新的列

import pandas as pd

df = pd.DataFrame({'team_A': ['Spain', 'Germany', 'Brazil', 'France'],
                   'team_B': ['USA', 'Argentina', 'Mexico', 'Belgium'],
                   'score_A': [5, 3, 2, 0],
                   'score_B': [4, 0, 3, 0]},
                  columns=['team_A', 'team_B', 'score_A', 'score_B'])
# 同行数据对比，输出分数高的国家
df['win_team'] = ''
mask = df['score_A'] - df['score_B']

df.loc[mask > 0, 'win_team'] = df.loc[mask > 0, 'team_A']
df.loc[mask < 0, 'win_team'] = df.loc[mask < 0, 'team_B']
df.loc[mask == 0, 'win_team'] = 'Draw'

print(df)


# 第二种DataFrame.iterrows()方法实现list
def find_with_team(df):
    winners = []
    for i, row in df.iterrows():
        if row['score_A'] > row['score_B']:
            winners.append(row['team_A'])
        elif row['score_A'] < row['score_B']:
            winners.append(row['team_B'])
        else:
            winners.append('Draw')
    return winners
df['winners'] = find_with_team(df)
print(df)