# 🎬 Simple Movie Recommendation Bot

Welcome to my first Python project! This little bot helps you discover movie recommendations based on different genres. It's a great way to explore basic data analysis with Python.

---

## ✨ What Does It Do?

This project is a simple Python script that recommends movies. It does this by:

1.  **Reading movie data:** It looks at two files: `movies.csv` (which has movie titles and their genres) and `ratings.csv` (which has user ratings for movies).
2.  **Calculating popularity:** It figures out the average rating for each movie and how many people have rated it.
3.  **Recommending by genre:** You can ask it for recommendations in a specific genre (like "Action" or "Comedy"), and it will list the top movies in that genre, prioritizing those with higher ratings and more votes.

---

## ⚙️ How It Works

The Python script `movie_recommender_backend.py` does all the magic!

* It uses a powerful Python library called `pandas` to read and work with the CSV files.
* It combines the movie information and ratings.
* It groups movies to find their average rating and total number of ratings.
* When you ask for a genre, it filters the movies and then sorts them to show the best ones first (more ratings usually mean more reliable recommendations!).

---

## 🚀 Getting Started

Follow these steps to get this bot running on your computer!

### Prerequisites

Before you start, make sure you have these installed:

1.  **Python:** You'll need Python 3 installed. You can download it from [python.org](https://www.python.org/downloads/).
2.  **pip:** This is Python's package installer, usually comes with Python.
3.  **Git:** If you're pulling this from GitHub, you'll need Git. Download it from [git-scm.com](https://git-scm.com/).
4.  **VS Code (Recommended IDE):** A great code editor that makes working with Python easy. Download from [code.visualstudio.com](https://code.visualstudio.com/).

### Installation

1.  **Get the Data Files:**
    * You need two CSV files: `movies.csv` and `ratings.csv`. These are commonly available from datasets like [MovieLens](https://grouplens.org/datasets/movielens/).
    * **Place both `movies.csv` and `ratings.csv` in the same folder as the `movie_recommender_backend.py` script.**

2.  **Install `pandas`:**
    * Open your VS Code terminal (Go to `Terminal` > `New Terminal`).
    * **Important:** Make sure the correct Python interpreter is selected in the bottom-left corner of VS Code (click it to change if needed).
    * In the terminal, type:
        ```bash
        pip install pandas
        ```
    * This command downloads and installs the `pandas` library, which your script needs.

---

## ▶️ How to Run the Bot

Once everything is set up, you can run your movie recommendation bot!

1.  **Open your project folder in VS Code.**
2.  **Open the integrated terminal** (`Terminal` > `New Terminal`).
3.  **Make sure you are in the directory where `movie_recommender_backend.py` is located.** (You can type `ls` or `dir` to see the files in the current directory).
4.  **Run the script:**
    ```bash
    python movie_recommender_backend.py
    ```

You will see movie recommendations printed directly in your terminal!

---

## 💡 Example Usage (from the code)

The script already has some examples built in:

```python
if __name__ == "__main__":
    print("Welcome to the Movie Recommendation Bot!\n")

    # Example 1: Top 5 Action movies
    print("Top 5 Action Movies:")
    action_movies = get_movie_recommendations(genre='Action', top_n=5)
    # ... (code to print results)

    # Example 2: Top 7 Comedy movies
    print("Top 7 Comedy Movies:")
    comedy_movies = get_movie_recommendations(genre='Comedy', top_n=7)
    # ... (code to print results)

    # Example 3: Top 3 Sci-Fi movies
    print("Top 3 Sci-Fi Movies:")
    scifi_movies = get_movie_recommendations(genre='Sci-Fi', top_n=3)
    # ... (code to print results)

    # Example 4: Overall Top 10 movies (no genre specified)
    print("Overall Top 10 Movies (All Genres):")
    all_movies = get_movie_recommendations(top_n=10)
    # ... (code to print results)
