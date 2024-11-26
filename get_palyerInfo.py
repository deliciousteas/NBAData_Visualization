from nba_api.stats.endpoints import playercareerstats
import pandas
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
import matplotlib.pyplot as plt



#获取球员的ID,所有球员，现役和退役球员，返回为id、full_name、first_name、last_name、is_activate
players_dic=players.get_players()
player_id=[player['id']for player in players_dic if player['full_name']=="Kyrie Irving"][0]
player_name=[]
#查询每个赛季比赛数据
session_list=['2017-18','2018-19','2019-20','2020-21','2021-22','2022-23',"2023-24"]
game_count=0


for session in session_list:
    #按照整个赛季而言
    gamelog=playergamelog.PlayerGameLog(player_id=player_id,season=session)
    gamelog_df=gamelog.get_data_frames()[0]#返回pandas的dataformat
    #print(gamelog_df)
    #steal_avg=gamelog_df['STL'].mean()
    Points_avg=gamelog_df['PTS'].mean()
    print(f"Kyrie Irving在{session}赛季平均得分为{Points_avg}")

    FG3A_avg=gamelog_df['FG3A'].mean()
    FG3M_avg=gamelog_df['FG3M'].mean()
      # 使用 .loc 方法
    print(f"Kyrie Irving在{session}赛季平均三分出手次数为{FG3A_avg}")
    print(f"Kyrie Irving在{session}赛季平均命中{FG3M_avg}三分")


