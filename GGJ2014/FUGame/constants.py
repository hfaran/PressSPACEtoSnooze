FU_APATH = "assets"

FU_WIDTH = 1366
FU_HEIGHT = 768
FU_FRAME_RATE = 30

FU_DIRECTS = {
    "F": (0,  1),
    "B": (0, -1),
    "L": (-1, 0),
    "R": (1,  0),
}

FU_LEVELS = ["title", "room", "computer", "office", "hills"]

FU_CMD_POS = (50, 650)
FU_CMD_COLOR = (211, 226, 33)

FU_CREDITS = [
    "CREDITS",
    "",
    "PROGRAMMERS",
    "PHATTRICK TRAN",
    "DYLAN DUMESNIL",
    "HAMZA FARAN",
    "",
    "STORY CONSULTANT",
    "R. MORGAN SLADE",
    "",
    "GRAPHICS",
    "MADISON CALVERT",
    "ANDREA DAGRACA",
    "",
    "MUSIC",
    "ALICE SHANG",
    "",
    "SOUND FX",
    "TREE OF AUDIO",

]

# Use this like self.my_var = FU_SWAG_WORDS[:], i.e., crreate a copy!!!!!
FU_SWAG_WORDS = ["SWAG!", "BOUNCY CASTLES!", "SUPER SWEET!", "GOLD STAR!",
                 "SUPREME!", "CHAMP-STAR!", "NEAT STREET!", "FANTASTIBLAM!", "SO GOOD!",
                 "SUNSHINE!", "AWESOME-TASTIC!", "SILKY SMOOTH!", "GLEE-SPLOSION!",
                 "SMILE TOWN!", "AWESOME!", "GLEE-SUPREME!", "MAXIMUM HAPPY!",
                 "RAINBOWS FOR DAYS!", "CLEAR SKIES!", "FREE HUGS!", "GRIN-TO-WIN!"]


#assert all(i.startswith("FU_") for i in __all__)
