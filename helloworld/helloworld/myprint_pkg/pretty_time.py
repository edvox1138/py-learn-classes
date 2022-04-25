from datetime import datetime

# Return a string representing the date and time, controlled by an explicit format string.
def dtToPrettyTime(date_time_obj : datetime):
    dt_string = date_time_obj.strftime("%Y/%m/%d %H:%M:%S")
    return dt_string