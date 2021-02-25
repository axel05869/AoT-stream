from bs4 import BeautifulSoup
import requests
import re
import os

def episode_info_grabber(MALanimelink):
	html = requests.get(MALanimelink).text
	soup = BeautifulSoup(html, 'html.parser')
	find = soup.find_all('a', {'class':'fw-b'})

	eptitles = []
	for title in find:
		eptitles.append(title.text)
	return eptitles


def episode_link_generator(link,how_many:int): # generate GOGO anime episode link
	remove = link.replace('category/','')
	
	eplinks = []
	n = 1
	while n <= how_many:
		eplinks.append(f'{remove}-episode-{n}')
		n+=1
	return eplinks


def video_link_grabber(gogoepisodelink):
	html = requests.get(gogoepisodelink).text
	soup = BeautifulSoup(html, 'html.parser')
	
	source = ['anime', 'vidcdn', 'streamsb', 'cloud9', 'xstreamcdn', 'mp4upload']
	for s in source:
		try:
			videolink = soup.find('li', {'class':s}).a['data-video']
			if s in ['anime', 'vidcdn']:
				videolink = f'https:{videolink}'
			return videolink
		except:
			pass