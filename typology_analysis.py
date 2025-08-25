import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_typology(df):
    # Goal frequency
    goal_counts = df['main goal(s)'].value_counts()
    print("Goal Frequency:\n", goal_counts)
    
    # Measure frequency
    measures = df['measures_list'].explode().value_counts()
    print("Measure Frequency:\n", measures)
    
    # Characteristics
    eco_counts = df['eco'].value_counts()
    multi_counts = df['multi'].value_counts()
    intensity_counts = df['intensity'].value_counts()
    gradualism_counts = df['gradualism'].value_counts()
    
    print("Economic Impact:\n", eco_counts)
    print("Multilateral Nature:\n", multi_counts)
    print("Intensity:\n", intensity_counts)
    print("Gradualism:\n", gradualism_counts)
    
    # Visualizations
    plt.figure(figsize=(10, 6))
    sns.barplot(x=goal_counts.values, y=goal_counts.index)
    plt.title('Frequency of Sanction Goals')
    plt.xlabel('Count')
    plt.savefig('../data/goal_frequency.png')
    plt.close()
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=measures.values, y=measures.index)
    plt.title('Frequency of Sanction Measures')
    plt.xlabel('Count')
    plt.savefig('../data/measure_frequency.png')
    plt.close()

if __name__ == "__main__":
    df = pd.read_csv('../data/sanctions_cleaned.csv')
    analyze_typology(df)
