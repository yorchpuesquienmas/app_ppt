import random
import streamlit as st

# Definimos las opciones de los jugadores:
opciones = ["Piedra", "Papel", "Tijeras"]

# Cargar Imágenes:
tijeras = 'tijeras.jpeg'
piedra = 'piedra.jpeg'
papel = 'papel.jpeg'

# Creamos las funciones que definen las reglas de juego de Piedra, Papel o Tijera:
@st.cache
def ganador(opcion_j1, opcion_j2):
    if (opcion_j1 == "Piedra" and opcion_j2 == "Tijeras") or \
        (opcion_j1 == "Tijeras" and opcion_j2 == "Papel") or \
        (opcion_j1 == "Papel" and opcion_j2 == "Piedra"):
        print(opcion_j1, "vs", opcion_j2)
        return "Gana Jugador 1"
    elif opcion_j1 == opcion_j2:
        print(opcion_j1, "vs", opcion_j2)
        return "Empatan"
    else:
        print(opcion_j1, "vs", opcion_j2)
        return "Gana Jugador 2"
    
# Estructura de la Aplicación:
# Agregamos un título:
st.title('Bienvenidos al juego de Piedra, Papel o Tijeras')
# Agregamos la instrucción para el usuario:
st.write('Selecciona una de las opciones para jugar contra el computador:') 
# Menú de seleccción para el usuario:
opcion_j1 = st.selectbox('Selecciona una:', opciones)
if opcion_j1 == "Tijeras":
    st.image(tijeras, use_column_width = False, width = 200)
elif opcion_j1 == "Papel":
    st.image(papel, use_column_width = False, width = 200)
elif opcion_j1 == "Piedra":
    st.image(piedra, use_column_width = False, width = 200)
    
# Selección del adversario:
opcion_j2 = random.choice(opciones)
st.write("Selección de tu adversario:")
st.write(opcion_j2) # Nos muestra en pantalla la elección del adversario
if opcion_j2 == "Tijeras":
    st.image(tijeras, use_column_width = False, width = 200)
elif opcion_j2 == "Papel":
    st.image(papel, use_column_width = False, width = 200)
elif opcion_j2 == "Piedra":
    st.image(piedra, use_column_width = False, width = 200)


# Obtenemos el resultado del juego:
st.header("Resultado del juego:")
st.write(ganador(opcion_j1, opcion_j2))

