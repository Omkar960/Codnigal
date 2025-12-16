import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from colorama import init, Fore
import time
import sys
from textblob import TextBlob
import random

init(autoreset=True)

def randomizer(df):
    if df.empty:
        return "No movies available."
    random_row = df.sample(n=1).iloc[0]
    title = random_row['Series_Title']
    rating = random_row['IMDB_Rating']
    genre = random_row['Genre']
    return f"🎥 Random Movie: {title} (Rating: {rating}, Genre: {genre})"








def load_data(file_path="imdb_top_1000.csv"):
    try:
        df = pd.read_csv(file_path)  
        df['combined features'] = df['Genre'].fillna('') + ' ' + df["Overview"].fillna(' ')
        return df
    except FileNotFoundError:
        print(f'{Fore.RED}Error: File {file_path} not found. Check the path.')
        sys.exit()

movies_df = load_data()


tfidf = TfidfVectorizer(stop_words = "english")
tfidf_matrix = tfidf.fit_transform(movies_df['combined features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def list_genres(df):
    return sorted(set(genre.strip() for sublist in df['Genre'].dropna().str.split(', ') for genre in sublist))
genres = list_genres(movies_df)

def recommend_movies(genre=None, mood=None, rating=None,top_n=5):
    filtered_df = movies_df
    if genre:
        filtered_df = filtered_df[filtered_df['Genre'].str.contains(genre,case=False, na= False)]
    if rating:
        filtered_df = filtered_df[filtered_df['IMDB_Rating']>= rating]
    filtered_df = filtered_df.sample(frac=1).reset_index(drop=True)

    recommendations = []
    for idx, row in filtered_df.iterrows():
        overview = row["Overview"]
        if pd.isna(overview):
            pass
        polarity = TextBlob(overview).sentiment.polarity
        if (mood and ((TextBlob(mood).sentiment.polarity < 0 and polarity > 0)or polarity >= 0)) or not mood:
            recommendations.append((row['Series_Title'],polarity))
        if len(recommendations) == top_n:
            break

    return recommendations if recommendations else "No suitable movie recommendations."

def display_recommendations(recs,name):
    print(f"{Fore.YELLOW} AI-Analyzed Movie Recommendations for {name}: ")

    for idx,(title, polarity) in enumerate(recs, 1):
        sentiment = "Positive 😊" if polarity > 0 else "Negative 😥" if polarity < 0 else "Neutral 😐 "
        print(f"{Fore.CYAN}{idx}. 🎥 {title} (Polarity : {polarity:.2f}, {sentiment})")

def processing_animation():
    for _ in range(3):
        print(Fore.YELLOW + ", ", end= "", flush=True)
        time.sleep(0.5)
def handle_ai(name):
    print(Fore.BLUE + "\n 🔍 Let's find the perfect movie for you! \n")

    print(Fore.GREEN + "Available Genres: ", end="")
    for idx,genre in enumerate(genres,1):
        print(f"{Fore.CYAN}{idx}. {genre}")
    print()

    while True:
        genre_input = input(Fore.YELLOW + "Enter genre number or name: ").strip()

        if genre_input.isdigit() and 1 <= int(genre_input) <= len(genres):
            genre = genres[int(genre_input)-1]
            break
        elif genre_input.title() in genres:
            genre = genre_input.title()
            break
        print(Fore.RED + "Inavlid input. Try again. \n")

    mood = input(Fore.YELLOW + "How fo you feel today? (Describe your mood): ").strip()
    
    print(Fore.BLUE + "\nAnalysing mood", end="",flush=True)
    processing_animation()
    polarity = TextBlob(mood).sentiment.polarity
    mood_desc = "positive 😊" if polarity > 0 else "negative 😥" if polarity < 0 else "neutral 😐"

    print(f"\n {Fore.GREEN}Your mood is {mood_desc} (Polarity:{polarity:.2f}).\n")
    while True:
        rating_input = input(f"{Fore.YELLOW} Enter minimum IMDB rating(7,6 - 9.3)or 'skip': ").strip()
        if rating_input.lower() == "skip":
            rating = None
            break
        try:
            rating = float(rating_input)
            if 7.6 <= rating <= 9.4:
                break
            else:
                print(Fore.RED + "Rating out of range. Try again. \n")
        except ValueError:
            print(Fore.RED + "Invalid input. Try again.")
    
    print(f"{Fore.BLUE}\n Finding movies for {name}", end ="", flush = True)
    processing_animation()

    recs = recommend_movies(genre = genre, mood=mood, rating=rating,top_n = 5)
    if isinstance(recs,str):
        print(Fore.RED + recs + "\n")
    else:
        display_recommendations(recs, name)
    while True:
        action = input(Fore.YELLOW + "\nWould you like more recommendations? (yes/no): ").strip().lower()
        if action == "no":
            print(Fore.GREEN + f"\n Enjoy your movie picks, {name}! 🎬🍿\n")
            break
        elif action == "yes":
            recs = recommend_movies(genre=genre,mood=mood,rating=rating,top_n=5)
            if isinstance(recs,str):
                print(Fore.RED + recs + "\n")

            else:
                display_recommendations(recs,name)
        else:
            print(Fore.RED + "Invalid choice. Try again.\n")

def main():
    print(Fore.BLUE + " 🎥 Welcome to your Personal Movie Recommendation Assistant! 🎥\n ")
    name = input(Fore.YELLOW + "What's your name? ").strip()

    print(f"\n{Fore.GREEN}Great to meet you {name}\n")
    handle_ai(name)

    print("Another movie choice is:")
    print(randomizer(movies_df))

    
   

if __name__ == "__main__":
    main()



        


