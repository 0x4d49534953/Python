class Node(object):
    def __init__(self,value=None,next_node=None):
        self.value=value
        self.next=next_node
    def __str__(self):
        return f"[Node with value {self.value}]"

def print_linked_list(head):
    cur=head
    while cur is not None:
        print (cur)
        cur = cur.next 

def sortList(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        swap = 0
        if head != None:
            while(1):

                swap = 0
                tmp = head
                while(tmp.next != None):
                    x=tmp.value
                    y=tmp.next.value
                    if type(x) is str:
                        x= ord(x[0])
                    if type(y) is str:
                        y=ord(y[0])

                    if x > y:
                        # swap them
                        swap += 1
                        p = tmp.value
                        tmp.value = tmp.next.value
                        tmp.next.value = p
                        tmp = tmp.next
                    else:
                        tmp = tmp.next

                if swap == 0:
                    break
                else:
                    continue



            return head
        else:
            return head

def reverse_linked_list(head):
    cur=head
    prev=None
    following=cur.next
    while cur is not None:
        cur.next = prev 
        prev= cur     
        cur = following     
        if following:               
            following = following.next
    return prev

             
h, a, b, c, d = Node(3), Node("Внезапно"), Node(2), Node(6), Node(5)

h.next = a
a.next = b
b.next = c
c.next = d

print_linked_list(h)

print("---")
h=reverse_linked_list(h)
print_linked_list(h)
print("---")
h= sortList(h)
print_linked_list(h)