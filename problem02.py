import json
import pprint

def music_info(musics):
    result = []
    for music in musics:
        music_detail = {}
        music_detail['singer'] = music['singer']
        music_detail['title'] = music['title']
        # [] + [ {iu} ] => [{iu}]
        result = result + [music_detail]
    return result

musics_json = open('data/musics.json', encoding = 'UTF8')
musics_list = json.load(musics_json)

pprint.pprint(musics_list)
