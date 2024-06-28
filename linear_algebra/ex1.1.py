#for P in [True, False]:
#   for Q in [True, False]:
#      print (P <= Q, not (P or Q))
for P in [True, False]:
   for Q in [True, False]:
      print (P == Q, ((P <= Q) and (Q <= P)))
