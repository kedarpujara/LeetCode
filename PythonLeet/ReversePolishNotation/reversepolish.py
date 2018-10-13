def reverse(tokens):
    stack = []
    operators = ["*", "/", "+", "-"]
    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        elif token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            print(operand1)
            print(operand2)
            if token == "*":
                stack.append((operand1*operand2))
            elif token == "/":
                val = abs(operand1)/abs(operand2)
                if operand1 < 0 or operand2 < 0:
                    if operand1 < 0 and operand2 < 0:
                        continue
                    else:
                        val *= -1                                                
                stack.append(val)                
            elif token == "+":
                stack.append((operand1+operand2))
            elif token == "-":
                stack.append((operand1-operand2))
        print(stack)
    return stack.pop()

tokens = ["2", "1", "+", "3", "*"]
token2 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
token3 = ["4", "13", "5", "/", "+"]
token4 = ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]
print(reverse(token4))
#print(6/132)


nums = [2,5,3,2,7,1,4]
print(nums[0:1])