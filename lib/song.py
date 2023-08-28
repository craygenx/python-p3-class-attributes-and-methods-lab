class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(self):
        if self.genre not in self.genres:
            self.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist not in self.artists:
            self.artists.append(self.artist)

    @classmethod
    def add_to_genre_count(cls):
        if cls.genre_count.get(cls, None) is None:
            cls.genre_count[cls] = 1
        else:
            cls.genre_count[cls] += 1

    def add_to_artist_count(self):
        if self.artist_count.get(self.artist, None) is None:
            self.artist_count[self.artist] = 1
        else:
            self.artist_count[self.artist] += 1

