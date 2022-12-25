README 
This program uses two scripts edevice.py and scheduler.py to simulate the Scheduler Consumer and producer problem with   python, semaphores, 
thread and sockets. Edevice.py connects to the socket of scheduler.py and while it still connected generates a message to send to the 
scheduler and waits until scheduler.py sends a signal back that it receives it to send more. The scheduler.py opens a udp socket and has a 
consumer thread and a production thread. The producer thread recovers what edevice sent, adds it to the queue and then sorts it by the 
shortest job first and then sends a signal back to the edevice to send another message. The consumer thread removes the first element in 
queue and then sleeps for the amount of time the element consumes. schedule.py continues until the nth message variable is consumed and 
produce which by default  is 30.

Instructions: to run it first run the scheduler by typing python3 scheduler2.py [port] then you can run edevices by typing  edevice2.py <id> 
<server address> <server port> if you want to add more devices i recommend piping the devices like this: edevice.py <1> <server address> 
<server port> | edevice.py <2> <server address> <server port> to simulate more than 1 device sending messages  to the scheduler.

