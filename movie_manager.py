from movie import Movie
import json
from datetime import datetime

class MovieManager:
    def __init__(self):
        self.movie_list : list[Movie] = []
        self.json_path = "./data/movies.json"

    # Persistance of data:
    def load_from_json(self):
        try:
            with open(self.json_path, "r") as json_file:
                data = json.load(json_file)
                for movie in data:
                    movie_to_add = Movie(movie["title"], movie["released_date"], movie["description"])
                    
                    self.movie_list.append(movie_to_add)
        except FileNotFoundError:
            print("The file library.json doesn't exist!")

    def save_to_json(self) -> None:
        data = []

        for movie in self.movie_list:
            movie_for_data = {
                "title" : movie.title,
                "released_date": movie.released_date ,
                "description": movie.description,
                            }
            data.append(movie_for_data)
        
        with open(self.json_path, "w") as json_file:
            json.dump(data, json_file, indent=4)


    # CRUD
    def create_movie(self, new_movie):
        self.movie_list.append(new_movie)
    
    def get_all_movies(self) -> None:
        for movie in self.movie_list:
            print(movie)

    def get_movie_by_title(self, title) -> None:
            for movie in self.movie_list:
                if movie.title.lower() == title.lower():
                    print(movie)
                    break
            else:
                print(f"No movie with this title!")

    def get_movies_sorted_by_date(self):
        get_list = self.movie_list 

        get_list.sort(key=lambda x: datetime.strptime(x.released_date, '%d/%m/%Y'))
        return get_list
    
    def update_movie_by_title(self, title, new_title, new_released_date, new_description):
        new_movie = Movie(new_title, new_released_date, new_description)

        for movie in self.movie_list:
            if movie.title.lower() == title.lower():
                self.movie_list[self.movie_list.index(movie)] = new_movie
        else:
            print(f"No movie with this title!")


    def delete_movie_by_title(self, title):
            for movie in self.movie_list:
                if movie.title.lower() == title.lower():
                    self.movie_list.remove(movie)
                    break
            else:
                print(f"No movie with this title!")

# new_manager = MovieManager()
# new_manager.load_from_json()

# print("All movies")
# print(new_manager.get_all_movies())

# test_movie = Movie("bla", "14/06/2020", "bla bla bla bla bla")
# new_manager.create_movie(test_movie)

# new_manager.update_movie_by_title("bla", "blabla", "14/06/2020", "bla bla bla bla bla x2")

# new_manager.save_to_json()

# print("Get movie bla")
# new_manager.get_movie_by_title("bla")

# new_manager.delete_movie_by_title("bla")
# print(new_manager.get_all_movies())

# print("Film list in order of released date")
# for movie in new_manager.get_movies_sorted_by_date():
#     print(movie, "\n")