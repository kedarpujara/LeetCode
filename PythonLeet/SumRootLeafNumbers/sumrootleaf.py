class Solution:
    total_sum = 0
    def sum_left(self, root):
        total_sum = 0
        return self.dfs(root, 0)
    

    def dfs(self, curr_node, curr_sum):
        if not curr_node:
            return 
        curr_sum = curr_sum*10 + root.val

        if not curr_node.left and not curr_node.right:
            return curr_sum = curr_sum*10 + curr_node.val
        else:
            return self.dfs(curr_node.left, curr_sum) + self.dfs(curr_node.right, curr_sum)


        self.dfs(curr_node.left, curr_sum)
        self.dfs(curr_node.right, curr_sum)