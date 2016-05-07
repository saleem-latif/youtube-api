__author__ = 'Saleem Latif'

from youtube.api.search import Search
from youtube.api import Youtube
from pprint import pprint

youtube = Youtube("AIzaSyABmYiOMnn_H5CnQehAbm0a1BTbUlEUV9Y")

search = Search(youtube)

result = search(q="SMILEY - DEAD MAN WALKING")

pprint(result)
items = list(result.items)

videos_search = search.videos()
videos = list(videos_search.items)

next_page = result.next_page_token
result = search(q="SMILEY - DEAD MAN WALKING", pageToken=next_page)
pprint(result)
items = list(result.items)

pprint(items)
