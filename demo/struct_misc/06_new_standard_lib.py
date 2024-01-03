from zoneinfo import ZoneInfo
from datetime import datetime
 
now = datetime.now(tz=ZoneInfo("Europe/London"))
print(now) # Output: 2023-07-11 16:25:00+01:00
