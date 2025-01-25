import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkOTVjY2YwZWRkZTUzMjQ3ODhjMTU1MjQ4YjM5ZTUzNSIsIm5iZiI6MTcyMzAyMjc2Mi4wNjk2NDMsInN1YiI6IjY2YjMzOWE2OGQ5YTU5OTExMzRiZjhlYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ljTQM4HxsblTlilNJ7RS5AHuOZYFFkuJ4VtSbGKdXzs"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    poster_path = data['poster_path']

    full_path = "https://image.tmdb.org/t/p/w500"+poster_path
    return full_path


fetch_poster(64)