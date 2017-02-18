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
        choose() # let's do the time warp again
    elif choice == 'd':
        print('decoding...')
        decode.run_decode(playlist_wav, playlist_txt)
        # read playlist
        playlist_json = open(playlist_txt, "r").read()
        playlist = json.loads(playlist_json)

        # play videos
        for video in playlist['playlist']:
            # youtube_dl = [
            #     'youtube-dl',
            #     '-g',
            #     '\'' + video + '\''
            # ]
            youtube_dl = 'youtube-dl -g \'' + video + '\''
            response = subprocess.check_output(youtube_dl, stderr=subprocess.STDOUT, shell=True)
            print ('response:', response)
            subprocess.check_output('omxplayer \'' + response + '\'')
            # print('omx:', omx))
            # youtube_dl = '`youtube-dl -g ' + video + '`'
            # omx = 'omxplayer' + youtube_dl
            # subprocess.call(omx)

        # youtube_dl = '`youtube-dl -g ' + playlist[0] + '`'



        # wipe wav
        subprocess.call(['rm', playlist_wav])


choose()
