from requests import get

# url = 'http://talkpython.fm/episodes/all'

# test_url = 'http://talkpython.fm/episodes/show/28/making-python-fast-profiling\
# -python-code'

# data = get(test_url)
# print(data.content)

# Got a direct url for download. Yay! :D
url = 'http://talkpython.fm/episodes/download/'

for num in range(1, 3):
    print(num)
    response = get(url+str(num))
    print(response.status_code)
