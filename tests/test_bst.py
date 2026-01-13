import pytest
from src.binary_search_tree import BST


def test_insert_and_search():
    bst = BST()
    assert bst.insert(50)
    assert bst.insert(30)
    assert bst.insert(70)
    
    assert bst.search(50)
    assert bst.search(30)
    assert not bst.search(100)


def test_inorder_traversal():
    bst = BST()
    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        bst.insert(v)
    
    assert bst.inorder() == [20, 30, 40, 50, 60, 70, 80]
