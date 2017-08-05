def insertion_sort(listing):
 for i in range(1,len(listing)):
  key=listing[i]
  j=i-1
  while j>=0 and listing[j]>key:
   listing[j+1]=listing[j]
   j=j-1
  listing[j+1]=key
 return listing
print("Enter the elements of the list:\n\n")
listing=list(map(int, raw_input().split()))
listing=insertion_sort(listing)
print("\nThe list after sorting is:\n\n")
for i in range(0,len(listing)):
 print listing[i],