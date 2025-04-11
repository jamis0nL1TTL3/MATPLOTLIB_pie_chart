import matplotlib.pyplot as plot
# set up your lists
numlist = [8, 6, 5, 3]
namelist = ['sophomores', 'juniors', 'seniors', 'freshmen']
colorlist = ['purple', 'yellow', 'orange', 'green' ]
explodelist = [0.1, 0.1, 0.2, 0.4]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.0f%%', colors=colorlist,
    	explode = explodelist, startangle = 180)
plot.axis('equal')
plot.savefig('piechart.png')
