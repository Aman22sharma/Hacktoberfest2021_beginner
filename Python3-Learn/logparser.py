#Author :- Ved Prakash Bhaskar
#Python Concept :- This program will parse the given log file and print out a report giving how long the device was ON and the timestamp of any ERR conditions.

# Github Link :- https://github.com/iamvpbhaskar


# logparser.py
import datetime
import sys

def get_next_event(filename):
    with open(filename, "r") as datafile:
        for line in datafile:
            if "dut: Device State: " in line:
                line = line.strip()
                # Parse out the action and timestamp
                action = line.split()[-1]
                timestamp = line[:19]
                yield (action, timestamp)

def compute_time_diff_seconds(start, end):
    format = "%b %d %H:%M:%S:%f"
    start_time = datetime.datetime.strptime(start, format)
    end_time = datetime.datetime.strptime(end, format)
    return (end_time - start_time).total_seconds()

def extract_data(filename):
    time_on_started = None
    errs = []
    total_time_on = 0

    for action, timestamp in get_next_event(filename):
        # First test for errs
        if "ERR" == action:
            errs.append(timestamp)
        elif ("ON" == action) and (not time_on_started):
            time_on_started = timestamp
        elif ("OFF" == action) and time_on_started:
            time_on = compute_time_diff_seconds(time_on_started, timestamp)
            total_time_on += time_on
            time_on_started = None
    return total_time_on, errs

if __name__ == "__main__":
    total_time_on, errs = extract_data(sys.argv[1])
    print(f"Device was on for {total_time_on} seconds")
    if errs:
        print("Timestamps of error events:")
        for err in errs:
            print(f"\t{err}")
    else:
        print("No error events found.")


