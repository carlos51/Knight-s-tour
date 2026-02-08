## Knight’s Tour Visualization (Heuristic-Based)

This project is a visual simulation of the **Knight’s Tour problem** implemented in Python using Pygame.  
It computes and animates a complete knight’s tour on an `n × n` chessboard starting from an arbitrary position.

The solution is generated using a **custom heuristic-based algorithm inspired by Warnsdorff’s rule**, combined with additional tie-breaking strategies to improve reliability and avoid dead ends.

### How it works
- Each board cell keeps track of the number of available knight moves (degree).
- At each step, the knight moves to the unvisited square with the **lowest number of onward moves**.
- When multiple candidates exist, additional heuristics are applied:
  - Minimum Manhattan distance to corners
  - Minimum distance to the board edges
- The board state is dynamically updated as moves are made.

### Features
- Dynamic generation of an `n × n` chessboard
- Full knight’s tour covering all squares exactly once
- Heuristic-based move selection (no brute force or backtracking)
- Smooth animation using linear interpolation between squares
- Visual trail of the knight’s path
- Adjustable board size and starting position

This project focuses on algorithmic thinking, heuristics, and visualization rather than brute-force search, providing an intuitive way to explore the Knight’s Tour problem.
