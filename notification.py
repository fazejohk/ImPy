from pydub import AudioSegment
from pydub.playback import play
from time import sleep

soundfx = AudioSegment.from_wav("/root/ImPy/ting.wav")



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
            play(soundfx)
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

