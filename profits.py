import matplotlib.pyplot as plt
import numpy
months = [1,2,3,4,5,6,7,8,9,10,11,12]
prof = [211000,183300,224700,222700,209600,201400,295500,361400,234000,266700,412800,300200]
products = ["facecream","facewash",	"toothpaste","bathingsoap","shampoo","moisturizer"]
faceprof = [2500,2630,2140,3400,3600,2760,2980,3700,3540,1990,2340,2900]
facewashprof = [1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760]
toothpasteprof = [5200,5100,4550,5870,4560,4890,4780,5860,6100,8300,7300,7400]
bathingprof = [9200,6100,9550,8870,7760,7490,8980,9960,8100,10300,13300,
14400]
shampprof = [1200,2100,3550,1870,1560,1890,1780,2860,2100,2300,2400,1800]
moisprof = [1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760]
def func():
    plt.plot(months,prof,color="r",linestyle="dotted",marker="o",linewidth=3,mec="black")
    plt.title("Monthly Profits")
    plt.xlabel("Month")
    plt.ylabel("Profits (£)")
    plt.show()
func()
def func2():
    plt.plot(months, faceprof, color="r", linestyle="dotted", marker="o", linewidth=2, label="facecream")
    plt.plot(months, facewashprof, color="g", linestyle="dotted", marker="o", linewidth=2, label="facewash")
    plt.plot(months, toothpasteprof, color="b", linestyle="dotted", marker="o", linewidth=2, label="toothpaste")
    plt.plot(months, bathingprof, color="y", linestyle="dotted", marker="o", linewidth=2, label="bathingsoap")
    plt.plot(months, shampprof, color="m", linestyle="dotted", marker="o", linewidth=2, label="shampoo")
    plt.plot(months, moisprof, color="c", linestyle="dotted", marker="o", linewidth=2, label="moisturizer")
    plt.title("Monthly Profits")
    plt.xlabel("Month")
    plt.ylabel("Profits (£)")
    plt.legend()
    plt.show()
func2()
def func3():
    plt.bar(months,faceprof,color='red',label='face cream')
    plt.bar(months,facewashprof,color='blue',label='face wash')
    plt.legend()
    plt.show()
    plt.title("Facewash VS Facecream")
    plt.xlabel("Month")
    plt.ylabel("Profits (£)")
func3()