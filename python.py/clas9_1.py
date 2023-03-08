# Pidiendo la lista de países al usuario
country_list = input("Ingresa una lista de países separados por comas: ")

# Convirtiendo la lista de texto en una lista de Python
country_list = country_list.split(',')

# Usando set para eliminar duplicados
unique_country_list = list(set(country_list))

# Ordenando la lista de países alfabéticamente
unique_country_list.sort()

# Mostrando la lista de países ordenados y sin duplicados
print("La lista de países es:", ", ".join(unique_country_list))