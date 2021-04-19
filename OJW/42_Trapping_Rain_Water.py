class Solution:

    def trap(self, height: List[int]) -> int:

        if len(height) == 0:
            return 0

        answer = 0
        mid = height.index(max(height))
        left = 1
        right = len(height) - 2
        max_height = height[mid]

        left_max, right_max = height[0], height[-1]

        while left < mid:

            if height[left] < left_max:
                answer += left_max - height[left]
            else:
                left_max = height[left]

            left += 1

        while right > mid:

            if height[right] < right_max:
                answer += right_max - height[right]
            else:
                right_max = height[right]

            right -= 1

        return answer
