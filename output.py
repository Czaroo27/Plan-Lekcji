def print_schedule(schedule):
    for day, lessons in schedule.items():
        print(f"\n📅 {day}:")
        for subject, teacher, room in lessons:
            print(f"  - {subject} z {teacher} w {room}")
