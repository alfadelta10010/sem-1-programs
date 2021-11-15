# 6) If the person leaves home at 6:52 am, and runs1 mile at an easy pace (8:15 per
# mile), then 3 miles at a tempo (7:12 per mile) and 1 mile at easy pace again, what
# time does the person get back home for breakfast?
normalTime = (8 * 60) + 15
fastTime = (7 * 60) + 12
totalTime = 2 * normalTime + 3 * fastTime
totalTimeRound = totalTime // 60
print("The person reaches home in {} minutes".format(totalTimeRound))
finalTime = (6 * 60 + 52 + totalTimeRound)
hrs = finalTime // 60
mins = finalTime % 60
print("The person reaches home by {}:{}".format(hrs, mins))
