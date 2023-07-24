import dev_test_lib as test
import game_button_dots as dots
import time as t

time_await = 0.5

def test_1(): # get coords
    print(test.get_coord())

def test_coords():
    test_dot = dots.resize_dot(800, 900)
    print(test_dot.info())
    
def test_access():
    print(dots.ADD_PAWN.info())

def test_buttons_pos():
    for i in range(0, 5):
        for j in range (0, 3):
            t.sleep(time_await)
            test.move_to(dots.Pawn(i, j))
            t.sleep(time_await)
            test.move_to(dots.Upgrade(i))
        test.move_to(dots.Hero_Skill())


## main func
## В бой меджу мечами точка (x=986, y=848)
def run_test():
    #test_1()
    #test_coords()
    #test_access()
    test_buttons_pos()
    
run_test()
