import matplotlib.pyplot as plt
print("Study tracker. Enter one day and its hours at a time")
h=[]
d=[]
done=False
while not done:
    date=input("enter date: ")
    d.append(date)
    hours=float(input("enter study hours of that day: "))
    h.append(hours)
    choice=input("To enter more days press enter. If done: type q:")
    if choice.lower()=="q":
        done = True
plt.plot(d, h, marker="o")
plt.xlabel("Date")
plt.ylabel("Study hours")
plt.title("Study hours over time")
plt.show()