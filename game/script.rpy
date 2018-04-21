# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")



init python:
    # Hold all of the character images in a list
    char_list = ["dummy_char_yellow.png","dummy_char_green.png","dummy_char_orange.png","dummy_char_blue.png"]
    # As well as a position in the list that we are looking at
    char_list_pos = 0
    
    char = char_list[char_list_pos]
    
    def cycle(dir, clp, cl):
        return (clp + dir)%len(cl)
                
    class Hero:
        def __init__(self, image, pronouns):
            self.image = image
            if pronouns == "m":
                self.spro = "he"
                self.opro = "him"
                self.xpro = "his"
                self.ppro = "his"
                self.rpro = "himself"
            elif pronouns == "f":
                self.spro = "she"
                self.opro = "her"
                self.xpro = "her"
                self.ppro = "hers"
                self.rpro = "herself"
            elif pronouns == "p":
                self.spro = "they"
                self.opro = "them"
                self.xpro = "their"
                self.ppro = "theirs"
                self.rpro = "themselves"
            elif pronouns == "n":
                self.spro = "ze"
                self.opro = "zir"
                self.xpro = "zir"
                self.ppro = "zirs"
                self.rpro = "zirself"
        

# The game starts here.

label start:

    

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # Staging variables to make sure that we allow players to back-track and
    # forward-track at will as they go through character creation
    $ stage_1_complete = False
    $ stage_2_complete = False
    $ stage_3_complete = False
    $ stage_4_complete = False
    $ stage_5_complete = False
    $ stage_6_complete = False

    scene dummy_bg

    
    #"Create your character! Begin by selecting an appearance and your preferred pronouns. \n\nWhen you are satisfied, press \"Confirm\" to proceed."

# Create cycling button that swaps between character appearances
screen cycle_character_screen():
    frame:
        xalign 0.1 ypos 20
        vbox:
            
            text "Select a character image:"
            grid 2 1:
                xalign 0.5
                textbutton "<":
                    clicked [SetVariable("char_list_pos", cycle(-1, char_list_pos, char_list)), 
                        SetVariable("char", char_list[cycle(-1, char_list_pos, char_list)]),
                        Jump("stage_1")]

                textbutton ">":
                    clicked [SetVariable("char_list_pos", cycle(1, char_list_pos, char_list)), 
                        SetVariable("char", char_list[cycle(1, char_list_pos, char_list)]), 
                        Jump("stage_1")]
            #image char
            

# Create confirmation button that moves to next stage and sets stage_1_complete to True

# 

    
label stage_1:

    image c:
        "[char]"
    show c:
        xalign 0.1
        yalign 1.0

    show screen cycle_character_screen
    "Create your character! Begin by selecting an appearance and your preferred pronouns. currently on model [char]. \n\nWhen you are satisfied, press \"Confirm\" to proceed."
    
    


    # This ends the game.

    return


#label char_update:
#    #"updating character art! [char_list_pos]"
#    $ char = char_list[char_list_pos]
#    show char at left
#    with dissolve
#    #"Does it look different?"
#    jump stage_1