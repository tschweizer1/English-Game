# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define unknown = Character("???")

define commentary = Character("")

define player = Character("[playerName]")

define mom = Character("Mom")


# The game starts here.

    
label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Welcome to Insert Game Name"

    e "Before we begin, we’d like to give a quick warning regarding the context of this game – if you are uncomfortable with themes of murder, do not continue this game!"

    e "This game is purely fictional – any resemblance to real life places or people is coincidental"

    e "Now enjoy the game!"

    $ playerName = renpy.input("What is your name?: ", length=20)

    $ playerName.strip()

    if not playerName:
        $ playerName = "Charles the III"

    player "My name is [playerName]"

    scene black
    with fade

    unknown "... [playerName]!"

    unknown "[playerName!u]!!!"

    commentary "{i}Sheets rustling{/i}"

    play audio "alarm.ogg"

    scene bedroom
    with dissolve

    mom  "[playerName]! Wake up! You're going to be late!"

    player "Nnnn..."

    player "Crap..."

    player "{i}Slept in again... you think I would've learned after being late so many times already.{/i}"

    player "{i}Oh well, guess I better get ready and go{/i}"
    
    # This ends the game.

    return
