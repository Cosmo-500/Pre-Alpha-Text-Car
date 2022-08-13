repetita_start = False
repetita_stop = False
while True:
    resposta = input(" >").upper()
    if resposta == "HELP":
        print("""
start - to start the car
stop - to stop the car
quit - to extit""")
    elif resposta == "START":
        if not repetita_start:
            print("Car started")
            repetita_start = True
            repetita_stop = False
        elif repetita_start == True:
            print("Car alright on")
    elif resposta == "STOP":
        if not repetita_stop:
            print("Car stopped")
            repetita_stop = True
            repetita_start = False
        elif repetita_stop == True:
            print("Car alright stopped")
    elif resposta == "QUIT":
        break
    else:
        print("I don't get the joke man")