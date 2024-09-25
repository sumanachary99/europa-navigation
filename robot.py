from grid import Grid

class Robot:
    directions = [ 'N','NE',"E","SE",'S','SW','W', 'NW' ]

    def __init__(self,x,y, direction,grid):
        self.x = x
        self.y = y
        self.direction = direction
        self.grid = grid
  
  #Grid size is 3, 3 
  # Current position is 1 1 NE
  # L , M - 1,2

    def turn_left(self):

        current_index = Robot.directions.index(self.direction)
        self.direction = Robot.directions[(current_index - 1) % 8]
        

    def turn_right(self):
        current_index = Robot.directions.index(self.direction)
        self.direction = Robot.directions[(current_index + 1) % 8]
     
    def move(self):
        
        if self.direction == 'N':
            if self.grid.is_valid_position(self.x,self.y + 1):
                self.y += 1
        elif self.direction =='E':
            if self.grid.is_valid_position(self.x + 1,self.y):
                self.x += 1
        elif self.direction == 'S':
            if self.grid.is_valid_position(self.x,self.y - 1):
                self.y -= 1
        elif self.direction == 'W':
            if self.grid.is_valid_position(self.x - 1,self.y):
                self.x -=1
        elif self.direction == 'NE':
            if self.grid.is_valid_position(self.x + 1,self.y + 1):
                self.x += 1
                self.y += 1
        elif self.direction == 'SE':
            if self.grid.is_valid_position(self.x + 1,self.y - 1):
                self.x += 1
                self.y -= 1
        elif self.direction == 'NW':
            if self.grid.is_valid_position(self.x - 1,self.y + 1):
                self.x -=1
                self.y += 1
        elif self.directom == 'SW':
            if self.grid.is_valid_position(self.x - 1,self.y - 1):
                self.x -=1
                self.y -=1
       
        

    def execute_instructions(self,instructions):
        for command in instructions:
            if command == 'L':
                self.turn_left()
            elif command == 'R':
                self.turn_right()
            elif command == 'M':
                self.move()
    def __str__(self) -> str:
        return f"{self.x} {self.y} {self.direction}"
