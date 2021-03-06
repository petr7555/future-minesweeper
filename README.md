## How to run this?
Run `python main.py` in the root directory.

### Choosing the right technology
Because the visualisation could be as simple as needed, I chose to create a console application.
Python is great for this purpose. It is fast to write, easy to read and I am very familiar with it.

### The problem consists of the following parts:
1. Getting necessary input parameters from the user
2. Placing mines on the board
3. Placing clues on the board
4. Displaying the board


1. Getting user's input is very straightforward in Python.
What was not as straightforward is the input validation.
It makes sense to me to allow only positive integer for number of rows and columns and also for the number of mines.
This is written explicitly in the assignment as well.
However, the assignment states that ANY positive integers are valid, but I think that allowing only number of mines 
smaller of equal to the number of available cells is a reasonable constraint.

2. I chose a two dimensional array as a data structure to represent the field, which is created using lists in Python.
First I create and empty field.
The solution for the following problems assumes, that the generated field might be unsolvable. 
Generating a solvable field is a much more complex task. The algorithm for this task is described for example
on pages 53 and 54 in [this document](https://dspace.cvut.cz/bitstream/handle/10467/68632/F3-BP-2017-Cicvarek-Jan-Algorithms%20for%20Minesweeper%20Game%20Grid%20Generation.pdf).
Allowing unsolvable fields I can place mines by generating x and y coordinate and placing the mine here if there is not
mine already.
This approach is slow when the field is large and the mines are placed densely as the random function needs to 
guess an empty cell.

    In the interview the following alternative strategies emerged:
    2. Create a set of possible coordinates for mines and pick from this set at random.
    3. Generate all mines at the beginning of the field and shuffle the field.
    4. For each field, place the mine with probability of mines_left/remaining_fields.

3. Two algorithms to solve placement of clues came to my mind:
    1. Place clues when placing mines. After a mine is placed, it's adjacent cells' values would be incremented by one
    if there wasn't other mine. 
    2. Iterate over whole field and for each cell look on its adjacent cells. If the adjacent cell contains a mine, 
    increment the counter. Write the final number to the cell. 
    
    I chose the second algorithm because it seems more intuitive and readable to me.
    Considering performance, the first algorithm is in O(n) where n is the number of mines.
    The second is in O(n) where n is the number of cells.
    
    If solved with the second algorithm, the problem is embarrassingly parallel (map reduce). We can split the field into subsections
    and generate clues for each section on its own CPU. 
    Using the first option, this would require locks on the cells.
        
4. I displayed the board by printing the values of cells into the console separated by pipes.

### Output example:
```
Game, W: 15, H: 10, Mines 30
| | | | | |1|2|x|2|x|1|2|x|x|2|
|1|1| |1|1|2|x|2|2|1|1|2|x|x|2|
|x|1|1|2|x|4|3|2| |1|1|2|3|3|2|
|1|1|1|x|3|x|x|2|1|2|x|1|2|x|3|
| | |1|1|2|2|3|3|x|2|1|2|3|x|x|
| | |1|1|1| |1|x|2|1| |1|x|4|3|
|1|2|3|x|2|1|1|1|1|1|1|2|1|2|x|
|1|x|x|3|x|2|1|1|1|2|x|1| |1|1|
|1|3|3|3|1|2|x|1|2|x|4|2|1| | |
| |1|x|1| |1|1|1|2|x|3|x|1| | |
```