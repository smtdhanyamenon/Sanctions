import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def analyze_dynamics(df):
    # Sender frequency
    sender_counts = df['sender'].value_counts()
    print("Sender Frequency:\n", sender_counts)
    
    # Target frequency
    target_counts = df['target'].value_counts()
    print("Top 5 Targets:\n", target_counts.head())
    
    # Sender-goal crosstab
    sender_goal = pd.crosstab(df['sender'], df['main goal(s)'])
    print("Sender-Goal Crosstab:\n", sender_goal)
    
    # Temporal trends
    yearly_counts = df.groupby('start_year').size()
    print("Sanctions by Start Year:\n", yearly_counts)
    
    # Visualizations
    plt.figure(figsize=(10, 6))
    sns.heatmap(sender_goal, annot=True, cmap='Blues')
    plt.title('Sender vs. Main Goal')
    plt.savefig('../data/sender_goal_heatmap.png')
    plt.close()
    
    plt.figure(figsize=(10, 6))
    yearly_counts.plot(kind='line')
    plt.title('Sanctions Over Time')
    plt.xlabel('Year')
    plt.ylabel('Number of Sanctions')
    plt.savefig('../data/temporal_trend.png')
    plt.close()

if __name__ == "__main__":
    df = pd.read_csv('../data/sanctions_cleaned.csv')
    analyze_dynamics(df)
