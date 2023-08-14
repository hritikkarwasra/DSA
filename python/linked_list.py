# 1,6,2,0,0,1,3,5,6,5,4,2
#Create a linked list
#sort  the  linked list
#remove the duplicates present in the linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node= Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
def merge_sort_linked_list(head):
    if not head or not head.next:
        return head
    mid = find_middle(head)
    left = head 
    right = mid.next
    mid.next = None

    left_sorted = merge_sort_linked_list(left)
    right_sorted = merge_sort_linked_list(right)

    sorted_list = merge(left_sorted, right_sorted)

    return sorted_list


def find_middle(head):
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def merge(left, right):
    if not left:
        return right
    
    if not right:
        return left
    
    if left.data < right.data:
        left.next = merge(left.next, right)
        return left
    else:
        right.next = merge(left, right.next)
        return right 

def remove_duplicates(head):
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head


data = [1,6,2,0,0,1,3,5,6,5,4,2]
linked_list = LinkedList()
for i in data:
    linked_list.append(i)

print(linked_list.head.next.data)

# Sorted Linked List
linked_list.head = merge_sort_linked_list(linked_list.head)
head = linked_list.head
print('Sorted Linked List')
while head.next:
    print(head.data , "-->", end = "")
    head = head.next

# Removing duplicates
print("\n")
print('Removing Duplicates')
head = linked_list.head
head = remove_duplicates(head)
while head.next:
    print(head.data,  "-->", end = "")
    head = head.next


# Printed Results

# Sorted Linked List
# 0 -->0 -->1 -->1 -->2 -->2 -->3 -->4 -->5 -->5 -->6 -->

# Removing Duplicates
# 0 -->1 -->2 -->3 -->4 -->5 -->% 