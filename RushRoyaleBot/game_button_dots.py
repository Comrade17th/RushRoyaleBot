import dot_class as dt

SCREEN_WIDTH_DEV = 1920
SCREEN_HEIGHT_DEV = 1280

SCREEN_WIDTH = 1920 #1024
SCREEN_HEIGHT = 1280 #768

def resize_dot(x, y):
    return dt.dot(x * SCREEN_WIDTH / SCREEN_WIDTH_DEV,
    y * SCREEN_HEIGHT / SCREEN_HEIGHT_DEV)

def resize_x(x):
    return x * SCREEN_WIDTH / SCREEN_WIDTH_DEV

def resize_y(y):
    return y * SCREEN_HEIGHT / SCREEN_HEIGHT_DEV

ADD_PAWN = resize_dot(988,800)
HERO_SKILL = resize_dot(1153, 883)
UPGRADE_PAWN = resize_dot(793, 831) # dt x 64
UPGRADE_DT = resize_x(64)
PAWN_FIELD = resize_dot(847, 595) # dt x 55 y 55
FIELD_DT = resize_x(55)

def Add():
    return (ADD_PAWN)

# return dot where pawn may stay on center
def Pawn(x, y): 
    delta = FIELD_DT
    if (x < 0 or y < 0 or x > 5 or y > 3):
        print("error_pawn_out_of_range")
    else:
        return(dt.dot(PAWN_FIELD.x + delta / 2 + delta * x,
        PAWN_FIELD.y + delta / 2 + delta * y))

# return dot where pawn may stay on angle
def Pawn_(x, y): 
    delta = FIELD_DT
    if (x < 0 or y < 0 or x > 5 or y > 3):
        print("error_pawn_out_of_range")
    else:
        return(dt.dot(PAWN_FIELD.x + delta * x,
        PAWN_FIELD.y + delta * y))

# return dot of upgrade button on center
def Upgrade(x): 
    delta = FIELD_DT
    if (x < 0 or x > 4):
        print("error_upgrade_out_of_range")
    else:
        return(dt.dot(UPGRADE_PAWN.x + delta / 2 + delta * x, UPGRADE_PAWN.y + delta / 2))

# return dot of upgrade button on angle
def Upgrade_(x): 
    delta = FIELD_DT
    if (x < 0 or x > 4):
        print("error_upgrade_out_of_range")
    else:
        return(dt.dot(UPGRADE_PAWN.x + delta * x, UPGRADE_PAWN.y))

# return dot of hero button
def Hero_Skill():
    return(HERO_SKILL)

#UPGRADE_PAWN_BTN

#PAWN_FIELD