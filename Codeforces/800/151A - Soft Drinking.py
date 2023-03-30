# A group of 'n friends'

# Decided to buy 'k bottles'
# Each bottle has 'l milliliters'

# They bought 'c limes' 
# Cut each of them into 'd slices' 

# They found 'p grams of salt'

# Toast = Each friend needs nl milliliters of the drink, a slice of lime and np grams of salt.



if __name__ == "__main__":
    import math

    n, k, l, c, d, p, nl, np = map(int, input().split())

    bottleToast = (k*l)/nl
    limeToast = (c*d)
    saltToast = (p)/np

    print(math.floor(min(bottleToast, limeToast, saltToast)/n))

