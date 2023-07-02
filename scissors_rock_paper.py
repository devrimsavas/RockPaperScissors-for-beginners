#export necessary modules
from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox


#routine shows who win and if player wants to play again
def winner(whowin):
    messagebox.showinfo("GAME OVER", f"The winner is {whowin}")
    play_again=messagebox.askyesno("Play Again", "Do you want to play again?")
    if play_again:
        reset_scores()
    else:
        root.destroy()

#for new game ,scores and text must be resetted
def reset_scores():
    global score_player
    global score_computer
    score_player=0
    score_computer=0
    label_score_player.config(text=f"SCORE: {score_player}")
    label_score_computer.config(text=f"SCORE: {score_computer}")

    
    

#game main function 
def game(selection): #function takes user selection and compare with computer's selection
    global score_computer
    global score_player
    winner_name=""

   
        
    
    
    computer=random.choice(['Rock', 'Paper','Scissors']) #computer select a random value from list
    #screen out picture of items selected by computer
    if computer=='Rock':
        label_computer_image.config(image=image_rock)
    elif computer=='Paper':
        label_computer_image.config(image=image_paper)

    else:
        label_computer_image.config(image=image_scissors)

    player=selection
    if player=='Rock':
        label_player_image.config(image=image_rock)
    elif player=='Scissors':
        label_player_image.config(image=image_scissors)
    else:
        label_player_image.config(image=image_paper)


    label_computer.config(text=f'   COMPUTER: {computer.upper()}')
    label_player.config(text=f'      PLAYER: {player.upper()}')

    #check selections
    if player==computer:#both player picked same object
        result="      EVEN"
    #conditions for player wins
    if (player=='Rock' and computer=='Scissors') or (player=='Scissors' and computer=='Paper') or (player=='Paper' and computer=='Rock'):
        result="   YOU WON"
        score_player+=1
        
    #conditions for computer wins
    if (computer=='Rock' and player=='Scissors') or (computer=='Scissors' and player=='Paper') or (computer=='Paper' and player=='Rock'):
        result="COMPUTER WON"
        score_computer+=1

    #print out who won 
    label_winner.config(text=result)
    label_score_player.config(text=f"SCORE :{score_player}")
    label_score_computer.config(text=f"SCORE :{score_computer}")

    #i set winner's score as 5 but this can be changed. 
    if score_player>5:
        winner_name="player"
        winner(winner_name)
    elif score_computer>5:
        winner_name="computer"
        winner(winner_name)

#End of the function

#quit game function
def quit_game():
    
    quit_ask=messagebox.askyesno("QUIT", "Are you sure to exit ? (y/n)")
    if quit_ask:
        root.destroy()
    else:
        pass

def about_program():
    about_window=Toplevel(root)
    program_text=f"""This Easy Program made by Python Tkinter and
usedsome graphic found in internet.
Program winners score set as 5 but you can change it.
The aim is to demonstrate classic game with tkinter.
New beginners are targetted.
Use this program how you wish.
Thanks
Devrim Savas Yilmaz
"""
    about_window.title("About This Program")
    about_window.geometry("420x260")
    info_text=Text(about_window,width=40,height=10, wrap=WORD, borderwidth=3,spacing3=2,font=("Arial",12, "italic"))
    info_text.place(x=10,y=10)
    info_text.insert(END,program_text)
    info_text.config(state="disabled",bg="beige")
    close_this=Button(about_window,text="CLOSE THIS WINDOW", command=about_window.destroy)
    close_this.place(x=150,y=230)
    

    about_window.mainloop()

#TKI GUI

root=Tk()
root.geometry("800x600")
root.title("Paper Rock Scissors")
root.resizable(False,False)
root.config(bg="green")

#file menus
my_menu=Menu(root)
root.config(menu=my_menu)
file_menu=Menu(my_menu)
my_menu.add_cascade(label="About",menu=file_menu,font=("Arial",12,"bold"))
file_menu.add_command(label="About This Program",font=("Arial",12),command=about_program)



#load images
image_rock=ImageTk.PhotoImage(Image.open('rock.png'))
image_scissors=ImageTk.PhotoImage(Image.open('scissors.png'))
image_paper=ImageTk.PhotoImage(Image.open('paper.png'))



global score_player
score_player=0 #reset score
result=""
global score_computer
score_computer=0

#image holder
holder=LabelFrame(root,width=780,height=330,borderwidth=3)
holder.place(x=10,y=200)

#label for winner
label_winner=Label(holder, text="GAME STARTED", font=("Arial",16))
label_winner.place(x=300,y=150)

#score player
label_score_player=Label(holder,text=f"SCORE :{score_player}",font=("Arial",16))
label_score_player.place(x=90,y=290)
#score_computer
label_score_computer=Label(holder,text=f"SCORE :{score_computer}",font=("Arial",16))
label_score_computer.place(x=570,y=290)

#players Area 
label_player=Label(holder, text="",font=("Arial",16))
label_player.place(x=5,y=5)

label_player_image=Label(holder,image=image_rock)
label_player_image.place(x=5, y=40)


#computer Area
label_computer=Label(holder,text="",font=("Arial",16))
label_computer.place(x=500, y=5)
label_computer_image=Label(holder,image=image_rock)
label_computer_image.place(x=500,y=40)

#Buttons
button_rock=Button(root, text="ROCK", width=20, font=("Arial",16), fg="blue",bg="beige",borderwidth=3, command=lambda:game('Rock'))
button_rock.place(x=10,y=20)

button_scissors=Button(root, text="SCISSORS", width=20, font=("Arial",16), fg="blue",bg="beige",borderwidth=3, command=lambda:game('Scissors'))
button_scissors.place(x=10,y=70)

button_paper=Button(root, text="PAPER", width=20, font=("Arial",16), fg="blue",bg="beige",borderwidth=3, command=lambda:game('Paper'))
button_paper.place(x=10,y=130)

button_quit=Button(text="QUIT", width=15,command=lambda:quit_game(),fg="blue",font=("Arial",16))
button_quit.place(x=600,y=550)

root.mainloop()






    
        
        
