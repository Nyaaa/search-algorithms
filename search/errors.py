class PathNotFound(Exception):
    """Raised when a path cannot be calculated."""


class VertexNotFound(PathNotFound):
    """Raised when a given vertex is not a part of a given graph."""
