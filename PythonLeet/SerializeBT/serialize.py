def serialize(self, root):
    if not root:
        return "#"
    return root.val + "," + self.serialize(root.left) + "," + self.serialize(root.right)

def deserialize(self, data):
    node_vals = data.split(",")
    self.deserialize_helper(node_vals, [0])

def deserialize_helper(self, node_vals, pos):
    if pos[i] == "#":
        pos[0] += 1
        return None 
    
    curr = TreeNode(int(node_vals[pos[0]]))
    pos[0] += 1

    curr.left = self.deserialize(node_vals, pos)
    curr.right = self.deserialize(node_vals, pos)

    return curr 