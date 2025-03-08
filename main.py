amountOfCoefs = int(input("Amount of coefs. = "))

coefList = []

for i in range(1, amountOfCoefs + 1):
    if i == 1:
        coefList.append(int(input("Leading coef. = ")))
    elif i == amountOfCoefs:
        coefList.append(int(input("Free coef. = ")))
    else:
        coefList.append(int(input(f"Coef no. {i} = ")))

freeCoef = coefList[len(coefList) - 1]
leadCoef = coefList[0]

def findDivisors(n):
    divisors = [1]
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            divisors.append(i)
    if n != 1:
        divisors.append(n)
    return divisors

freeCoefDivList1 = findDivisors(freeCoef)
freeCoefDivList = []

for i in range(len(freeCoefDivList1)):
    freeCoefDivList.append(freeCoefDivList1[i])
    freeCoefDivList.append(freeCoefDivList1[i] * (-1))
del freeCoefDivList1

leadCoefDivList = findDivisors(leadCoef)
Roots = []

for i in freeCoefDivList:
    for j in leadCoefDivList:
        if j == 0:
            continue
        frctn = i / j
        if frctn == int(frctn):
            frctn = int(frctn)
        tempSum = 0
        for x in range(len(coefList)):
            tempSum += frctn ** (len(coefList) - 1 - x) * coefList[x]
        if tempSum == 0:
            Roots.append(frctn)
print("Real solutions: ", end="")
for i in Roots[:len(Roots) - 2]:
    print(i, end=", ")
print(Roots[len(Roots) - 1])
