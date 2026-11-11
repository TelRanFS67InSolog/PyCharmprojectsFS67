n=int(input("enter the required number of balls: "))

balls = [10]*n

heavy_index = int(input("enter the number of heavy ball: "))
balls[heavy_index] = 11

def find_heavy_n(balls):
    """
    balls - список весов
    возвращает индекс тяжелого шарика
    """

    candidates = list(range(len(balls)))

    while len(candidates)>1:
        # if left two balls
        if len(candidates)==2:
            a,b=candidates
            return a if balls[a]>balls[b] else b

        # if left 3 balls
        if len(candidates) == 3:
            a,b,c=candidates

            if balls[a]>balls[b]:
                return a
            elif balls[b] > balls[a]:
                return b
            else:
                return c

        # divide on 3 parts
        third = len(candidates)//3

        if third == 0:
            third = 1
        group1 = candidates[:third]
        group2 = candidates[third:2 * third]
        group3 = candidates[2* third:]

        w1 = sum(balls[i] for i in group1)
        w2 = sum(balls[i] for i in group2)

        if w1 == w2:
            candidates = group3
        elif w1>w2:
            candidates = group1
        else:
            candidates = group2
    return candidates[0]

result = find_heavy_n(balls)

print("heavy ball is number:",result)









