import numpy as np
from mpi4py import MPI

"""
This code squares every number in an array using MPI parallel processing. 
You run code with many processors with the syntax (on your shell):
    $ mpiexec -n 4 python script.py
where the number after -n is the number of processors you want to run the 
script with. 

By Joelle Begin, modified from Adrian Liu's code and extensively commented. 
June 2020
"""

#this just talks to your computer to see how many processors are available
comm = MPI.COMM_WORLD

#every processor is assigned a number
myID = comm.rank

#master's job will be to send out tasks and gather the results
master = 0

# -1 since one of the processors is master
numHelpers = comm.size -1

#the array we want to perform the operation on
array = np.arange(1,10,1 )

'''we have to square every number in the array, so there are as many tasks
as there are numbers in the array''' 
num_tasks = len(array)

'''if there are more helpers than there are tasks, we only want as many helpers
as there are tasks to be active'''
num_active_helpers = min(numHelpers, num_tasks)

''' Every CPU sees the same script; we have to have conditional statements 
so the CPUs know what tasks to perform based on their ID which was assigned in
line 19. '''

if myID == master:
    '''master will manage the parallelization. It sends out tasks, recieves
    the results of the operation and gathers everything into a result array'''
    result = np.zeros(len(array)) #construcing empty array to hold results

    num_sent = 0 #need to keep track of how many assignments have been sent out!
    
    print('sending out assignments')
    for helperID in range(1, num_active_helpers+1):
        #looping through the helpers; these are the initial assignments
        print('I asked', helperID, 'to do number', helperID)
        
        '''this sends the value (helperID -1) to processor with ID == helperID.
        The tag is going to help us keep track of whether the process is finished'''
        comm.send(helperID-1, dest = helperID, tag = helperID)
        
        num_sent += 1

    for i in range(1, num_tasks+1):
        status = MPI.Status()

        '''here master recieves info from helper. temp will be the result of 
        the operation (number squared in this case). Master can recieve this 
        from any processor, which is important because we don't know the order
        that proceses will complete.'''
        temp = comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status)
        
        #ID of helper that just sent info
        sender = status.Get_source()
        tag = status.Get_tag()
        
        #placing result in corresponding entry of results array
        result[tag] = temp

        if num_sent < num_tasks: #ie there are more things to do
            '''sends next task to the processor who just sent results; we know
            this processor doesn't have anything to do since it just finished
            its previous task!'''
            comm.send(num_sent, dest = sender, tag = 1)
            print('I asked', sender, 'to do number', num_sent +1)
            num_sent += 1

        else: #ie everything has been done
            print('everything is done so I asked', sender, 'to pack up')
            
            '''tag = 0 is basically a flag to say "everything is done, you can 
            stop working" '''
            comm.send(0, dest = sender, tag = 0)
    
    print(result)

#here is what the helpers do
elif myID <= num_active_helpers:
    complete = False
    while (complete == False):
        status = MPI.Status()

        '''recieving assignment from master. The way this code is written, the 
        number the helper recieves corresponds to the index of the original 
        array that it will square'''
        assignment = comm.recv(source = master, tag = MPI.ANY_TAG, status = status)
        tag = status.Get_tag()

        if tag ==0:
            complete = True
        else:
            #getting the number it has to perform the operation on
            num = array[assignment]

            #performing the operation
            num_squared = num**2

            #sending the result back to master
            comm.send(num_squared, dest = master, tag = assignment)

'''code past this barrier will not be executed until the above processes are done
This is good to have in case you need to do more stuff to the result of the 
parallelization!
'''
comm.Barrier() 

