varList = [2, 4, 1, 88,9]
leftPointer = varList[0]

for i in range(1, len(varList)) :
  rightPointer = varList[i]
  if rightPointer > leftPointer :
    leftPointer = rightPointer

print(f"Angka Terbesar dalam array tersebut : {leftPointer}")
