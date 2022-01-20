#Problem Statement:
#A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, 
#the professor decides to cancel class if fewer than some number of students are present when class starts.
#Arrival times go from on time () to arrived late ().
#Given the arrival time of each student and a threshhold number of attendees, determine if the class is
#cancelled.

def angryProfessor(k, a):
 arr_late = []
 arr_ontime=[]
 for i in range(len(a)):
    if a[i] <= 0:
        arr_ontime.append(i)
    elif a[i] > 0:
        arr_late.append(i)
 if len(arr_ontime)<k:
     return "YES"
 else:
     return "NO"
        
t = int(input().strip())
for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)