# Assignment 3.1 DASS 

## Clash of Clans

Running the Game:

```````````````````````
python3 game.py

````````````````````````
Running the Replay: It will ask an input 
Note: Input is a number of the Game that you played from begining

``````````````````````
python3 replay.py

````````````````````````
### Features:
   - health bar will be showed above the king, cannons and troops
   - you can play accordingly
   - Rage Spell:
        ○ The Rage spell affects every troop alive in the game and the King.
        ○ It doubles damage and movement speed.
   - Heal Spell:
        ○ The Heal spell affects every troop alive in the game and the King.
        ○ It increases their health to 150% of the current health (capped at the maximum health)
    - King Sword attack:
        will shoot at range of 5 titles if you press and hold x

### Controls:

<button>w</button> - Move King upside <br>
<button>s</button> - Move King down side  <br>
<button>d</button> - Move King  right side<br>
<button>a<button>  - Move King left Side <br>
<button>j<button>  - spawning point 1 <br>
<button>l<button>  - spawning point 2 <br>
<button>p<button>  - spawning point 3 <br>
<button>t<button>  - Heal spell  <br>
<button>r<button>  - range spell <br>
<button>q<button>  - Quit Middle <br>
<button>x<button>  - press and hold for King Sword attack<br>

Note that all these controls are case sensitive.

### OOPS Concepts:

The game is written in a modular fashion, allowing new features to be added with minimum modification. Writing duplicate code is avoided using the principles of inheritance and polymorphism as and when needed.

### Run Instructions:

* pip3 install numpy
* pip3 install colorama
* pip3 install playsound
* python3 game.py