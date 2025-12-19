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
    def released_date(self, new_released_date) -> None:
        self._released_date = new_released_date

    def __str__(self):
        return f"{self.title} released on {self.released_date} \n '{self.description}'"

# La classe doit :
# Valider que la date est au format DD/MM/YYYY


# Optionnellement :
# Avoir une méthode to_dict() pour convertir le film en dictionnaire (pour JSON)
# Avoir une méthode from_dict(data) pour créer un film depuis un dictionnaire