import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def generate_visualizations(df):
    # Geographic distribution of targets
    target_counts = df['target'].value_counts().reset_index()
    target_counts.columns = ['target', 'count']
    
    # Note: For a world map, you may need ISO codes or coordinates
    fig = px.bar(target_counts, x='target', y='count', title='Sanction Targets by Country')
    fig.write_to_html('../data/target_distribution.html')
    
    # Intensity by sender
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='sender', y='intensity', data=df)
    plt.title('Sanction Intensity by Sender')
    plt.savefig('../data/intensity_by_sender.png')
    plt.close()

if __name__ == "__main__":
    df = pd.read_csv('../data/sanctions_cleaned.csv')
    generate_visualizations(df)
