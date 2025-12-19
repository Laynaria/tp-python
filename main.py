from movie_manager import MovieManager
from movie_cli import movie_cli

new_manager = MovieManager()
new_manager.load_from_json()

while(True):
    movie_cli(new_manager)