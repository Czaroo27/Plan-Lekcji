def print_schedule(schedule):
    for day, lessons in schedule.items():
        print(f"\n📅 {day}:")
        for subject, teacher, room, time in lessons:
            print(f"  - {time} | {subject} z {teacher} w {room}")
