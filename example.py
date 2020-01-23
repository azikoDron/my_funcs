def func1(y):  # need input("y")
    if y == "y":
        for a in "sto":
            for a1 in "sto":
                for a2 in "sto":
                    x = a + a1 + a2
                    if a != "s":  # если первая буква не S
                        if a2 != "s":  # если 3 - буква не S
                            if a1 == "s":  # если вторая = S
                                print(x)
def func2(b, b1, b2):
    x = b, b1, b2
    for k in x:
        for k1 in x:
            for k2 in x:
                x1 = k + k1 + k2
                print(x1)
def func3(v, v1, v2, v3):
    p = v, v1, v2, v3
    for e in p:
        for e1 in p:
            for e2 in p:
                for e3 in p:
                    ce = e + e1 + e2 + e3
                    print(ce)
te = input('how many letters 3 or 4 ? ')
if te == '3':
    func2(input('write a first letter: '), input('write  second letter: '), input('write third letter: '))
if te == '4':
    func3(input('write a first letter: '), input('write  second letter: '), input('write third letter: '),
          input('write four: '))

# g=(input(),input(),input())
# if x >= 'a' and x <= 'z':
# if x >='A' and x <= 'Z':
