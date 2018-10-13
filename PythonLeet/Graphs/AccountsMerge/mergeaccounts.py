from collections import defaultdict
class Solution(object):
    def accountsMerge(self, accounts):
        self.graph = self.create_graph(accounts)
        visited = [False]*len(accounts)

        merged_accounts = []

        for i, account in enumerate(accounts):
            if visited[i] == False:
                name = [account[0]]
                name.extend(self.dfs(i,visited,accounts))
                merged_accounts.append(name)
        return merged_accounts          
        
    def dfs(self, i, visited, accounts):
        stack = [i]
        emails = set()
        while stack:
            index = stack.pop()
            emails.update(accounts[index][1:])
            for email in accounts[index][1:]:
                for neigh_index in self.graph[email]:
                    if visited[neigh_index]:
                        continue
                    stack.append(neigh_index)
        return sorted(emails)


    def create_graph(self,accounts):
        self.graph = defaultdict(list)        
        for i, account in enumerate(accounts):
            for email in account[1:]:
                self.graph[email].append(i)
        return self.graph
        
    # def dfs(self, )
def main():
    s = Solution()
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], 
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]    
    s.accountsMerge(accounts)
main()