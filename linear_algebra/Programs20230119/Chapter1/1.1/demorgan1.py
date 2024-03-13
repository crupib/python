for P in [False, True]:
    for Q in [False, True]:
        print(P, Q, not P, not Q, P and Q,
              not(P and Q), (not P) or (not Q))

'''
False False True True False True True
False True True False False True True
True False False True False True True
True True False False True False False
'''
