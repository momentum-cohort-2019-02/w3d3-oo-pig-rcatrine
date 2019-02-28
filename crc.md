## Pig Rules
First player to reach or surpass 100 points wins. Points are earned by the value of die roll (2-6 only). If a 1 is rolled, the turn of the current player is over and no points are earned.

Human player starts by rolling the die. If a 1 is not rolled, they can choose to hold and take the points rolled, or continue to roll and potentially accumulate or lose points.


## Game
**Responsibilities**
- Dictates the flow of the game

**Collaborators**
- Human
- Computer


## Start_Game
**Responsibilities**
- Initiates the game
- Notifies Player1 that the game has started, first roll will commence

**Collaborators**
- Game
- Human
- Computer


## Players
**Responsibilities**
- Chooses to roll or hold/pass
- Computer Player holds/passes at 20

**Collaborators**
- Game


## Human
**Responsibilities**
- Chooses to roll or hold/pass

**Collaborators**
- Game


## Computer
**Responsibilities**
- Chooses to roll or hold/pass
- Computer Player holds/passes at 20

**Collaborators**
- Game


## Die
**Responsibilities**
- Adds points to players total
- If the outcome of a roll greater than 1, player may continue to roll or hold/pass
- If 1 is rolled, player loses points, passes off turn

**Collaborators**
- Score
- Turn


## Score
**Responsibilities**
- Determines who wins/loses
- Compiles score at the end of each turn
- Verifies when score of 100 is reached/surpassed

**Collaborators**
- Game
- Win


## Win
**Responsibilities**
- Games ends at >= 100 total score

**Collaborators**
- Score
- Turn