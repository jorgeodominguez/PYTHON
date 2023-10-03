#Remover elementos de la lista
import os
os.system("cls")

nums=[1,3,5,7,9,11,99,15,88,19,100]

print(nums,len(nums))
nums.remove(99)
print(nums,len(nums))
nums.pop()#ultimo
print(nums,len(nums))
nums.clear()#limpiar todo
print(nums,len(nums))