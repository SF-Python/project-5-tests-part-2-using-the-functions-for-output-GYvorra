# Gaston Yvorra
# COP 2002 0M1
# 20240702
# Lecture - Module 7
# Peoject 5 (Part 1 & 2)

from random import randrange

portNameArray = ["FTP", "FTP", "SSH", "Telnet", "SMTP", "DNS", "DHCP", "DHCP", "HTTP", "POP3", "NetBIOS", 
"NetBIOS", "IMAP", "SNMP", "SNMP", "LDAP", "HTTPS", "SMB", "RDP"]

portNumArray = ["20", "21", "22", "23", "25", "53", "67", "68", "80", "110", "137", "139",
"143", "161", "162", "389", "443", "445", "3389"]


def numToName(portNumArray: list[str], portNameArray:  list[str], portNumber:  str) -> str:
    index = 0
    for port in portNumArray:
        if port == portNumber:
            return portNameArray[index]
        else:
            index += 1
    return "PortNumber not found in list"

#Uses the portName (string) to find it in the portNameArray (string array and find the corresponding port number in the portNumArray (string array).
def nameToNum(portNumArray: list[str], portNameArray: list[str], portName: str) -> list[str]:
    result = []
    for index in range(len(portNumArray)): # using the index compare the portNameArray value at the index with the portName
        if portName == portNameArray[index]: # if the index value == portName
            result.append(portNumArray[index])
    return result # returns a list of values for the port name



# Ensures that the user's input for the menu is either, 12, 2, 3 or m and returns their valid input.
# The user will continue to be reprompted until they enter either a 1, 2 or 3 as this function will be used to determine which couce the user wants
def getInput():
    userInput = ""
    while userInput not in ["1", "2", "3", "m"]:
        userInput = input("Choice:  ").strip()
    return userInput 

# Only things in the main function will execute if the file is run.
def menu():
    prompt = "Main Menu"
    prompt += "\n1. Given a port number, identify the PROTOCOL (use abbreviation)."
    prompt += "\n2. Given a port protocol, identify a port NUMBER."
    prompt += "\n3. Exit\n"
    print(prompt)
    userInput = getInput()
    return userInput.strip()

def qWhatNumber():
    msg = "Option 2: Identify the port's NUMBER."
    msg += "\n----------------------------------------\n"
    print(msg)
    selection = ""
    while selection != "m":
        qIndex = randrange(0, len(portNameArray))
        qName = portNameArray[qIndex]
        answer = nameToNum(portNumArray, portNameArray, qName)
        prompt = f"What is the number for protocol {qName} (m=Main Menu)? "
        selection = input(prompt).strip()
        while selection in ["", "\n"]:
            selection = input(prompt).strip()
        if selection in answer:
            print("Correct answer!\n")
        else:
            msg = f"Incorrect. The correct answer is {portNumArray[qIndex]}.\n"
            print(msg)

def qWhatName():
    msg = "Option 1: Identify the port's PROTOCOL."
    msg += "\n----------------------------------------\n"
    print(msg)
    selection = ""
    while selection != "m":
        qIndex = randrange(0, len(portNameArray))
        qNum = portNumArray[qIndex]
        answer = numToName(portNumArray, portNameArray, qNum)
        prompt = f"What is the protocol for port {qNum} (m=Main Menu)? "
        selection = input(prompt).strip()
        while selection in ["", "\n"]:
            selection = input(prompt).strip()
        if selection == answer:
            print("Correct answer!\n")
        else:
            msg = f"Incorrect. The correct answer is {portNameArray[qIndex]}.\n"
            print(msg)

def main():
    selection = ""
    while selection != "3":
        selection = menu()
        if selection == "1":
            qWhatName()
        elif selection == "2":
            qWhatNumber()
    print("\nProgram Complete. I hope this has helped in studying for the CompTIA A+ certification.")


    
    # print(" thedandRange fn print a dandom integer between 0 and the value you provide")
    # random_index=randrange(len(portNameArray))
    # print(portNameArray[random_index])


if __name__ == "__main__":
    main()


