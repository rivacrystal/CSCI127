#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: October 27, 2021
#This program looks at olympic world records

def worldRecord(gender, event):
     """
     Write a function worldRecord(), that takes two parameters: gender (string) and the event type (int).
     The function should return a float for the Olympic world record for the event.

     Men's Standard, event type 100 meters: record is 9.63 seconds.
     Men's Standard, event type 200 meters: record is 19.30 seconds.
     Men's Standard, event type 400 meters: record is 43.03 seconds.
     Women's Standard, event type 100 meters: record is 10.62 seconds.
     Women's Standard, event type 200 meters: record is 21.34 seconds.
     Women's Standard, event type 400 meters: record is 48.25 seconds.
     Return -1 for any other value
     """

     time = 0.0

     if gender == "men":
          if event == 100:
               time += 9.63
          elif event == 200:
               time += 19.30
          elif event == 400:
               time += 43.03
          else:
               time -= 1
     elif gender == "women":
          if event == 100:
               time += 10.62
          elif event == 200:
               time += 21.34
          elif event == 400:
               time += 48.25
          else:
               time -= 1
     else:
          time -= 1
          
     return(time)

def main():
     z = input('Enter the gender: ').lower()
     t = int(input('Enter the event distance: '))
     record = worldRecord(z,t)
     print("The record for "+z+" 's "+ str(t) + " meters is", record)

#Allow script to be run directly:
if __name__ == "__main__":
     main()
