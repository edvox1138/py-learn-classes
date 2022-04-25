from datetime import datetime

# Unix timestamp date 
def dtSinceEpoch(date_time_obj: datetime):
    # 2.7 compatibility
    timestamp = ((date_time_obj) - datetime(1970,1,1)).total_seconds()
    return int(timestamp)