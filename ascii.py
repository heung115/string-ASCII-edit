import sys
import getopt

#stringValue = sys.argv[1]
stringValue = input()
operator = sys.argv[1]
inputEditValue = sys.argv[2]
minAsciiNum = 96
maxAsciiNum = 122

print("==================================================")
for i in range(len(stringValue)):
  
#or stringValue[i]=="\'"
  if(stringValue[i]==" " or stringValue[i]=="."  or stringValue[i]=="(" or stringValue[i]==")"):
    print(stringValue[i], end="")
    continue

  match operator:
    case '+':
      temp = ord(stringValue[i]) + int(inputEditValue)
      if temp > maxAsciiNum:
        temp = temp - maxAsciiNum + minAsciiNum
      print(chr(temp), end="")
    case '+':
      temp = ord(stringValue[i]) - int(inputEditValue)
      if temp > maxAsciiNum:
        temp = temp - maxAsciiNum + minAsciiNum
      print(chr(temp), end="")
    case '*':
      temp = ord(stringValue[i]) * int(inputEditValue)
      if temp > maxAsciiNum:
        temp = temp - maxAsciiNum + minAsciiNum
      print(chr(temp), end="")
    case '%':
      temp = ord(stringValue[i]) % int(inputEditValue)
      if temp > maxAsciiNum:
        temp = temp - maxAsciiNum + minAsciiNum
      print(chr(temp), end="")
print()