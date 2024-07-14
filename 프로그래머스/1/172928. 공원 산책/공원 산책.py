dog = None
obstacle = []

# 지나갈 때 장애물이 있다면 True 리턴
def is_장애물(way, distance):
    for i in range(1, distance + 1):
        장애물여부 = False
        if way == 'E':
            if [dog[0], dog[1] + i] in obstacle:
                장애물여부 = True
        elif way == 'W':
            if [dog[0], dog[1] - i] in obstacle:
                장애물여부 = True
        elif way == 'N':
            if [dog[0] - i, dog[1]] in obstacle:
                장애물여부 = True
        elif way == 'S':
            if [dog[0] + i, dog[1]] in obstacle:
                장애물여부 = True

        if 장애물여부:
            return True

# 공원밖이라면 True 리턴
def is_공원밖(way, distance, park_width, park_height):
    if way == 'E':
        if dog[1] + distance >= park_width:
            return True
        else:
            return False
            # dog[1] += distance
    elif way == 'W':
        if dog[1] - distance < 0:
            return True
        else:
            return False
            # dog[1] -= distance
    elif way == 'N':
        if dog[0] - distance < 0:
            return True
        else:
            return False
            # dog[0] -= 1
    elif way == 'S':
        if dog[0] + distance >= park_height:
            return True
        else:
            return False
            # dog[0] += 1
    return False

def move(way, distance, park_width, park_height):
    # 공원밖이거나 장애물이 있다면 pass
    if is_공원밖(way, distance, park_width, park_height) or is_장애물(way, distance):
        pass
    else:
        # 여기에 작성
        if way == 'E':
            dog[1] += distance
        elif way == 'W':
            dog[1] -= distance
        elif way == 'N':
            dog[0] -= distance
        elif way == 'S':
            dog[0] += distance
    
def whereIsDogObstacle(park):
    global dog
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S":
                dog = [i, j]
            if park[i][j] == "X":
                obstacle.append([i, j])

def solution(park, routes):
    answer = []
    whereIsDogObstacle(park)
    park_width = len(park[0])
    park_height = len(park)
    for route in routes:
        way, distance = route.split(" ")
        move(way, int(distance), park_width, park_height)

    answer = [dog[0], dog[1]]
    return answer