from movie import Movie
import json

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


    def create_movie(self, new_movie):
        self.movie_list.append(new_movie)
    
    def get_all_movies(self) -> None:
        for movie in self.movie_list:
            print(movie)

    # def get_movie_by_title(self) -> None


# Méthodes à implémenter :
# b) CRUD

# get_movie_by_title : Rechercher un film par titre (insensible à la casse)
# get_movies_sorted_by_date : Retourner les films triés par date de sortie croissante
# update_movie_by_title : Modifier un ou plusieurs champs d'un film trouvé par titre
# delete_movie_by_title : Supprimer un film par titre

new_manager = MovieManager()
new_manager.load_from_json()

print(new_manager.get_all_movies())

test_movie = Movie("bla", "14/06/2020", "bla bla bla bla bla")

new_manager.create_movie(test_movie)
new_manager.save_to_json()