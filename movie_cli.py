from movie_manager import MovieManager
from movie import Movie

def movie_cli(movie_manager_to_use : MovieManager):
    print("\nMenu")
    print("1. Create a film")
    print("2. Show all films")
    print("3. Update a film")
    print("4. Delete a film")
    print("5. Quit")

    choice = input("\nWhat do you want to do ? ")

    match choice:
        case "1":
            title = input("Movie Title: ")
            released_date = input("Released Date in dd/mm/yy format only: ")
            description = input("Description: ")

            new_movie = Movie(title,released_date, description)
            movie_manager_to_use.create_movie(new_movie)
            print(f"\nSuccessfully created {title} movie in the list")
            movie_manager_to_use.save_to_json()
        
        case "2":
            print("\nAll Movies:")
            movie_manager_to_use.get_all_movies()

        case "5":
            print("Goodbye")
            exit(0)