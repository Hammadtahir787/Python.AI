
from datetime import datetime
current_time = datetime.now()
formatted_datetime = current_time.strftime("%d-%m-%y %H:%M:%S")
print(f"The current date and time is:{formatted_datetime}")
