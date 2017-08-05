def binary_search(element):
 beg=0
 end=len(listing)-1
 mid=(beg+end)//2
 while beg<=end:
  if listing[mid]==element:
   return mid
  else:
   if listing[mid]>element:
    end=mid-1
   else:
    beg=mid+1
   mid=(beg+end)//2
 return -1
global listing
listing=[]
print("\nEnter the elements: \n")
listing=list(map(int,raw_input().split()))
print("Enter the element you want to search: ");
element=int(input())
result=binary_search(element)
if result==-1:
 print("\nElement is not present in the array")
else:
 print('\nElement '+str(element)+' is present at index '+str(result))