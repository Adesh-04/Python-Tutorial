def add_time(x,y):
    hrs1 = x[0:2]
    min1 = x[3:5]
    T1=x[5:]
    days=0
    if hrs1=="12":
        if T1 =="am":
            hrs1="00" 
    
    hrs2 = y[0:2]
    min2 = y[3:]  
    T_hrs = int(hrs1)+int(hrs2)
    T_min = int(min1)+int(min2)
    while T_min>60:
        T_hrs+=1
        T_min=T_min-60
    while T_hrs>24:
        T_hrs=T_hrs-24
        days+=1
    if 0<=T_hrs<=12:
        T1="am"
    if T_hrs>12:
        T1="pm"
    while T_hrs>12:
        T_hrs=T_hrs-12
    print(T_hrs,":",T_min,T1,"(",days,"days )")
    
    #Format of x :  HH:MM pm/am
    #Format of y :  HH:MM
add_time("01:02 am","01:12")