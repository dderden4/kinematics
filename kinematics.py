import math

#Translational
def translational():
    var = input("What variable are you solving for? (displacement: x, initial velocity: vo, final velocity: v, acceleration: a, or time: t) ")
    
    #Displacement
    if (var == "x" or var == "displacement"):
        var2 = input("What variable do you not have the value of? (final velocity: v, acceleration: a, or time: t) ")
        #x=vo*t+0.5*a*t^2
        if (var2 == "v" or var2 == "final velocity"):
            op = float(tt())
            print("displacement = " + str(tvo()*op + 0.5*ta()*op**2) + " meters")
        #x=0.5(v+vo)*t
        elif (var2 == "a" or var2 == "acceleration"):
            op = float(tv() + tvo())
            print("displacement = " + str(0.5*op*tt()) + " meters")
        #x=(v^2-vo^2)/2*a
        elif (var2 == "t" or var2 == "time"):
            op = float(tv()**2-tvo()**2)
            op2 = float(2*ta())
            print("displacement = " + str(op/op2) + " meters")
        else:
            print("Error, please restart and input the correct variable or variable name.")
    #Initial Velocity        
    elif (var == "vo" or var == "initial velocity"):
        var2 = input("What variable do you not have the value of? (displacement: x, final velocity: v, acceleration: a, or time: t) ")
        #vo=v-a*t
        if (var2 == "x" or var2 == "displacement"):
            print("initial velocity = " + str(tv() - ta()*tt()) + " meters/second")
        #vo=(x-0.5*a*t)/t
        elif (var2 == "v" or var2 == "final velocity"):
            t = float(tt())
            op = float(tx()-0.5*ta()*t)
            print("initial velocity = " + str(op/t) + " meters/second")
        #vo=((2*x)/t)-v
        elif (var2 == "a" or var2 == "acceleration"):
            op = float(2*tx())
            op2 = float(op/tt())
            print("initial velocity = " + str(op2-tv()) + " meters/second")
        #vo=sqrt(v^2-(2*a*x))
        elif (var2 == "t" or var2 == "time"):
            op = float(tv()**2)
            op2 = float(2*ta()*tx())
            op3 = float(op-op2)
            if (op3 > 0):
                print("initial velocity = " + str(math.sqrt(op3)) + " meters/second")
            else:
                print("Error, your value under the square root sign is negative.")
        else:
            print("Error, please restart and input the correct variable or variable name.")
    #Final Velocity    
    elif (var == "v" or var == "final velocity"):
        var2 = input("What variable do you not have the value of? (displacement: x, acceleration: a, or time: t) ")
        #v=vo+a*t
        if (var2 == "x" or var2 == "displacement"):
            print("final velocity = " + str(tvo() + ta()*tt()) + " meters/second")
        #v=((2*x)/t)-vo
        elif (var2 == "a" or var2 == "acceleration"):
            op = float(2*tx())
            op2 = float(op/tt())
            print("final velocity = " + str(op2-tvo()) + " meters/second")
        #v=sqrt(vo^2+(2*a*x))
        elif (var2 == "t" or var2 == "time"):
            op = float(tvo()**2)
            op2 = float(2*ta()*tx())
            op3 = float(op+op2)
            if (op3 > 0):
                print("initial velocity = " + str(math.sqrt(op3)) + " meters/second")
            else:
                print("Error, your value under the square root sign is negative.")
        else:
            print("Error, please restart and input the correct variable or variable name.")
    #Acceleration
    elif (var == "a" or var == "acceleration"):
        var2 = input("What variable do you not have the value of? (displacement: x, final velocity: v, or time: t) ")
        #a=(v-vo)/t
        if (var2 == "x" or var2 == "displacement"):
            vv = float(tv() - tvo())
            print("acceleration = " + str(vv/tt()) + " meters/second^2")
        #a=(2(x-vo*t))/t^2
        elif (var2 == "v" or var2 == "final velocity"):
            t = float(tt())
            op = float(tx()-tvo()*t)
            op2 = float(2*op)
            print("acceleration = " + str(op2/t**2) + " meters/second^2")
        #a=(v^2-vo^2)/(2*x)
        elif (var2 == "t" or var2 == "time"):
            op = float(tv()**2-tvo()**2)
            op2 = float(2*tx())
            print("acceleration = " + str(op/op2) + " meters/second^2")
        else:
            print("Error, please restart and input the correct variable or variable name.")
    #Time        
    elif (var == "t" or var == "time"):
        var2 = input("What variable do you not have the value of? (displacement: x, final velocity: v, or acceleration: a) ")
        #t=(v-vo)/a
        if (var2 == "x" or var2 == "displacement"):
            vv = float(tv() - tvo())
            print("time = " + str(abs(vv/ta())) + " seconds")
        #t=quadratic formula (0.5*a*t^2+vo*t-x=0)
        elif (var2 == "v" or var2 == "final velocity"):
           a = float(0.5*ta())
           b = float(tvo())
           c = float(-tx())
           sq = float(math.sqrt(b**2-4*a*c))
           bo = float(2*a)
           main1 = float((-b+sq)/bo)
           main2 = float((-b-sq)/bo)
           if (main1 > 0 and main2 < 0):
               print("time = " + str(main1) + " seconds")
           elif (main1 < 0 and main2 > 0):
               print("time = " + str(main2) + " seconds")
           else:
                print("Error, both values are either positive and positive or negative and negative.")
        #t=(2x)/(v-vo)
        elif (var2 == "a" or var2 == "acceleration"):
            op = float(2*tx())
            op2 = float(tv() + tvo())
            print("time = " + str(abs(op/op2)) + " seconds")
        else:
            print("Error, please restart and input the correct variable or variable name.")
    else:
        print("Error, please restart and input the correct variable or variable name.")

#Rotational
def rotational():
    var = input("What variable are you solving for? (angle: th, initial angular velocity: wo, final angular velocity: w, angular acceleration: a, or time: t) ")
    
    #Angle
    if (var == "th" or var == "angle"):
        var2 = input("What variable do you not have the value of? (final angular velocity: w, angular acceleration: a, or time: t) ")
        #th=wo*t+0.5*a*t^2
        if (var2 == "w" or var2 == "final angular velocity"):
            op = float(rt())
            print("angle = " + str(rwo()*op + 0.5*ra()*op**2) + " radians")
        #th=0.5(w+wo)*t
        elif (var2 == "a" or var2 == "angular acceleration"):
            op = float(rw() + rwo())
            print("angle = " + str(0.5*op*rt()) + " radians")
        #th=(w^2-wo^2)/2*a
        elif (var2 == "t" or var2 == "time"):
            op = float(rw()**2-rwo()**2)
            op2 = float(2*ra())
            print("angle = " + str(op/op2) + " radians")
        else:
            print("Error, please restart and input the correct variable or variable name.")
    #Initial Angular Velocity        
    elif (var == "wo" or var == "initial angular velocity"):
        var2 = input("What variable do you not have the value of? (angle: th, final angular velocity: w, angular acceleration: a, or time: t) ")
        #wo=w-a*t
        if (var2 == "th" or var2 == "angle"):
            print("initial angular velocity = " + str(rw() - ra()*rt()) + " radians/second")
        #wo=(th-0.5*a*t)/t
        elif (var2 == "w" or var2 == "final angular velocity"):
            t = float(rt())
            op = float(rth()-0.5*ra()*t)
            print("initial angular velocity = " + str(op/t) + " radians/second")
        #wo=((2*th)/t)-w
        elif (var2 == "a" or var2 == "angular acceleration"):
            op = float(2*rth())
            op2 = float(op/rt())
            print("initial angular velocity = " + str(op2-rw()) + " radians/second")
        #wo=sqrt(w^2-(2*a*th))
        elif (var2 == "t" or var2 == "time"):
            op = float(rw()**2)
            op2 = float(2*ra()*rth())
            op3 = float(op-op2)
            if (op3 > 0):
                print("initial angular velocity = " + str(math.sqrt(op3)) + " radians/second")
            else:
                print("Error, your value under the square root sign is negative.")
        else:
            print("Error, please restart and input the correct variable or variable name.")
    #Final Angular Velocity    
    elif (var == "w" or var == "final angular velocity"):
        var2 = input("What variable do you not have the value of? (angle: th, angular acceleration: a, or time: t) ")
        #w=wo+a*t
        if (var2 == "th" or var2 == "angle"):
            print("final angular velocity = " + str(rwo() + ra()*rt()) + " radians/second")
        #w=((2*th)/t)-wo
        elif (var2 == "a" or var2 == "angular acceleration"):
            op = float(2*rth())
            op2 = float(op/rt())
            print("final angular velocity = " + str(op2-rwo()) + " radians/second")
        #w=sqrt(wo^2+(2*a*th))
        elif (var2 == "t" or var2 == "time"):
            op = float(rwo()**2)
            op2 = float(2*ra()*rth())
            op3 = float(op+op2)
            if (op3 > 0):
                print("initial angular velocity = " + str(math.sqrt(op3)) + " radians/second")
            else:
                print("Error, your value under the square root sign is negative.")
        else:
            print("Error, please restart and input the correct variable or variable name.")
    #Angular Acceleration
    elif (var == "a" or var == "angular acceleration"):
        var2 = input("What variable do you not have the value of? (angle: th, final angular velocity: w, or time: t) ")
        #a=(w-wo)/t
        if (var2 == "th" or var2 == "angle"):
            vv = float(rw() - rwo())
            print("angular acceleration = " + str(vv/rt()) + " radians/second^2")
        #a=(2(th-wo*t))/t^2
        elif (var2 == "w" or var2 == "final angular velocity"):
            t = float(rt())
            op = float(rth()-rwo()*t)
            op2 = float(2*op)
            print("angular acceleration = " + str(op2/t**2) + " radians/second^2")
        #a=(w^2-wo^2)/(2*th)
        elif (var2 == "t" or var2 == "time"):
            op = float(rw()**2-rwo()**2)
            op2 = float(2*rth())
            print("angular acceleration = " + str(op/op2) + " radians/second^2")
        else:
            print("Error, please restart and input the correct variable or variable name.")
    #Time        
    elif (var == "t" or var == "time"):
        var2 = input("What variable do you not have the value of? (angle: th, final angular velocity: w, or angular acceleration: a) ")
        #t=(w-wo)/a
        if (var2 == "th" or var2 == "angle"):
            vv = float(rw() - rwo())
            print("time = " + str(abs(vv/ra())) + " seconds")
        #t=quadratic formula (0.5*a*t^2+wo*t-th=0)
        elif (var2 == "w" or var2 == "final angular velocity"):
           a = float(0.5*ra())
           b = float(rwo())
           c = float(-rth())
           sq = float(math.sqrt(b**2-4*a*c))
           bo = float(2*a)
           main1 = float((-b+sq)/bo)
           main2 = float((-b-sq)/bo)
           if (main1 > 0 and main2 < 0):
               print("time = " + str(main1) + " seconds")
           elif (main1 < 0 and main2 > 0):
               print("time = " + str(main2) + " seconds")
           else:
                print("Error, both values are either positive and positive or negative and negative.")
        #t=(2th)/(w-wo)
        elif (var2 == "a" or var2 == "angular acceleration"):
            op = float(2*rth())
            op2 = float(rw() + rwo())
            print("time = " + str(abs(op/op2)) + " seconds")
        else:
            print("Error, please restart and input the correct variable or variable name.")
    else:
        print("Error, please restart and input the correct variable or variable name.")


#Translational variables
def tx():
    x = float(input("What is the value of the initial displacement in meters? "))
    return x

def tvo():
    vo = float(input("What is the value of the initial velocity in meters/second? "))
    return vo

def tv():
    v = float(input("What is the value of the final velocity in meters/second? "))
    return v
    
def ta():
    a = float(input("What is the value of the acceleration in meters/second^2? "))
    return a
    
def tt():
    t = float(input("What is the value of the time in seconds? "))
    if (t < 0):
      print("Time cannot be a negative value, please restart the program.")
    else:
     return t

#Rotational variables
def rth():
    th = float(input("What is the value of the angle in radians? "))
    return th

def rwo():
    wo = float(input("What is the value of the initial angular velocity in radians/second? "))
    return wo

def rw():
    w = float(input("What is the value of the final angular velocity in radians/second? "))
    return w
    
def ra():
    a = float(input("What is the value of the angular acceleration in radians/second^2? "))
    return a
    
def rt():
    t = float(input("What is the value of the time in seconds? "))
    if (t < 0):
      print("Time cannot be a negative value, please restart the program.")
    else:
     return t
    
#MAIN
count = 0
while count == 0:
  setE = input("Do you want to access the translational or rotational kinematic equations? (trasnlational: t or rotational: r) ")
  if (setE == "t" or setE == "translational"):
    translational()
    count += 1
  elif (setE == "r" or setE == "rotational"):
    rotational()
    count += 1
  else:
    print("Error, please restart and input t to access the translational equations or r to access the rotational equations.")

while count == 1:
  restart = input("Do you want to access the translational or rotational kinematic equations again? (yes: y or no: n) ")
  if (restart == "yes" or restart == "y"):
    setEE = input("Do you want to access the translational or rotational kinematic equations? (trasnlational: t or rotational: r) ")
    if (setEE == "t" or setEE == "translational"):
      translational()
    elif (setEE == "r" or setEE == "rotational"):
      rotational()
    else:
      print("Error, please restart and input t to access the translational equations or r to access the rotational equations.")
  elif (restart == "no" or restart == "n"):
    count += 1
    print("Code Complete.")
  else:
    print("Please only input yes: y or no: n")
