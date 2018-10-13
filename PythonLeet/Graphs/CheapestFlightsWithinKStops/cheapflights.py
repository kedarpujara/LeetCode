from collections import defaultdict
import heapq
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        self.graph = self.build_graph(flights)
        print(self.graph)

        pq = []
        
        heapq.heappush((src,0,))

        for val in self.graph[src]:
            heapq.heappush(pq, val)
        
        path = [src]
        depth = 0
        while pq:
            curr = heapq.heappop(pq)

            #print(pq)
            depth += 1
            for val in self.graph[curr]:
                heapq.heappush(pq, val)
            
            print(pq)




    def build_graph(self, flights):
        self.graph = defaultdict(list)
        for flight in flights:
            self.graph[flight[0]].append((flight[2], flight[1], 0))
        return self.graph


def main():
    s = Solution()
    n = 5
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    flights = [["A", "B", 300], ["A","C",200],["A","D",800],["B","D",400],["C","D",300],["D","E",100]]
    src = "A"
    dst = "F"
    k = 1
    s.findCheapestPrice(n,flights,src,dst,k)
main()