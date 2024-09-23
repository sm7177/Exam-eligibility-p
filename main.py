num = 300
clas = int(input("Number of classes attended:"))

atten = (clas/float(num))*100
print("Total attendance=300")
print ("Your Attendance is: ", atten,"%")
if atten >= 70:
    print ("You are allowed to sit in exam")
else:
    print ("Sorry, you are not allowed to sit in the exam.")

