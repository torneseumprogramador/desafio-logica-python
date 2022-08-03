# try:
#   print(x)
# except:
#   print("An exception occurred")

# try:
#     x = "r1"
#     print(int(x))
# except:
#     print("o x não contem somente números")

# try:
#   # x = "r1"
#   # print(int(x))
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")


# try:
#   # print(x)
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")

# try:
#   print(x)
#   # print("oi")
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")


# try:
#   # f = open("demofile.txt", "w")
#   f = open("demofile.txt", "r")
#   try:
#     f.write("Lorum Ipsum")
#   except Exception as e:
#     print(e)
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except Exception as e:
#     print(e)
#     print("Something went wrong when opening the file")


# x = -1
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")


try:
  # int("r1")
  x = "hello"
  if not type(x) is int:
    raise TypeError("Only integers are allowed")
except TypeError:
  print("Tipo tratado de erro")
except:
  print("Erro de qualquer tipo")

