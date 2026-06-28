import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

#Setup
os.makedirs("Task4_Submission", exist_ok=True)
sns.set_theme(style="darkgrid", palette="husl")
plt.rcParams["figure.figsize"] = (14, 8)

# Load Accident data
df = pd.read_csv("accidents_dataset.csv")
df['Start_Time'] = pd.to_datetime(df['Start_Time'])
df['Hour'] = df['Start_Time'].dt.hour
df['Day'] = df['Start_Time'].dt.day_name() 

print('=== TASK 04: ACCIDENT DATA ANALYSIS ===')
print(f'Total Accidents: {len(df)}\n')

# 1. Accident Severity Count
plt.figure() 
sns.countplot(x='Severity', data=df)
plt.title('1. Accident Severity Levels')
plt.savefig('Task4_Submission/01_Severity.png', dpi=300, bbox_inches='tight')
plt.show() 

# 2. Accidents by Time of Day
plt.figure()
sns.countplot(x='Hour', data=df)
plt.title('2. Accidents by Hour of Day') 
plt.savefig('Task4_Submission/02_Hour.png', dpi=300, bbox_inches='tight')
plt.show()

#3. Accidents by Day of Week
plt.figure()
sns.countplot(x='Day', data=df, order=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
plt.title('3. Accidents by Day of Week')
plt.xticks(rotation=45)
plt.savefig('Task4_Submission/03_Day.png', dpi=300, bbox_inches='tight')
plt.show()
# 4. Weather Conditions
plt.figure()
top_weather = df['Weather_Condition'].value_counts().nlargest(10)
sns.barplot(y=top_weather.index, x=top_weather.values)
plt.title('4. Top 10 Weather Conditions During Accidents') 
plt.savefig('Task4_Submission/04_Weather.png', dpi=300, bbox_inches='tight')
plt.show()

print('\nDone! Check Task4_Submission folder. You have 4 accident graphs now.')