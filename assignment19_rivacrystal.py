#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: September 29, 2021
#This program decides what kind of influencer you are

followers = int(input("Enter amount of social media followers:"))

if followers < 0:
    print("Your influencer tier is: Error")
elif followers < 1000:
    print("Your influencer tier is: Hyper Influencer")
elif followers < 10000:
    print("Your influencer tier is: Nano Influencer")
elif followers < 100000:
    print("Your influencer tier is: Micro Influencer")
elif followers < 500000:
    print("Your influencer tier is: Mid-Tier Influencer")
elif followers < 1000000:
    print("Your influencer tier is: Macro Influencer")
elif followers > 1000000:
    print("Your influencer tier is: Celebrity Influencer")
