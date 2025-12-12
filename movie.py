import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from colorama import init, Fore
import time
import sys

init(autoreset= True)
def load_data(file_path = "imdb_top_1000.csv"):
    try:
        df = pd.read_csv(file_path)
        df["combined features"] = df[ "Genre"].fillna('') + ' ' + df["Overview"].fillna(' ')
        return df
    except FileNotFoundError:
        print(f"{Fore.RED} Error : this file {file_path} was not found")
        exit()
movies_df = load_data()