fr# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Q1
def calculate(min,max):
    res = 0
    for i in range(min,max+1):
        res+=i
    return res
print(calculate(1,3))
print(calculate(4,8))
        

# Q2
data = {"count":3, "employees":[{"name":"John","salary":30000},
                                {"name":"Bob","salary":60000},
                                {"name":"Jenny","salary":50000}]}
def avg(data):
    name_list=[]
    salary_list=[]
    for i in range(len(data["employees"])):
        name = data["employees"][i]["name"]
        salary = data["employees"][i]["salary"]
        name_list.append(name)
        salary_list.append(salary)
    return sum(salary_list)/len(name_list)

print(avg({"count":3, "employees":[{"name":"John","salary":30000},{"name":"Bob","salary":60000},{"name":"Jenny","salary":50000}]}))
    


# Q3
def maxProduct(nums):
    final_list = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!=j and j>i:
                final_list.append(nums[i]*nums[j])
    return max(final_list)
                
print(maxProduct([5, 20, 2, 6]))  
print(maxProduct([10, -20, 0, 3])) 

# Q3 alternative solutions
def maxProduct_alternative(nums):
    positive_list = []
    negative_list = []
    zero_list=[]
    final_list = []
    
    for num in nums:
        if num>0:
            positive_list.append(num)
        elif num<0:
            negative_list.append(num)
        else:
            zero_list.append(num)
            
    positive_list.sort()
    negative_list.sort()
    
    if len(positive_list)>=2:
        positive_res = positive_list[-1]*positive_list[-2]
        final_list.append(positive_res)
    
    if len(negative_list)>=2:
        negative_res = negative_list[0]*negative_list[1]
        final_list.append(negative_res)
        
    if len(zero_list)>0:
        zero_res = 0
        final_list.append(zero_res)

    if len(positive_list)>0 and len(negative_list)>0:
        odd_res = positive_list[0]*negative_list[-1]
        final_list.append(odd_res)
    
    return max(final_list)


        
    
#04
def twoSum(nums, target):
    #final_list = []
    for i in range(len(nums)):
        for j in range(0,len(nums)):
            if i!=j and j>i:
                res = nums[i]+nums[j]
                if res == target:
                    #final_list.append([i,j])
                    return [i,j]
    #return final_list.sum()

            
print(twoSum([2, 11, 7, 15], 9))



#05
def maxZeros(nums):
    count=0
    count_list=[]
    for num in nums:
        if num==0:
            count+=1
            count_list.append(count)
        elif num!=0 and count!=0:
            count=0
    if len(count_list)>0:
        return max(count_list)
    else:
        return 0

print(maxZeros([0,1,0,0]))
print(maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]))
print(maxZeros([1, 1, 1, 1, 1]))


