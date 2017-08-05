def kadane():
 max_sum_so_far=listing[0]
 max_here=0
 for i in range(0,len(listing)):
  max_here=max_here+listing[i]
  if(max(max_sum_so_far,max_here)==max_here):
   max_sum_so_far=max_here
  if(max_here<0):
   max_here=0
 return max_sum_so_far
global listing
listing=[]
listing=list(map(int, raw_input().split()))
result=kadane()
print(result)