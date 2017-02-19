import pyaudio

standard_sample_rates = [8000.0, 9600.0, 11025.0, 12000.0, 16000.0, 22050.0, 24000.0, 32000.0,44100.0, 48000.0, 88200.0, 96000.0,192000.0]

p = pyaudio.PyAudio()
devinfo = p.get_device_info_by_index(2)  # Or whatever device you care about.
for s in standard_sample_rates:
    if p.is_format_supported(s,  # Sample rate
                             input_device=devinfo['index'],
                             input_channels=devinfo['maxInputChannels'],
                             input_format=pyaudio.paInt16):
      print ('Yay!', s)
  else:
      print('boo', s)
