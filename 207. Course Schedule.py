class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjacency_list = {

        }

        def dfs(node, adjacency_list,visited,start):

            if not node in adjacency_list:
                visited.add(node)
                return False

            visited.add(node)
            if start in adjacency_list[node]:
                return True

            returnVal = False
            for neighbour in adjacency_list[node]:
                if neighbour not in visited:
                    returnVal = returnVal or dfs(neighbour,adjacency_list,visited,start)
            return returnVal 


        for p in prerequisites:
            course = p[0]
            prereq = p[1]

            if not prereq in adjacency_list:
                adjacency_list[prereq] = [course]

            else:
                adjacency_list[prereq].append(course)

            
        for node in adjacency_list:
            if dfs(node,adjacency_list,set(),node):
                return False

        return True
