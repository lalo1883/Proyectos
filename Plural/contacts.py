
contacts = {
    "number" : 4,
    "students" : 
    [
        {"name":"Sara Holderness", "email":"sarah@example.com"},
        {"name":"Harr Potter", "email":"harry@example.com"},
        {"name":"Hermione Granger", "email":"hermione@example.com"},
        {"name":"Ron weasley", "email":"ron@example.com"},
    ]
}

for i in contacts["students"]:
    print("El correo es: ", i["email"])

for i in contacts["students"]:
    print(i["name"])  #Eres especifico en llamar una parte del diccionario