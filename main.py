

def print_options():
  print("------------------------------------------------")
  print("A. Assign a seat to a passenger.")
  print("B. Print a boarding pass.")
  print("C. Display status report.")
  print("D. Print a passenger manifest.")
  print("E. Quit.")
  print("------------------------------------------------")



def manifest():
  alpha=input("Would you like to print the list alphabetically \n by passengers' last names? If yes, type \"Y\". \nIf no, type any other key. \n --------------------------------------------- \n ")
  if alpha.lower().strip()=="y":
    print()####
    alpha_passengers=sorted(passengers, key=lambda x: x[0])
    for i in range(len(alpha_passengers)):
      print(alpha_passengers[i][0],"\t\t\t", passengers[i][2])
    print()
  else:
    for i in range(len(passengers)):
      print(passengers[i][2],"\t\t", passengers[i][0])
    print()





done=False

passengers = [["Elliott, Jen", None, None], ["Blocher, Emily", None, None], ["Lohr, Jennifer",None, None], ["Metzmeier, Angie", None, None], ["Dillon, Heather", None, None], ["Rose, Kristin", None, None], ["Miller, Ronda", None, None], ["Coomer, Kelly", None, None], ["Allen, Christina", None, None], ["Dean, Cindy", None, None],["Allen, Becky", None, None], ["Fowler, Beth", None, None], ["Garcia, Angela", None, None], ["McMillin, Denise", None, None], ["Tally, Laura", None, None], ["Breen, Jen", None, None], ["Scott, Kim", None, None], ["Walker, Stephanie", None, None], ["Walker, Michelle", None, None], ["Bliss, Scott", None, None], ["Hisey, Debbie", None, None], ["Hisey, Nancy", None, None], ["Utz, Beth", None, None], ["Endres, Erin", None, None], ["Hall, Joyce", None, None], ["Scott, Peggy", None, None], ["Solomon, Jane", None, None], ["Solomon, Winston", None, None], ["Helton, Indy", None, None]]



while not done:
  print_options()
  option=input("Please type a letter to indicate your choice of options.")
  if option.lower().strip()=="a":
    print() #Assign a seat
  elif option.lower().strip()=="b":
    print()#Print a boarding pass
  elif option.lower().strip()=="c":
    print() #Seating status report
  elif option.lower().strip()=="d":
    manifest()
    again=input("Would you like to continue or quit?\n Please type Q to quit or any other key to continue.\n")
    if again.lower().strip()=="q":
      done=True
  elif option.lower().strip()=="e" or option.lower().strip()=="q":
    done=True
  else:
    option=input("Invalid entry. Please type a letter to indicate your choice of options.")


