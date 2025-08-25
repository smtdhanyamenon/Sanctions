import pandas as pd

def load_and_clean_data(file_path):
    # Load CSV
    df = pd.read_csv(file_path)
    
    # Handle missing values
    df.fillna({'goals': 'Unknown', 'main goal(s)': 'Unknown', 'measures': ''}, inplace=True)
    
    # Convert timeframe to start and end years
    df['start_year'] = df['timeframe'].str.split('-').str[0].astype(int)
    df['end_year'] = df['timeframe'].str.split('-').str[1].replace('ongoing', pd.Timestamp.now().year).astype(int)
    
    # Split measures into a list
    df['measures_list'] = df['measures'].str.split(', ')
    
    return df

if __name__ == "__main__":
    df = load_and_clean_data('../data/sanctions_dataset.csv')
    df.to_csv('../data/sanctions_cleaned.csv', index=False)
    print("Data cleaned and saved to data/sanctions_cleaned.csv")
