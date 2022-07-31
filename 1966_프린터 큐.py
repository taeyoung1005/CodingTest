test_case = int(input())
for _ in range(test_case):
    count = 0
    N, M = map(int, input().split())
    severity_list = list(map(int, input().split()))
    
    severity_list_index = [0 for i in range(N)]
    severity_list_index[M] = "find"
    
    while True:
        if severity_list[0] == max(severity_list):
            count += 1
            if severity_list_index[0] != "find":
                del severity_list_index[0]
                del severity_list[0]
            else:
                print(count)
                break
                
        else:
            severity_list.append(severity_list.pop(0))
            severity_list_index.append(severity_list_index.pop(0))