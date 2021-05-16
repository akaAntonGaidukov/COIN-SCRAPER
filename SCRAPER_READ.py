# Lib list
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Read from log file
file = open("CoinScraper.csv", "r",encoding="utf-8")

filestr =file.read()
splitlist = filestr.split("\n") #split list by rows

file.close()

# Create lists -> improve by adding name of coin in to log file to make this process automatic
DateTime = []
pdoge = []
peth = []
pshibu = []

# Unzip list values to separate lists, by order. -> improve by adding names or by reading data from df created in csv
for el in splitlist:
    try:
        date, time, doge, eth, shi = el.split(",")
        DateTime.append(date+time)
        pdoge.append(float(doge))
        peth.append(float(eth))
        pshibu.append(float(shi))
    except ValueError: # for empty values and other strange shits.
        pass

# Plot setup
ax1 = plt.subplot(411)
plt.plot(DateTime, pdoge)
plt.setp(ax1.get_xticklabels(), visible=False)
plt.title("DOGE",fontsize=7,loc="right")

ax2 = plt.subplot(412, sharex=ax1)
plt.plot(DateTime, peth)
plt.setp(ax2.get_xticklabels(), visible=False)
plt.title("ETH",fontsize=7,loc="right")
plt.ylabel("Price RUB")

ax3 = plt.subplot(413, sharex=ax1)
plt.plot(DateTime, pshibu)
plt.setp(ax3.get_xticklabels(), fontsize=6)

ax3.tick_params(axis='x', labelrotation = 90)
myLocator = mticker.MultipleLocator(12) #values to skip, helps to scale the X axis (dates overlaping eachother) -> improve by automating this parameter based on
ax3.xaxis.set_major_locator(myLocator) # length of X values and setting a function from it like - mticker.MultipleLocator((len(X))/100)

plt.xlabel("Time")
plt.title("SHIB",fontsize=7,loc="right")

plt.show()