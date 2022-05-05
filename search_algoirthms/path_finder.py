"""Module to find paths in a Maze."""
from __future__ import annotations

from .maze import Maze
from .node import Node


class PathFinder:
    """Find the path from start to goal using A* search."""

    MAX_ITERATIONS = 100000

    def __init__(self, maze: Maze) -> PathFinder:
        """
        # Find the path from start to goal using A* search.

        Args:
            maze: Maze
                The maze to search.
        """
        self.maze = maze

    def create_path_from_node(self, node) -> list[tuple[int, int]]:
        """
        Create a path from the last node by following the parents.

        Args:
            node: Node
                The last node in the path.

        Returns: list[tuple[int, int]]
            The path from start to goal.
        """
        path = []

        while node:
            path.append(node.position)
            node = node.parent

        # Python list magic to reverse the list
        path = path[::-1]
        return path

    def _print_step(self, iteration: int, current_node: Node) -> None:
        """
        Print out the current step of the search.

        Args:
            iteration: int
                The current iteration of the search.

            current_node: Node
                The current node to print.

        Returns: None
        """
        print("---")
        print("Iteration #", iteration)
        _path = self.create_path_from_node(current_node)
        self.maze.print_maze(
            path=_path,
            to_visit_nodes=self.to_visit,
            visited_nodes=self.visited,
        )

    def a_star_search(self, show_steps: bool = False) -> list[tuple[int, int]]:
        """
        # Find the path from start to goal using A* search.

        Args:
            show_steps: bool
                Whether to print out each step of
                the search to the console or not.

        Returns: list[tuple[int, int]]
            The path from start to goal.
        """
        print("# Searching best path using A* ...")
        # Setup start and initialize
        start_node = Node(
            position=self.maze.start_position,
            parent=None,
        )
        end_node = Node(
            position=self.maze.goal_position,
            parent=None,
        )

        self.to_visit = []
        self.visited = []

        self.to_visit.append(start_node)

        # Track iterations to avoid infinite looping.
        iteration = 1

        # While there are still nodes to visit.
        while len(self.to_visit) > 0:

            current_node = self.to_visit[0]
            current_index = 0

            if show_steps:
                self._print_step(
                    iteration=iteration,
                    current_node=current_node,
                )

            # Iterate nodes to identify cost.
            for i in range(len(self.to_visit)):
                node = self.to_visit[i]
                if node.cost < current_node.cost:
                    current_node = node
                    current_index = i

            iteration += 1
            if iteration > self.MAX_ITERATIONS:
                print(" * Too many iterations...")
                # Too many iterations, return partial path.
                return self.create_path_from_node(current_node)

            # Remove the current node from the to visit list
            # and add it to the visited list.
            self.to_visit.pop(current_index)
            self.visited.append(current_node)

            # Check if the goal has been found.
            if current_node == end_node:
                print(
                    f" * Completed after {iteration} steps. "
                    f" * Costed {current_node.cost}"
                )
                return self.create_path_from_node(current_node)

            # Find valid children of the current node.
            self._get_children(current_node=current_node)

    def _get_children(self, current_node: Node):
        """
        Find the children of the current node.

        Check all allowed moves on a current node
        to see if they are valid. If valid, append
        the child to the to_visit list.

        Args:
            current_node: Node
                The current node to check.

        Returns: None
        """
        for move in self.maze.MOVES:
            child = self._get_child(
                current_node=current_node,
                move=move,
            )
            if child:
                self.to_visit.append(child)

    def _get_child(self, current_node: Node, move: tuple[int, int]) -> Node | None:
        """
        Calculate the next node to search.

        Args:
            current_node: Node
                The current node to search from.

            move: tuple[int, int]
                The move to make from the current node
                to see if it is a valid move.

        Returns: Node | None
            The next node to search from the current node
            or None if the move is not valid.
        """
        # Calculate new position from the current move.
        next_pos = (
            current_node.position[0] + move[0],
            current_node.position[1] + move[1],
        )
        # Get the cost of the move.
        cost = self.maze.get_cost_at_position(next_pos)

        # Check if the next node is not a wall.
        if cost >= self.maze.TOO_EXPENSIVE_COST:
            return

        # Create the new child node.
        child = Node(current_node, next_pos)
        # Calculate the accumulated cost.
        child.cost = cost + current_node.cost

        check_cost = [i for i in self.to_visit if i == child and child.cost >= i.cost]
        # If the child node is due to be visited, and the total cost is not lower.
        if len(check_cost) > 0:
            return

        return child
