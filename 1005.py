T = int(input())
for t in range(T):
   X = []
   Y = []
   N, K = input().split()
   N, K = int(N), int(K)
   D = input().split()
   for i, d in enumerate(D):
       D[i] = int(d)

   for k in range(K):
       tmp = input().split()
       X.append(int(tmp[0]))
       Y.append(int(tmp[1]))

   W = int(input())-1

   result = [[0]*len(Y) for i in range(len(X))]