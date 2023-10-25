
favorite_artist_song = []
while True:
    artist = input("Enter your favorite artist: ")

    if artist.lower() == 'quit':
        break
    song = input("Enter your favorite song:")
    favorite = {'artist':artist, 'song':song}
    favorite_artist_song.append(favorite)





def l_l():
     for entry in favorite_artist_song:
            artist_name = entry['artist']
            songs = entry["song"]
            filtered_song_name = songs.split(",")
            
            c = len(filtered_song_name)
            
               
            alex.penup()
            alex.begin_fill()
            alex.left(90)
            alex.forward(15 * c)
            alex.left(90)
            alex.forward(15)
            alex.left(90)
            alex.forward(15 * c)
            alex.end_fill()
            alex.penup()
            alex.forward(15)
            alex.write(artist_name)
            alex.backward(15)
            alex.left(90)
            alex.forward(70)
            
            
            
                   
import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")
screen.title("favourite songs")
tess = turtle.Turtle()
tess.hideturtle()
tess.color("black")
tess.pensize(3)

alex = turtle.Turtle()
alex.color("black","red")
alex.hideturtle()

bar_pen = turtle.Turtle()
bar_pen.color("black","red")
bar_pen.hideturtle()




def look_move():
    tess.forward(-300)
    tess.left(90)
    tess.forward(160)



tess.pensize(2)
tess.hideturtle()
def draw_x():
    tess.penup()
    tess.forward(-160)
    tess.pendown()
    
    
    for i in range(1,16):
        tess.forward(15)
        tess.left(90)
        tess.forward(20)
        tess.write(i)
        tess.forward(-20)
        tess.right(90)
    tess.penup()
    alex.backward(270)



        

look_move()
draw_x() 
l_l()

bar_pen.penup()
bar_pen.left(90)
bar_pen.forward(250)
bar_pen.pendown()
bar_pen.begin_fill()

bar_pen.left(90)
bar_pen.fd(10)
bar_pen.left(90)
bar_pen.fd(10)
bar_pen.left(90)
bar_pen.fd(10)
bar_pen.left(90)
bar_pen.fd(10)
bar_pen.end_fill()
bar_pen.penup()
bar_pen.left(90)
bar_pen.fd(8)
bar_pen.left(90)
bar_pen.fd(20)
bar_pen.left(90)
bar_pen.fd(10)
bar_pen.write("songs")


screen.mainloop()



