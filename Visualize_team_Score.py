import matplotlib.pyplot as plt
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.endpoints import teamgamelog



plt.rcParams['font.sans-serif'] = ['SimHei']
# 获取球队信息
teams_info = teams.get_teams()
# 金州勇士队信息
gsw_info = [team for team in teams_info if team['full_name'] == "Memphis Grizzlies"][0]
gsw_id = gsw_info['id']
gsw_name = gsw_info['full_name']

# 获取比赛数据
#session_list = ['2012-13','2013-14','2014-15','2015-16','2016-17','2017-18', '2018-19', '2019-20', '2020-21', '2021-22', '2022-23', "2023-24"]
session_list=[]
for year in range(2000,2024):
    season=f"{year}-{str(year+1)[-2:]}"
    session_list.append(season)
points_avg_list = []
fg3a_avg_list = []
fg3m_avg_list = []

for session in session_list:
    gamelog = teamgamelog.TeamGameLog(team_id=gsw_id, season=session)
    gamelog_df = gamelog.get_data_frames()[0]

    points_avg = gamelog_df['PTS'].mean()
    points_avg_list.append(points_avg)

    fg3a_avg = gamelog_df['FG3A'].mean()
    fg3a_avg_list.append(fg3a_avg)

    fg3m_avg = gamelog_df['FG3M'].mean()
    fg3m_avg_list.append(fg3m_avg)

# 绘图
fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# 平均得分
axs[0].plot(session_list, points_avg_list, marker='o', color='b')
for i, txt in enumerate(points_avg_list):
    axs[0].text(i, txt, f'{txt:.2f}', ha='right', va='bottom', color='b')
axs[0].set_title(f'{gsw_name} 平均得分')
axs[0].set_xlabel('赛季')
axs[0].set_ylabel('得分')

# 平均三分出手次数
axs[1].plot(session_list, fg3a_avg_list, marker='o', color='r')
for i, txt in enumerate(fg3a_avg_list):
    axs[1].text(i, txt, f'{txt:.2f}', ha='right', va='bottom', color='r')
axs[1].set_title(f'{gsw_name} 平均三分出手次数')
axs[1].set_xlabel('赛季')
axs[1].set_ylabel('出手次数')

# 平均三分命中次数
axs[2].plot(session_list, fg3m_avg_list, marker='o', color='g')
for i, txt in enumerate(fg3m_avg_list):
    axs[2].text(i, txt, f'{txt:.2f}', ha='right', va='bottom', color='g')
axs[2].set_title(f'{gsw_name} 平均三分命中次数')
axs[2].set_xlabel('赛季')
axs[2].set_ylabel('命中次数')

plt.tight_layout()
plt.show()