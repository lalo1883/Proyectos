current_movies = {
    "Avengers": "10:00am",
    "Grinch": "11:00am",
    "Batman": "12:00pm",
    "Space Jam": "3:00pm",
}

print("We're showing the following movies: ")

for key in current_movies:
    print(key)

movie = input("What movie would you like the showtime for?: ")

showtime = current_movies.get(movie)  #El diccionario Obtiene el valor del input movie y lo compara con sus keys 
print(movie)                          #Y cuando encuentra un match saca el valor (horario) y lo asigna a showtime
print(showtime)  #Si el input no hace match con alguna llave el valor es "None" 

if showtime == None:
    print("Requested movie isn't playing ")
else:
    print(movie, "is playing at:", showtime )