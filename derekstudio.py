class Student(object):
	def __init__(self, name):
		self.name = name
		self.piano_pieces = list()

	def addSong(self, song):
		self.piano_pieces.append(song)

class PianoPiece(object):
	def __init__(self, title, yt_link):
		self.title = title
		self.yt_link = yt_link

	def __str__(self):
		return self.title

rami = Student("Rami")
kinglion = PianoPiece("King Lion", "https://youtu.be/l2IKfqGvm2o")
rami.addSong(kinglion)

zack = Student("Zack")
myfrog = PianoPiece("My Frog", "https://youtu.be/gi5PofvyPZE")
zack.addSong(myfrog)

meredith = Student("Meredith")
rainbowfish = PianoPiece("Rainbow Fish", "https://youtu.be/TtAdy102eTE")
cantankerouskangaroo = PianoPiece("Cantankerous kangaroo", "https://youtu.be/4TZu3EuaBFA")
meredith.addSong(cantankerouskangaroo)
meredith.addSong(rainbowfish)

soncia = Student("Soncia")
bbb = PianoPiece("Beach Buggy Boogie", "https://youtu.be/5VAMyyHXnzo")
soncia.addSong(bbb)

travis = Student("Travis")
clarinetblues = PianoPiece("Clarinet Blues", "https://youtu.be/Nwil151lP0o")
videogamemaster = PianoPiece("Video Game Master", "https://youtu.be/7NBtvJyM154")
travis.addSong(clarinetblues)
travis.addSong(videogamemaster)

bennett = Student("Bennett")
wethands = PianoPiece("Wet Hands", "https://youtu.be/LdTvneIXLUc")
winterdreams = PianoPiece("Winter Dreams", "https://youtu.be/EOv8BQKGv5c")
honeysucklerag = PianoPiece("Honeysuckel Rag", "https://youtu.be/PyTDgK1s3WM")
bennett.addSong(wethands)
bennett.addSong(winterdreams)
bennett.addSong(honeysucklerag)

ben = Student("Ben")
whirlingtarentella = PianoPiece("Whirling Tarentlla", "https://youtu.be/5Zo1OJso4FI")
rockintree = PianoPiece("Rockin' Around the Christmas tree", "https://youtu.be/pmI3ZMLLjKk")
jazzromance = PianoPiece("Jazz Romance", "https://youtu.be/DFTrhQtx9BM")
carolofthebells = PianoPiece("tso", "https://youtu.be/eRpsPB-bviU")
ben.addSong(whirlingtarentella)
ben.addSong(rockintree)
ben.addSong(jazzromance)
ben.addSong(carolofthebells)

daniel = Student("Daniel")
summermood = PianoPiece("summermood", "https://youtu.be/E1jME8RJ-Jw")
scherzo = PianoPiece("Scherzo", "https://youtu.be/aR8CAJ_CsY8")
goingplaces = PianoPiece("Going Places", "https://youtu.be/9oiU4ijW2vY")
daniel.addSong(summermood)
daniel.addSong(scherzo)
daniel.addSong(goingplaces)

tap = Student("Tap")
dinojourney = PianoPiece("Dinosaur Journey", "https://youtu.be/EC_OrrzHu1k")
tap.addSong(dinojourney)

derek = Student("Derek")
dinojourney = PianoPiece("Debussy Prelude", "https://youtu.be/Lx7mgrCwtlE")
derek.addSong(dinojourney)


# Debug
student_list = list()
student_list.append(rami)
student_list.append(zack)
student_list.append(soncia)
student_list.append(bennett)
student_list.append(ben)
student_list.append(daniel)
student_list.append(meredith)

# for student in student_list:
# 	print student.name
# 	for song in student.piano_pieces:
# 		print "\t", song.title
# 		print "\t\t", song.yt_link
# 	print "-" * 72