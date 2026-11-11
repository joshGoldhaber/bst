'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the functions in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    The AVLTree is a subclass of BST.
    '''

    def __init__(self, xs=None):
        super().__init__(xs)

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes have a balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        if node is None:
            return True
        balance = AVLTree._balance_factor(node)
        if balance < -1 or balance > 1:
            return False
        if not AVLTree._is_avl_satisfied(node.left):
            return False
        if not AVLTree._is_avl_satisfied(node.right):
            return False
        return True

    @staticmethod
    def _left_rotate(node):
        if node is None or node.right is None:
            return node
        old_right = node.right
        new_left = Node(node.value)
        new_left.left = node.left
        new_left.right = old_right.left
        new_root = Node(old_right.value)
        new_root.left = new_left
        new_root.right = old_right.right
        return new_root

    @staticmethod
    def _right_rotate(node):
        if node is None or node.left is None:
            return node
        old_left = node.left
        new_right = Node(node.value)
        new_right.right = node.right
        new_right.left = old_left.right
        new_root = Node(old_left.value)
        new_root.right = new_right
        new_root.left = old_left.left
        return new_root

    def insert(self, value):
        self.root = AVLTree._insert(value, self.root)

    @staticmethod
    def _insert(value, node):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = AVLTree._insert(value, node.left)
        elif value > node.value:
            node.right = AVLTree._insert(value, node.right)
        return AVLTree._rebalance(node)

    @staticmethod
    def _rebalance(node):
        balance = AVLTree._balance_factor(node)
        if balance > 1:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._left_rotate(node.left)
            return AVLTree._right_rotate(node)
        if balance < -1:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
            return AVLTree._left_rotate(node)
        return node
