# https://leetcode.com/problems/course-schedule/submissions/

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        p = defaultdict(list)
        for x, y in prerequisites:
            p[x].append(y)

        trees = set()
        checking = set()

        def check_tree(root):
            if root in trees:
                return True
            if root in checking:
                return False
            checking.add(root)
            for child in p[root]:
                if not check_tree(child):
                    return False
            trees.add(root)
            checking.remove(root)
            return True
        
        for node in range(numCourses):
            if not check_tree(node):
                return False
        return True