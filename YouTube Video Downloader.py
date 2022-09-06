from pytube import YouTube
SAVE_PATH = "E:/" 
link=["https://www.youtube.com/watch?v=XEA_o1eAVw8",
	"https://www.youtube.com/watch?v=KxD3dvMyQdI"
	]

for i in link:
	try:
  
		yt = YouTube(i)
	except:
		print("A connection error occurred.")
	mp4files = yt.filter('mp4')
  
	d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
	try:
		d_video.download(SAVE_PATH)
	except:
		print("An error occurred.")
print('Complete!')
