import argparse
from datetime import datetime, timedelta

def parse_arguments():
    parser = argparse.ArgumentParser(description="Calculate temperature rate of change.")
    
    # Temperature inputs
    parser.add_argument('-t1', '--temp1', type=float, required=True, help="Initial temperature")
    parser.add_argument('-t2', '--temp2', type=float, required=True, help="Final temperature")
    
    # Time inputs with default interval choices
    parser.add_argument('--start_time', type=str, default=None, 
                        help="Start time (Format: YYYY-MM-DD HH:MM:SS). Defaults to current time.")
    parser.add_argument('--interval', type=str, choices=['5m', '30m', '1h', '3h'], default='1h',
                        help="Time interval between readings (default: 1h)")
    
    return parser.parse_args()

def main():
    args = parse_arguments()
    
    # Define mapping from string choice to total minutes
    interval_mapping = {
        '5m': 5,
        '30m': 30,
        '1h': 60,
        '3h': 180
    }
    
    # Map the chosen interval to minutes and calculate seconds
    minutes = interval_mapping[args.interval]
    
    # Parse start time or default to right now
    if args.start_time:
        try:
            start_dt = datetime.strptime(args.start_time, "%Y-%m-%d %H:%M:%S")
        except ValueError as e:
            print(f"Error parsing start_time: {e}")
            return
    else:
        start_dt = datetime.now()
        
    # Calculate end time using timedelta
    end_dt = start_dt + timedelta(minutes=minutes)

    # Calculate rate of change (degrees per minute)
    temp_diff = args.temp2 - args.temp1
    rate_per_minute = temp_diff / minutes

    # Output the results
    print(f"Start Time: {start_dt.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"End Time:   {end_dt.strftime('%Y-%m-%d %H:%M:%S')} (Interval: {args.interval})")
    print(f"Temperature Change: {temp_diff:+.2f} degrees")
    print(f"Rate of Change:     {rate_per_minute:+.4f} degrees per minute")

if __name__ == "__main__":
    main()
