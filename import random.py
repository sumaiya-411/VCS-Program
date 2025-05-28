import random
from datetime import datetime, timedelta

# Simulate power state readings for 60 minutes
def simulate_machine_data(minutes=60):
    states = []
    current_state = random.choice(["ON", "OFF"])
    for _ in range(minutes):
        # Randomly change state or keep same
        if random.random() < 0.1:  # 10% chance to switch
            current_state = "OFF" if current_state == "ON" else "ON"
        states.append(current_state)
    return states

# Track uptime and downtime
def track_uptime(states):
    uptime = 0
    downtime = 0
    current_time = datetime.now()
    
    log = []
    last_state = None
    
    for minute, state in enumerate(states):
        timestamp = current_time + timedelta(minutes=minute)
        if state == "ON":
            uptime += 1
        else:
            downtime += 1
        
        if state != last_state:
            log.append(f"{timestamp.strftime('%H:%M')} - State changed to {state}")
            last_state = state
    
    return log, uptime, downtime

# Run simulation
machine_data = simulate_machine_data()
log_entries, total_uptime, total_downtime = track_uptime(machine_data)

# Print log
for entry in log_entries:
    print(entry)

print(f"\nTotal Uptime: {total_uptime} minutes")
print(f"Total Downtime: {total_downtime} minutes")

