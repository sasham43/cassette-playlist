# inspired by and relying entirely on: http://dabeaz.blogspot.com/2010/09/using-telnet-to-access-my-superboard-ii.html

import decode
import encode

print('starting...')

print('decoding...')
decode.run_decode("playlist.wav", "playlist.txt")

# print('encoding...')
# encode.run_encode("playlist.txt", "playlist.wav")
