import pdb
from models.artist import Artist
from models.album import Album
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

artist1 = Artist("Queen")
album1 = Album("A Night at the Opera", "Rock", artist1)
album2 = Album("A Day at the Races", "Rock", artist1)

artist_repository.save(artist1)
album_repository.save(album2)
album_repository.save(album1)


album_repository.select_all()
artist_repository.select_all()

