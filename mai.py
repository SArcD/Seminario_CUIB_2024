import streamlit as st
from fpdf import FPDF

# Función para mostrar información del autor
def mostrar_acerca_del_autor(foto, nombre, grado, reseña, correo, perfil_scholar):
    st.image(foto, width=150)
    st.subheader(nombre)
    st.write(f"**Grado:** {grado}")
    st.write(reseña)
    st.write(f"**Correo:** {correo}")
    st.write(f"**Perfil:** [Google Scholar]({perfil_scholar})")

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

dates = {
    "Inicio": "Inicio",
    "30 de agosto: Miguel Huerta": "30 de agosto: Miguel Huerta",
    "06 de septiembre: Mónica Ríos": "06 de septiembre: Mónica Ríos",
    "13 de septiembre: Mariano, Julio y Minerva": "13 de septiembre: Mariano, Julio y Minerva",
    "20 de septiembre: Daniela Rios y Victoria García y Julián": "20 de septiembre: Daniela Rios y Victoria García y Julián",
    "27 de septiembre: Julián": "27 de septiembre: Julián",
    "04 de octubre: Fernanda y Cesar": "04 de octubre: Fernanda y Cesar",
    "11 de octubre: Yoli y Mónica Ríos": "11 de octubre: Yoli y Mónica Ríos",
    "18 de octubre: Ricardo y Fernanda García": "18 de octubre: Ricardo y Fernanda García",
    "25 de octubre: Liliana y Alondra": "25 de octubre: Liliana y Alondra",
    "08 de noviembre: Paola García y Angie Del Toro": "08 de noviembre: Paola García y Angie Del Toro",
    "15 de noviembre: Xóchitl Trujillo": "15 de noviembre: Xóchitl Trujillo",
    "22 de noviembre: Santiago Arceo": "22 de noviembre: Santiago Arceo",
    "29 de noviembre: Alberto Bricio y Ricardo Marentes y Valeria Ibarra": "29 de noviembre: Alberto Bricio y Ricardo Marentes y Valeria Ibarra"
}

# Función para generar un PDF con la información de la página
def generar_pdf(foto, nombre, grado, reseña, correo, perfil_scholar, resumen_platica, enlace_pdf):
    pdf = FPDF()
    pdf.add_page()

    # Título
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt="Evento: Creación y tipos de hipótesis", ln=True, align='C')

    pdf.ln(10)  # Añadir un espacio vertical después del título

    # Acerca del autor
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt="Acerca del autor", ln=True)
    pdf.image(foto, x=10, y=40, w=30)  # Añadir la imagen del autor
    pdf.set_xy(55, 30)  # Posicionar el texto al lado de la imagen
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, f"Nombre: {nombre}\nGrado: {grado}\nReseña: {reseña}\nCorreo: {correo}\nPerfil: {perfil_scholar}")

    pdf.ln(10)  # Añadir un espacio vertical después de la sección "Acerca del autor"

    # Sobre la plática
    pdf.set_y(170)  # Ajustar la posición para empezar después de la imagen y texto
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt="Sobre la plática", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, resumen_platica)

    pdf.ln(10)  # Añadir un espacio vertical después de la sección "Sobre la plática"

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
    reseña = ("Miguel Huerta Doctor en Ciencias con especialidad en Fisiología y Biofísica. "
              "Es Profesor-Investigador Titular C del Centro Universitario de Investigaciones Biomédicas "
              "de la Universidad de Colima. Es miembro del Sistema Nacional de Investigadores en el nivel 3 emérito. "
              "Su campo de investigación es la Biomedicina, con énfasis en la fisiología y biofísica del sistema neuromuscular "
              "y la fisiopatología de la diabetes mellitus. Ha publicado más de cien artículos revistas indizadas al Journal "
              "of Citation Reports y ha graduado a más de 40 Maestros y Doctores en Ciencias en programas SNP-CONAHCyT.")
    correo = "huertam@ucol.mx"
    perfil_scholar = "https://scholar.google.com.mx/citations?user=7jGGpnoAAAAJ&hl=en&oi=ao"
    
    # Mostrar sección "Acerca del autor"
    mostrar_acerca_del_autor(foto, nombre, grado, reseña, correo, perfil_scholar)
    
    # Información sobre la plática
    resumen_platica = ("Esta plática abordará la creación y tipos de hipótesis en la investigación científica, "
                       "explorando las diferencias entre hipótesis nulas y alternativas, y cómo formularlas correctamente.")
    
    # Mostrar sección "Sobre la plática"
    mostrar_sobre_la_platica(resumen_platica)
    
    # Enlace directo al PDF
    enlace_pdf = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/asp.pdf"  # Reemplaza con el enlace directo al PDF
    mostrar_diapositivas(enlace_pdf)
    
    # Botón para generar y descargar el PDF
    pdf = generar_pdf(foto, nombre, grado, reseña, correo, perfil_scholar, resumen_platica, enlace_pdf)
    st.download_button(
        label="Descargar PDF con los datos del evento",
        data=pdf,
        file_name="evento_30_agosto.pdf",
        mime="application/pdf",
    )

# Página de inicio con el resumen
def pagina_inicio():
    st.title("Seminario del Centro de Investigaciones Biomédicas")
    
    st.write("""
    **Objetivo de las sesiones del seminario:**
    
    El seminario del Centro de Investigaciones Biomédicas de la Universidad de Colima tiene como objetivo fomentar la 
    actualización y el intercambio de conocimientos entre investigadores, profesores y estudiantes en temas de 
    relevancia científica. Durante las sesiones, se abordarán diversas áreas de la biomedicina con un enfoque en 
    la innovación y la colaboración interdisciplinaria. Estas sesiones son una oportunidad para que los participantes 
    presenten sus proyectos, discutan hallazgos recientes y establezcan redes de colaboración.
    """)

    st.write("""
    **Datos de contacto:**
    
    **Encargado:** Santiago Arceo Díaz  
    **Correo:** santiarceo@ucol.mx
    """)

# Página principal
def main():
    st.sidebar.title("Calendario de Eventos Académicos")
    
    # Usa un selectbox para seleccionar la página
    selected_page = st.sidebar.selectbox(
        "Selecciona una fecha para ver más detalles:",
        list(dates.keys())
    )
    
    # Lógica para mostrar la página seleccionada
    if selected_page == "Inicio":
        pagina_inicio()
    elif selected_page == "30 de agosto: Miguel Huerta":
        pagina_ejemplo()
    # Aquí añadirás funciones similares para cada una de las fechas/eventos

if __name__ == "__main__":
    main()
