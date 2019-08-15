myList = [str(i) for i in range(1, 27)]
val = 1
n = int(input("Number of list elements: "))
print()
arr = [input("Enter list element %d: " % (i+1)) for i in range(n)]
print("\n"+str(arr))

for i in range(n-1):
    testList = []
    testList.extend(arr)
    if (testList[i]+testList[i+1]) in myList:
        testList[i:i+2] = ["".join(testList[i:i+2])]
        print(testList)
        val += 1
        for j in range(i+1, n-2):
            countPair = 1
            while countPair < n // 2:
                if j <= len(testList)-2:
                    if (testList[j]+testList[j+1]) in myList:
                        testList[j:j + 2] = ["".join(testList[j:j + 2])]
                        print(testList)
                        val += 1
                        countPair += 1
                    else:
                        break
                else:
                    break
print("\nTotal possibilities are:", val)
