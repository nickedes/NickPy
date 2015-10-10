from requests import get

url = 'http://talkpython.fm/episodes/all'

test_url = 'http://talkpython.fm/episodes/show/28/making-python-fast-profiling\
-python-code'

data = get(test_url)
print(data.content)
