# Europa-navigation
The Europa Navigation Module is a Python-based solution for NASA's mission to explore Jupiter's moon, Europa. This module simulates the movement of robots on Europa's icy surface, processing navigation instructions to explore the terrain efficiently.

## Setup Instructions

1. Clone the repository:

   git clone https://github.com/your-username/europa_mission.git
   cd europa_mission
   
2. Install dependencies (if any). This script only uses Python's built-in libraries, so no extra dependencies are needed.

3. Run the program:

   python main.py
   
4. Input the following values interactively:

   5 5
   
   1 2 N
   
   LMLMLMLMM
   
   3 3 E
   
   MMRMMRMRRM
   
6. Expected output:

   1 3 N
   5 1 E
   
### Assumptions:
- The plateau's lower-left corner is always at (0, 0).
- Input is given in the format specified in the problem statement.
