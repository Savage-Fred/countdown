# Countdown
This project is based on the number game in the British television show [Countdown](https://en.wikipedia.org/wiki/Countdown_(game_show)). I've really become obsessed wtih this game recently.  

## How the Game Works 
* Player chooses **b** "big numbers" such that **b** is between 1 and 4
* **b** numbers are drawn from {25,50,75,100} with no duplicates.
* The difference of 6 and **b** = **l** where **l** is the number of "little numbers" drawn from [1...10] with no duplicates allowed.
* A random target **t** between 100 and 999 is choosen.
* The players use any of the 4 basic arithmetic operators (+,-,\*,/) in any order using the choosen numbers at most once to try to get as close to the target as possible.
* Whoever is closest wins

# Conjecture
It is not always possible to hit the target - provable by counterexample. However, I conject that there exists some relaxation of the rules under which it is **always possible** to combine a set of randomly chosen integers using some set of arithmetic operations to yield a pre-chosen result. 

## Possible Relaxations
1. Let the total number of playable numbers (**p**) be greater than 6 - *Corollary - at what number **p** is it always possible to hit the target*
  * There are obvious trivial solutions on an upper bound for **p** 
2. Restrictions on **t** in combination with other relaxations
3. Include ALL binary operations.
4. Include unary operations.
5. Relax the randomness. For any given **t** is it always possible to choose **p** numbers such that they combine using some set of arithmetic operations to equal **t**

## Places to Research
So far I've gone down a few rabbitholes looking for answers. They are listed here in no particular order and are here for my reference later. 
* Compiler parser trees for the actual program
* Advanced Algebra
* First and Second order Arithmetic
* Linear Combinations - this can be generalized as "under what conditions is there a linear combination that yields a given result."
* Can this be drawn as a graph and then it becomes a traversal problem. Does it even make sense to do it this way?
* Whats the time complexity of the problem?
* Combinatorics - how many ways are there to combine numbers using x number of operations. I started working this out and never finished. It's less trivial than I wanted it to be.
