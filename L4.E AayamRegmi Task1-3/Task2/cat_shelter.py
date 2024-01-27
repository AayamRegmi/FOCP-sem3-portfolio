import sys

def shelter_status(filename):

    Average_visit_length=0
    Longest_visit=0
    Shortest_visit=float('inf') #used for comparison for longest and shortest visit
    total_visit=0

    our_cat_visits=0
    other_cat_visits=0
    
    total_time=0

    try: 
        with open(filename, 'r') as log:
            for line in log:
                line_list = line.strip().split(',') #stores the value of each line of log file in a list

                if line_list[0] == 'END': #Ends the loop and closes the file when End is found
                    break

                if line_list[0] == 'OURS': #calculations for our cat
                    our_cat_visits += 1

                    #calculates the time frame which the cat was in the shelter
                    session_time = int(line_list[2]) - int(line_list[1])
                    
                    #calculates all the total time
                    total_time += session_time
                    Average_visit_length = total_time / our_cat_visits
                    total_visit += 1
                    
                    #calculate the longest and shortest time cat spent
                    if session_time < Shortest_visit:
                        Shortest_visit = session_time
                    if session_time > Longest_visit:
                        Longest_visit = session_time

                else:
                    other_cat_visits += 1

        print("Log File Analysis")
        print("=================\n")  
        print(f"Cats Visits: {our_cat_visits}") 
        print(f"Other cats: {other_cat_visits}\n")    
        print(f"Total Time in House {total_time//60} hours, {total_time%60} minutes")
        print(f"Average Visit Length: {int(Average_visit_length)} minutes\n")
        print(f"Longest Visit       : {Longest_visit} minutes")
        print(f"Shortest Visit      : {Shortest_visit} minutes")
    
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")

    
    
        
if len(sys.argv)!=2:
    print("Missing command line argument")
else:
    shelter_status(sys.argv[1])    