items , anna_not_eat = map(int , input().split())
bill = list(map(int , input().split()))
brian_charged = int(input())

del bill[anna_not_eat]

actual = sum(bill)/2

if brian_charged > actual:
    print(int(brian_charged - actual))
elif brian_charged == actual:
    print('Bon Appetit')
else:
    print(int(actual - brian_charged))
