class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited = defaultdict(int)
        for index, num in enumerate(numbers):
            # print(visited)
            if visited[target-num] == 0:
                visited[num] = index+1
            else:
                # print('hello')
                # print(index)
                # print(visited[target-num])
                # return [1, 2]
                return sorted([index+1, visited[target-num]])