import random
temperatures=[]
for i in range(7):
	temperatures.append(random.randint(26,41))
the_days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
ctr=0
good_days_count=0
for i in range(7):
	if(temperatures[i]%2==0):
		ctr=ctr+1
		print(the_days[i]+"is a good day")
		good_days_count=good_days_count+1
highest_temp=0
for i in range(7):
	if(temperatures[i]>temperatures[highest_temp]):
		highest_temp=i
lowest_temp=0
for i in range(7):
	if(temperatures[i]<temperatures[lowest_temp]):
		lowest_temp=i
highest_temp_day=the_days[highest_temp]
lowest_temp_day=the_days[lowest_temp]
x=0.0 
for i in range(7):
	x=x+temperatures[i]
x=x/7
above_avg =[]
for i in range(7):
	if(temperatures[i]>x):
		above_avg.append(temperatures[i])
print("The wether report")
for i in range(7):
	print(the_days[i],":",temperatures[i])
print("shelly have",ctr,"good days")
print("the hotwqtest temperature is:",highest_temp,"on",highest_temp_day)
print("the lowest temperature is:",lowest_temp,"on",lowest_temp_day)
print("the avrage temperature is:", x)
print("the days with above avrage temperature were",above_avg)