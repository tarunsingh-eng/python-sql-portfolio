logs = [
    "100,SUCCESS,Login",
    "550,ERROR,Database Timeout",
    "200,ERROR,Invalid Input",
    "600,SUCCESS,Logout",
    "900,ERROR,Unauthorized Access"
]

result = [
    # what you want to collect
    message 
    for log in logs 
    for timestamp, status, message in [log.split(",")]
    if status == "ERROR" and int(timestamp) > 500

    # split the log into parts
    # unpack into variables
    # apply your conditions here
]

print(result)