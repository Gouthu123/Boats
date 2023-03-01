import colorama
from colorama import Fore
from fractions import Fraction



direction_of_stream_towards_boat=input("enter direction of stream towards boat 'along' or 'against' or 'along and against': ").lower()
print("Direction of stream : "+direction_of_stream_towards_boat)
if direction_of_stream_towards_boat == "along":
    print(" you can find only one value by placing '?'")
    distance = input("enter distance: ")
    print("Distance : "+distance+" km")
    speed_of_boat = input("enter speed of boat: ")
    print("Speed of boat : "+speed_of_boat+" km/hr")
    speed_of_stream = input("enter speed of stream : ")
    print("Speed of stream : "+speed_of_stream+" km/hr")
    time = input("enter time : ")
    print("Time : "+time+" hr")
    if distance == "?":
        formula = "Time = Distance/(speed of boat+speed of stream)"
        print("if boat goes along the direction of stream : ")
        print(formula)
        speed_of_boat = Fraction(speed_of_boat)
        speed_of_stream = Fraction(speed_of_stream)
        time = Fraction(time)
        print("i.e Distance=(Speed of boat+speed of stream)*(Time)")
        total_distance = float(round((speed_of_boat+speed_of_stream)*(time), 2))
        if total_distance >= 0:
            print(" ")
            print(Fore.GREEN+"Distance : "+str(total_distance)+" km")
        else:
            print(Fore.RED+"Invalid details")
    elif time == "?":
        formula = "Time = Distance/(speed of boat+speed of stream)"
        print("if boat goes along the direction of stream : ")
        print(formula)
        speed_of_boat = Fraction(speed_of_boat)
        speed_of_stream = Fraction(speed_of_stream)
        distance = Fraction(distance)
        total_time = float(round(distance/(speed_of_boat+speed_of_stream),2))
        if total_time >= 0:
            print(" ")
            print(Fore.GREEN+"Time : "+str(total_time)+" hr")
        else:
            print(Fore.RED+"invalid details")
    elif speed_of_boat == "?":
        formula = "Time = Distance/(speed of boat+speed of stream)"
        print("if boat goes along the direction of stream : ")
        print(formula)
        time = Fraction(time)
        speed_of_stream = Fraction(speed_of_stream)
        distance = Fraction(distance)
        print("i.e speed of boat=(Distance/Time)-speed of boat")
        total_speed_of_boat = float(round((distance/time)-speed_of_stream, 2))
        if total_speed_of_boat >= 0:
            print(" ")
            print(Fore.GREEN+"Speed of boat : "+str(total_speed_of_boat)+" km/hr")
        else:
            print(Fore.RED+"Invalid details")
    elif speed_of_stream == "?":
        formula = "Time = Distance/(speed of boat+speed of stream)"
        print("if boat goes along the direction of stream : ")
        print(formula)
        time = Fraction(time)
        speed_of_boat = Fraction(speed_of_boat)
        distance = Fraction(distance)
        print("i.e speed of stream=(Distance/Time)-speed_of_stream")
        total_speed_of_stream = float(round((distance/time)-speed_of_boat, 2))
        if total_speed_of_stream >= 0:
            print(" ")
            print(Fore.GREEN+"Speed of stream : "+str(total_speed_of_stream)+" km/hr")
        else:
            print(Fore.RED + "Invalid details")

if direction_of_stream_towards_boat == "against":
    print(Fore.GREEN+" you can find only one value by placing '?'")
    distance = input("enter distance: ")
    print("Distance : "+distance+" km")
    speed_of_boat = input("enter speed of boat: ")
    print("Speed of boat : "+speed_of_boat+" km/hr")
    speed_of_stream = input("enter speed of stream : ")
    print("Speed of stream : "+speed_of_stream+" km/hr")
    time = input("enter time : ")
    print("Time : "+time+" hr")
    if distance == "?":
        formula = "Time = Distance/(speed of boat-speed of stream)"
        print("if boat goes against the direction of stream : ")
        print(formula)
        speed_of_boat = Fraction(speed_of_boat)
        speed_of_stream = Fraction(speed_of_stream)
        time = Fraction(time)
        print("i.e Distance=(Speed of boat+speed of stream)*(Time)")
        total_distance = float(round((speed_of_boat-speed_of_stream)*(time), 2))
        if total_distance >= 0:
            print(" ")
            print(Fore.GREEN+"Distance : "+str(total_distance)+" km")
        else:
            print(Fore.RED + "Invalid details")
    elif time == "?":
        formula="Time = Distance/(speed of boat-speed of stream)"
        print("if boat goes against the direction of stream : ")
        print(formula)
        speed_of_boat = Fraction(speed_of_boat)
        speed_of_stream = Fraction(speed_of_stream)
        distance = Fraction(distance)
        total_time = float(round(distance/(speed_of_boat-speed_of_stream), 2))
        if total_time >= 0:
            print(" ")
            print(Fore.GREEN+"Time : "+str(total_time)+" hr")
        else:
            print(Fore.RED + "Invalid details")
    elif speed_of_boat == "?":
        formula = "Time = Distance/(speed of boat-speed of stream)"
        print("if boat goes against the direction of stream : ")
        print(formula)
        time = Fraction(time)
        speed_of_stream = Fraction(speed_of_stream)
        distance = Fraction(distance)
        print("i.e speed of boat=(Distance/Time)-speed of boat")
        total_speed_of_boat = float(round((distance/time)+speed_of_stream, 2))
        if total_speed_of_boat >= 0:
            print(" ")
            print(Fore.GREEN+"Speed of boat : "+str(total_speed_of_boat)+" km/hr")
        else:
            print(Fore.RED + "Invalid details")
    elif speed_of_stream == "?":
        formula = "Time = Distance/(speed of boat-speed of stream)"
        print("if boat goes against the direction of stream : ")
        print(formula)
        time = Fraction(time)
        speed_of_boat = Fraction(speed_of_boat)
        distance = Fraction(distance)
        print("i.e speed of stream=(Distance/Time)-speed_of_stream")
        total_speed_of_stream = float(round((distance/time)+speed_of_boat, 2))
        if total_speed_of_stream >= 0:
            print(" ")
            print(Fore.GREEN+"Speed of stream : "+str(total_speed_of_stream)+" km/hr")
        else:
            print(Fore.RED + "Invalid details")
if direction_of_stream_towards_boat == "along and against" or direction_of_stream_towards_boat == "against and along":
    downstream_distance = input("Enter downstream distance : ")
    print("Downstream distance : "+downstream_distance+ " km")
    downstream_time = input("Enter downstream time : ")
    print("Downstream time : "+downstream_time+" hr")
    upstream_distance = input("Enter upstream distance :")
    print("Upstream Distance : "+upstream_distance+" km")
    upstream_time = input("enter upstream time: ")
    print("Upstream time : "+upstream_time+" hr")
    print("downstream speed=downstream distance/downstream time")
    downstream_speed = float(round((Fraction(downstream_distance)/Fraction(downstream_time)), 2))
    print("Downstream speed : "+str(downstream_speed)+" km/hr")
    print("upstream speed=upstream distance/upstream time")
    upstream_speed = float(round((Fraction(upstream_distance)/Fraction(upstream_time)), 2))
    print("Upstream speed : "+str(upstream_speed)+" km/hr")
    speed = input("Enter 'speed of boat' or 'speed of stream' or 'both':").lower()
    if speed == "speed of boat":
        print("Speed of boat=(downstream speed+upstream speed)/2")
        speed_of_boat = float(round((Fraction(downstream_speed)+Fraction(upstream_speed))/2, 2))
        if speed_of_boat >= 0:
            print(Fore.GREEN+"Speed of boat : "+str(speed_of_boat)+" km/hr")
        else:
            print(Fore.RED + "Invalid details")
    elif speed == "speed of stream":
        print("Speed of stream=(downstream speed-upstream speed)/2")
        speed_of_stream = float(round((Fraction(downstream_speed) - Fraction(upstream_speed)) / 2, 2))
        if speed_of_stream >= 0:
            print(Fore.GREEN+"Speed of stream : " + str(speed_of_stream) + " km/hr")
        else:
            print(Fore.RED + "Invalid details")
    elif speed == "both":
        print("Speed of boat=(downstream speed+upstream speed)/2")
        print("Speed of stream=(downstream speed-upstream speed)/2")
        speed_of_boat = float(round((Fraction(downstream_speed) + Fraction(upstream_speed)) / 2, 2))
        if speed_of_boat >= 0:
            print(Fore.GREEN+"Speed of boat : " + str(speed_of_boat) + " km/hr")
        else:
            print(Fore.RED + "Invalid details")
        speed_of_stream = float(round((Fraction(downstream_speed) - Fraction(upstream_speed)) / 2, 2))
        if speed_of_stream >= 0:
            print(Fore.GREEN+"Speed of stream : " + str(speed_of_stream) + " km/hr")
        else:
            print(Fore.RED + "Invalid details")




