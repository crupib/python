from pprint import pprint
x = [
  {'apple': [1,2,3], 'orange':[4,5,6]},
  {'pear': [7,8,9], 'pineapple':[10,11,12]},
  {'durian':[13,14,15], 'banana':[16,17,18]}
]
print("Old print")
print(x)
print('\n')
print('\n')
print("pprint")
print('\n')
print('\n')
pprint(x, indent=4, width=30)
y = {
  'name':'tom',
  'dad': {'name': 'jerry',
          'dad':{'name':'greg'},
          'mom':{'name':'susie'}
          },
  'mom': {'name': 'mary'},
  'wife': {'name': 'susan'},
  'son': {'name': 'tim',
          'dad':{'name':'tom'},
          'mom':{'name':'susan'},
          'wife':{'name':'cassie'},
          'daughter': {'name':'lala',
                        'husband': 'bobo'
                        }
          }
}

print("Old print")
print('\n')
print('\n')
print(y)
print("pprint")
print('\n')
print('\n')
pprint(y, indent=4, width=30)
