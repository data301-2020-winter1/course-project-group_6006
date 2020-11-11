import pandas as pd

# seperator for our data files should be ";" but for normal csv's it's ","

def load_and_process(url_or_path_to_csv_file, seperator):
    
    # Method Chain (Load data and deal with missing data)
    df = (
        pd.read_csv(url_or_path_to_csv_file, sep=seperator)
        .rename(columns={"fixed acidity": "fa", "volatile acidity": "va", "citric acid": "ca", 
                         "residual sugar": "rs", "free sulfur dioxide": "fsd", "total sulfur dioxide": "tsd"})
        .drop_duplicates()
        .dropna(axis=0, subset=['fa','va','ca','rs','chlorides','fsd','tsd','density','pH','sulphates','alcohol'])
        .reset_index()
        .drop(['index'],axis=1)
    )
    
    return df
