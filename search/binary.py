from .errors import VertexNotFound


def search(data, value):
    """

    Args:
        data (): Sorted data
        value (): Value to look for

    Returns:
        value index

    Raises:
        VertexNotFound if nothing found
    """
    left = 0
    right = len(data) - 1

    while True:
        middle = (left + right) // 2

        if middle < left or middle > right:
            raise VertexNotFound

        if data[middle] < value:
            left = middle + 1
        elif data[middle] > value:
            right = middle - 1
        else:
            return middle
