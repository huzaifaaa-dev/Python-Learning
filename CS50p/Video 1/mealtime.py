# A Program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all.
def main():
    time = input("What time is it? ")
    convertedtime = convert(time)
    if convertedtime >= 7.0 and convertedtime <= 8.0:
        print("breakfast time")
    elif convertedtime >= 12.0 and convertedtime <= 13.0:
        print("lunch Time")
    elif convertedtime >= 18.0 and convertedtime <= 19:
        print("dinner Time")



def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    minutes = minutes / 60
    time = hours + minutes
    return time

if __name__ == "__main__":
    main()