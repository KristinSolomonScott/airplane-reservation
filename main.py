

def print_options():
  print("------------------------------------------------")
  print("A. Assign a seat to a passenger.")
  print("B. Print a boarding pass.")
  print("C. Display status report.")
  print("D. Print a passenger manifest.")
  print("E. Quit. ")
  print("------------------------------------------------")


global first_full
first_full=False

global business_full
business_full=False

global economy_full
economy_full=False

assignments=[]
'''This function  (1) adds one name and seat number to the "assignments" list, (2) deletes the name from the "passengers" list, and (3) marks the seat as taken in the "seats" list. '''
def assign_seat():
  if len(passengers)>0:
    section=input("Which section? \nA. First Class\nB. Business Class\nC. Economy\n")
    if section.lower().strip()=="a":
      global first_full
      if first_full==False:
        for i in range(len(seats)):
          if (seats[i][0][1].endswith("1") or seats[i][0][1].endswith("2") or seats[i][0][1].endswith("3")) and seats[i][1]==0:
            assignments.append([seats[i],passengers[0]]) #add name & seat number to "assignments" list
            ##
            print("////////////")
            print("Assignments list:\n")
            for item in assignments:
              print(item , "\n")
            print("////////////")
              ##
            del passengers[0]  #remove name from passengers list after seat is assigned
            seats[i][1]="X"  #change seat to show as taken in "seats" list
            if seats[20][1]=="X":
              first_full=True
            break
      else:
        print("First class is full.")
  
  
          
    elif section.lower().strip()=="b":
      global business_full
      if business_full==False:
        for i in range(len(seats)):
          if (seats[i][0][1].endswith("4") or seats[i][0][1].endswith("5") or seats[i][0][1].endswith("6")) and seats[i][1]==0:
            assignments.append([seats[i],passengers[0]]) #add name & seat number to "assignments" list
            ##
            print("////////////")
            print("Assignments list:\n")
            for item in assignments:
              print(item , "\n")
            print("////////////")
              ##
            
            del passengers[0] #remove name from passengers list after seat is assigned
            seats[i][1]="X" #change seat to show as taken in "seats" list
            if seats[41][1]=="X":
              business_full=True
            break
      else:
        print("Business section is full.")
  
          
    elif section.lower().strip()=="c":
      global economy_full
      if economy_full==False:
        for i in range(len(seats)):
          if i>41 and seats[i][1]==0:
            assignments.append([seats[i],passengers[0]])
  
  
            ##
            print("////////////")
            print("Assignments list:\n")
            for item in assignments:
              print(item , "\n")
            print("////////////")
              ##
            del passengers[0]
            seats[i][1]="X" 
            if seats[139][1]=="X":
              economy_full=True
            break
      else:
        print("Economy section is full.")
  else:
    print("***********************************************************")
    print("There are no passengers to assign. Please choose another option.")
    print("***********************************************************")
    print()


def manifest():
  alpha=input("Would you like to print the list alphabetically \n by passengers' last names? If yes, type \"Y\". \nIf no, type any other key. \n --------------------------------------------- \n ")
  if alpha.lower().strip()=="y":
    print()
    print("Seat Number \t\t\t Passenger Name")
    print("---------------------------------------------")
    alpha_passengers=sorted(assignments, key=lambda x: x[1])
    for i in range(len(alpha_passengers)):
      print(alpha_passengers[i][0][0],"\t\t\t", alpha_passengers[i][1])
    print()
  else:
    print()
    print("Seat Number \t\t\t Passenger Name")
    for i in range(len(assignments)):
      print(assignments[i][0][0], "\t\t\t", assignments[i][1])
    print()




def status_report():
  place=0
  for x in range(20):
      for i in range(8):
        if i==3:
          print("  ", end="")
        else:
          print(seats[place][1], end="")
          place+=1
      print()





done=False


passengers= ["Elliott, Jen", "Blocher, Emily", "Lohr, Jennifer", "Metzmeier, Angie", "Dillon, Heather", "Rose, Kristin","Miller, Ronda", "Coomer, Kelly", "Allen, Christina", "Dean, Cindy", "Allen, Becky","Fowler, Beth","Garcia, Angela", "McMillin, Denise", "Tally, Laura", "Breen, Jen", "Scott, Kim", "Walker, Stephanie", "Walker, Michelle", "Bliss, Scott", "Hisey, Debbie", "Hisey, Nancy", "Utz, Beth", "Endres, Erin", "Hall, Joyce", "Scott, Peggy", "Solomon, Jane", "Solomon, Winston", "Helton, Indy" ]


seats = [["A1", 0], ["B1",0], ["C1",0],["D1",0],["E1",0],["F1",0],["G1",0],["A2", 0], ["B2",0], ["C2",0],["D2",0],["E2",0],["F2",0],["G2",0], ["A3", 0], ["B3",0], ["C3",0],["D3",0],["E3",0],["F3",0],["G3",0], ["A4", 0], ["B4",0], ["C4",0],["D4",0],["E4",0],["F4",0],["G4",0], ["A5", 0], ["B5",0], ["C5",0],["D5",0],["E5",0],["F5",0],["G5",0], ["A6", 0], ["B6",0], ["C6",0],["D6",0],["E6",0],["F6",0],["G6",0], ["A7", 0], ["B7",0], ["C7",0],["D17",0],["E7",0],["F7",0],["G7",0], ["A8", 0], ["B8",0], ["C8",0],["D8",0],["E8",0],["F8",0],["G8",0], ["A9", 0], ["B9",0], ["C9",0],["D9",0],["E9",0],["F9",0],["G9",0], ["A10", 0], ["B10",0], ["C10",0],["D10",0],["E10",0],["F10",0],["G10",0], ["A11", 0], ["B11",0], ["C11",0],["D11",0],["E11",0],["F11",0],["G11",0], ["A12", 0], ["B12",0], ["C12",0],["D12",0],["E12",0],["F12",0],["G12",0], ["A13", 0], ["B13",0], ["C13",0],["D13",0],["E13",0],["F13",0],["G13",0],["A14", 0], ["B14",0], ["C14",0],["D14",0],["E14",0],["F14",0],["G14",0], ["A15", 0], ["B15",0], ["C15",0],["D15",0],["E15",0],["F15",0],["G15",0], ["A16", 0], ["B16",0], ["C16",0],["D16",0],["E16",0],["F16",0],["G16",0], ["A17", 0], ["B17",0], ["C17",0],["D17",0],["E17",0],["F17",0],["G17",0], ["A18", 0], ["B18",0], ["C18",0],["D18",0],["E18",0],["F18",0],["G18",0] , ["A19", 0], ["B19",0], ["C19",0],["D19",0],["E19",0],["F19",0],["G19",0], ["A20", 0], ["B20",0], ["C20",0],["D20",0],["E20",0],["F20",0],["G20",0]]



while not done:
  print_options()
  option=input("Please type a letter to indicate your choice of options.\n")
  if option.lower().strip()=="a":
    print("Number of items in \"seats\" list:", len(seats))  ###
    print("Number of items in \"assignments\" list:", len(assignments))  ###
    print("Number of items in \"passengers\" list:", len(passengers))  ###
    assign_seat()
      
  elif option.lower().strip()=="b":
    print()#Print a boarding pass
  elif option.lower().strip()=="c":
    status_report() #Seating status report
  elif option.lower().strip()=="d":
    manifest()
    again=input("Would you like to continue or quit?\n Please type Q to quit or any other key to continue.\n")
    if again.lower().strip()=="q":
      done=True
  elif option.lower().strip()=="e" or option.lower().strip()=="q":
    done=True
  else:
    option=input("Invalid entry. Please type a letter to indicate your choice of options.\n\n")


