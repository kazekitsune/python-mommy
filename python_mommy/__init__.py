import random
import subprocess
import sys
import colorama
import termcolor
import os

# config. separate with "/" to make a list of choices
MOMMYS_ROLE = os.environ.get("PYTHON_MOMMYS_ROLE", "mommy") # anything
MOMMYS_PRONOUNS = os.environ.get("PYTHON_MOMMYS_PRONOUNS", "her") # anything
MOMMYS_LITTLE = os.environ.get("PYTHON_MOMMYS_LITTLE", "girl") # anything
MOMMYS_EMOTES = os.environ.get("PYTHON_MOMMYS_EMOTES", "❤️/💖/💗/💓/💞") # anything
MOMMYS_MOODS = os.environ.get("PYTHON_MOMMYS_MOODS", "chill") # strictly chill/thirsty/yikes
MOMMYS_PARTS = os.environ.get("PYTHON_MOMMYS_PARTS", "milk") # anything
MOMMYS_FUCKING = os.environ.get("PYTHON_MOMMYS_FUCKING", "slut/toy/pet/pervert/whore") # anything

responses = {
    "chill": {
        "positive": [
            "*pets your head*",
            "*gives you scritches*",
            "you're such a smart cookie~",
            "that's a good AFFECTIONATE_TERM~",
            "MOMMYS_ROLE thinks MOMMYS_PRONOUN little AFFECTIONATE_TERM earned a big hug~",
            "good AFFECTIONATE_TERM~\nMOMMYS_ROLE's so proud of you~",
            "aww, what a good AFFECTIONATE_TERM~\nMOMMYS_ROLE knew you could do it~",
            "you did it~!",
            "MOMMYS_ROLE loves you~",
            "*gives you a sticker*"
        ],
        "negative": [
            "MOMMYS_ROLE believes in you~",
            "don't forget to hydrate~",
            "aww, you'll get it next time~",
            "do you need MOMMYS_ROLE's help~?",
            "MOMMYS_ROLE still loves you no matter what~",
            "oh no did MOMMYS_ROLE's little AFFECTIONATE_TERM make a big mess~?",
            "MOMMYS_ROLE knows MOMMYS_PRONOUN little AFFECTIONATE_TERM can do better~",
            "MOMMYS_ROLE still loves you~",
            "just a little further, sweetie~"
        ]
    },















    "thirsty": {
        "positive": [
            "*tugs your leash*\nthat's a VERY good AFFECTIONATE_TERM~",
            "*runs MOMMYS_PRONOUN fingers through your hair* good AFFECTIONATE_TERM~ keep going~",
            "*smooches your forehead*\ngood job~",
            "*nibbles on your ear*\nthat's right~\nkeep going~",
            "*pats your butt*\nthat's a good AFFECTIONATE_TERM~",
            "*drags MOMMYS_PRONOUN nail along your cheek*\nsuch a good AFFECTIONATE_TERM~",
            "*bites MOMMYS_PRONOUN lip*\nmhmm~",
            "give MOMMYS_PRONOUN a kiss~",
            "*heavy breathing against your neck*"
        ],
        "negative": [
            "do you think you're going to get a reward from MOMMYS_ROLE like that~?",
            "*grabs your hair and pulls your head back*\nyou can do better than that for MOMMYS_ROLE can't you~?",
            "if you don't learn how to code better, MOMMYS_ROLE is going to put you in time-out~",
            "does MOMMYS_ROLE need to give MOMMYS_PRONOUN little AFFECTIONATE_TERM some special lessons~?",
            "you need to work harder to please MOMMYS_ROLE~",
            "gosh you must be flustered~",
            "are you just keysmashing now~?\ncute~",
            "is MOMMYS_ROLE's little AFFECTIONATE_TERM having trouble reaching the keyboard~?"
        ]
    },
    "yikes": {
        "positive": [
            "keep it up and MOMMYS_ROLE might let you cum you little DENIGRATING_TERM~",
            "good DENIGRATING_TERM~\nyou've earned five minutes with the buzzy wand~",
            "mmm~ come taste MOMMYS_ROLE's MOMMYS_PART~",
            "*slides MOMMYS_PRONOUN finger in your mouth*\nthat's a good little DENIGRATING_TERM~",
            "you're so good with your fingers~\nMOMMYS_ROLE knows where MOMMYS_PRONOUN DENIGRATING_TERM should put them next~",
            "MOMMYS_ROLE is getting hot~",
            "that's a good DENIGRATING_TERM~",
            "yes~\nyes~~\nyes~~~",
            "MOMMYS_ROLE's going to keep MOMMYS_PRONOUN good little DENIGRATING_TERM~"
        ],
        "negative": [
            "you filthy DENIGRATING_TERM~\nyou made a mess, now clean it up~\nwith your tongue~",
            "*picks you up by the throat*\npathetic~",
            "*drags MOMMYS_PRONOUN claws down your back*\ndo it again~",
            "*brandishes MOMMYS_PRONOUN paddle*\ndon't make me use this~",
            "DENIGRATING_TERM.\nDENIGRATING_TERM~\nDENIGRATING_TERM~~",
            "get on your knees and beg MOMMYS_ROLE for forgiveness you DENIGRATING_TERM~",
            "MOMMYS_ROLE doesn't think MOMMYS_PRONOUN little DENIGRATING_TERM should have permission to wear clothes anymore~",
            "never forget you belong to MOMMYS_ROLE~",
            "does MOMMYS_ROLE need to put you in the DENIGRATING_TERM wiggler~?",
            "MOMMYS_ROLE is starting to wonder if you should just give up and become MOMMYS_PRONOUN breeding stock~"
        ]
    }
}

colorama.just_fix_windows_console()

for mood in MOMMYS_MOODS.split("/"):
    if mood not in responses.keys():
        print(termcolor.colored("mommy does not like her mood \""+mood+"\"~"))
        exit(1)

def make_response(template):
    return template.replace("MOMMYS_ROLE", random.choice(MOMMYS_ROLE.split("/")))\
                   .replace("AFFECTIONATE_TERM", random.choice(MOMMYS_LITTLE.split("/")))\
                   .replace("DENIGRATING_TERM", random.choice(MOMMYS_FUCKING.split("/")))\
                   .replace("MOMMYS_PRONOUN", random.choice(MOMMYS_PRONOUNS.split("/")))\
                   .replace("MOMMYS_PART", random.choice(MOMMYS_PARTS.split("/")))\
                   + " " + random.choice(MOMMYS_EMOTES.split("/"))

if __name__ == "__main__":
    fail = False
    try:
        code = subprocess.run(["python", *sys.argv[1:]]).returncode
    except: fail = True
    if code != 0: fail = True

    situation = "negative" if fail else "positive"
    print()
    print(
        termcolor.colored(make_response(random.choice(responses[random.choice(MOMMYS_MOODS.split("/"))][situation])), attrs=["bold"])
    )
    exit(code)
