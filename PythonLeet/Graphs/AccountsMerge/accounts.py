"""
Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, 
and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person 
if there is some email that is common to both accounts. Note that even if two accounts have the same name, 
they may belong to different people as people could have the same name. A person can have any number of accounts initially, 
but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. 
The accounts themselves can be returned in any order.
"""
from collections import defaultdict

class Solution(object):
    def 



    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        i = 0
        account_dict = defaultdict(list)
        for i in range(len(accounts)):
            name = True
            for email in accounts[i]:                
                if name == False:
                    account_dict[i][1].append(email)       
                if name:
                    name = False     
                    account_dict[i].append([email])
                    account_dict[i].append([])
        
        print(account_dict[0][0][0])
        print(account_dict[0][1])
        account_array = []

        for entry in account_dict:
            print(account_dict[entry])
            name = account_dict[entry][0][0]
            for email in account_dict[entry][1]:
                account_array.append((email, entry, name))
        
        # print(account_dict)
        # print("")
        # print(account_array)
        result = []
        prev = account_array[0][0]
        for i in range(1,len(account_array)):
            if account_array[i][0] == prev:
                #If they are different keys with the same email
                if account_array[i-1][1] != account_array[i][1]:
                    account_array[i][1] = account_array[i-1][1]
                    self.merge(account_array[i-1], account_array[i], account_dict, account_array)

    def change_all_tuple_keys(self, account_array, key, new_key):
        for account in account_array:
            if account_array[]

    def merge(self, tup1, tup2):
        for email in account_dict[tup2][1]:
            if email not in account_dict[tup1[1]][1]:
                account_dict[tup1[1]][1]append(email)
        
        account_dict[tup2][1] = []
        return account_dict


def main():
    s = Solution()
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], 
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
    s.accountsMerge(accounts)

main()
