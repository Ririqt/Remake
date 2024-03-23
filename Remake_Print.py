from pyfiglet import Figlet

font_1 = Figlet(font="epic")
your_name = str(input("Enter Your Name: "))
your_dream_job = str(input("Enter Your Dream Job: "))

text_art_1 = (font_1.renderText("Hi" + your_name + "!"))
text_art_2 = (font_1.renderText("I hope you will become a " + your_dream_job + "!"))

print('\033[95m' + text_art_1 + text_art_2)

your_birth_month = str(input(your_name + "!" + "When is your birth month?: "))
your_school = str(input("What school do you will pursue " + your_dream_job + "?: "))

print("Have a blast on " + your_birth_month + "!")
print("Study Hard at " + your_school + "!")

