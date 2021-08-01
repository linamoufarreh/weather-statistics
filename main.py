readings=""
list_readings=[]
while True:
    readings= input("Enter a list of temperatures separated by a space:")
    if readings!="stop":
        list_readings= readings.split(" ") + list_readings
    else:
        break

#turning list of readings into list of float numbers:
float_temp=0
float_list=[]
for k in range(0, len(list_readings)):
    float_temp= float(list_readings[k])
    float_list.insert(k,float_temp)
print(float_list)

for l in range(0, len(list_readings)):
    if float_list[l]>50 or float_list[l]<-50:
        list_readings.remove(list_readings[l])
        float_list.remove(float_list[l])
#average:
temp=0
for i in range(0, len(list_readings)):
    temp= int(list_readings[i])+ temp
    average= float(temp/len(list_readings))
print("The average temperature is:", average)

#3 max and min temperatures:

sorted_list= sorted(float_list)
print("Minimum temperatures:")
for j in range(0, 3):
    print(sorted_list[j])

print("Maximum temperatures:")
for e in range(len(float_list)-1,len(float_list)-4,-1):
    print(sorted_list[e])
