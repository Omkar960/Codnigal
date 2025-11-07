class pairelements():
    def sum(self,nums,target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return(lookup[target-num],i)
            lookup[num] = i
value = int(input("Enter the number you want the sum of: "))
print(pairelements().sum((10,20,30,40,50,60,70),value))
        
