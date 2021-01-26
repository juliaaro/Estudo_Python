x = int(input())
t = int(input())
v_1 = float(input())
v_2 = float(input())

t_1 = (x / v_1)
t_2 = (x / v_2) + t/60

if t_1 > t_2:
    print('False')
else:
    print('True')