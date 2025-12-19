class Movie:
    def __init__(self, title, released_date, description):
        self.title = title
        self.released_date = released_date # string format DD/MM/YYYY
        self.description = description

    @property
    def title(self) -> str:
        return self._title
    
    @title.setter
    def title(self, new_title) -> None:
        self._title = new_title.title()

    @property
    def released_date(self) -> str:
        return self._released_date
    
    @released_date.setter # string format DD/MM/YYYY
    def released_date(self, new_released_date: str) -> None:
        # Error case not totally well working, it doesn't return the error like it should and just break for now
        try:
            destructured_date = new_released_date.split("/")
        
            if len(destructured_date) == 3:
                if destructured_date[0].isnumeric() and destructured_date[1].isnumeric() and destructured_date[2].isnumeric():
                    self._released_date = new_released_date

        except Exception:
            print("erreur")

    def __str__(self):
        return f"{self.title} released on {self.released_date} \n'{self.description}'"

test_movie = Movie("bla", "14/06/2020", "bla bla bla bla bla")
print(test_movie)


# Optionnellement :
# Avoir une méthode to_dict() pour convertir le film en dictionnaire (pour JSON)
# Avoir une méthode from_dict(data) pour créer un film depuis un dictionnaire