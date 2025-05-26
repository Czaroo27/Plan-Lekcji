def print_schedule(schedule):
    for class_name, class_schedule in schedule.items():
        print(f"\n===== Plan lekcji dla klasy {class_name} =====")
        for day, lessons in class_schedule.items():
            print(f"\n📅 {day}:")
            for subject, teacher, room, time in lessons:
                print(f"  - {time} | {subject} z {teacher} w {room}")
