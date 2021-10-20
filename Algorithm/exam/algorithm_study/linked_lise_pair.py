class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs_repeat(self, head: ListNode) -> ListNode:
        root = prev = ListNode()
        prev.next = head

        # prev - head - tail - tail.next => prev - tail - head - tail.next
        while head and head.next:
            # tail이 head를 가리키도록 할당
            tail = head.next
            head.next = tail.next
            tail.next = head

            # prev가 tail을 가리키도록 할당
            prev.next = tail

            # 다음번 비교를 위해 이동
            head = head.next  # 원래 tail.next로 이동
            prev = prev.next.next  # prev.next는 tail, prev.next.next는 head. 즉, head.next의 이전 노드로 이동

        return root.next


# s1 = Solution()
# result = s1.swapParis([1, 2, 3, 4])
# print(result)
