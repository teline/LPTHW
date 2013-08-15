class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
				   "I don't want to get sued",
				   "So I'll stop right there"])
				   
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])

mother_we_share_lyrics = ["I'm in misery where you can seem as old as your omens", "And the mother we share will never keep your proud head from falling", "The way is long but you can make it easy on me", "And the mother we share will never keep our cold hearts from \n\tcalling"]

mother_we_share = Song(mother_we_share_lyrics)
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

mother_we_share.sing_me_a_song()