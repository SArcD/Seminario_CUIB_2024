import streamlit as st
from pdf2image import convert_from_path

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

# Función para mostrar diapositivas en PDF como imágenes
def mostrar_diapositivas(pdf_file):
    st.subheader("Diapositivas")
    if pdf_file:
        images = convert_from_path(pdf_file)
        for i, image in enumerate(images):
            st.image(image, caption=f'Diapositiva {i+1}', use_column_width=True)
    else:
        st.write("No hay diapositivas disponibles para esta plática.")

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
    
    # Mostrar diapositivas (en PDF como imágenes)
    pdf_file = "asp.pdf"   # Reemplaza con la ruta al archivo PDF de las diapositivas
    mostrar_diapositivas(pdf_file)

# Página principal
def main():
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
        ]
    )
    
    if page == "Inicio":
        st.title("Calendario de Eventos Académicos")
        st.write("Selecciona una fecha en la barra lateral para ver más detalles.")
    elif page == "30 de agosto: Miguel Huerta":
        pagina_ejemplo()
    # Aquí añadirás funciones similares para cada una de las fechas/eventos

if __name__ == "__main__":
    main()
