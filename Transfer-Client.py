#Created and designed by Christopher Castillo. 
#Copyright © 2021 Chris36021. All rights reserved.
#Created in 2021.
import socket

#This entire section creates the socket using the information below and 
#establishes the connection to the host/server.
sock3t = socket.socket()
host = input(str("Please enter the host (or IP) address of the sender: "))
#host = "192.168.137.23"              #Adress of the Raspberry Pi used for the test.
port = 6969
sock3t.connect((host,port))
print("Connection established.")

#Here, the .txt file containing the necessary information is received from the host.
prep_file = open("img-info.txt", 'wb')
txt_data = sock3t.recv(1024)
prep_file.write(txt_data)
prep_file.close()

#Here, the necessary information about the file that is going to be received 
#afterwards is read and saved in variables so the can be used.
prep_file_txt = open("img-info.txt", 'r')
file_info = prep_file_txt.readline().split(" ")
file_size = int(file_info[1])
file_name = file_info[0]
file = open(file_name, 'wb')
file_data = b''                      #Empty byte variable
#This loop ensures that all the necessary information (in bytes) about the file is
#received in the client computer; without any extra data to corrupt the file.
while len(file_data) != file_size: 
    file_data += sock3t.recv(1024)
file.write(file_data)
prep_file_txt.close()
file.close()
print("File has been received successfully.")