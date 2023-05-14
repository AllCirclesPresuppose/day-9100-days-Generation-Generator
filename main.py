print("Generation Generator!")
print("What generation are you a part of? Lets find out!")
print()
year = int(input("What year were you born? "))
if year > 2015:
    print("You're part of Generation Alpha!🤖")
elif year > 1995:
    print("You're part of Generation Z!📱")
elif year > 1981:
    print("You're part of the Millenials!💻")
elif year > 1964:
    print("You're part of Generation X!🖥️")
elif year > 1947:
    print("You're part of the Baby Boomers!🖳")
elif year > 1925:
    print("You're part of the Traditionalists!📝")
elif year < 1925:
    print("You're too old! why are you taking this!!📜")
