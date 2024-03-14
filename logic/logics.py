import random as ran

enemies = [(5,5), (-10,17), (15,-3)]
def New_Soldier():
    
    min_x = min(enemies, lambda i: i[0])[0]
    min_y = min(enemies, lambda i: i[0])[1]
    max_x = max(enemies, lambda i: i[0])[0]
    max_y = max(enemies, lambda i: i[0])[1]
    

    new_sold = (minn(min_x, max_x), minn(min_y, max_y))
    for enemy in enemies:
        if new_sold[0] - 5 <= enemy[0] <= new_sold[0] + 5 and new_sold[1] - 5 <= enemy[1] <= new_sold[1] + 5:
            if new_sold[0] > 0:
            new_sold = (minn(min_x + 5, max_x), minn(min_y, max_y))




def minn(min_x, max_x, min_y, max_y):
    if (abs(min_x) > abs(max_x)):
        x = min_x
    else:
        x = max_x
    if (abs(min_y) > abs(max_y)):
        y = min_y
    else:
        y = max_y

    if (x > 0 and y > 0) or (x == 0 and max(min_y, max_y) > 0) or (y == 0 and max(min_x, max_x) > 0):
        chet = 1
    elif x < 0 and y > 0 or (x == 0 and max(min_y, max_y) > 0) or (y == 0 and max(min_x, max_x) > 0):
        chet = 2
    elif x < 0 and y < 0:
        chet = 3
    elif x > 0 and y < 0:
        chet = 4

    return {'x':x, 'y':y, 'chet':chet}
