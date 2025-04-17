# Write a script that build 3 queues using append
# Once queues are built apply WFQ to the queues to pop items off the queues and print he output of the queue
# Then pop and print 3 values from PREMIUM, pop and print 2 values from STANDARD, pop and print 1 value from ECONOMY until all queues are empty


prem_queue = []    # Premium queue
stan_queue = []    # Standard queue
econ_queue =[]     # Economy queue

with open(".venv/packets.txt.py", "r") as file:   # Opens .txt file and read the contents
    for line in file:   # For every line in the file do the following/the following apply
        contents = line.split()     # The variable titled, 'contents', takes each individual line and splits the contents (packet_types and names)
        packet_type, name = contents    # Sets the split contents of each line into two variable, packet_type and name
        if packet_type == 'P':      # If the packet_type is 'P' then...
            prem_queue.append(name) # Append the name to the prem_queue queue
        elif packet_type == 'S':    # If the packet_type is 'S' then...
            stan_queue.append(name) # Append the name to the stan_queue queue
        elif packet_type == 'E':    # If the packet_type is 'E' then...
            econ_queue.append(name) # Append the name to the econ_queue queue
        else:   # If else then print 'oops!'
            print ("opps!")

print ("Premium:")  # Print 'Premium:'
print (prem_queue)  # Print the full premium queue
print ("Standard:") # Print 'Standard:'
print (stan_queue)  # Print the full standard queue
print ("Economy:")  # Print 'Economy:'
print (econ_queue)  # Print the full economy queue


def pop_it():   # Create a function that will pop a certain amount of names from the desired queue
    num_round = 0   # Variable used to keep track of how many loops have been done, set at 0
    while prem_queue or stan_queue or econ_queue:   # While loop that includes prem_queue, stan_queue, and econ_queue
        for _ in range(3):  # There's no set variable I want repeated, but the loop to be repeated 3 times
            if prem_queue:  # If the queue is the PREMIUM queue then...
                three_value = prem_queue.pop(0) # Made a variable so the information from the 'prem_queue.pop(0)' can be used
                print("PREMIUM popped:", three_value)   # Then print the three popped PREMIUM values
        for _ in range (2): # There's no set variable I want repeated, but the loop to be repeated 2 times
            if stan_queue:  # If the queue is the STANDARD queue then...
                two_value = stan_queue.pop(0)   # Made a variable so the information from the 'stan_queue.pop(0)' can be used
                print("STANDARD popped:", two_value) # Then print the two popped STANDARD values
        if econ_queue:  # If the queue is the ECONOMY queue then...
            one_value = econ_queue.pop(0)   # Made a variable so the information from the 'econ_queue.pop(0)' can be used
            print ("ECONOMY popped:", one_value)    # Then print the one popped ECONOMY value
        num_round += 1  # Adds one everytime loop is done
        print ("Round:", num_round) # Then prints the round number

print (pop_it())    # Call the pop_it function
