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
        print('start decoding...')
        decode.run_decode(playlist_wav, playlist_txt)
        print('decoded.  start playing...')
        # read playlist
        playlist_json = open(playlist_txt, "r").read()
        playlist = json.loads(playlist_json)

        # play videos
        for video in playlist['playlist']:
            print('video:', video)
            youtube_dl = 'youtube-dl -g \'' + video + '\''
            response = subprocess.check_output(youtube_dl, stderr=subprocess.STDOUT, shell=True)
            # print ('response:', response)
            response_str = response.decode('utf-8') # decode to String
            response_list = response_str.split('\n')
            # print ('response_list:', response_list)
            # response is the url twice cuz why the f not
            video_url = response_list[0].strip('\n')
            # print ('video_url:', video_url)
            omx = [
                'omxplayer',
                video_url
            ]
            subprocess.call(omx)



        # wipe wav
        subprocess.call(['rm', playlist_wav])


choose()
