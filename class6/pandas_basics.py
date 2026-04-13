import pandas as pd

#task 3:数据处理 欧洲杯
euro12=pd.read_csv(r'C:\Users\ASUS\Desktop\data.csv')
print("(3)Goals:")
print(euro12["Goals"])
num=len(euro12['Team'])
print(f"(4)involved team numbers is: {num}")
num_cols = len(euro12.columns)
print(f"(5) 列的数量: {num_cols}")
discipline=euro12[['Yellow Cards','Team','Red Cards']]
print(discipline)
discipline_sort=discipline.sort_values(by=['Red Cards','Yellow Cards'])
print(f"(7)discipline_sort:\n{discipline_sort}")
yellow_cards_mean = euro12['Yellow Cards'].mean()
print(f"(8) 黄牌平均值: {yellow_cards_mean}")
teams_goals_gt_6=euro12[euro12['Goals']>6]
print("(9) 进球数超过 6 的球队:")
print(teams_goals_gt_6)
teams_start_with_G = euro12[euro12['Team'].str.startswith('G')]
print("(10) 以 G 开头的球队:")
print(teams_start_with_G)
first_7_cols=euro12.iloc[:,:7]
print("(11) 前 7 列数据预览:")
print(first_7_cols.head())
#指定球队
target_teams = euro12[euro12['Team'].isin(['England', 'Italy', 'Russia'])]
shooting_accuracy = target_teams[['Team', 'Shooting Accuracy']]
print("(13) 指定球队的射正率:")
print(shooting_accuracy)
