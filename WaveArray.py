class Solution:
    def convertToWave(self, n, arr):
        for i in range(0, n-1, 2):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
