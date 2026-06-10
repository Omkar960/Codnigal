import matplotlib.pyplot as plt
import numpy as np
y1 = np.array([3,8,1,10])
y2 = np.array([6,2,7,5])
plt.xlabel("Score")
plt.ylabel("Attempts")
plt.title("Bowling scores")
plt.plot(y1,marker="o",color="r",linewidth=20,mec="green")
plt.plot(y2,marker="x",color="b",linewidth=40,mec="red")
plt.show()