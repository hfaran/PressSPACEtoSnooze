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

FU_LEVELS = ["room", "work"]

FU_CMD_POS = (50, 650)


#assert all(i.startswith("FU_") for i in __all__)
