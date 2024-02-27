
def getFactors(num):
  factors = [1]
  endRange = int(num/2) + 1
  for i in range(2,endRange):
    if num % i == 0:
      factors.append(i)
  factors.append(num)
  return factors
def problem6():
  while True:
    number = input("Please insert a valid +ve integer: ")
    if number.isnumeric():
      number = int(number)
      break
  print(f"The factors list is: {getFactors(number)}")

problem6()
