"""
Formatics path graph: Structural navigation graphs.

Implements graph-based path tracking and element relationships.
"""

from dataclasses import dataclass, field
from typing import Any, List, Optional, Set


@dataclass
class Node:
    """A node in the Formatics path graph."""

    value: Any
    edges: Set["Node"] = field(default_factory=set)

    def connect(self, other: "Node") -> None:
        """Create edge to another node."""
        self.edges.add(other)

    def disconnect(self, other: "Node") -> None:
        """Remove edge to another node."""
        self.edges.discard(other)

    def neighbors(self) -> List["Node"]:
        """Get all connected nodes."""
        return list(self.edges)

    def __hash__(self) -> int:
        return id(self)

    def __repr__(self) -> str:
        return f"Node({self.value}, edges={len(self.edges)})"


class PathGraph:
    """Graph structure for Formatics paths."""

    def __init__(self):
        """Initialize empty path graph."""
        self.nodes: List[Node] = []

    def add_node(self, value: Any) -> Node:
        """Add node to graph."""
        node = Node(value=value)
        self.nodes.append(node)
        return node

    def connect_nodes(self, source: Node, target: Node) -> None:
        """Create directed edge between nodes."""
        source.connect(target)

    def find_path(self, start: Node, end: Node) -> Optional[List[Node]]:
        """Find path between two nodes (BFS)."""
        if start == end:
            return [start]

        visited = set()
        queue = [(start, [start])]

        while queue:
            current, path = queue.pop(0)
            if current in visited:
                continue

            visited.add(current)

            for neighbor in current.neighbors():
                if neighbor == end:
                    return path + [neighbor]
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

        return None

    def __repr__(self) -> str:
        return f"PathGraph(nodes={len(self.nodes)})"
