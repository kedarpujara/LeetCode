def delete(head, data):
	if not head:
		return 
	if not head.next: 
		head = None
		return 
	if head.val == data:
		#deleteHead
	while head.next != head:
		if head.next.val == data:
			head.next = head.next.next 
			break
		head = head.next
	if deleteHead:
		head.next = head.next.next
		head = head.next