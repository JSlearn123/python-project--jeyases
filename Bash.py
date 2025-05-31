import pandas as pd

def get_movie_recommendations(genre=None, top_n=10):
    """
    Recommends movies based on a specified genre, prioritizing by rating count and average rating.

    Args:
        genre (str, optional): The genre to filter movies by. If None, returns overall top movies.
        top_n (int): The number of top recommendations to return.

    Returns:
        list: A list of dictionaries, where each dictionary represents a recommended movie
              with its title, genres, average rating, and rating count.
    """
    try:
        # Load datasets
        movies_df = pd.read_csv('C:/Users/jeyases/Desktop/movie/movies.csv')
        ratings_df = pd.read_csv('C:/Users/jeyases/Desktop/movie/ratings.csv')
    except FileNotFoundError:
        print("Error: movies.csv or ratings.csv not found. Please ensure they are in the same directory.")
        return []

    # Merge dataframes
    merged_df = pd.merge(ratings_df, movies_df, on='movieId')

    # Calculate average rating and rating count for each movie
    movie_stats = merged_df.groupby(['movieId', 'title', 'genres']).agg(
        average_rating=('rating', 'mean'),
        rating_count=('rating', 'count')
    ).reset_index()

    # Ensure genres are treated as strings for splitting
    movie_stats['genres'] = movie_stats['genres'].astype(str)

    if genre:
        # Filter by genre (case-insensitive and partial match)
        filtered_movies = movie_stats[movie_stats['genres'].str.contains(genre, case=False, na=False)]
    else:
        # If no genre specified, consider all movies
        filtered_movies = movie_stats.copy()

    # Sort movies by rating_count (popularity) and then by average_rating
    # We add a small regularization to average_rating to handle movies with very few ratings
    # A common approach is a weighted average if dealing with cold start, but for simplicity
    # just sorting by count and then average is often sufficient for basic recommendations.
    min_ratings_threshold = 5 # only consider movies with at least 5 ratings for better average reliability
    filtered_movies = filtered_movies[filtered_movies['rating_count'] >= min_ratings_threshold]

    recommended_movies = filtered_movies.sort_values(
        by=['rating_count', 'average_rating'],
        ascending=[False, False]
    ).head(top_n)

    # Format the output
    output = recommended_movies[[
        'movieId', 'title', 'genres', 'average_rating', 'rating_count'
    ]].to_dict(orient='records')

    # Convert average_rating to a more readable format
    for movie in output:
        movie['average_rating'] = round(movie['average_rating'], 2)

    return output

if __name__ == "__main__":
    print("Welcome to the Movie Recommendation Bot!\n")

    # Example 1: Top 5 Action movies
    print("Top 5 Action Movies:")
    action_movies = get_movie_recommendations(genre='Action', top_n=5)
    if action_movies:
        for i, movie in enumerate(action_movies):
            print(f"{i+1}. {movie['title']} (Rating: {movie['average_rating']}/5.0, Votes: {movie['rating_count']})")
    else:
        print("No Action movies found or not enough rated movies for this genre.")
    print("\n" + "="*50 + "\n")

    # Example 2: Top 7 Comedy movies
    print("Top 7 Comedy Movies:")
    comedy_movies = get_movie_recommendations(genre='Comedy', top_n=7)
    if comedy_movies:
        for i, movie in enumerate(comedy_movies):
            print(f"{i+1}. {movie['title']} (Rating: {movie['average_rating']}/5.0, Votes: {movie['rating_count']})")
    else:
        print("No Comedy movies found or not enough rated movies for this genre.")
    print("\n" + "="*50 + "\n")

    # Example 3: Top 3 Sci-Fi movies
    print("Top 3 Sci-Fi Movies:")
    scifi_movies = get_movie_recommendations(genre='Sci-Fi', top_n=3)
    if scifi_movies:
        for i, movie in enumerate(scifi_movies):
            print(f"{i+1}. {movie['title']} (Rating: {movie['average_rating']}/5.0, Votes: {movie['rating_count']})")
    else:
        print("No Sci-Fi movies found or not enough rated movies for this genre.")
    print("\n" + "="*50 + "\n")

    # Example 4: Overall Top 10 movies (no genre specified)
    print("Overall Top 10 Movies (All Genres):")
    all_movies = get_movie_recommendations(top_n=10)
    if all_movies:
        for i, movie in enumerate(all_movies):
            print(f"{i+1}. {movie['title']} (Rating: {movie['average_rating']}/5.0, Votes: {movie['rating_count']})")
    else:
        print("No movies found or not enough rated movies overall.")