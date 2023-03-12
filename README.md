# Sudoku solver

This Sudoku solver is implemented using backtracking. This project has helped me learn about graph traversal algorithms, writing tests and a database-server-client interface.

Backtracking is very performant and the code is able to solve the hardest of Sudoku puzzles in a few milliseconds.

```
python3 unittests.py # Run unit tests. It will output any errors.
python3 server.py # The server depends on Flask, and uses backtrack.py as the solver engine.
```
