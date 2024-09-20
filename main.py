
from robot import Robot
from grid import Grid

def main():
    plateau_size = input().split()
    print(plateau_size, "Grid Size")
    grid = Grid(int(plateau_size[0]),int(plateau_size[1]))
    
    while True:
        try:
            position = input().split()
            if not position:
                break

            x = int(position[0])
            y = int(position[1])
            direction = position[2]
            robot = Robot(x,y,direction,grid)

            instructions = input().strip()
            print(instructions , "instructions")
            robot.execute_instructions(instructions)

            print(robot)

        except EOFError:
            break




if __name__ == "__main__":
    main()