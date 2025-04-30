import pulp

# Instantiate our problem class

model = pulp.LpProblem("Profit_maximising_problem", pulp.LpMaximize)

A = pulp.LpVariable('A', lowBound=0, cat='Integer')
B = pulp.LpVariable('B', lowBound=0, cat='Integer')
model += 5000 * A + 2500 * B, "Profit"

model += 3 * A + 2 * B <= 20 
model += 4 * A + 3 * B <= 30 
model += 4 * A + 3 * B <= 44

model.solve()
pulp.LpStatus[model.status]
print("\n")
print (A.varValue)
print (B.varValue)

print("\n")
print (pulp.value(model.objective))
 
