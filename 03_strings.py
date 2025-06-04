# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=8643

### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo

nombre, apellido, edad = "David", "Gautos", 17
print("Mi nombre es {} {} y mi edad es {}".format(nombre, apellido, edad))
print("Mi nombre es %s %s y mi edad es %d" % (nombre, apellido, edad))
print("Mi nombre es " + nombre + " " + apellido + " y mi edad es " + str(edad))
print(f"Mi nombre es {nombre} {apellido} y mi edad es {edad}")

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(d)
print(f)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones del lenguaje

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("7".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("ta" == "ta")  # No es lo mismo
