import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




df_match = pd.read_csv("match_data.csv")
print(df_match.head())

df_info = pd.read_csv("match_info_data.csv")
print(df_info.head())

# Missing values count for each column
print(df_match.isnull().sum())
print(df_info.isnull().sum())

# Fill missing value with 'unknown'
print(df_match.fillna('unknown',inplace=True))

# check for duplicate value
print(df_match.duplicated().sum())
print(df_info.duplicated().sum())

# checking the column datatypes
print(df_match.dtypes)
print(df_info.dtypes)

# convert in date time format
df_match['start_date'] = pd.to_datetime(df_match['start_date'])  # Date format convert

df_info['date'] = pd.to_datetime(df_info['date'])






# ✅ remove the Duplicate rows 
df_match = df_match.drop_duplicates()  # ✅ Duplicate rows remove ho jayengi

# Check karne ke liye print karo
df_match = df_match.drop_duplicates()
print(f"Duplicates removed. New shape: {df_match.shape}")

# Number of duplicate rows drop
print("Number of duplicate rows removed:", df_match.duplicated().sum())  


df_info = df_info.drop_duplicates()
print(f"Duplicates removed. New shape: {df_info.shape}")

# Number of duplicate rows remove
print("Number of duplicate rows removed ",df_info.duplicated().sum())

# EDA
print(df_info['winner'].value_counts())  # Yeh check karega ki data sahi hai ya nahi

# Most succesfull team
plt.figure(figsize=(12,6))
team_wins = df_info['winner'].value_counts() 

# sns.barplot(x=team_wins.index, y=team_wins.values, hue=team_wins.index, palette="viridis", legend=False)
# plt.xticks(rotation=90)
# plt.title('Most successful teams in IPL')
# plt.xlabel('Teams')
# plt.ylabel('Number of wins')
# plt.show()

#2️⃣ Most Consistent Players
# top_player = df_info['player_of_match'].value_counts().head(10)

# plt.figure(figsize=(10,5))
# sns.barplot(x=top_player.index , y=top_player.values,palette='coolwarm')
# plt.xticks(rotation=90)
# plt.title("Top 10 Players with Most Player of the Match Awards")
# plt.xlabel("Players")
# plt.ylabel("Counts")
# plt.show()

#3️⃣ Toss Impact on Match Results?
toss_winner_match_winner= df_info[df_info['toss_winner']==df_info['winner']]
toss_win_percentage = len(toss_winner_match_winner) / len(df_match) * 100
print(f"toss winning team won the match{toss_win_percentage:.2f}% times")

#4️⃣ Batting First vs Chasing Comparison
batting_first = df_info[df_info['win_by_runs'] > 0].shape[0]
chasing = df_info[df_info['win_by_wickets'] > 0].shape[0]

plt.pie([batting_first,chasing],labels=['Batting firstwin','Chasing win'],autopct='%1.1f%%', colors=['blue','red'])
plt.title("Batting first vs chasing -winning comparison")
plt.show()

#5️⃣ Best Venues for Batting & Bowling
venue_runs = df_info.groupby('venue')['win_by_runs'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=venue_runs.index,y=venue_runs.values, palette = 'magma')
plt.xticks(rotation=45, ha='right', fontsize=12)  # 45-degree angle, right align, bigger font

plt.title("Top 10 high scores venues in IPL")
plt.xlabel("Venus")
plt.ylabel("Averge Run in Winning Matches")
plt.show()

