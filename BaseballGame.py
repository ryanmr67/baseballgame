def StartMessage():
    print("Hello My Fellow PO")
    print("Would You Like To Indulge In The PO Lifestyle")
    return input ("Are You Ready To Start Your PO Journey? (Yes/No)")




def StartGame():
    if StartMessage() == "yes":
        Print("Lets Get In The Weight Room")
    else: 
        Print("Go Back To Hitting You Scrub")
StartMessage()
StartGame()