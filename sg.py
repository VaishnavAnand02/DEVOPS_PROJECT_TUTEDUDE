grade_store = {"Aarush":"A","Aleena":"B","Dion":"A","Sameer":"A"}
def add_new_stud(name,grade):
    if grade_store.get(name,None)==None:
        grade_store.update({name:grade})
        print_stud()
    else:
        print("Student already exists!")
def upd_stud(name,grade):
    if grade_store.get(name,None) != None:
        grade_store.update({name:grade})
        print_stud()
    else:
        print("Student doesn't exists!")
def print_stud():
    for key,val in grade_store.items():
        print(key,val)

def main():
    action = int(input("Select an action\n1.add student\n2.update grade\n3.print grades of all students\n4.exit\n"))
    while action!=4:
        if action==1:
            name =  input("Enter student's name:\n")
            grade = input("Enter student's grade:\n")
            add_new_stud(name,grade)
            print("added!\n")
        elif action==2:
            name =  input("Enter student's name:\n")
            grade = input("Enter student's grade:\n")
            upd_stud(name,grade)
            print("updated\n")
        else:
            print_stud()
        action = int(input("Select an action\n1.add student\n2.update grade\n3.print grades of all students\n4.exit\n"))
if __name__=="__main__":
    main()