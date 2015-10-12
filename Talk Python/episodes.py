from requests import get

# url = 'http://talkpython.fm/episodes/all'

# Got a direct url for download. Yay! :D
url = 'http://talkpython.fm/episodes/download/'
location = '/home/nickedes/Music/Talk Python/'

for num in range(1, 30):
    response = get(url+str(num)+'/')
    print(response.status_code)
    # if response.status_code == '200':
    data = response.content
    filename = location + str(num) + '.mp3'
    with open(filename, 'wb') as f:
        f.write(data)
    # doing this for d first time :P
    print('-Downloaded-', num)
