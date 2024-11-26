from nba_api.stats.endpoints import playercareerstats
import pandas
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
import matplotlib.pyplot as plt  # 导入 Matplotlib 库

# 设置显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']

career = playercareerstats.PlayerCareerStats(player_id="77")
frame = career.get_data_frames()[0]

# 获取球员的ID
players_dic = players.get_players()
player_id = [player['id'] for player in players_dic if player['full_name'] == "Kyrie Irving"][0]

# 初始化列表以存储每个赛季的数据
session_list = ['2017-18', '2018-19', '2019-20', '2020-21', '2021-22', '2022-23', "2023-24"]
Points_avg_list = []
FG3A_avg_list = []
FG3M_avg_list = []

for session in session_list:
    gamelog = playergamelog.PlayerGameLog(player_id=player_id, season=session)
    gamelog_df = gamelog.get_data_frames()[0]

    # 计算每个赛季的平均得分、三分出手次数和三分命中次数
    Points_avg = gamelog_df['PTS'].mean()
    FG3A_avg = gamelog_df['FG3A'].mean()
    FG3M_avg = gamelog_df['FG3M'].mean()

    # 将平均得分、三分出手次数、三分命中次数添加到列表中
    Points_avg_list.append(Points_avg)
    FG3A_avg_list.append(FG3A_avg)
    FG3M_avg_list.append(FG3M_avg)

    print(f"Kyrie Irving在{session}赛季平均得分为{Points_avg}")
    print(f"Kyrie Irving在{session}赛季平均三分出手次数为{FG3A_avg}")
    print(f"Kyrie Irving在{session}赛季平均命中{FG3M_avg}三分")

# 绘制图表
fig, ax1 = plt.subplots(figsize=(10, 6))

# 绘制平均得分
color = 'tab:red'
ax1.set_xlabel('赛季')
ax1.set_ylabel('得分', color=color)
ax1.plot(session_list, Points_avg_list, color=color, marker='o', label='平均得分')
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True)

# 添加第二个 y 轴（三分出手次数和三分命中次数）
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('三分次数/三分命中次数', color=color)
ax2.plot(session_list, FG3A_avg_list, color=color, marker='o', linestyle='--', label='平均三分出手次数')
ax2.plot(session_list, FG3M_avg_list, color='orange', marker='o', linestyle='--', label='平均三分命中次数')
ax2.tick_params(axis='y', labelcolor=color)

# 调整 y 轴刻度范围和间隔
ax1.set_ylim(0, 30)  # 平均得分范围
ax2.set_ylim(0, 15)  # 平均三分出手次数和命中次数范围
ax2.yaxis.set_ticks(range(0, 16, 2))  # 设置 y 轴刻度间隔

fig.tight_layout()  # 自动调整布局以避免重叠
fig.legend(loc="upper left")  # 添加图例
plt.title('Kyrie Irving 赛季数据变化')
plt.xticks(rotation=45)  # 旋转 x 轴标签以免重叠
plt.show()
