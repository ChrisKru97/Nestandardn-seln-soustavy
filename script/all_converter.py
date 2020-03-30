import sys

def convertToBase10(n, base):
    number = []
    negative = False

    # If n is a negative number (it's a string at this moment of the code)..
    # then replace the minus sign with a blank character to correctly convert string to int...
    # so the algorithm can continue.
    if n[0] == '-':
        n = n.replace('-', '')
        negative = True

    for i in n:
        number.append(int(i))

    number = number[::-1]
    if negative:
        for i in range(len(number)):
            number[i] = number[i] * -1
            number[i] = number[i] * (base ** i)
    else:
        for i in range(len(number)):
            number[i] = number[i] * (base ** i)

    return sum(number)

def convertToAnyBase(n, base):
    a = 0
    i = 0

    # Special case: If n is less than zero and base is greater than zero...
    #               then we have to take the absolute value of n before dividing it...
    #               using the // operator. Reason is because taking e.g. math.floor(-2.5)...
    #               returns -3.0 which is one off the actual value (we actually want -2 in this example).
    #               After we get the correct n, we can now negate it.
    if n < 0 and base > 0:
        while n < 0:
            remainder = n % base
            n = abs(n)
            n //= base
            n = -n

            # If the base is negative, remainder will be a negative number.
            # Add the absolute value of the base to the remainder and add one to n.
            # https://en.wikipedia.org/wiki/Negative_base#Calculation
            if remainder < 0:
                remainder += abs(base)
                n += 1

            a += remainder * (10 ** i)
            i += 1

        return -a

    while n != 0:
        remainder = n % base
        n //= base

        # If the base is negative, remainder will be a negative number.
        # Add the absolute value of the base to the remainder and add one to n.
        # https://en.wikipedia.org/wiki/Negative_base#Calculation
        if remainder < 0:
            remainder += abs(base)
            n += 1

        a += remainder * (10 ** i)
        i += 1
    return a 

def main():
    x = sys.argv[1]
    baseIn = int(sys.argv[2])
    baseOut = int(sys.argv[3])

    if baseIn == 0 or baseOut == 0:
        print("Cannot have bases of 0. Exiting...")
        raise SystemExit

    print("You entered " + x + " in base " + str(baseIn) + ".")

    n = convertToBase10(x, baseIn)

    if baseOut == 1:
        ones = str(1) * n
        print("Your number in base " + str(baseOut) + " is " + str(ones) + ".")
    elif baseOut == -1:
        ones = str(1) * n
        print("Your number in base " + str(baseOut) + " is " + str('-' + ones) + ".")
    else:
        # If both bases are ten then we have already calculated its value.
        if abs(baseIn) == 10 and abs(baseOut) == 10:
            print("Your number in base " + str(baseOut) + " is " + str(n) + ".")
        else:
            print("Your number in base " + str(baseOut) + " is " + str(convertToAnyBase(n, baseOut)) + ".")

if __name__ == "__main__":
    main()
