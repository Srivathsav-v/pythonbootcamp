import math
from typing import List


class Search(object):
    def __init__(self, nums: List[int]):
        self.nums = nums
    def binary_search(self, target: int) -> str | bool:
        low = 0
        high = len(self.nums) - 1
        try:
            while low <= high:
                mid = math.floor((low + high) / 2)
                if target == self.nums[mid]:
                    return True
                elif target < self.nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            return False
        except TypeError:
            return(TypeError)
        except IndexError:
            return(IndexError)

    def quicksort(self, arr: List[int], low: int, high: int) -> None:
        pass

    def mergesort(self, arr: List[int], low: int, high: int) -> None:
        pass