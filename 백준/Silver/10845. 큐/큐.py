import sys

q = []

N = int(sys.stdin.readline().strip())

def q_empty():
    return 1 if len(q) == 0 else 0

def q_size():
    return len(q)

def q_push(n):
    q.append(n)

def q_front():
    if q_empty():
        return -1
    else:
        return q[0]

def q_back():
    if q_empty():
        return -1
    else:
        return q[-1]

def q_pop():
    if q_empty():
        return -1
    else:
        return q.pop(0)

for _ in range(N):
    command = sys.stdin.readline().strip()
    if "push" in command:
        q_push(int(command.split()[1]))
    elif command == "front":
        print(q_front())
    elif command == "back":
        print(q_back())
    elif command == "size":
        print(q_size())
    elif command == "empty":
        print(q_empty())
    elif command == "pop":
        print(q_pop())