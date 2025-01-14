print("\n")

lst = []

def PrimeNumberGenerator(x):

  if x <= 0:
    print("\n")
    raise ValueError("\n\nTHE NUMBER MUST BE A POSITIVE WHOLE NUMBER\n")

  elif x == 1:
    print("1 is Not a Prime Number")

  else:
    for i in range(2, x+1):

      check = 0

      for j in range(2, i):
        if i % j == 0:
          check = 1

      if check == 0:
        lst.append(i)

    print("\n")
    print("The Prime Numbers are:")
    print(lst)


x = int(input("Generate Prime Numbers up to: "))


if __name__ == '__main__':
  PrimeNumberGenerator(x)

print("\n")

