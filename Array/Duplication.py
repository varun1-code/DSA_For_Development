"""Two Sum
Given an array of integers nums and an integer target,
return the indices of the two numbers such that they add up to target."""
class Solution: 
    def twosum(self,nums:list[int],target:int):
        seen={}
        result=[]
        for index,num in enumerate(nums):
            compliment=target-num
            if compliment in seen:
                result.append([seen[compliment], index])
                #return [seen[compliment],index]
                del seen[compliment] 
            else:
                seen[num] = index
        return result
if __name__=="__main__":
    solution=Solution()
    result=solution.twosum([1,2,3,4,5,6,7,8,9,1,7],8)
    print(result)