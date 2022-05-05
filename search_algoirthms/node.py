"""Module containing Node object definition."""
from __future__ import annotations


class Node:
    """Represent a node of a Maze object."""

    def __init__(self, parent: Node | None, position: tuple[int, int]) -> Node:
        """
        # Nodes of a Maze object.

        Args:
            parent: Node
                The parent node of this node.

            position: tuple[int, int]
                The position of this node.
        """
        self.cost: float = 0
        self.parent: Node = parent
        self.position: tuple = position

    def __eq__(self, other: Node):
        """Python magic method to compare two nodes."""
        return self.position == other.position
