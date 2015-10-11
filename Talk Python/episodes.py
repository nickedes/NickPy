from requests import get

# url = 'http://talkpython.fm/episodes/all'

# Got a direct url for download. Yay! :D
url = 'http://talkpython.fm/episodes/download/'

for num in range(1, 2):
    response = get(url+str(num)+'/').content
    filename = "1.mp3"
    with open(filename, 'wb') as f:
        f.write(response)
