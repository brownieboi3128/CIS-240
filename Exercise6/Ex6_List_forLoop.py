#Christian Brown

fav_colors = ['red', 'green', 'blue']

def saveFile():
    f = open("colors.txt", "a")
    for fav_color in fav_colors:
        f.write(fav_color + "\n")
    f.close()

saveFile()
