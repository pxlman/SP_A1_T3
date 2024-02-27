def encrypt(ch,val):
  alphas = "abcdefghijklmnopqrstuvwxyz"
  try:
    n = alphas.index(ch)
    isLower = True
  except:
    n = alphas.index(ch.lower())
    isLower = False
  newOrd = (n + val) % 26
  if isLower:
    return alphas[newOrd]
  else:
    return alphas[newOrd].upper()

def problem4():
  while True:
    txt = input("Please insert the text to encrypt(Only alphabatic and spaces are encrypted): ")
    for i in txt:
      if i.isalpha():
        break

  while True:
    shift = input("Please insert a shift value from 1 to 25: ")
    if shift.isnumeric():
      shift = int(shift)
        if shift <= 25 and shift >= 1:
          break
        else:
          continue


  newTxt = ""
  for i in txt:
    if i.isalpha():
      newTxt += encrypt(i,shift)
    else:
      newTxt += i
      

  print(f"\n- The encypted text is:\n########\n{newTxt}\n########")
problem4()
