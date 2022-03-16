def Addition(x,y):
    if x<0:
        print("INVALID")
    elif y<0:
        print("INVALID")
    else:
        if x<1000:
            if 99<x<=999:
                a=x%10 #last digit
                b=x-a
                b2=b/10
                c=b2%10 #middle digit
                d=b2-c
                d2=d/10 #1st digit
                print ("    ",d2,c,a)
            
            elif 9 <x<=99:
                a=x%10  #last digit
                b=x-a
                b2=b/10 #1st digit
                print ("      ",b2,a)
            elif 0 <=x<=9:
                a=x #1st digit
                print ("     ",a)
            else :
                print ("User input number value is big")
            
        print("+")
            
        q=x+y  
        
        if y<1000:             
            if 99<y<=999:
                p=y%10 #last digit
                o=y-p
                o1=o/10
                i=o1%10 #middle digit
                u=o1-i
                u1=u/10 #1st digit
                print ("    ",u1,i,p)
            elif 9 <y<=99: 
                p=y%10  #last digit
                o=y-p
                o1=o/10 #1st digit
                print ("      ",o1,p)
                                
            elif 0 <=y<=9:
                p=y #1st digit
                print ("     ",p)
            else :
                print ("User input number value is big")
                        
        print(" ______________")
                                        
        if q<10000:
            if 999<q<=9999:
                a1=q%10 #last digit
                b1=q-a1
                b3=b1/10
                c1=b3%10 # 2nd last digit
                d1=b3-c1
                d3=d1/10  
                e1=d3%10 #2nd digit
                f1=d3-e1
                f3=f1/10 #1st digit
                print( "  ",f3,e1,c1,a1)
            elif 99<q<=999:
                a1=q%10 #last digit
                b1=q-a1
                b3=b1/10
                c1=b3%10 #middle digit
                d1=b3-c1
                d3=d1/10 #1st digit
                print ("    ",d3,c1,a1)
            elif 9<q<=99:
                a1=q%10  #last digit
                b1=q-a1
                b3=b1/10 #1st digit
                print ("      ",b3,a1)       
            elif 0<=q<=9:
                a1=q
                print( "    ",a1)
Addition (209,563)
                                                        
            