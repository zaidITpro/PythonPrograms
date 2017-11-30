from collections import defaultdict

class graph:
	def __init__(self):
		self.graph=defaultdict(list)

	def addedge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def BFS(self,s):
		queue=[]
		visited=[False for i in range(len(self.graph))]
		queue.append(s)
		visited[s]=True
		while queue:
			source=queue.pop(0)
			print(source,end=' ')
			for i in self.graph[source]:
				if visited[i]==False:
					queue.append(i)
					visited[i]=True
g=graph()
g.addedge(0, 1)
g.addedge(0, 2)
g.addedge(1, 3)
g.addedge(2, 3)
g.addedge(3, 4)
g.addedge(4, 5)
print("\n\nThe BFS traversal of the above graph is:\n\n")
g.BFS(1)
print("\n\n")
