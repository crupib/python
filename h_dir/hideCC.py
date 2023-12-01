def maskify(cc):
    if len(cc) < 4:
        return cc
    return "*" * (len(cc)-4) + cc[-4:]

cc = input("enter cc ")
ccmask = maskify(cc)
print(ccmask)
