"""1.ASSIGNMENT: HOSPITAL PATIENT RECORD MANAGEMENT SYSTEM:--
A multi-specialty hospital is currently maintaining patient records manually in registers. As the number of patients is
 increasing, it has become difficult to search, update, and manage records efficiently.

The hospital management has decided to develop a simple Patient Record Management System using Python. 
The system should store patient information in a nested dictionary where:

Key → Patient ID
Value → Dictionary containing patient details

Each patient record should contain:

Patient Name
Age
Gender
Disease
Doctor Name
Sample Data Structure
{
101:{
    "name":"Ajay",
    "age":35,
    "gender":"Male",
    "disease":"Fever",
    "doctor":"Dr. Sharma"
},
102:{
    "name":"Ravi",
    "age":42,
    "gender":"Male",
    "disease":"Diabetes",
    "doctor":"Dr. Gupta"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=====================================
 HOSPITAL PATIENT MANAGEMENT SYSTEM
=====================================

1. Add New Patient
2. Search Patient
3. Update Patient Disease
4. Delete Patient Record
5. Display All Patients
6. Count Total Patients
7. Display Patients By Disease
8. Display Oldest Patient
9. Display Youngest Patient
10. Exit

Functional Requirements
1. Add New Patient

Accept the following information from the user:

Patient ID
Patient Name
Age
Gender
Disease
Doctor Name

Store the record in the nested dictionary.

Validation:
If the Patient ID already exists, display:

Patient ID already exists.

2. Search Patient

Accept Patient ID from the user.

If the patient exists, display complete information.

Sample Output

Patient ID : 101
Name       : Ajay
Age        : 35
Gender     : Male
Disease    : Fever
Doctor     : Dr. Sharma

If Patient ID is not found:

Patient Record Not Found

3. Update Patient Disease

Accept Patient ID.

If found:

Ask for new disease.
Update the disease information.

Sample Output

Disease Updated Successfully
4. Delete Patient Record

Accept Patient ID.

If found:

Remove the patient record.

Sample Output

Patient Record Deleted Successfully

Otherwise:

Patient Not Found
5. Display All Patients

Display all patient records in a formatted manner.

Sample Output

--------------------------------
Patient ID : 101
Name       : Ajay
Age        : 35
Disease    : Fever
Doctor     : Dr. Sharma
--------------------------------

Patient ID : 102
Name       : Ravi
Age        : 42
Disease    : Diabetes
Doctor     : Dr. Gupta
6. Count Total Patients

Display the total number of patients currently stored.

Sample Output

Total Patients : 25
7. Display Patients By Disease

Accept a disease name from the user.

Display all patients suffering from that disease.

Sample Output

Enter Disease : Fever

101  Ajay
108  Aman
115  Neha

If no patient is found:

No Patient Found
8. Display Oldest Patient

Find and display the patient having the highest age.

Sample Output

Oldest Patient Details

Patient ID : 110
Name       : Ravi
Age        : 68
Disease    : Diabetes
Doctor     : Dr. Gupta
9. Display Youngest Patient

Find and display the patient having the minimum age.

Sample Output

Youngest Patient Details

Patient ID : 121
Name       : Riya
Age        : 4
Disease    : Viral Fever
Doctor     : Dr. Mehta
10. Exit

Terminate the application.

Sample Output

Thank You For Using Hospital Patient Management System"""




d={
101:{
    "name":"Ajay",
    "age":35,
    "gender":"Male",
    "disease":"Fever",
    "doctor":"Dr. Sharma"
},
102:{
    "name":"Ravi",
    "age":42,
    "gender":"Male",
    "disease":"Diabetes",
    "doctor":"Dr. Gupta"
}
}

while True:
    print("""=====================================
 HOSPITAL PATIENT MANAGEMENT SYSTEM
=====================================

1. Add New Patient
2. Search Patient
3. Update Patient Disease
4. Delete Patient Record
5. Display All Patients
6. Count Total Patients
7. Display Patients By Disease
8. Display Oldest Patient
9. Display Youngest Patient
10. Exit""")
    choice=int(input("ENTER THE CHOICE"))
    match choice:
        case 1:
            print("ADD THE NEW PATIENT")
            n=int(input("enter the patient id"))
            if n in d:
                print("patient already exists")
            else:
                name=input("enter name :")
                age=int(input("enter age:"))
                gender=input("enter the gender:")
                disease=input("enter disease:")
                doctor=input("enter doctor name:")
                d[n]={
                "name":name,
                "age":age,
                "gender":gender,
                "disease":disease,
                "doctor":doctor
                }
                print("PATIENT  added successfully")
        case 2:
            print("search patient")
            a=int(input("enter patient id"))
            if a in d:
                print(d.get(a))
            f=0
            for k,v in d.items():
                if a==k:
                    print("patient id :",k)
                    print("name:",v["name"])
                    print("age:",v["age"])
                    print("disease:",v["disease"])
                    print("doctor :",v["doctor"])
                    f=1
                if f==0:
                    print("Patient Record Not Found")
        case 3:
            print("accept PATIENT DISEASE")
            a=int(input("enter patient id"))
            if a in d:
                c=input("enter the new disease")
                d[a].update({"disease":c})
                print("disease updated successfully")
            else:
                print("patient id not found")


        case 4:
            print("delete patient record")
            a=int(input("enter patient id"))
            if a in d:
                del d[a]
            else:
                print("patient id not found")
        case 5:
            print("display all reords")
            for id,details in d.items():
                 print("-"*30)
                 print("patient id:",id)
                 
                 for k,v in details.items():
                     print(k,":",v)
        case 6:
            print("6. Count Total Patients")
            print(len(d))
        case 7:
            print("7. Display Patients By Disease")
            a=input("enter disease:")
            c=0
            for k,v in d.items():
                if v["disease"].lower()==a.lower():
                    print(k,v["name"])
                    c=1
            if c==0:
                print("No Patient Found")
        case 8:
            print("8. Display Oldest Patient")
            w=0
            for k,v in d.items():
                for i,m in v.items():
                    if i.lower()=="age":
                        if m >w:
                            w=m 
            for k,v in d.items():
                if v["age"]==w:
                    print("patient id:",k)
                    print("name:",v["name"])   
                    print("age:",v["age"])   
                    print("disease:",v["disease"])   
                    print("doctor:",v["doctor"])   
        case 9:
            print("Display Youngest Patient")
            w=23252#w = list(d.values())[0]["age"]
            for k,v in d.items():
                for i,m in v.items():
                    if i.lower()=="age":
                        if m <w:
                            w=m 
            for k,v in d.items():
                if v["age"]==w:
                    print("patient id:",k)
                    print("name:",v["name"])   
                    print("age:",v["age"])   
                    print("disease:",v["disease"])   
                    print("doctor:",v["doctor"])
        case 10:
            print("Thank You For Using Hospital Patient Management System")
            break