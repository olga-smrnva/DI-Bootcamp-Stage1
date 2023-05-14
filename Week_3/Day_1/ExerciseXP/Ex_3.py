# 1. Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).

class Song:
	def __init__(self, song_lyrics):
		self.lyrics = song_lyrics

# 2. Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.

	def sing_me_a_song (self):
		print(*self.lyrics, sep='\n')
		

# 3. Create an object, for example:

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

# 4. Then, call the sing_me_a_song method.

stairway.sing_me_a_song()