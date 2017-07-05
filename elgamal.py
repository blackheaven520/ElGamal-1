""" Author: Shamveel Ahammed
    El Gamal Public-key cryptosystems """

from random import randint


# part-1
# The algorithm is linear in the size of the input: O(n)

# Time Complexity
# Best Case: O(1) if y is divisible of x, then algorithm terminates in one call
# Worst Case: O(logn) when x,y are two Fibonacci numbers

def hcf(a, b):
    if b is 0:
        return a
    else:
        r = a % b
        return hcf(b, r)


# part - 2
# x -> g^x mod p

# The algorithm is linear in the size of the input-O(n)(running time)
# and the number of operations is proportional to the number of times d = x can be
# at most [log b]
# Best case = O(1)

def fme(g, x, p):
    d = g
    e = x
    s = 1
    while e != 0:
        if e % 2 == 1:
            s = (s * d) % p
        d = (d * d) % p
        e /= 2
    return s


# part - 3

# The algorithm will have a time complexity of - O(n^2) (running time)
# and a size complexity of O(log n)
# Best case - O(1)
# Worst Case - O(n^2) (exponential)
# y = g^x mod p


def dl(y, g, p):
    for x in range(p):
        if y == fme(g, x, p):
            return x


# part - 4

# The algorithm will have a time complexity of O(n) (running time)
# and a size complexity of O(n)
# Best case - O(1)
# Worst Case - O(n)


def imp(y, p):
    for x in range(p):
        if (y * x) % p == 1:
            return x


# part - 5
# User Interface and calling rest of the functions

def main():
    print("Prime modulus is 65537\n")
    print("Primitive root wrt 65537 is 3\n")
    while True:
        try:
            # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
            c = input("Choose: e (encrypt) | d (decrypt) |k (get public key) | x (exit)?:\n")
        except ValueError:
            print("Sorry, incorrect input.")
            continue
        else:
            # Key was successfully parsed!
            break

    if c == 'k':
            n = int(input("Please select a private key within 1 to 65537:\n"))
            key = fme(3, n, 65537)
            print("Your Public key is:%d\n" % key)
            print("########################################\n")
            main()

    elif c == 'e':
            print("Please select a number between 1 and 65537 \n")
            sn = int(input("Type secret number to send:\n"))
            rand_key = randint(0, 100) % 100
            ans1 = fme(3, rand_key, 65537)
            pk = int(input("Type recipient’s public key :\n"))
            ans2 = (sn * fme(pk, rand_key, 65537)) % 65537
            print("The encrypted secret is : (%d,%d)\n" % (ans1, ans2))
            print("########################################\n")
            main()

    elif c == 'd':
            print("Type in received message in form a[space]b:\n")
            en1, en2 = map(int, input().split())
            priv_key = int(input("Type in your private key:\n"))
            # Getting the value of a ^ x mod p
            ans3 = fme(en1, priv_key, 65537)
            # Getting the inverse of modulo prime
            ans4 = imp(ans3, 65537)
            # Getting the message
            ans5 = (en2 * ans4) % 65537
            print("The decrypted secret is:%d\n" % ans5)
            print("########################################\n")
            main()

    elif c == 'x':
            print("########## The Program ended! ###############\n")
            exit(0)

    else:
            print("Please select a option from above\n")
            print("########################################\n")
            main()


####################
## Calling the main function
####################
main()
