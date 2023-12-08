from datetime import datetime, timedelta

dt = datetime(2000, 1, 1)
print(dt)

# minus 1 day 
print(dt-timedelta(days=1))

# difference in day 
print(datetime(2022, 1, 1) - dt)

print(datetime.now())
