# Input
did_squats = True
workouts_list = []

# Manipulate
workouts_list.append(did_squats)

print(workouts_list)

if did_squats is True:
    workouts_list.append("Arm day")
else:
    workouts_list.append("Get that booty, hoe!")

# Output
with open("out.txt", "w+") as w:
    w.write(f"Workouts: {workouts_list}")
    w.close()
