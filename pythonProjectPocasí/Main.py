from symbol import factor

sun = True
windy = False
mist = True


if sun == True and windy == False and mist == False:
    print("Je dobré počasí a není třeba deštník")
if mist == True or sun == False and windy == False :
    print("Je dobré si vzíti deštník")
if windy == True and sun == True:
    print("Vzíti čepici")
if mist:
    print ("Vezměte si reflexní oblečení")


