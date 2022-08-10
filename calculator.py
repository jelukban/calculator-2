"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
# input_string = input("")
# tokens = input_string.split(' ')
file_name = open("data2.txt")

for line in file_name:
  line = line.rstrip()
  tokens = line.split(' ')

  try:
    tokens[1] = float(tokens[1])
  except   ValueError:
    print("This is a not entry")
    continue

  try:
    tokens[2] = float(tokens[2])
  except   ValueError:
    print("This is a not entry")
    continue
  except IndexError:
    continue

  # print(tokens)

  while True:
    if tokens[0] == 'pow':
      print(power(num1 = float(tokens[1]), num2 = float(tokens[2])))
      break

    elif tokens[0] == 'add':
      print(add(num1 = float(tokens[1]), num2 = float(tokens[2])))
      break

    elif tokens[0] == 'subtract':
      print("{:.5f}".format(subtract(tokens[1],tokens[2])))
        #subtract(num1 = float(tokens[1])f"{:.2f}", num2 = float(tokens[2])))
      break

    elif tokens[0] == 'multiply':
      print(multiply(num1 = float(tokens[1]), num2 = float(tokens[2])))
      break

    elif tokens[0] == 'divide':
      print(divide(num1 = float(tokens[1]), num2 = float(tokens[2])))
      break

    elif tokens[0] == 'mod':
      print(mod(num1 = float(tokens[1]), num2 = float(tokens[2])))
      break

    elif tokens[0] == 'square':
      print(square(num1 = float(tokens[1])))
      break

    elif tokens[0] == 'cube':
      print(cube(num1 = float(tokens[1])))
      break

file_name.close()
