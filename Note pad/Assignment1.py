def Arithmatic_arranger():
    main=[]
    i=0
    print ("\t \n \t Welcome\n")
    a11=int(input("Expression counts:"))
    print ("Only Addition and subtraction")
    print ("Use \" for Expressions" )
    int(a11)
    while a11>0:
        a12=input("Enter:")
        str(a12)
        main.append(a12)
        a11-=1
        i+=1
        if a11==0:
            break
    ii=0
    while i>0:
        
        x=main[ii]
        i1=0
        list1=[]
        list2=[]
        i2=0
        i3=1
        i4=0
        while i1>=0:
            q=x[i1]
            if q== "-":
                break
            if q== "+":
                break;  
            list1.append(x[i1])
            i1+=1
        str1=""
        for i2 in list1:
            str1+=i2
        print ("{:>10}".format(str1))
        while i3>0:
            q1=x[-i3]
            if q1=="-":
                break;
            if q1=="+":
                break;
            list2.append(x[-i3])
            i3+=1
        str2=""
        for i4 in reversed(list2):
            str2+=i4
        if q=="+":
            print ("+","{:>8}".format(str2))
        if q=="-":
            print ("-","{:>8}".format(str2))
        print ("-"*10)
        if q=="+":
            sum1=int(str1)+int(str2)
            print ("{:>10}".format(sum1),"\n")
        if q=="-":
            sub1=int(str1)-int(str2)
            print ("{:>10}".format(sub1),"\n")
        ii+=1
        if ii == i:
            break
Arithmatic_arranger()