from collections import defaultdict
class IdentityResolutionApi:
    def __init__ (self):
        print("hello")

    def addLink(self, id1, id2):
        self.graph = defaultdict(list)
        #If the two nodes are already linked, return 
        if self.isLinked(id1, id2):
            return
        
        #If there is no current entry for identifier, create the entry 
        if id1 not in self.graph:
            self.graph[id1] = []
        if id2 not in self.graph:
            self.graph[id2] = []
  
        #Get the current links for the given identifiers 
        curr_links1 = self.graph[id1]
        curr_links2 = self.graph[id2]
        
        #Add the identifier to the list of the nodes it is linked to 
        curr_links1.append(id1)
        curr_links2.append(id2)
        
        print("here")
        print(self.graph)
        print(curr_links1)
        print(curr_links2)
        
        #Add the links from the other 
        for i in range(len(curr_links1)):
            for j in range(len(curr_links2)):
                self.graph[curr_links1[i]].append(curr_links2[j])            
        for i in range(len(curr_links2)):
            for j in range(len(curr_links1)):
                self.graph[curr_links2[i]].append(curr_links1[j]) 
        return 0
    """
    1. Check if both elements are in the graph 
    2. If they are, go through the links of the first identifier 
        -> If id2 is in there, then a link exists (TRUE)
        -> Otherwise, there is no link (FALSE)
    """
    def isLinked(self, id1, id2):
        if id1 == id2:
            return True 
        if id1 not in self.graph or id2 not in self.graph:
            return False 

        links = self.graph[id1]
        for link in links:
            if link == id2:
                return True 
        return False 

def main():
    ires = IdentityResolutionApi()
    ires.addLink("a1", "a2")
    print(ires.isLinked("a1", "a2"))


main()