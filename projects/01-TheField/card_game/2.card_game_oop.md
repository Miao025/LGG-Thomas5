# Challenge: OOP in python with a card game

- Repository: `challenge-card-game-becode`
- Type of Challenge: `Consolidation`
- Duration: `2 days`
- Deadline: `dd/mm/yy H:i AM/PM`
- Team challenge : `solo`

## Mission objectives

Create a card game in python.

![Card game!](https://media.giphy.com/media/3o7TKP35NXE4rWwXjW/giphy.gif)

## Learning Objectives

- Make a good usage of classes.
- Use Object-Oriented-Programming (OOP).
- Use imports in a clean way.
- Use a clean architecture.
- Structure a project.
- Go deeper in object inheritance.

## The Mission

You apply for a job as a developer for an online casino called `WeTakeYourMoney`.

They are interested in your profile.
During the interview challenge, they ask you to build a card game in Python.

### Must-have features

We want you to build a basis for a card game. There is not an actual game being played in the must-have version. There are no points that get counted.
What we want is just that a deck of cards gets created, and split between the different players and each player plays a card at every turn, until there are no cards left.

- The game is working until each player doesn't have any cards left.
- The game generates all the cards.
- The game distributes all the cards.

### Nice-to-have features

Once you have the basis of a card game, you can go ahead and make a real card game from it.

- Make the game interactive, at each turn, ask the player which card he/her wants to play.
- Create game-over conditions and add the possibility in the game to end because of the aforementioned conditions.
- Add points for each player if the card is the most `powerful` card played that turn.
- Select a winner out of the players at the end of the game.

### Constraints

#### Imports

```python
# You CAN'T import like this:
import whatever_file
# You CAN'T import like this:
import .whatever_file
# You CAN'T import like this:
from .whatever_file.whatever_function
# You CAN'T import like this:
from .whatever_function
# You CAN'T import like this:
from whatever_file
```

```python
# You CAN import like this:
from whatever_file import whatever_function_or_class
```

#### Code style

- Each **class** should have a [`__str__()` method](https://medium.com/swlh/understanding-repr-and-str-in-python-65dd41538943).
- Each **function or class** has to be **typed**
- Each **function or class** has to contain a **docstring** formatted like this:

```python
def add(number_one: int, number_two: int) -> int:
    """
    Function that will perform the add operation between two numbers (in params).

    :param number_one: An int that will be added to the second parameter.
    :param number_two: An int that will be added to the fist parameter.
    :return: An int that is the result of the two params being added to each other.
    """
    result = number_one + number_two
    return result
```

- Your code should be **formatted** with [black](https://pypi.org/project/black/).
- Your code should be **commented**.
- Your code should be **cleaned of any commented unused code**.

#### Repo

- Your repo should only contain the files specified.
- Your README should be nice and complete (see the #Deliverables section below). Feel free to add more information.

Please keep the must-have version separate from the nice-to-have version by using a different branch on GitHub. Please specify that in your README too.

### Steps

It goes without saying, but please, **read through all of this before starting.**

Make sure that you understand the concept of OOP, as this project will make intensive use of it.

_What is a card game ?_

For those that don't know, a deck of cards is composed of 52 cards. Each card has a symbol (one of `[♥, ♦, ♣, ♠]`) and a value, ranging from `['A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K']`.
If you do the math, 4 \* 13 = 52, so each card is unique in a deck of cards.

_How to program a python project ?_
Until now, you've mostly been working on `.ipynb` files, so called _Jupyter Notebooks_ or `IPython notebooks`.
For a project like this, notebooks are really not a good idea. You'll notice the `.py` file extension in the coming files. These are **python** source files.
Unlike notebooks, which get read using `jupyter` or `jupyter-lab`,
editing python source files is done in an [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment) or a text editor.

Here are a list of popular IDEs or text editors to choose from:

- [vscode](https://code.visualstudio.com/) (IDE/Text editor)
- [PyCharm](https://www.jetbrains.com/pycharm/) (IDE)
- [Atom](https://atom.io/) (Text editor)
- [Sublime Text](https://www.sublimetext.com/) (Text editor)
- [vim](https://www.vim.org/) (Text editor)

Now, let's get to the heart of it!
And I repeat, **read through all of this before starting.**

#### 0. preparation

Create a GitHub repo called `challenge-card-game-becode`. In this repository create 2 files:

- `README.md`
- `main.py`

And a folder:

- `utils`

In the `utils` folder create 3 files:

- `card.py`
- `player.py`
- `game.py`

You're ready to go!

#### 1. A simple card

##### 1.1 Symbol

In `card.py`:

Create a class called `Symbol` with two attributes:

- `color` which is a string.
- `icon` which is a single character out of this list `[♥, ♦, ♣, ♠]`.

##### 1.2 Card

In the same file, create a class `Card` that **inherits** from `Symbol` and add an attribute:

- `value` which is a string (one of `['A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K']`)

#### 2. A bunch of players

In `player.py` create a class `Player` that contains these attributes:

- `cards` which is a list of `Card`. _(you will need to import `Card` from `card.py`)_. In a real card game, this is equivalent to the cards that the player has in his hands.
- `turn_count` which is an int starting a 0.
- `number_of_cards` which is an int starting at 0.
- `history` which is a list of `Card` that will contain all the cards played by the player.

And some methods:

- `play()` that will:
  - **randomly** pick a `Card` in `cards`.
  - Add the `Card` to the `Player`'s `history`.
  - Print: `{PLAYER_NAME} {TURN_COUNT} played: {CARD_NUMBER} {CARD_SYMBOL_ICON}`.
  - Return the `Card`.

#### 3. A complete deck

Create a `Deck` class that contains:

- An attribute `cards` which is going to contain a list of instances of `Card`.
- A `fill_deck()` method that will fill `cards` with a complete card game _(an instance of 'A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K' for each possible symbol [♥, ♦, ♣, ♠])_. Your deck should contain **52 cards at the end**.
- A `shuffle()` method that will shuffle all the list of `cards`.
- A `distribute()` that will take a list of `Player` as parameter and will distribute the cards evenly between all the players.

#### 4. A board

In `game.py` create:

A class called `Board` that contains:

- An attribute `players` that is a list of `Player`. It will contain all the players that are playing.
- An attribute `turn_count` that is an int.
- An attribute `active_cards` that will contain the last card played by each player.
- An attribute `history_cards` that will contain all the cards played since the start of the game, except for `active_cards`.
- A method `start_game()` that will:
  - Start the game,
  - Fill a `Deck`,
  - Distribute the cards of the `Deck` to the players.
  - Make each `Player` `play()` a `Card`, where each player should only play 1 card per turn, and all players have to play at each turn until they have no cards left.
  - At the end of each turn, print:
    - The turn count.
    - The list of active cards.
    - The number of cards in the `history_cards`.

#### 5. Let's play

In `main.py`:

- Import everything you need to start the game!
- Start the game. You should only run this file to have the game running.

## Deliverables

1. Publish your source code on the GitHub repository.
2. Pimp up the README file:
   - Description
   - Installation
   - Usage
   - (Visuals)
   - (Contributors)
   - (Timeline)
   - (Personal situation)

## Evaluation criteria

| Criteria       | Indicator                                                    | Yes/No |
| -------------- | ------------------------------------------------------------ | ------ |
| 1. Is complete | The student has realized all must-have features.             |        |
|                | There is a published GitHub repo available.                  |        |
|                | The game runs until the end without any error.               |        |
|                | The game starts by running `python main.py` in the terminal. |        |
| 2. Is correct  | The code is well typed.                                      |        |
|                | There is a docstring for every function/method/class.        |        |
|                | All the constraints are respected.                           |        |
| 3. Is great    | There is an interaction with the user.                       |        |
|                | The game is playable with multiple users.                    |        |

## Final note

![You've got this!](https://media.giphy.com/media/BcCoMy2A0eYELrRZ6O/giphy.gif)
