from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.endpoints import teamgamelog
teams=teams.get_teams()
#team basic info  :id、full_name、abbreviation缩写、nickname、city、state、year_founed
gsw=[x for x in teams if x['full_name']=="Golden State Warriors"][0]
print(gsw)
# teams _num

gsw_city=gsw['city']
gsw_id=gsw['id']
gsw_name=gsw['full_name']
gsw_games=leaguegamefinder.LeagueGameFinder(team_id_nullable=gsw_id).get_data_frames()[0]

session_list=['2017-18','2018-19','2019-20','2020-21','2021-22','2022-23',"2023-24"]
for session in session_list:
    #按照整个赛季而言
    gamelog=teamgamelog.TeamGameLog(team_id=gsw_id,season=session)
    gamelog_df=gamelog.get_data_frames()[0]#返回pandas的dataformat
    #print(gamelog_df)
    #steal_avg=gamelog_df['STL'].mean()
    Points_avg=gamelog_df['PTS'].mean()
    print(f"{gsw_name}在{session}赛季平均得分为{Points_avg}")

    FG3A_avg=gamelog_df['FG3A'].mean()
    FG3M_avg=gamelog_df['FG3M'].mean()
      # 使用 .loc 方法
    print(f"{gsw_name}在{session}赛季平均三分出手次数为{FG3A_avg}")
    print(f"{gsw_name}在{session}赛季平均命中{FG3M_avg}三分")