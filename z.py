from datetime import datetime
from pprint import pprint
import matplotlib.pyplot as plt
import numpy

def raw2point(raw, advance=0):
	dto = datetime.fromisoformat(raw)
	return (dto.year, dto.month, dto.day, dto.hour+advance)

with open('aqis.csv', 'r') as f:
	lines = [l.strip().split(',') for l in f.readlines()]

data = {}

for aqi, raw in lines[1:]:
	data[raw2point(raw)] = int(aqi)

# Map temperatures to the points (rounding by hour).

with open('temps.csv', 'r') as f:
	lines = [l.strip().split(',') for l in f.readlines()]

temps = {}

for raw, _, _, temp in lines[1:]:
	temps[raw2point(raw, 1)] = int(temp)

tempvsaqi = {}

for point, aqi in data.copy().items():
	if point in temps:
		if (temp := abs(temps[point])) in tempvsaqi:
			tempvsaqi[temp].append(data[point])
		else:
			tempvsaqi[temp] = [aqi]

for temp, aqis in tempvsaqi.copy().items():
	if len(aqis) < 10:
		del tempvsaqi[temp]
		continue
	tempvsaqi[temp] = sum(aqis)/len(aqis)

tempvsaqi = dict(sorted(tempvsaqi.items()))

pprint(data)

x = numpy.array(list(tempvsaqi.keys()))
a, b = numpy.polyfit(list(tempvsaqi.keys()), list(tempvsaqi.values()), 1)

plt.scatter(x, list(tempvsaqi.values()), label=f"AQI")
plt.plot(x, a*x+b)
plt.title(f'Average AQI vs temperature')
plt.xlabel('Temperature')
plt.ylabel('AQI')
plt.legend()
plt.show()