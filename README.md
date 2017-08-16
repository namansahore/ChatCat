# ChatCat


## Introduction 


Chatcat establish server and opens a PORT (Default 5555) for communication between clients. Communication established by the server between clients is one to one, it means that sender can send message to only one receiver in a connection. This script can be modified in different ways to evoke server as well as client's functions. 

Author		:	[Naman Sahore](https://github.com/namansahore)


## Working

Execute the script on a python 3 machine. Now we have a server listening on TCP PORT 5555 which act as a medium between clients for sending and receiving messages.
![serverstarted](https://user-images.githubusercontent.com/30320729/29249328-e07444da-804a-11e7-83b9-7aede8605096.JPG)
Clients can reach to the server with the help of netcat or telnet:

	nc SERVER_IP SERVER_PORT
    telnet SERVER_IP SERVER_PORT

![client](https://user-images.githubusercontent.com/30320729/29249331-fe1b7ce2-804a-11e7-9aac-e13fb667c0f0.JPG)

As you get connected with server server starts showing your logs. Now you are in interactive command line with ChatCat.

![serverstat](https://user-images.githubusercontent.com/30320729/29249366-86d50f80-804b-11e7-8d06-78b16a03f1ce.JPG)


Enter your name it should be unique.
![nameerror](https://user-images.githubusercontent.com/30320729/29249402-aa6b6682-804c-11e7-92f1-109eafc3cc4e.JPG)

Enter your cat's name or receiver's name, it should be client of the server.
![caterror](https://user-images.githubusercontent.com/30320729/29249403-b8c19314-804c-11e7-9117-11ade01d3245.JPG)

Now you can communicate with your cat or receiver. :envelope:

For terminating session you can simply type 'exit'. As you type 'exit', terminating command send to your receiver and you quit the session.

All the logs of connections drop or made are shown on server's terminal.

And here's some code! :clipboard:


This is [on GitHub](https://raw.githubusercontent.com/namansahore/ChatCat/master/ChatCat.py) so let me know if I have broken it somewhere.



### Stuff used to make this:

 * [PyCharm](https://www.jetbrains.com/pycharm/): python IDE
 * [Python 3.6.2](https://www.python.org/)
