
import sched, psutil, time
event_schedule = sched.scheduler(time.time, time.sleep)

def check_sys():
    cpu_usage = psutil.cpu_percent()
    print("CPU usage: ", cpu_usage)
    if cpu_usage > 10:
        N = int(cpu_usage / 10)
        print(f"CPU usage: {cpu_usage} Run docker {N} times.")
    else:
        print("Keep docker containers to 1")
    event_schedule.enter(3, 1, check_sys, )


e1 = event_schedule.enter(1, 1, check_sys,)
event_schedule.run()