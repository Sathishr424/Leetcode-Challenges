class Solution:
    def canVisitAllRooms(self, rooms):
        if len(rooms)==1: return True
        keys = rooms[0]
        visited = [False]*len(rooms)
        visited[0] = True
        for i in range(1,len(rooms)):
            if i in keys:
                keys += rooms[i]
                visited[i] = True
        if visited.count(True) == len(rooms): return True
        previous = len(keys)
        while True:
            for i in range(1,len(rooms)):
                if i in keys and not visited[i]:
                    keys += rooms[i]
                    visited[i] = True
            if visited.count(True) == len(rooms): return True
            if len(keys) == previous:
                break
            else: previous = len(keys)
        return visited.count(True) == len(rooms)

print(Solution().canVisitAllRooms([[7,16,8,16,19,8],[10],[9,11],[3,14,16,19],[8,10,19,1,7],[13,5,10,15,4],[6,13],[14,14,11,12,18],[3],[17,9],[1,2,6,9,6],[12,12,2],[4,4],[2,13,17],[17],[],[11,15],[3,5],[15,18,5],[7,18,1]]))
print(Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))