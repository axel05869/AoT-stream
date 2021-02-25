from pathlib import Path
import os

class colors:
  reset = "\033[0m"
  blue = "\033[34m"
  brightblue = "\033[34;1m"
  yellow = "\033[33m"
  brightyellow = "\033[33;1m"
  brightred = "\033[31;1m"


def dataPath():
    path = str(Path.home()/'aotstream_data')
    return path


def makePath(path):
    if not os.path.exists(path):
        os.makedirs(path)


opstreamlogo = fr'''
{colors.brightred}
   _____   __    __                 __                     __________ __  __                 
  /  _  \_/  |__/  |______    ____ |  | __   ____   ____   \__    ___|___/  |______    ____  
 /  /_\  \   __\   __\__  \ _/ ___\|  |/ /  /  _ \ /    \    |    |  |  \   __\__  \  /    \ 
/    |    |  |  |  |  / __ \\  \___|    <  (  <_> |   |  \   |    |  |  ||  |  / __ \|   |  \
\____|__  |__|  |__| (____  /\___  |__|_ \  \____/|___|  /   |____|  |__||__| (____  |___|  /
        \/                \/     \/     \/             \/                          \/     \/ 
{colors.reset}
'''

def menu():
  print()
  print('[1] Season 1')
  print('[2] Season 2')
  print('[3] Season 3')
  print('[4] The final season')


def generate_html(videolink, episodenumber, episodetitle, season):
  html_str = f'''
  <!DOCTYPE html>
  <html style="height:100%;">
  <head>
    <title>AoT stream</title>
  </head>
  <body style="height:100%; background-color:#0B0B0C;">
    <div style="height:100%; width:1280px; padding-top: 50px; margin:0 auto;">
      <center>
      <iframe src="{videolink}" width="1280" height="720" allowfullscreen style="border:none;"></iframe>
      </center>
      <h2 style="color:#C8C3BC; font-family:Gill Sans,sans-serif; float:left;">S{season} Episode {episodenumber} - {episodetitle}</h2>
      <image src="https://bit.ly/3kiR4om" style="width:220px; margin-top:8px; float:right;" alt="One Piece Logo">
    </div>
  </body>
  </html>
  '''
  return html_str