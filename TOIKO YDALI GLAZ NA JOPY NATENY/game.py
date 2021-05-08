from pygame import*
W=1300
H=700
win = display.set_mode((W,H))
bg = image.load("pole.jpg")
while True:

    for e in event.get():
        if e.type == 12:
            exit()
    win.blit(bg,(0,0))

    display.update()