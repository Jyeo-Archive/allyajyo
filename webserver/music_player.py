import os
import pathlib
import random
def music_path():
    return str(pathlib.Path.home()) + '\\music'

def get_playlist():
    playlist = [f for f in os.listdir(music_path()) if os.path.isfile(os.path.join(music_path(), f))]
    # get list of mp3 filenames(=playlist) on music folder

    # print(playlist)
    for idx, filename in enumerate(playlist):
        if os.path.splitext(filename)[1].lower()!='.mp3':
            #print(filename)
            playlist.remove(filename)
        # else:
        #     print(filename)
    # print(playlist)
    # remove filenames of non-mp3 files on playlist

    random.shuffle(playlist) # randomly shuffle items in playlist
    playlist = [music_path() + '\\' + filename for filename in playlist]
    # add music_path to filename
    return playlist

def get_random_music():
    return random.choice(get_playlist())

def get_music_tags(filename):
    music_tags = []
    from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
    mp3 = MP3File(filename)
    try:
        tags = mp3.get_tags()
    except:
        pass
    song = ''
    album = ''
    artist = ''
    try:
        song = tags['ID3TagV2']['song']
    except:
        song = filename.replace(music_path() + '\\', '')
        song = song.replace('.mp3', '')
    try:
        artist = tags['ID3TagV2']['artist']
    except:
        artist = "알 수 없는 아티스트"
    try:
        album = tags['ID3TagV2']['album']
    except:
        album = "알 수 없는 앨범"
    if album == None: 
        album = "알 수 없는 앨범"
    # import sys
    music_tags.append(song)
    music_tags.append(artist)
    music_tags.append(album)
    # sys.stdout.write(song + "\n" + artist + ', ' + album + "\n")
    return music_tags

if __name__ == "__main__":
    playlist = get_playlist()
    for music in playlist:
        print("=====")
        music_tags = get_music_tags(music)
        print (music_tags[0] + "\n" + music_tags[1] + ', ' + music_tags[2])
        print("=====")