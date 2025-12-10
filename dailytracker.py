import matplotlib.pyplot as plt
done=False
namelist=[]
durlist=[]
activities=[]
day=input("enter date: ")
totals={}
while done == False:
    activity=input("enter activity:")
    startTime=float(input("enter start time:"))
    endTime=float(input("enter end time:"))
    while endTime<startTime:
        print("invalid time period")
        startTime=float(input("enter start time:"))
        endTime=float(input("enter end time:"))    

    dic={"name":activity,"started at": startTime, "ended at": endTime}
    activities.append(dic)
    choice=input(("press enter to add another activity, or type q to finish:"))
    if choice.lower() == "q":
        done = True
        
for item in activities:
    start=item["started at"]
    end=item["ended at"]
    name=item["name"]
    timeTaken=end-start
    if name in totals:
        totals[name]+=timeTaken
    else:
        totals[name]=timeTaken
namelist=list(totals.keys())
durlist=list(totals.values())

plt.pie(durlist,labels=namelist,autopct='%1.1f%%')
plt.title(f"{day} break down")
plt.show()
    
