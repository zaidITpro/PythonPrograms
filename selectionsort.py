def selection_sort(listing):
 for i in range(0,len(listing)-1):
  minimum=i
  for j in range(i+1,len(listing)):
   if(listing[minimum]>listing[j]):
    minimum=j
  temp=listing[i]
  listing[i]=listing[minimum]
  listing[minimum]=temp
 return listing
listing=[]
print("\nEnter the elements: \n")
listing=list(map(int, raw_input().split()))
listing=selection_sort(listing)
print("\nElements after sorting: \n")
for i in range(0,len(listing)):
 print listing[i],