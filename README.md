# Countdown
This project is based on the number game in the British television show [Countdown](https://en.wikipedia.org/wiki/Countdown_(game_show)). The game can be summarized as follows: 
<ul>
  <li> Player chooses **b** "big numbers" such that **b** is between 1 and 4</li>
  <li> **b** numbers are drawn from {25,50,75,100} with no duplicates. </li>
  <li> The difference of 6 and **b** = **l** where **l** is the number of "little numbers" drawn from [1...10] with no duplicates allowed. </li>
  <li> a random target **t** between 100 and 999 is choosen.</li>
  <li> The players use addition, multiplication, subtraction, and/or division in any order using the choosen numbers at most once to try to get as close to the target as possible.</li>
  <li> Whoever is closest wins</li>
</ul>

# Conjecture
It is not always possible to hit the target - provable by counterexample. However, I conject that there exists some relaxation of the rules under which it is always possible to combine a set of randomly chosen integers using some set of arithmetic operations to achieve a desired outcome. 

## Possible Relaxations
<ol>
  <li> Let the total number of playable numbers (**p**) be greater than 6 - *Corollary - at what number **p** is it always possible to hit the target* 
    <ul> 
      <li> There are obvious trivial solutions on an upper bound for **p** 
    </ul>
  </li>
  <li> Restrictions on **t** in combination with other relaxations </li>
  <li> Include ALL binary operations. </li>
  <li> Include unary operations. </li>
  <li> Relax the randomness. For any given **t** is it always possible to choose **p** numbers such that they combine using some set of arithmetic operations to equal **t** </li>
</ol>

## Places to Research
So far I've gone down a few rabbitholes looking for answers. They are listed here in no particular order and are here for my reference later. 
<ul>
  <li> Compiler parser trees for the actual program</li>
  <li> Advanced Algebra - really should've paid more attention in undergrad</li>
  <li> First and Second order Arithmetic</li>
  <li> Linear Combinations - this can be generalized as "under what conditions is there a linear combination that yields a given result."</li>
  <li> Can this be drawn as a graph and then it becomes a traversal problem. Does it even make sense to do it this way?</li>
  <li> Whats the time complexity of the problem? </li>
  <li> Combinatorics - how many ways are there to combine numbers using x number of operations. I started working this out and never finished. It's less trivial than I wanted it to be.</li>
</ul>
