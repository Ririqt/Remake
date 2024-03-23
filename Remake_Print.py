# Pseudocode

# 1. Import Modules for Fancy Style in Outputs
from pyfiglet import Figlet

# 2. Inputting User's Name and Dream Job
font_1 = Figlet(font="epic")
your_name = str(input("Enter Your Name: "))
your_dream_job = str(input("Enter Your Dream Job: "))

# 3. Display The User's Name and Dream Job with Style
text_art_1 = (font_1.renderText("Hi" + your_name + "!"))
text_art_2 = (font_1.renderText("I hope you will become a " + your_dream_job + "!"))

print('\033[95m' + text_art_1 + text_art_2)

# 4. Inputting User's Additional Info
font_2 = Figlet(font="cybermedium")
your_birth_month = str(input(your_name + "! " + "When is your birth month?: "))
your_school = str(input("What school do you will pursue " + your_dream_job + "?: "))

# 5. Display the User's Additional Info with Style
text_art_3 = (font_2.renderText("Have a blast on " + your_birth_month + "!"))
text_art_4 = (font_2.renderText("Study Hard at " + your_school + "!"))

print('\033[92m' + text_art_3 + text_art_4)
