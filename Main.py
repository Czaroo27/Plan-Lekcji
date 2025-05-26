from scheduler import generate_schedule
from output import print_schedule
from exporter import export_schedule_to_pdf

if __name__ == "__main__":
    schedule = generate_schedule()
    print_schedule(schedule)
    export_schedule_to_pdf(schedule)
