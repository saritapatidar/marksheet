print("Enter class:")
while True:
    try:
        c=int(input())
        if c<=12:
            break
    except ValueError:
        print("it is wrong")
print("Roll_number:")
while True:
    try:
        r=int(input())
        roll=str(r)
        if len(roll)!=5:
            raise ValueError
        else:
            break
    except ValueError:
        print("It is wrong please enter right")
print("scholar no:")
while True:
    try:
        scho=int(input())
        sc=str(scho)
        if len(sc)!=5:
            raise ValueError
        else:
            break
    except ValueError:
        print("It is wrong please enter valid")
print("aadhar no:")
while True:
    try:
        aa=int(input())
        aadh=str(aa)
        if len(aadh)!=12:
            raise ValueError
        else:
            break
    except ValueError:
        print("It is wrong please enter valid")
print("sssmid:")
while True:
    try:
        ss=int(input())
        ssm=str(ss)
        if len(ssm)!=8:
            raise ValueError
        else:
            break
    except ValueError:
        print("IT is wrong please enter valid")
print("family id:")
while True:
    try:
        fa=int(input())
        family=str(fa)
        if len(family)!=8:
            raise ValueError
        else:
            break
    except ValueError:
        print("It is wrong please enter valid")
print("cast:")
special="!, @, #, $, %, ^, &, *, (, ), -, _, =, +,|,{,},;,:,/,?,.,>,<."
while True:
    try:
        ca=input()
        for i in ca:
            if i in special:
                raise ValueError
        break
    except ValueError:
        print("It is wrong please enter valid")
while True:
    try:
        NAME=input("Enter the name:")
        for i in NAME:
            if i in special:
                raise ValueError
        break
    except ValueError:
        print("It is wrong please enter valid")
print("father name")
while True:
    try:
        Father_name=input("Enter the father name:")
        for i in Father_name:
            if i in special:
                raise ValueError
        break
    except ValueError:
        print("It is wrong please enter right name")
#print("mother name")
while True:
    try:
        Mother_name=input("Enter the mother name:")
        for i in Mother_name:
            if i in special:
                raise ValueError
        break
    except ValueError:
        print("It is wrong Please enter valid name")
print("Date of birth")
from datetime import datetime
birth=input("Enter the date(dd-mm-yyyy):")
format_data = "%d-%m-%Y"
Date_of_birth=datetime.strptime(birth, format_data)

print(f"Name :{NAME}")
print(f"Father name :{NAME}")
print(f"Mother name :{NAME}")
print(f"Date of birth :{Date_of_birth}")
total_number=100

k="english"
k1="Hindi"
k2="maths"
k3="value education"
k4="Life skill activities"
while True:
    try:
        lo=int(input("enter the english number:"))
        if lo>100:
            raise ValueError
        else:
            break
    except ValueError:
        print("it is wrong")
while True:
    try:
        h=int(input("enter the hindi number:"))
        if h>100:
            raise ValueError
        else:
            break
    except ValueError:
        print("it is wrong")
while True:
    try:
        m=int(input("enter the maths number:"))
        if m>100:
            raise ValueError
        else:
            break
    except ValueError:
        print("it is wrong")
while True:
    try:
        v=int(input("enter the value education:"))
        if v>100:
            raise ValueError
        else:
            break
    except ValueError:
        print("it is wrong")
while True:
    try:
        l=int(input("enter the life skill activities:"))
        if l>100:
            raise ValueError
        else:
            break
    except ValueError:
        print("it is wrong")
if lo<=100 and lo>=80:
    dis="A"
elif lo<80 and lo>60:
    dis="B"
elif lo<60 and lo>40:
    dis="C"
else:
    dis="D"
if h<=100 and h>=80:
    dise="A"
elif h<80 and h>60:
    dise="B"
elif h<60 and h>40:
    dise="C"
else:
    dise="D"
if m<=100 and m>=80:
    disea="A"
elif m<80 and m>60:
    disea="B"
elif m<60 and m>40:
    disea="C"
else:
    disea="D"
if v<=100 and v>=80:
    diseas="A"
elif v<80 and v>60:
    diseas="B"
elif v<60 and v>40:
    diseas="C"
else:
    diseas="D"
if l<=100 and l>=80:
    d="A"
elif l<80 and l>60:
    d="B"
elif l<60 and l>40:
    d="C"
else:
    d="D"
marks_total=lo+h+m+v+l
ts=500

if marks_total<=500 and marks_total>=400:
    gr="A+"
elif marks_total<400 and marks_total>=300:
    gr="A"
else:
    gr="B"
PERCENTAGE=marks_total*100/500
if PERCENTAGE>60:
    GH="FIRST"
else:
    GH="SECOND"
if PERCENTAGE>33:
    result="Pass"
else:
    result="Fail"
print("-"*100)
print(f"|         {'VISHWAKARMA NAGAR kAROND BHOPAL - 462038 [M.P]':<90}|")
print(f"|         {'MARK SHEET CUM - CERTIFICATE  2023-24         ':<90}|")
print("-"*100)
print(f"|{'class':<10}{'Roll_number':<15}{'Scholar no':<15}{'Aadhar no':<20}{'SSSMID':<15}{'Family id':<15}{'CAST':<9}|")
print(f"|{c:<10}{r:<15}{scho:<15}{aa:<20}{ss:<15}{fa:<15}{ca:<9}|")
print("-"*100)
print(f"|{'CARTIFIED THAT':<99}|")
print(f"|student Name :{NAME:<85}|")
print(f"|Father  name :{Father_name:<85}|")
print(f"|Mother name  :{Mother_name:<85}|")
print(f"|Date of birth:{birth:<85}|")
print("-"*100)
print(f"| {'Subject':<25}|{'Maxmarks':<15}|{'OBT.MArks':<10}|{'GRADE':<45}|")
print("-"*100)
print(f"| {k:<25}|{total_number:<15}|{lo:<10}|{dis:<45}|")
print("-"*100)
print(f"| {k1:<25}|{total_number:<15}|{h:<10}|{dise:<45}|")
print("-"*100)
print(f"| {k2:<25}|{total_number:<15}|{m:<10}|{disea:<45}|")
print("-"*100)
print(f"| {k3:25}|{total_number:<15}|{v:<10}|{diseas:<45}|")
print("-"*100)
print(f"| {k4:25}|{total_number:<15}|{l:<10}|{d:<45}|")
print("-"*100)
print(f"|{'Total':<20}{ts:<20}{gr:<59}|")
print("-"*100)
print(f"|{'Othe Subject':<30}{'Annual grade':<69}|")
print(f"|{'GK':<30}{'A':<69}|")
print(f"|{'COMPUTER':<30}{'A':<69}|")
print(f"|{'DAWING':<30}{'A':<69}|")
print("-"*100)
print(f"|{'Percentage':<15}{PERCENTAGE:<15}{'Rank':<15}{'-':<54}|")
print(f"|{'Division':<15}{GH:<15}{'Result':<15}{result:<54}|")
print("-" * 100)
print("it is merge ")


# #  Compare Two Large Files Line by Line
# # You are given two large text files. Write a program that compares them line by line and prints the differences. If a line exists in one file but not the other, highlight it.

# # Example Output:
# # Line 5 differs:
# # File1: "The quick brown fox"
# # File2: "The quick blue fox"
# with open('file1.txt','w') as f:
#     f.write("The quick brown fox")
# with open('file2.txt','w') as f:
#     f.write("The quick blue fox")
# if 
