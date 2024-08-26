import streamlit as st

# Función para mostrar información del autor
def mostrar_acerca_del_autor(foto, nombre, grado, reseña, correo):
    st.image(foto, width=150)
    st.subheader(nombre)
    st.write(f"**Grado:** {grado}")
    st.write(reseña)
    st.write(f"**Correo:** {correo}")

# Función para mostrar información sobre la plática
def mostrar_sobre_la_platica(resumen):
    st.subheader("Sobre la plática")
    st.write(resumen)

# Función para mostrar un enlace directo al PDF
def mostrar_diapositivas(enlace_pdf):
    st.subheader("Diapositivas")
    if enlace_pdf:
        st.markdown(f"[Haz clic aquí para ver las diapositivas]( {enlace_pdf})", unsafe_allow_html=True)
        st.markdown(f"![Ver diapositivas en PDF]({enlace_pdf})")
    else:
        st.write("No hay diapositivas disponibles para esta plática.")


dates = {
    "30 de agosto": "30 de agosto: Miguel Huerta",
    "06 de septiembre": "06 de septiembre: Mónica Ríos",
    "13 de septiembre": "13 de septiembre: Mariano, Julio y Minerva",
    "20 de septiembre": "20 de septiembre: Daniela Rios y Victoria García y Julián",
    "27 de septiembre": "27 de septiembre: Julián",
    "04 de octubre": "04 de octubre: Fernanda y Cesar",
    "11 de octubre": "11 de octubre: Yoli y Mónica Ríos",
    "18 de octubre": "18 de octubre: Ricardo y Fernanda García",
    "25 de octubre": "25 de octubre: Liliana y Alondra",
    "08 de noviembre": "08 de noviembre: Paola García y Angie Del Toro",
    "15 de noviembre": "15 de noviembre: Xóchitl Trujillo",
    "22 de noviembre": "22 de noviembre: Santiago Arceo",
    "29 de noviembre": "29 de noviembre: Alberto Bricio y Ricardo Marentes y Valeria Ibarra"
}

# Página de ejemplo
def pagina_ejemplo():
    st.title("Evento: Creación y tipos de hipótesis")

    # Datos del autor
    foto = "DrHuerta.jpg"  # Cambia esta ruta a la imagen del autor
    nombre = "Miguel Huerta"
    grado = "PhD en Ciencias"
    reseña = ("Miguel Huerta es un experto en metodología de la investigación con más de 10 años de experiencia "
               "en la enseñanza de técnicas científicas. Ha colaborado en múltiples proyectos de investigación "
               "y publicado numerosos artículos en revistas indexadas.")
    correo = "miguel.huerta@example.com"
    
    # Mostrar sección "Acerca del autor"
    mostrar_acerca_del_autor(foto, nombre, grado, reseña, correo)
    
    # Información sobre la plática
    resumen_platica = ("Esta plática abordará la creación y tipos de hipótesis en la investigación científica, "
                       "explorando las diferencias entre hipótesis nulas y alternativas, y cómo formularlas correctamente.")
    
    # Mostrar sección "Sobre la plática"
    mostrar_sobre_la_platica(resumen_platica)
    
    # Enlace directo al PDF
    enlace_pdf = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/asp.pdf"  # Reemplaza con el enlace directo al PDF
    mostrar_diapositivas(enlace_pdf)

# Página principal
def main():
    if "page" not in st.session_state:
        st.session_state.page = "Inicio"
    
    st.sidebar.title("Calendario de Eventos Académicos")
    page = st.sidebar.selectbox(
        "Selecciona una fecha para ver más detalles:",
        [
            "Inicio",
            "30 de agosto: Miguel Huerta",
            "06 de septiembre: Mónica Ríos",
            "13 de septiembre: Mariano, Julio y Minerva",
            "20 de septiembre: Daniela Rios y Victoria García y Julián",
            "27 de septiembre: Julián",
            "04 de octubre: Fernanda y Cesar",
            "11 de octubre: Yoli y Mónica Ríos",
            "18 de octubre: Ricardo y Fernanda García",
            "25 de octubre: Liliana y Alondra",
            "08 de noviembre: Paola García y Angie Del Toro",
            "15 de noviembre: Xóchitl Trujillo",
            "22 de noviembre: Santiago Arceo",
            "29 de noviembre: Alberto Bricio y Ricardo Marentes y Valeria Ibarra",
        ],
        index=["Inicio", "30 de agosto: Miguel Huerta", "06 de septiembre: Mónica Ríos", "13 de septiembre: Mariano, Julio y Minerva",
               "20 de septiembre: Daniela Rios y Victoria García y Julián", "27 de septiembre: Julián", "04 de octubre: Fernanda y Cesar",
               "11 de octubre: Yoli y Mónica Ríos", "18 de octubre: Ricardo y Fernanda García", "25 de octubre: Liliana y Alondra",
               "08 de noviembre: Paola García y Angie Del Toro", "15 de noviembre: Xóchitl Trujillo", "22 de noviembre: Santiago Arceo",
               "29 de noviembre: Alberto Bricio y Ricardo Marentes y Valeria Ibarra"].index(st.session_state.page)
    )
    
    if page == "Inicio":
        st.session_state.page = "Inicio"
        st.title("Calendario de Eventos Académicos")
        st.write("Haz clic en una fecha para ver más detalles sobre el evento.")
        # Mostrar el calendario de eventos con enlaces
        for date, event in dates.items():
            if st.button(date):
                st.session_state.page = event
                st.experimental_rerun()
    elif page == "30 de agosto: Miguel Huerta":
        st.session_state.page = "30 de agosto: Miguel Huerta"
        pagina_ejemplo()
    # Añadirás funciones similares para cada una de las fechas/eventos

if __name__ == "__main__":
    main()
