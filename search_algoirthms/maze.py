"""Module to define and analyse a Maze."""
from __future__ import annotations

from math import sqrt


class Maze:
    """Class representing a Maze to search."""

    # Icons used to represent the maze.
    WALL = "⬜"
    EMPTY_SPACE = "  "
    AGENT = "🧍"
    GOAL = "🏁"
    # Icons used to represent the path and searched nodes.
    TRAVELLED = "✅"
    TO_VISIT = "❔"
    VISITED = "❌"

    # Store the maze map and heuristic cost of the map.
    maze_map = []
    heuristic_map = []

    start_position = (0, 0)
    goal_position = (0, 0)
    size = ()

    # Set the cost of walls or other impassable nodes
    # to this value so we can easily ignore them.
    TOO_EXPENSIVE_COST = 1000

    # Rules for moving in the map.
    MOVES = (
        (0, -1),  # Up
        (0, 1),  # Down
        (-1, 0),  # Left
        (1, 0),  # Right
    )

    def __init__(self, maze_map: list[list[int]] = None) -> Maze:
        """
        # Create a Maze.

        Args:
            maze_map: list[list[int]]
                A map of the maze.
        """
        self.maze_map = maze_map or []

        if len(self.maze_map) > 1 and len(self.maze_map[0]) > 1:
            self.size = (len(self.maze_map[0]), len(self.maze_map))
            self.pre_process()

        else:
            raise ValueError("Maze must be at least 2x2")

    def pre_process(self):
        """
        Process the maze to generate heuristics.

        This is done by calculating the distance
        from the goal for each position.
        """
        # Populate empty copy of maze map to store heuristic cost in.
        self.heuristic_map = [
            [0 for _ in range(self.size[0])] for _ in range(self.size[1])
        ]

        for y in range(0, self.size[1]):

            for x in range(0, self.size[0]):

                node = self.maze_map[y][x]

                cost = self.heuristic_map[y][x]

                # Set a wall
                if node == 1:
                    cost = self.TOO_EXPENSIVE_COST
                else:
                    # Calculate cost from goal to current node
                    distance_cost = sqrt(
                        (self.goal_position[0] - x) ** 2
                        + (self.goal_position[1] - y) ** 2
                    )
                    cost += distance_cost

                    # Set the starting position
                    if node == -1:
                        self.start_position = (x, y)
                    # Set the goal position
                    elif node == 9:
                        self.goal_position = (x, y)

                # Set the heuristic cost to the position
                self.heuristic_map[y][x] = cost

    def get_cost_at_position(self, position: tuple[int, int]):
        """
        Return the cost of a provided position.

        Args:
            position: tuple[int, int]
                The position to get the cost of.
        """
        return self.heuristic_map[position[1]][position[0]]

    def print_maze(
        self,
        path: list[tuple[int, int]] = None,
        step: int = 0,
        to_visit_nodes: list[tuple[int, int]] = None,
        visited_nodes: list[tuple[int, int]] = None,
    ) -> None:
        """
        Print the maze to the console.

        Args:
            path: list[tuple[int, int]]
                The path taken by the algorithm to
                be visualised.

            step: int
                Option to visualise the path up
                to a specific step.

            to_visit_nodes: list[tuple[int, int]]
                Nodes to be visualised as to_visit.

            visited_nodes: list[tuple[int, int]]
                Nodes to be visualised as visited.

        Returns: None
        """
        maze_map = self.maze_map.copy()

        if to_visit_nodes:
            for node in to_visit_nodes:
                maze_map[node.position[1]][node.position[0]] = "?"

        if visited_nodes:
            for node in visited_nodes:
                maze_map[node.position[1]][node.position[0]] = "x"

        # If there is a path to print, print it
        # Otherwise print the base maze
        if path:
            # If step is 0, visualise the whole path
            if step == 0:
                step = len(path)

            # Add the path to the maze
            for i in range(0, step):
                position = path[i]
                maze_map[position[1]][position[0]] = "."

            # Last position of the path is the agent
            position = path[step - 1]
            maze_map[position[1]][position[0]] = -1

        output_str = self._build_string(maze_map=maze_map)

        print(output_str)

    def _build_string(self, maze_map: list[list[int]]) -> str:
        """
        Build the output string for the maze.

        Args:
            maze_map: list[list[int]]
                The maze to be printed.

        Returns: str
            The string to be printed.
        """
        output_str = ""
        x, y = 0, 0
        for line in maze_map:
            for position in line:
                printable_char = self._get_printable_char(position=position)

                output_str += printable_char
                x += 1

            output_str += "\n"
            y += 1

        return output_str

    def _get_printable_char(self, position: int | str) -> str:
        """
        Return the printable character for a given position's value.

        Args:
            position: int | str
                The position in the maze map to get
                a character for. Must be either a -1,
                0, 1, or 9.

        Returns: str
            The printable character for the position.
        """
        # A wall
        if position == 1:
            printable_char = self.WALL
        # The start
        elif position == -1:
            printable_char = self.AGENT
        # The goal
        elif position == 9:
            printable_char = self.GOAL
        # Position travelled
        elif position == ".":
            printable_char = self.TRAVELLED
        # Position to search
        elif position == "?":
            printable_char = self.TO_VISIT
        # Position visited
        elif position == "x":
            printable_char = self.VISITED
        # Empty space
        else:
            printable_char = self.EMPTY_SPACE

        return printable_char
