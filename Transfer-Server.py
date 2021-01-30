#Created and designed by Christopher Castillo. 
#Copyright © 2021 Chris36021. All rights reserved.
#Created in 2021.
import socket
import os

#This entire section creates the socket using the information below and 
#establishes the connection to the client.
sock3t = socket.socket()
host = socket.gethostname()
port = 6969
#The '' makes the socket less restrictive when it comes to accepting connections.
sock3t.bind(('', port))
#This tells the socket the amount of connections it should expect
sock3t.listen(1)
print("The server host is: ",host)
print("Awaiting any incoming connections...")
#.accept() method returns a tuple containing a socket object and an address.
connection, address = sock3t.accept()
print(address, " Has connected to the server.")

file_name = input(str("Please enter the name of the file to send (with extension): "))
#file_name = "4k360.jpg"                        #Name of the file that was initially tested.

'''
The point of this next section of code is to make the file transfer process work correctly with
any file. For no data corrpution to happen, both the client and the server need to know
the size of the file that is going to be trasnferred; which may be difficult when doing an
automated process with a file that was recently created. To get around this issue, I made it
so a text file containing both the size and the name of the file that the server is going to send is
sent before the actual file. That wasy, the client computer has access to the necessary information.
'''

#This creates the .txt file containing the required info.
file_size = os.path.getsize(file_name)
file_info = file_name + " " + str(file_size) + "\n"
file_info_file = open("file-info.txt", "w")
file_info_file.write(file_info)
file_info_file.close()

#This part sends the information about the file the server is going to send afterwards.
prep_file_size = os.path.getsize("file-info.txt")
prep_file = open("file-info.txt", 'rb')
prep_file_data = prep_file.read(prep_file_size)
connection.send(prep_file_data)
print("File information has been transmitted successfully.")

#This part sends the file that the host specified beforehand.
file = open(file_name , 'rb')
file_data = file.read(file_size)
connection.send(file_data)
print("Data has been transmitted successfully.")