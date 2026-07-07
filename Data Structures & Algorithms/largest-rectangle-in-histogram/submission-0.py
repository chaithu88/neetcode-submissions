class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        stack1=[]
        stack2=[]
        psc=[0]*n
        nsc=[0]*n
        area=0
        max_area=0
        for i in range(n-1,-1,-1):
            while stack1 and heights[i]<=heights[stack1[-1]]:
                stack1.pop()
            if stack1:
                nsc[i]=stack1[-1]
            else:
                nsc[i]=n
            stack1.append(i)
        for i in range(n):
            while stack2 and heights[i]<=heights[stack2[-1]]:
                stack2.pop()
            if stack2:
                psc[i]=stack2[-1]
            else:
                psc[i]=-1
            stack2.append(i)
        for  i in range(n):
            area=heights[i]*(nsc[i]-psc[i]-1)
            max_area=max(max_area,area)
        return max_area


