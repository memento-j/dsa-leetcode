# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    
    # 19. Remove Nth Node From End of List
    #Given the head of a linked list, remove the nth node from the end of the list and return its head.
    
    #Example 1:
    # Input: head = [1,2,3,4,5], n = 2
    # Output: [1,2,3,5]
    
    # Example 2:
    # Input: head = [1], n = 1
    # Output: []
    
    # Example 3:
    # Input: head = [1,2], n = 1
    # Output: [1]
    
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        Left = dummy
        Right = head

        while n > 0:
            Right = Right.next
            n -= 1
        
        while Right:
            Right = Right.next
            Left = Left.next

        Left.next = Left.next.next
        
        return dummy.next

    # time complexity: O(n)
    # space complexity: O(1)


def build_linked_list(values):
    dummy = ListNode()
    curr = dummy

    for val in values:
        curr.next = ListNode(val)
        curr = curr.next

    return dummy.next


def linked_list_to_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


# ---------- Test Cases ----------

if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([1, 2, 3, 4, 5], 2),    # remove 4
        ([1], 1),                # remove only node
        ([1, 2], 1),             # remove tail
    ]

    for values, n in tests:
        head = build_linked_list(values)

        print(f"Input: {values}, n={n}")

        result = solution.removeNthFromEnd(head, n)

        print("Output:", linked_list_to_list(result))
        print("-" * 40)
    
