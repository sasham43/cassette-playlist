# inspired by and relying entirely on: http://dabeaz.blogspot.com/2010/09/using-telnet-to-access-my-superboard-ii.html

import decode, encode, json, subprocess

print('starting...')

playlist_txt = "playlist.txt"
playlist_wav = "playlist.wav"

def choose():
    choice = input("(e)ncode or (d)ecode?")

    if choice == 'e':
        print('encoding...')
        encode.run_encode(playlist_txt, playlist_wav)
        choose() # loop
    elif choice == 'd':
        print('decoding...')
        decode.run_decode(playlist_wav, playlist_txt)
        # read playlist
        playlist_json = open(playlist_txt, "r").read())
        playlist = json.loads(playlist_json)

        # play videos
        for video in playlist['playlist']:
            print('video:', video)

        # wipe wav
        subprocess.call(['rm', playlist_wav])


choose()
