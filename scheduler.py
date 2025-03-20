import random
from data import lessons, teachers, hours_per_week, rooms

def generate_schedule():
    schedule = {day: [] for day in ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek"]}

    for lessons, hours in hours_per_week.items():
        for _ in range(hours):
            day = random.choice(list(schedule.keys()))
            teacher = next((t for t in teachers if lessons in teachers[t]), None)
            room = random.choice(rooms)
            schedule[day].append((lessons, teacher, room))

    return schedule
