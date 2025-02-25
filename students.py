high_scores = []
f = open("students.txt", "w")
f.write("***** STUDENT GRADES *****")
f.close()


def add():
    name = input("Enter the name of the student: ")
    mark = int(input("Enter the grade: "))
   
    f = open("students.txt", "a")
    f.write(f"\n{name}:{mark}")
    
    f.close()
    
def display():
    f = open("students.txt", "r")
    r = f.readlines()
    
    print("\n***** STUDENT GRADES *****\n")
    for each_person in r[1:]:
        personnel = each_person.strip()
        colon = personnel.find(':')
        print(f"***** {personnel.upper()[:colon]} *****\n")
        print(f"Grade : {personnel[colon + 1:]}\n")
        print("*************\n")
        if int(personnel[colon+1:]) > 75:
            high_scores.append(personnel[:colon])
        
    print("***** STUDENTS WHO SCORED ABOVE 75 ARE: *****\n")
    count = 1
    for each in high_scores:
        print(f"{count}.{each}")    
        count+=1
    print(f"\n Total number of students who scored above 75 are: {len(high_scores)}")    
        
    f.close()
    

while 1:
    print("\n***** SELECT AN OPTION *****\n")
    print("1. Add    2. Display   3.Exit\n")
    choice = int(input("Choice: "))
        
    if choice == 1:
            add()
            
    elif choice == 2:
            display()
        
    elif choice == 3:
            break

