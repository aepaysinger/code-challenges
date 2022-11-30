from code_challenges.code_wars.sort_binary_tree import Node, sort_binary_tree


def test_sort_binary_tree_a():
    actual = sort_binary_tree(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1))
    expected =[1, 2, 3, 4, 5, 6]

    assert actual == expected, f"Returned {actual} instead of {expected}"