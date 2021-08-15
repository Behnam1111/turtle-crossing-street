Turtle crossing game 
How it works: 
1. A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right. 

![img.png](static/img.png)
2. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.

3. When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. On the next level, the car speed increases.

4. When the turtle collides with a car, it's game over and everything stops.

![img_1.png](static/img_1.png)

Step 2 - Break down the Problem

Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north.

![img_2.png](static/img_2.png)

Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle)

![img_3.png](static/img_3.png)

Detect when the turtle player collides with a car and stop the game if this happens.

![img_4.png](static/img_4.png)

Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). When this happens, return the turtle to the starting position and increase the speed of the cars.

![img_5.png](static/img_5.png)

Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre.

![img_6.png](static/img_6.png)