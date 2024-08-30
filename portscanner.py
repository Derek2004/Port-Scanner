#!/usr/bin/python3

# Import socket module to enable netwirk functionality
import socket

#Create a new sosket object 's' using the socket() function
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Setting a socket timeout of for socket operations
s.settimeout(5)

# To prompt the user to input the IP address they want to scan and store the input in the variable
host = input("Enter the IP you want to scan" "\n")

# To prompt the user to input the port they want to scan and store the input in the variable
# The input is converted to an integer since port numbers are integers
port = int(input("Enter the port you want to scan" "\n"))

# Define the port scanner function which takes the port as its argument 
# The function checks if the port provided is open or closed
def portScanner(port):

    # Use connect_ex to attempt to connect to the host and port
    # connect_ex returns 0 if the connection was successful, indicating the port is open
    # Any non-zero value indicates the port is closed
    if s.connect_ex((host, port)):
        print("The Port is closed")
    else:
        print("The Port is open")

# Call the portScanner function to perform the port scan on the user-specified port
portScanner(port)