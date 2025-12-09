import matplotlib.pyplot as plt
done=False
namelist=[]
durlist=[]
activities=[]
while done is False:
    activity=input("enter activity:")
    startTime=float(input("enter start time:"))
    endTime=float(input("enter end time:"))
    dic={"name":activity,"started at": startTime, "ended at": endTime}
    activities.append(dic)
    lmk=input("type 'True' if done:")
    if lmk == "True":
        done=True
for item in activities:
    start=item["started at"]
    end=item["ended at"]
    name=item["name"]
    timeTaken=end-start
    print(name,": lasted",timeTaken,"hours")
    namelist.append(name)
    durlist.append(timeTaken)
print(namelist)
print(durlist)
plt.pie(durlist,labels=namelist,autopct='%1.1f%%')
plt.show()
    
