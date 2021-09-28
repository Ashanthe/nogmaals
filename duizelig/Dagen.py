dag = input("Welke dag kiest u? ")
welkedag = ""

while dag != welkedag:
    if welkedag == "maandag":
        welkedag = "dinsdag"
    elif welkedag == "dinsdag":
        welkedag = "woensdag"
    elif welkedag == "woensdag":
        welkedag= "donderdag"
    elif welkedag == "donderdag":
        welkedag = "vrijdag"
    elif welkedag == "vrijdag":
        welkedag = "zaterdag"
    elif welkedag == "zaterdag":
        welkedag = "zondag"
    else: welkedag = "maandag"

    print(welkedag)



  



    


