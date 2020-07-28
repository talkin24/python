music_json = open('data/music.json', encoding = 'UTF8')

import json

music_dict = json.load(music_json)

def music_info(music):
    result = {}
    result['singer'] = music{'singer'}
    result['title'] = music{'title'}

print(result)
