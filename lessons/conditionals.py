"""Checks light, if green, says go"""
""" .lower() makes whole input lowercase"""

light: str = input("What color if the light? "). lower()

if(light == "green" ):
    print("Go! ")
    print("Drive safe! Love, mom. ")
else:
   if(light != "red "):
       if(light == "yellow "):
           print("Slow down! ")
       else:
           print("Go report this to the authorities. ")
   else:
       print("Stop! ")
print("Don't look at your phone! ")