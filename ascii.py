import sys
import getopt
import argparse


#stringValue = sys.argv[1]
#operator = sys.argv[1]
#inputEditValue = sys.argv[2]

parser = argparse.ArgumentParser(description='Argparse Tutorial')
parser.add_argument('text', help="put string want to convert")
parser.add_argument('op', help = "put operator")
parser.add_argument('num', type=int, help = "put int circulate")
parser.add_argument('--max',          required=False,type=int,   default=122)
parser.add_argument('--min',          required=False,type=int,   default=96)
args    = parser.parse_args()

stringValue = args.text
operator = args.op
inputEditValue = args.num
minAsciiNum = args.min 
maxAsciiNum = args.max

print("==================================================")

for i in range(len(stringValue)):
#or stringValue[i]=="\'"
#option filtering
  if(stringValue[i]==" " or stringValue[i]=="."  or stringValue[i]=="(" or stringValue[i]==")"):
    print(stringValue[i], end="")
    continue
#option cycle
  match operator:
    case '+':
      temp = ord(stringValue[i]) + inputEditValue
      if temp > maxAsciiNum:
        temp = temp - maxAsciiNum + minAsciiNum
      print(chr(temp), end="")
    case '-':
      temp = ord(stringValue[i]) - int(inputEditValue)
      if temp < minAsciiNum:
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