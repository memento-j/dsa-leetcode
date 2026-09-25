# 1448. Count Good Nodes in Binary Tree

# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(root: TreeNode) -> int:
    return



####
#### TEST CASES
####
if __name__ == "__main__":
    # Example 1
    #       3
    #      / \
    #     1   4
    #    /   / \
    #   3   1   5
    #
    # Expected: 4

    root1 = TreeNode(
        3,
        TreeNode(
            1,
            TreeNode(3)
        ),
        TreeNode(
            4,
            TreeNode(1),
            TreeNode(5)
        )
    )

    print(goodNodes(root1))  # 4


    # Example 2
    #       3
    #      /
    #     3
    #    /
    #   4
    #  /
    # 2
    #
    # Good nodes: 3,3,4
    # Expected: 3

    root2 = TreeNode(
        3,
        TreeNode(
            3,
            TreeNode(
                4,
                TreeNode(2)
            )
        )
    )

    print(goodNodes(root2))  # 3


    # Example 3
    #       1
    #      / \
    #     2   3
    #
    # Every node is good
    # Expected: 3

    root3 = TreeNode(
        1,
        TreeNode(2),
        TreeNode(3)
    )

    print(goodNodes(root3))  # 3


    # Example 4
    #       5
    #      / \
    #     4   3
    #    /     \
    #   2       1
    #
    # Only root is good
    # Expected: 1

    root4 = TreeNode(
        5,
        TreeNode(
            4,
            TreeNode(2)
        ),
        TreeNode(
            3,
            None,
            TreeNode(1)
        )
    )

    print(goodNodes(root4))  # 1