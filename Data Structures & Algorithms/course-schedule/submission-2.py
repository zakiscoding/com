class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        prereq_count=[0]*numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            prereq_count[course]+=1
        
        q = deque()
        for course in range(numCourses):
            if prereq_count[course]==0:
                q.append(course)
        
        taken = 0
        while q:
            course = q.popleft()
            taken+=1
            for nxt in graph[course]:
                prereq_count[nxt]-=1
                if prereq_count[nxt]==0:
                    q.append(nxt)
        return numCourses == taken