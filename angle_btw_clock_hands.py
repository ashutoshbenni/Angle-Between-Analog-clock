from sys import exit

def angle(hh , mm):
	hh =  hh if hh <13 else hh - 12
	ans = abs(0.5 * (hh * 60 + mm) - 6 * mm)
	return min(360 - ans, ans)
	
	
try:
	hh, mm = list(map(int, input("Please enter time in hh:mm format\n").split(":")))
except ValueError:
	print ("Invalid input")
	exit()

print (angle(hh, mm))
		  
"""
try:
	hh, mm = list(map(int, input("Please enter time in hh:mm format\n").split(":")))
except Exception:
	print ("Input is in invalid format")
	exit()
	
minute_hand = mm // 5
hour_hand = hh if hh < 13 else hh - 12
angle = 0

if mm == 0:
	if hh > 6:
		angle = (12 - hour_hand) * 30
	else:
		angle = hour_hand * 30

else:
	print (hour_hand, minute_hand, mm)	

	if hour_hand > minute_hand:
		angle = (mm / 2) + (hour_hand - minute_hand - 1) * 30 + ((minute_hand + 1) * 5 - mm) * 6
		angle = angle if angle <= 180 else 360 - angle

	elif hour_hand < minute_hand:
		angle = ((60 - mm) / 2) + (minute_hand - hour_hand - 1) * 30 + (mm - (minute_hand * 5)) * 6
		angle = angle if angle <= 180 else 360 - angle

	else:
		angle = abs((mm) / 2 - (mm - (minute_hand * 5)) * 6)

print (angle)   		
"""
