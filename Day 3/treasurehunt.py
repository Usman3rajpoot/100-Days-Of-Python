print("We Come In treasure find game")
a = input("You Are at Cross road , turn in left or Right:")
if a=="left" or a== "Left":
  b = input("you Came To Lake ,swim or wait:")
  if b=="swim" or b=="Swim":
    c = int(input("they are 3 doors on island , Enter 1,2 or 3:"))
    if c==1:
      print("You Died")
    elif c==2:
      print("congrates you won")
    else:
      print("you died")
  else:
    print("you died")

else:
  print("You Died") 