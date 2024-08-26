import streamlit as st
from fpdf import FPDF
import base64

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
    else:
        st.write("No hay diapositivas disponibles para esta plática.")

# Función para generar un PDF con la información de la página
def generar_pdf(foto, nombre, grado, reseña, correo, resumen_platica, enlace_pdf):
    pdf = FPDF()
    pdf.add_page()

    # Título
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt="Evento: Creación y tipos de hipótesis", ln=True, align='C')

    # Acerca del autor
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt="Acerca del autor", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, f"Nombre: {nombre}\nGrado: {grado}\nReseña: {reseña}\nCorreo: {correo}")

    # Sobre la plática
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt="Sobre la plática", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, resumen_platica)

    # Enlace al PDF de diapositivas
    if enlace_pdf:
        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, txt="Diapositivas", ln=True)
        pdf.set_font("Arial", "", 12)
        pdf.cell(200, 10, txt=f"Ver diapositivas en: {enlace_pdf}", ln=True, link=enlace_pdf)

    return pdf.output(dest="S").encode("latin1")

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
    
    # Botón para generar y descargar el PDF
    pdf = generar_pdf(foto, nombre, grado, reseña, correo, resumen_platica, enlace_pdf)
    st.download_button(
        label="Descargar PDF con los datos del evento",
        data=pdf,
        file_name="evento_30_agosto.pdf",
        mime="application/pdf",
    )

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
        # Mostrar el calendario de eventos con botones
        for date, event in dates.items():
            if st.button(date):
                st.session_state.page = event
    elif st.session_state.page == "30 de agosto: Miguel Huerta":
        pagina_ejemplo()
    # Aquí añadirás funciones similares para cada una de las fechas/eventos

if __name__ == "__main__":
    main()
