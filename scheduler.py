import random
from data import lessons, teachers, hours_per_week, rooms

max_hours_per_day = 8

lesson_hours = ["8:00", "8:55", "9:50", "10:45", "11:40", "12:35", "13:30", "14:25"]


def generate_schedule():
    schedule = {day: [] for day in ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek"]}

    for lessons, hours in hours_per_week.items():
        for _ in range(hours):
            while True:
                day = min(schedule, key=lambda d: len(schedule[d]))
                if len(schedule[day]) < max_hours_per_day:  
                    break  
                if schedule[day] and schedule[day][-1][0] != lessons and any(l[0] == lessons for l in schedule[day]):
                    continue


            teacher = next((t for t in teachers if lessons in teachers[t]), None)
            room = random.choice(rooms)
            schedule[day].append((lessons, teacher, room))  

    return schedule  

