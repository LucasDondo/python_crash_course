# (Simple) UML Diagram
::: mermaid
classDiagram
direction BT

class TheBowMan

class PlayButton
PlayButton --* TheBowMan

class Arrow
Arrow --* TheBowMan

class Bow
Bow --* TheBowMan

class Target
Target --* TheBowMan

class Stats
Stats --* TheBowMan

class Line
Line --* Stats
:::