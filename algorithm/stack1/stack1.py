# C style

def push(item):
    global top
    if top > 100 - 1:
        return
    else:
        top += 1
        stack[top] = item

def pop(): # isEmpty?
    global top
    if top == -1:
        print("Stack is empty!")
        return
    else:
        result = stack[top]
        top -= 1
        return result

stack = [0] * 100 # gloabl이 디폴트, 참조형(R, W)
top = -1 # global이 디폴트, 값형(R), 단 값형에 write를 하려면 매개변수로 넘기거나 global 설정을 해줘야함

push(1)
push(2)
push(3)
print(pop())
print(pop())
print(pop())



