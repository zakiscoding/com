from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        indegree= [0]*numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course]+=1
        
        q=deque()
        for i in range(numCourses):
            if indegree[i] ==0:
                q.append(i)
        taken = 0
        while q:
            num=q.popleft()
            taken+=1
            for i in graph[num]:
                indegree[i]-=1

                if indegree[i]==0:
                    q.append(i)

        return numCourses==taken