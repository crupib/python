#!/usr/local/bin/python3
from collections import deque
company_names = deque()

company_names.append('Tesla')
company_names.append('SpaceX')
print(company_names)

company_names.appendleft('DeepMind')
print(company_names)
company_names.pop()
print(company_names)
company_names.popleft()
print(company_names)
