class TvProgram:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    def __str__(self):
        return f'Name: {self._name} - Year: {self.year} - Likes: {self._likes}'

    @property
    def likes(self):
        return self._likes

    @property
    def name(self):
        return self._name

    def like(self):
        self._likes += 1

    @name.setter
    def name(self, new_name):
        self._name = new_name


class Movie(TvProgram):
    def __init__(self, name, year, length):
        super().__init__(name, year)
        self.length = length

    def __str__(self):
        return f'Name: {self._name} - Year: {self.year} - Length: {self.length} min - Likes: {self._likes}'


class TvShow(TvProgram):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'Name: {self._name} - Year: {self.year} - Seasons: {self.seasons} - Likes: {self._likes}'


class Playlist():
    def __init__(self, name, tv_programs):
        self.name = name
        self.tv_programs = tv_programs

    def __iter__(self):
        return self.tv_programs.__iter__()

    def __len__(self):
        return len(self.tv_programs)


avengers = Movie('avengers - guerra infinita', 2018, 160)
atlanta = TvShow('atlanta', 2018, 2)

avengers.like()
avengers.like()
avengers.like()

atlanta.like()
atlanta.like()

playlist = Playlist('minha playlist', [atlanta, avengers])

for programa in playlist:
    print(programa)