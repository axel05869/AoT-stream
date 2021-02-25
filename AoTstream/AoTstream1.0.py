import os
import webbrowser
import colorama

from modules.grabber import *
from modules.misc import *


colorama.init() # this will fix ansii color not working on terminal
makePath(dataPath())


print(opstreamlogo)

# last watch episode
try:
	with open(dataPath() + '/lastwatch.txt', 'r') as f:
		lastwatch = f.read()
		print(colors.brightyellow + lastwatch + colors.reset)
except FileNotFoundError:
	pass


menu()

while True:
	choose = input('> ')
	if choose in ['1','2','3','4']:
		break
	else:
		continue

print()
try:
	if choose == '1':
		episodetitles = episode_info_grabber('https://myanimelist.net/anime/16498/Shingeki_no_Kyojin/episode')
		totalep = int(len(episodetitles)/2)
		episodelinks = episode_link_generator('https://gogoanime.vc/category/shingeki-no-kyojin', totalep)
	if choose == '2':
		episodetitles = episode_info_grabber('https://myanimelist.net/anime/25777/Shingeki_no_Kyojin_Season_2/episode')
		totalep = int(len(episodetitles)/2)
		episodelinks = episode_link_generator('https://gogoanime.vc/category/shingeki-no-kyojin-season-2', totalep)
	if choose == '3':
		episodetitles = episode_info_grabber('https://myanimelist.net/anime/35760/Shingeki_no_Kyojin_Season_3/episode')
		totalep = int(len(episodetitles)/2)
		episodelinks = episode_link_generator('https://gogoanime.vc/category/shingeki-no-kyojin-season-3', totalep)
	if choose == '4':
		episodetitles = episode_info_grabber('https://myanimelist.net/anime/40028/Shingeki_no_Kyojin__The_Final_Season/episode')
		totalep = int(len(episodetitles)/2)
		episodelinks = episode_link_generator('https://gogoanime.vc/category/shingeki-no-kyojin-the-final-season', totalep)
except:
	print(f'Connection error!\n')
	os.system('pause')
	exit()


while True:
	while True:
		try:
			inputep = int(input(f'Input episode number to watch. between 1 to {totalep}: '))
			if inputep > totalep or inputep < 1:
				continue
			else:
				break
		except ValueError:
			continue

	with open(dataPath() + '/lastwatch.txt', 'w') as f: # save input to lastwatch
		lastwatch = f.write(f'Last Watch: S{choose} Episode {inputep} - {episodetitles[inputep-1]}')

	try:
		videolink = video_link_grabber(episodelinks[inputep - 1]) # index list starts at 0. -1 will allow to get list data correctly
	except:
		print(f'Cannot connect to server!\n')
		os.system('pause')
		exit()

	print(f'\t{colors.brightred}Shingeki no Kyojin S{choose} - Episode {inputep}{colors.reset}')
	print(f'\t{colors.brightred}{episodetitles[inputep-1]}{colors.reset}')
	print(f'\t{colors.brightred}{videolink}{colors.reset}\n')


	# attach data to html and open on browser
	html = generate_html(videolink, inputep, episodetitles[inputep-1], choose)
	saveTo = dataPath() + '/videostream.html'
	with open(saveTo, "w") as f:
		f.write(html)
	
	webbrowser.open(f'file:///{saveTo}')