import random
from data import subject, teachers, hours_per_week, rooms

max_hours_per_day = 8
lesson_hours = [
    "08:00 - 08:45", "08:50 - 09:35", "09:40 - 10:25", "10:40 - 11:25", 
    "11:30 - 12:15", "12:45 - 13:30", "13:35 - 14:20", "14:30 - 15:15"
]

days = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek"]

def generate_schedule():
    schedule = {
    "1A": { day: [] for day in days },
    "1B": { day: [] for day in days }
    
}


    for class_name, class_subjects in hours_per_week.items():
      for subject, hours in class_subjects.items():
        for _ in range(hours):
            placed = False
            attempts = 0

            while not placed and attempts < 100:
                day = random.choice(days)
                if len(schedule[class_name][day]) >= max_hours_per_day:
                    attempts += 1
                    continue

                available_teachers = [
                    name for name, data in teachers.items()
                    if subject in data["subjects"] and day in data["availability"]
                ]

                if not available_teachers:
                    attempts += 1
                    continue

                teacher = random.choice(available_teachers)
                room = random.choice(rooms)
                time_slot = lesson_hours[len(schedule[class_name][day])]

                conflict = any(
                    time_slot == lesson[3] and teacher == lesson[1]
                    for other_class in schedule
                    for lesson in schedule[other_class][day]
                )
                if conflict:
                    attempts += 1
                    continue

                schedule[class_name][day].append((subject, teacher, room, time_slot))
                placed = True



    return schedule
