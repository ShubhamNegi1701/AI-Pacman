# AI-Pacman
In this project, Pacman agent will find paths through his maze world, both to reach a particular location and to collect food efficiently. Try to build general search algorithms and apply them to Pacman scenarios.
![687474703a2f2f61692e6265726b656c65792e6564752f696d616765732f7061636d616e5f67616d652e676966](https://user-images.githubusercontent.com/56329050/74513220-f175bf80-4ebe-11ea-8415-ba19273b4c48.gif)


Start a game by the command:
```
python pacman.py
```
You can see the list of all options and their default values via:
```
python pacman.py -h
```
HW1 Search
DFS, BFS, UCS, ASTAR, ASTAR heuristic
```
 python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=dfs
 python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
 python pacman.py -l bigMaze -p SearchAgent -a fn=ucs
 python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```
Corner problem, Corner heuristic
```
 python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
 python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
```
