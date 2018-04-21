# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")



init python:

    
    class Hero:
        def __init__(self):
            self.image = " "
            self.name = ""
            self.animal = ""
            self.heritage = ""
            self.stress = 0 # representation of damage suffered by hero
            
            self.stats = {"end":0, "ath":0, "rea":0, "wis":0, "cha":0, "mag":0}
            # Endurance, Athletics, Reasoning, Wisdom, Charisma, Magic
            
            self.human_relations = {"hun":20, "bak":20, "min":20, "may":20, "bar":20, "con":20}
            # Hunter, Baker, Mining Foreman, Mayor, Bartender, Construction Worker
            
            self.animal_relations = {"dee":20, "wol":20, "fox":20, "bea":20, "tur":20, "rab":20}
            # Deer, Wolves, Foxes, Beavers, Turtles, Rabbits

            self.spro = "___"
            self.opro = "___"
            self.xpro = "___"
            self.ppro = "___"
            self.rpro = "_______"

            # Insert other attributes needed here.
            

            
        def update_image(self, image):
            self.image = image
        def update_name(self, name):
            self.name = name
        def update_animal(self, animal):
            self.animal = animal
        def update_heritage(self, heritage):
            self.heritage = heritage
            
        def update_stat(self, stat_key, stat_shift): # shifts attribute with 3-letter name ("end", "ath", etc.) by the amount input
            self.stats[stat_key] += stat_shift
        def get_stat(self, stat_key): # returns the value of the stat under stat_key ("end", "ath", etc.)
            return self.stats[stat_key]
        
        
        def update_human_relation(self, human_key, relation_shift): # shifts human relation with 3-letter name ("bak", "hun", etc.) by the amount input
            self.human_relations[human_key] += relation_shift
        def get_human_relation(self, human_key): # returns the value of the stat under stat_key ("bak", "hun", etc.)
            return self.human_relations[human_key]
        
        
        
        def update_animal_relation(self, animal_key, relation_shift): # shifts attribute with 3-letter name ("dee", "bea", etc.) by the amount input
            self.animal_relations[animal_key] += relation_shift
        def get_animal_relation(self, animal_key): # returns the value of the stat under stat_key ("dee", "bea", etc.)
            return self.animal_relations[animal_key]
        
        
        def update_pronouns(self, pronouns):
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
            else:
                self.spro = "___"
                self.opro = "___"
                self.xpro = "___"
                self.ppro = "___"
                self.rpro = "_______"
            

    hero = Hero()
    # Hold all of the character images in a list
    char_list = ["dummy_char_yellow.png","dummy_char_green.png","dummy_char_orange.png","dummy_char_blue.png"]
    # As well as a position in the list that we are looking at
    char_list_pos = 0
    
    char = char_list[char_list_pos]
    
    def cycle(dir, clp, cl):
        return (clp + dir)%len(cl)
    
    # Staging variables to make sure that we allow players to back-track and
    # forward-track at will as they go through character creation
    stage_1_complete = False
    stage_2_complete = False
    stage_3_complete = False
    stage_4_complete = False
    stage_5_complete = False
    stage_6_complete = False
    gender_selected = ""




################################################################################
#
# Screen Definitions: Character Creation
#
################################################################################
    
   

    
    
screen s1_screen():
    modal True

    # Create confirmation button that moves to next stage and sets stage_1_complete to True
    frame:
        xalign 0.5 ypos 450
        vbox:
            textbutton "Confirm":
                if not gender_selected == "": #Should only be clickable once pronouns have been selected
                    clicked [SetVariable("stage_1_complete", True), Function(hero.update_image, char), Jump("stage_2")]

    # Create cycling button that swaps between character appearances
    frame:
        xalign 0.1 ypos 20
        vbox:
            xalign 0.5
            text "Select a character image:"
            grid 2 1:
                textbutton "<":
                    clicked [SetVariable("char_list_pos", cycle(-1, char_list_pos, char_list)), 
                        SetVariable("char", char_list[cycle(-1, char_list_pos, char_list)]),
                        Jump("stage_1")]

                textbutton ">":
                    clicked [SetVariable("char_list_pos", cycle(1, char_list_pos, char_list)), 
                        SetVariable("char", char_list[cycle(1, char_list_pos, char_list)]), 
                        Jump("stage_1")]
            
    # Create gender selection frame with selected buttons fading out
    # TODO: better understand idle/hover/clicked/selected/selected-hover image options and how
    # to seamlessly display them
    frame:
        xalign 0.9 ypos 20
        vbox:
            
            text "Click a pronoun to assign \n it to your character. [gender_selected]"
            textbutton "he, him, his":
                if not gender_selected == "m":
                    clicked [Function(hero.update_pronouns, "m"), SetVariable("gender_selected", "m"), Jump("stage_1"), SensitiveIf(gender_selected == "m")] 
            textbutton "she, her, hers":
                if not gender_selected == "f":
                    clicked [Function(hero.update_pronouns, "f"), SetVariable("gender_selected", "f"), Jump("stage_1"), SensitiveIf(gender_selected == "f")] 
            textbutton "ze, zir, zirs":
                if not gender_selected == "n":
                    clicked [Function(hero.update_pronouns, "n"), SetVariable("gender_selected", "n"), Jump("stage_1"), SelectedIf(gender_selected == "n")] 
            textbutton "they, them, theirs":
                if not gender_selected == "p":
                    clicked [Function(hero.update_pronouns, "p"), SetVariable("gender_selected", "p"), Jump("stage_1"), SelectedIf(gender_selected == "p")] 
         
         
    
                
                
            


################################################################################
# 
# Stages: Character Creation
#
################################################################################

label start:
    scene dummy_bg
    $ hero = Hero()




label stage_1:

    # Dynamic imagery to reload avatar at each step
    image c:
        "[char]"
    show c:
        xalign 0.1
        yalign 1.0

   
    show screen s1_screen
    "Create your character! Begin by selecting an appearance and your preferred pronouns. [hero.spro] and [hero.xpro] dog are headed to the place that is [hero.ppro]. [hero.spro] leads [hero.opro] to [hero.rpro]. \n\nWhen you are satisfied, press \"Confirm\" to proceed."
     
     #"Create your character! Begin by selecting an appearance and your preferred pronouns. \n\nWhen you are satisfied, press \"Confirm\" to proceed."



   

label stage_2:
    # Hide away old materials
    hide screen s1_screen
    hide c
    
    # Use permanent character assets rather than temporary variables from here forward
    image h = "[hero.image]"
    show h:
        xalign 0.1
        yalign 1.0
    show h at center
    with moveinleft
    "Congratulations! You have selected this avatar, with the pronouns [hero.spro], [hero.opro], [hero.ppro]."


    # This ends the game.
    return


#label char_update:
#    #"updating character art! [char_list_pos]"
#    $ char = char_list[char_list_pos]
#    show char at left
#    with dissolve
#    #"Does it look different?"
#    jump stage_1