'''
Name                :           Chat Cat
Programming Language:           Python 3.6.2
Release Date        :           13th August 2017
Author              :           Naman Sahore
E-Mail              :           namanshore@gmail.com
GitHub              :           https://github.com/namansahore
        For any query please contact

    This is a client server based chatting python code
which executes on server side and provides a medium to
their clients to send and receive messages between each
other.

Default PORT : 5555
'''
import socket                                        #IMORTING LIBRARIES FOR SOCKET AND THREADING
from _thread import *

host = ''                                            # IT IS A VOID HOST BECAUSE WE ONLY WANTS TO LISTEN ON SERVER SIDE
port = 5555                                          # SETTING A PORT FOR LISTENING YOU CAN CHANGE IS AS PER YOUR NEED
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                    # BUILDING A SOCKET
clients = []                                         # THIS WILL TAKE RECORDS OF CLIENTS WHO CONNECTS
client_info = {}                                     # DICTIONARY OF NAME AND CONNECTION
banner = """
 _____ _           _     _____       _   
/  __ \ |         | |   /  __ \     | |  
| /  \/ |__   __ _| |_  | /  \/ __ _| |_ 
| |   | '_ \ / _` | __| | |    / _` | __|
| \__/\ | | | (_| | |_  | \__/\ (_| | |_ 
 \____/_| |_|\__,_|\__|  \____/\__,_|\__|

            By Naman Sahore                                      
"""

try:
    sock.bind((host, port))                          # BINDING PORT AND HOST WITH SOCKET
except socket.error as se:
    print('Error = ' + str(se))

sock.listen(5)                                       # START LISTENING


def t_client(con):
    """
    Client Handler
        This will take information about connection and make a chat thread
        for then
    :param con: About connection
    :return: An infinite loop which push messages to their respective cats
    """
    global client_info
    con.send(str.encode(banner))
    con.send(str.encode('Welcome :3\nEnter your name -> '))                 # SETTING UP CLIENT NAME
    name_set = False
    while not name_set:
        name = con.recv(1024)
        name = name.decode('utf-8')
        name = name.split()
        if len(name) is not 0:
            if not (name[0] in client_info.keys()):
                name = name[0]
                break
            else:
                con.send(str.encode('User already exists\n-> '))
        else:
            con.send(str.encode('Please enter your name\n-> '))

    client_info[name] = con

    con.send(str.encode('Enter your cat\'s name -> '))                      # SETTING UP RECEIVER NAME
    name_set = False
    while not name_set:
        r_name = con.recv(1024)
        r_name = r_name.decode('utf-8')
        r_name = r_name.split()
        if len(r_name) is not 0:
            if r_name[0] in client_info.keys():
                r_name = r_name[0]
                break
            else:
                con.send(str.encode('Cat doesn\'t exist !\n-> '))
        else:
            con.send(str.encode('Please enter your cat\'s name\n-> '))

    con.send(str.encode('Connection established :\n'))

    while True:                                      # AN INFINITE LOOP FOR TAKING MESSAGES FROM SENDER
        data = con.recv(1024)
        if con_check(data, name):                    # STOPPING THREAD
            data = str.encode('Cat run away... :3\n')
            snd_to_cat(data, name, r_name, str(name + ' -> '))
            break
        snd_to_cat(data, name, r_name, str(name + ' -> '))                  # SENDING MESSAGE TO RECEIVER
    con.close()                                      # CLOSING CONNECTION OF THE THREAD


def snd_to_cat(data, name, r_name, deco):
    """
    Message sender
        It takes the message from client handler or(t_client) and send it to respective
        receiver
    :param data:    encoded data send by the sender
    :param name:    name of the sender
    :param r_name:  name of the receiver
    :param deco:    decorator for marking the message
    :return:        None
    """
    global client_info
    deco = deco.encode('utf-8')
    for n in client_info.keys():
        if n == r_name:
            client_info[n].sendall(deco + data)
            client_info[n].sendall('====================================\n'.encode('utf-8'))


def con_check(data, name):
    """
    Connection Checker
        Takes the data from the sender and check for 'exit' command. If the command is 'exit'
        it returns True and sender thread closed by the Client Handler.
    :param data: Data from sender
    :param name: name of the sender
    :return:     Bool value (True/False)
    """
    global clients
    d_data = data.decode('utf-8')
    d_data = d_data.split()
    count = len(d_data)
    if count == 1:
        if d_data[0] == 'exit':
            del client_info[name]
            print('Disconnected from ' + str(con))
            return True
    else:
        return False

print(banner)
print('Server Started : ')
while True:                                         # AN INFINITE LOOP FOR ACCEPTING CONNECTIONS
    con, adr = sock.accept()
    clients.append(con)
    print('Connected to = ' + adr[0] + ' : ' + str(adr[1]))

    start_new_thread(t_client, (con,))              # START CONNECTION'S THREAD