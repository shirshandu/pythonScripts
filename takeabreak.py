# SCENARIO

# A programmer spends too much time at a stretch in their computers
# A Python program which refreshes them to take a break
# In this case I am playing a youtube song after every 2 hours
# Fell free to fork the project and enhance the code or shoot new ideas

import time
import webbrowser

total_breaks = 3
break_count = 0

print ("This program started on"+time.ctime())

while (break_count < total_breaks):
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=WwliN6p_zWw")
	break_count = break_count + 1
