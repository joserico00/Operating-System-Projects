readme.txt

ReadMe
Createdb.py creates a database dfs where it stores the files datanodes , 
blockids and names
Use: python createdb.py

meta-data.py is the metadata server where it receives packets and handles 
it commands, there are 5 possible commands

register makes a new data node and adds them to the database

put inserts new files into the database and sends back a list of datanodes

get, checks if a file is in the database and gives back the datanodes that 
has the file


blocks:add the datablock from the packet with the file to the database, 
letting the metadata know wheres the location of these files are

list gives a list of files to send back 

Use:python meta-data.py <port, default=8000>

data-node.py dataNode server, creates a datanode server for the metadata 
when called with a ip and port it sends a register packet 
to the metadata server to register it. the datanode recieves packets with 
2 commands get and put.
get: gets a file from the  blockid received from the packet and send it 
back to the asker

put: generates a blockid for the file it receives and stores it as the 
name.

use:python data-node.py <server address> <port> <data path> <metadata 
port,default=8000>

ls.py lists all the files in the database. it receives 2 parameters which 
is the ip and port. 
it sends a list packet to metadata server and recieves a list of packets 
and prints them
Use:python ls.py <server>:<port, default=8000>

copy.py program with the fuction of either copying a file from the dfs 
with copyfromdfs or sending a file to the dfs with copytodfs
copytodfs: can be called with python copy.py <source file> 
<server>:<port>:<dfs file path>
copytodfs contacts the metadata server with a put packet  to get a list of 
datanodes it can send the file. then copy opens the file 
i want to copy divides them by the the number of datanodes and sends it to 
the datanode with a put 
packet to get a blockid for each of them and then notify the metadata the 
blockid and  file saved


copyfromdfs: can be called with  python copy.py <server>:<port>:<dfs file 
path> <destination file>
contacts the metadata server to get datablocks that cotains the file then 
saves a new file with the datablocks from the datanodes sserver

Help:
https://docs.python.org/2/library/socketserver.html for sockets
https://docs.python.org/3/library/os.path.html#os.path.getsize for file 
path and getting the amount of bytes from a filewith path.size
Cheo in class  for hints on how to solve problems like for instance using 
sendall() to send all the data without mising any by having the other 
socket receive it by 
making while loop with recv
discussed with Carlos problems I had like database wise 
