# (Simple) UML Diagram
::: mermaid
classDiagram
direction BT

class AlienInvasion

class Alien
Alien --* AlienInvasion

class Bullet
Bullet --* AlienInvasion

class PlayButton
PlayButton --* AlienInvasion

class Settings
Settings --* AlienInvasion

class Stats
Stats --* AlienInvasion

class ScoreBoard
ScoreBoard --* AlienInvasion

class Astronaut
Astronaut --* ScoreBoard

class Score
Score --* ScoreBoard

class ScoreBar
ScoreBar --* AlienInvasion

class ScoreBarRocket
ScoreBarRocket --|> Rocket
ScoreBarRocket --*  ScoreBar

class Rocket
Rocket --* AlienInvasion
:::