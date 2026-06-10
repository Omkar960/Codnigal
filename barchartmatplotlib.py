import matplotlib.pyplot as plt

stunames = ["Sanjay","Rahul","Karan","Wasim","Ramesh","Ajay","Sartaj","Priya"]
stumarks = [34,50,50,40,50,50,10,50]
mark_perc = []
for i in stumarks:
    result = (i/50)*100
    mark_perc.append(result)
print(mark_perc)

def marklinechart():
    plt.plot(stunames,stumarks)
    plt.title("Student Marks Graph")
    plt.xlabel("Students name")
    plt.ylabel("Students Marks")
    plt.show()
marklinechart()
def percentbarchart():
    plt.bar(stunames,mark_perc)
    plt.title("Students' Percentage Graph")
    plt.xlabel("Student names")
    plt.ylabel("Student percentage")
    plt.show()
percentbarchart()
