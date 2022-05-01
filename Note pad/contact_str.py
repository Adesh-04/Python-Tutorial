phone_dict= {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "0":"zero",
}

contact = int(input("Phone: "))
n = str(contact)

for i in range(0,len(n)):
    print(phone_dict[n[i]] , sep="" , end=" " )

print(" ")