from django.shortcuts import render
import youtube_dl
from django.template.defaultfilters import filesizeformat

def videos(request):
	context = {}

	if request.POST:
		url =request.POST['url']		
		options = {
			'format': 'best',
			# 'outtmpl': 'DIR-PATH-HERE%(title)s'+'.mp4',
			'noplaylist': True,
			'extract-audio': True,
		}
		
		ydl = youtube_dl.YoutubeDL(options)
		# ydl.download([url ])
		video = ydl.extract_info(url, download=True )

		# urls = [f for f in info['formats'] ]
		video_streams = []
		for formato in video["formats"]:
			video_streams.append({			    
			    'extension': formato["ext"],
			    'file_size': filesizeformat(formato["filesize"]),
			    'video_url': formato["url"] + "&title=" + video["title"]
			})

		
		         


		context = {
           'title': video["title"],      
           'description': video["description"], 
           'likes': video["like_count"],
           'dislikes': video["dislike_count"],
           'duration': video["duration"],
           'views': video["view_count"],
           'ext': video["ext"],
           'format': video["format"],
           # 'resolution': video["resolution"],
           'url': video["url"] + "&title=" + video["title"],
           'video_streams': video_streams
       	}

		
		# context = { 'video_audio_streams': "yes" }

	return render(request, 'videos/index.html', context)




	