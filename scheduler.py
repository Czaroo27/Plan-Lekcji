import random
from data import subject, teachers, hours_per_week, rooms

max_hours_per_day = 8
lesson_hours = ["08:50 - 09: 35", "08:40 - 10:25", "10:40 - 11:25", "11:30 - 12:15", 
                "12:45 - 13:30", "13:35 - 14:20", "14:30 - 15:15", "15:20 - 16:05"]

def generate_schedule():
    schedule = {day: [] for day in ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek"]}

    for subject, hours in hours_per_week.items():
        for _ in range(hours):
            while True:
                day = min(schedule, key=lambda d: len(schedule[d]))
                if len(schedule[day]) < max_hours_per_day:  
                    break  

            teacher = next((t for t in teachers if subject in teachers[t]), None)
            room = random.choice(rooms)
            lesson_time = lesson_hours[len(schedule[day])]  
            schedule[day].append((subject, teacher, room, lesson_time))  

    return schedule  
