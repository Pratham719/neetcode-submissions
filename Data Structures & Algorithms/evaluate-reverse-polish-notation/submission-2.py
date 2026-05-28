class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for t in tokens:
            if t.isnumeric() or(t[0]=="-" and t[1:].isnumeric()):
                stack.append(int(t))
            else:
                if len(stack)>=2:
                    b=stack.pop()
                    a=stack.pop()
            
                if t=="+":
                    stack.append(a+b)
                elif t=="*":
                    stack.append(a*b)
                elif t=="/":
                    stack.append(int(a/b))
                elif t=="-":
                    stack.append(a-b)
        return stack[0]
            