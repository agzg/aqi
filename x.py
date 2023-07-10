from datetime import datetime
import matplotlib.pyplot as plt

raw = []

with open('data.csv', 'r') as f:
	raw = [l.strip() for l in f.readlines()]
	
aqi   = [int(l.split(',')[0]) for l in raw[1:]]
stamp = [l.split(',')[1] for l in raw[1:]]

dtime = []
for t in stamp:
	u = datetime.fromisoformat(t)
	dtime.append((
		u.year, u.month, u.day, u.hour, u.minute, u.second, u.weekday()
	))

data = {}
for i, point in enumerate(dtime):
	data[point] = aqi[i]

# BIANNUAL

# monthly_data = {}
# for point, aqi in data.items():
# 	if (pm := point[1]) in monthly_data:
# 		monthly_data[pm].append(aqi)
# 	else:
# 		monthly_data[pm] = [aqi]

# monthly_average = {}
# monthly_max = {}
# monthly_min = {}
# for month, aqis in monthly_data.items():
# 	monthly_average[month] = sum(aqis) / len(aqis)
# 	monthly_max[month] = max(aqis)
# 	monthly_min[month] = min(aqis)


# plt.plot(list(monthly_average.keys()), list(monthly_average.values()), label="Average")
# plt.plot(list(monthly_max.keys()), list(monthly_max.values()), label="Maximum", linestyle="--")
# plt.plot(list(monthly_min.keys()), list(monthly_min.values()), label="Minimum", linestyle="--")
# plt.title('Monthly AQI Data vs Month')
# plt.xlabel('Month')
# plt.ylabel('Monthly AQI Average')
# plt.legend()
# plt.show()

# MONTHLY

# for month in range(3, 11):
# 	daily_data = {}
# 	for point, aqi in data.items():
# 		if not point[1] != month:
# 			continue
# 		if (pd := point[2]) in daily_data:
# 			daily_data[pd].append(aqi)
# 		else:
# 			daily_data[pd] = [aqi]

# 	daily_average = {}
# 	daily_max = {}*hello*
# 	daily_min = {}
# 	for day, aqis in daily_data.items():
# 		daily_average[day] = sum(aqis) / len(aqis)
# 		daily_max[day] = max(aqis)
# 		daily_min[day] = min(aqis)

# 	plt.plot(list(daily_average.keys()), list(daily_average.values()), label="Average")
# 	plt.plot(list(daily_max.keys()), list(daily_max.values()), label="Maximum", linestyle="--")
# 	plt.plot(list(daily_min.keys()), list(daily_min.values()), label="Minimum", linestyle="--")
# 	plt.title(f'Daily AQI Data For Month {month} vs Day')
# 	plt.xlabel('Day')
# 	plt.ylabel('Daily AQI Data')
# 	plt.legend()
# 	plt.savefig(f'monthly{month}.png')
# 	plt.cla()


# MONTHLY MAXIMUMS

# for month in range(3, 11):
# 	daily_data = {}
# 	for point, aqi in data.items():
# 		if not point[1] != month:
# 			continue
# 		if (pd := point[2]) in daily_data:
# 			daily_data[pd].append(aqi)
# 		else:
# 			daily_data[pd] = [aqi]

# 	daily_max = {}
# 	for day, aqis in daily_data.items():
# 		daily_max[day] = max(aqis)

# 	plt.scatter(list(daily_max.keys()), list(daily_max.values()), label=f"Max. {month}", linestyle="-.")
# 	plt.title(f'Monthly Maximum AQIs')
# 	plt.xlabel('Day of month')
# 	plt.ylabel('Daily AQI Data')
# 	plt.legend()
# 	# plt.savefig(f'monthly{month}.png')
	# plt.cla()

# plt.show()
# plt.savefig('monthly-maxes.png')

# # MONTHLY MAXIMUMS ACCORDING TO WEEKDAY

# for month in range(3, 11):
# 	daily_data = {}
# 	for point, aqi in data.items():
# 		if not point[1] != month:
# 			continue
# 		if (pwd := point[-1]) in daily_data:
# 			daily_data[pwd].append(aqi)
# 		else:
# 			daily_data[pwd] = [aqi]

# 	weekday_average = {}
# 	for weekday, aqis in daily_data.items():
# 		weekday_average[weekday] = sum(aqis) / len(aqis)

# 	plt.plot(list(weekday_average.keys()), list(weekday_average.values()), label=f"Month {month}", linestyle="-.")
# 	plt.title(f'Monthly Average AQIs by Weekday')
# 	plt.xlabel('Weekday in month')
# 	plt.ylabel('Daily AQI Data')
# 	plt.legend()
# 	# plt.savefig(f'monthly{month}.png')
# 	# plt.cla()

# plt.show()
# plt.savefig('monthly-maxes.png')

## MONTHLY AVERAGES BASED ON WEEKDAY
# for month in range(3, 11):
# 	weekday_data = {}
# 	for weekday in range(7):
# 		weekday_data[weekday] = []

# 	for point, aqi in data.items():
# 		if point[1] != month:
# 			continue
# 		weekday_data[point[-1]].append(aqi)
# 	weekday_max = {}
# 	for weekday, aqis in weekday_data.items():
# 		weekday_max[weekday] = sum(aqis)/len(aqis)

# 	plt.plot(list(weekday_max.keys()), list(weekday_max.values()), label=f"Max. {month}", linestyle="-.")
# 	plt.title(f'Monthly average AQI by weekday')
# 	plt.xlabel('Weekday')
# 	plt.ylabel('AQI')
# 	plt.legend()
# plt.show()

## BIANNUAL DATA BASED ON WEEKDAY
# weekday_data = {}

# for weekday in range(7):
# 	weekday_data[weekday] = []

# for point, aqi in data.items():
# 	if (pwd := point[-1]) in weekday_data:
# 		weekday_data[pwd].append(aqi)
# 	else:
# 		weekday_data[pwd] = [aqi]

# weekday_max = {}
# weekday_min = {}
# weekday_averages = {}
# for weekday, aqis in weekday_data.items():
# 	weekday_max[weekday] = max(aqis)
# 	weekday_min[weekday] = min(aqis)
# 	weekday_averages[weekday] = sum(aqis)/len(aqis)

# plt.plot(list(weekday_averages.keys()), list(weekday_averages.values()), label=f"Average")
# print(list(weekday_min.keys()), list(weekday_min.values()))
# plt.plot(list(weekday_min.keys()), list(weekday_min.values()), label=f"Min.", linestyle="-.")
# plt.plot(list(weekday_max.keys()), list(weekday_max.values()), label=f"Max.", linestyle="-.")
# plt.title(f'Biannual AQI data by weekday')
# plt.xlabel('Weekday')
# plt.ylabel('AQI')
# plt.legend()
# plt.show()

weekday_data = {}

for weekday in range(7):
	weekday_data[weekday] = []

for point, aqi in data.items():
	if (pwd := point[-1]) in weekday_data:
		weekday_data[pwd].append(aqi)
	else:
		weekday_data[pwd] = [aqi]

plt.plot(list(weekday_averages.keys()), list(weekday_averages.values()), label=f"Average")
print(list(weekday_min.keys()), list(weekday_min.values()))
plt.plot(list(weekday_min.keys()), list(weekday_min.values()), label=f"Min.", linestyle="-.")
plt.plot(list(weekday_max.keys()), list(weekday_max.values()), label=f"Max.", linestyle="-.")
plt.title(f'Biannual AQI data by weekday')
plt.xlabel('Weekday')
plt.ylabel('AQI')
plt.legend()
plt.show()