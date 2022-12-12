class menu:
    def __init__(self, userChoice):
        self.userChoice = userChoice
        if userChoice == "A":
            count = 0
            file = open("reservation.txt")
            lines = file.readlines()[1:]
            file.close()
            for line in lines:
                count += 1

            if count == 0:
                print("There are no Reservations!!")
                print()
            else:
                file = open("reservation.txt", "r")
                print(file.read())
                file.close()
                print()

        elif userChoice == "B":
            with open("reservation.txt", "r") as file:
                for nextLine in file:
                    pass

            if nextLine[0] == "#":
                number = 1
            else:
                number = int(nextLine[0]) + 1

            name = input("Enter Name: ")
            date = input("Enter Date: ")
            time = input("Enter Time: ")
            adults = int(input("No. of Adults: "))
            children = int(input("No. of Children: "))
            file = open("reservation.txt", "a")
            file.write(f"{number}\t{name}\t{date}\t{time}\t{adults}\t{children}\n")
            file.close()
            print('Reservation success...')
            print()

        elif userChoice == "C":
            reservationNum = input("Enter Reservation Number: ")
            file1 = open("reservation.txt", "r")
            lines = file1.readlines()
            file1.close()
            file2 = open("reservation.txt", "w")
            print()

            for line in lines:
                if not line.startswith(reservationNum):
                    file2.write(line)
            file2.close()
            print()
            

        elif userChoice == "D":
            adults, children, total_adults, total_children, total = 0, 0, 0, 0, 0
            file = open("reservation.txt", "r")
            list_of_lists = []
            report = ""
            i = 0

            for line in file:
                i += 1
                if i > 1:

                    stripped_line = line.strip()
                    line_list = stripped_line.split("\t")
                    adults += int(line_list[4])
                    children += int(line_list[5])
                    subtotal = (int(line_list[4]) * 500) + (int(line_list[5]) * 300)
                    total += subtotal
                    line_list.append(str(subtotal))
                    report += f"{line_list[0]}\t{line_list[2]}\t{line_list[3]}\t" \
                              f"{line_list[1]}\t{line_list[4]}\t{line_list[5]}\t{line_list[6]}\n"
            file.close()
            print()
            print("REPORT")
            print()
            print("#Date\tTime\tName\tAdults\tChildren\tSubtotal")
            print(report)
            print("Total Number of Adults: ", adults)
            print("Total Number of Children: ", children)
            print("Grand Total: PHP ", total)
            print("------------------- nothing follows----------------")
            print()
        elif userChoice == "E":
            import sys
            sys.exit("Thank you ! ")
            print()

        else:
            print("Invalid response. Please try again.")
            print()

while True:
    try:
        file = open("reservation.txt", "r")
    except FileNotFoundError:
        file = open("reservation.txt", "w+")
        file.write("#\tNamet\t        Date\t        Time\t    Adults\tChildren\n")
    file.close()
    print()

    print("==========RESTAURANT RESERVATION SYSTEM==========")
    print("===================System Menu====================")
    print("  [ A ] View all Reservations\t [ B ] Make Reservation")
    print("  [ C ] Delete Reservation\t [ D ] Generate Report")
    print("  [ E ] Exit\n")
    print('_________________________________________________________')

    selectionChoices = input('Enter Selection: ').upper()
    menu(selectionChoices)