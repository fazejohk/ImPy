#!/usr/bin/python

import pyaudio
import wave

def playSound(whatsong):
    # length of data to read.
    chunk = 1024
    
    wf = wave.open("ting.wav", 'rb')
  
    # create an audio object
    p = pyaudio.PyAudio()

    # open stream based on the wave object which has been input.
    stream = p.open(format=
                    p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # read data (based on the chunk size)
    data = wf.readframes(chunk)

    # play stream (looping from beginning of file to the end)
    while data != '':
        # writing to the stream is what *actually* plays the sound.
        stream.write(data)
        data = wf.readframes(chunk)

    # cleanup stuff.
    stream.close()
    p.terminate()




while 1:
    with open("/media/pi/GGX/Snote.txt", 'r') as f:
        global review
        global check
        review = f.read()
        check = ""

        if review == check:
            print "Alright going to sleep\n" + str(check)
            sleep(10)
        else:
            #play(soundfx)
            print "Something changed"
            check = str(review)
            break
while 1:
    if review == check:
        print "\nAlright going to sleep\n"
        sleep(10)
    else:
        play(soundfx)
        print "\nThis changed\n"
        print review
        check = str(review)

    with open("/media/pi/GGX/Snote.txt", 'r') as f:
        review = f.read()
        print "Review:" + review + "\n" + "Check:" + check
        if review == check:
            print "It is checked"
        else:
            play(soundfx)
            check = str(review)
            print "\nThis changed\n"
            print review

