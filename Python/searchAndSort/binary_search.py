import math 


def binarysearch(nums,target):
    low=0
    high=len(nums)-1
    while(low<=high):
        mid=math.floor((low+high)/2)
        if target == nums[mid]:
            return(mid)
            
        elif target < nums[mid]:
            high=mid-1
        else:
            low=mid+1
    return(-1)
# result=binarysearch(low,high)

def main():
    nums=[1,2,3,4,5,6,7]
    target=int (input("enter the target value : "))
    result=binarysearch(nums,target)
    print(result)

if __name__ == "__main__":
    main()