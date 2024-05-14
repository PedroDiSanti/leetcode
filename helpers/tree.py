from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert_ordered(self, val: int) -> None:
        if val is None:
            pass

        if self.val is None:
            self.val = val
        elif val < self.val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.insert_ordered(val)
        elif val > self.val:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.insert_ordered(val)

    def insert_unordered(self, val: int) -> None:
        if self.val is None:
            self.val = val
        elif self.left is None:
            self.left = TreeNode(val)
        elif self.right is None:
            self.right = TreeNode(val)
        else:
            nodes = deque([self])
            while nodes:
                node = nodes.popleft()
                if node.left is None:
                    node.left = TreeNode(val)
                    break
                elif node.right is None:
                    node.right = TreeNode(val)
                    break
                else:
                    nodes.append(node.left)
                    nodes.append(node.right)

    def print_tree(self, prefix="", is_left=True):
        if self.right is not None:
            self.right.print_tree(prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(self.val))
        if self.left is not None:
            self.left.print_tree(prefix + ("    " if is_left else "│   "), True)
