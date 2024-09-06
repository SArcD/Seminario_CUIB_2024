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
    "26 de abril: Santiago Arceo": "26 de abril: Santiago Arceo",
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

from fpdf import FPDF
import requests
from PIL import Image
from io import BytesIO

def generar_pdf(foto_url, nombre, grado, reseña, correo, perfil_scholar, resumen_platica, enlace_pdf):
    # Crear el PDF
    pdf = FPDF()
    pdf.add_page()

    # Título en negritas
    pdf.set_font("Times", "B", 16)
    pdf.cell(200, 10, txt="Evento: Creación y tipos de hipótesis", ln=True, align='C')

    pdf.ln(10)  # Añadir un espacio vertical después del título

    # Acerca del autor en negritas
    pdf.set_font("Times", "B", 14)
    pdf.cell(200, 10, txt="Acerca del autor", ln=True)
    
    # Añadir la imagen del autor desde la URL
    response = requests.get(foto_url)
    img = Image.open(BytesIO(response.content))
    img.save("temp_image.jpg")  # Guardar temporalmente para usarla en FPDF
    
    pdf.image("temp_image.jpg", x=10, y=pdf.get_y() + 5, w=30)  
    pdf.set_xy(55, pdf.get_y())  # Posicionar el texto al lado de la imagen

    # Texto al lado de la imagen
    pdf.set_font("Times", "", 14)  # Texto normal
    pdf.multi_cell(0, 10, f"Nombre: {nombre}\nGrado: {grado}\nReseña: {reseña}\nCorreo: {correo}\nPerfil: {perfil_scholar}")

    # Asegurarse de que el contenido siguiente no se superponga con la imagen
    current_y = max(pdf.get_y(), 70)  # Asegúrate de que el texto no suba por encima de la imagen
    pdf.set_y(current_y + 10)  # Añadir un espacio vertical después de la imagen y texto

    # Sobre la plática en negritas
    pdf.set_font("Times", "B", 14)
    pdf.cell(200, 10, txt="Sobre la plática", ln=True)
    
    # Resumen de la plática
    pdf.set_font("Times", "", 14)  # Texto normal
    pdf.multi_cell(0, 10, resumen_platica)

    pdf.ln(10)  # Añadir un espacio vertical después de la sección "Sobre la plática"

    # Enlace al PDF de diapositivas en negritas
    if enlace_pdf:
        pdf.set_font("Times", "B", 14)
        pdf.cell(200, 10, txt="Diapositivas", ln=True)
        pdf.set_font("Times", "", 12)  # Texto del enlace normal
        pdf.cell(200, 10, txt=f"Ver diapositivas en: {enlace_pdf}", ln=True, link=enlace_pdf)

    # Descargar la imagen de la cintilla desde GitHub y agregarla en la parte inferior
    cintilla_url = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/udec.png"  # URL de la imagen
    response = requests.get(cintilla_url)
    cintilla_img = Image.open(BytesIO(response.content))
    cintilla_img.save("temp_cintilla.png")  # Guardar temporalmente la imagen de la cintilla
    
    # Añadir la cintilla (imagen) centrada en la parte inferior
    image_width = 75  # Ancho de la imagen cintilla (ajústalo si es necesario)
    pdf_width = 210
    x_position = (pdf_width - image_width) / 2  # Centrar la imagen
    y_position = 280  # Posición en la parte inferior, ajustada para la altura de la imagen

    pdf.image("temp_cintilla.png", x=x_position, y=y_position, w=image_width)

    return pdf.output(dest="S").encode("latin1")




# Página de ejemplo
def pagina_ejemplo():
    st.title("Evento: Creación y tipos de hipótesis")

    # Datos del autor
    foto = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/DrHuerta.jpg"
    #foto = "DrHuerta.jpg"  # Cambia esta ruta a la imagen del autor
    nombre = "Miguel Huerta"
    grado = "PhD en Ciencias"
    reseña = "Miguel Huerta Doctor en Ciencias con especialidad en Fisiología y Biofísica Es Profesor-Investigador Titular C del Centro Universitario de Investigaciones Biomédicas de la Universidad de Colima. Es miembro del Sistema Nacional de Investigadores en el nivel 3 emérito. Su campo de investigación es la Biomedicina, con énfasis en la fisiología y biofísica del sistema neuromuscular y la fisiopatología de la diabetes mellitus. Ha publicado más de cien artículos revistas indizadas al Journal of Citation Reports y ha graduado a más de 40 Maestros y Doctores en Ciencias en programas SNP-CONAHCyT."
    #st.markdown(f"<p style='text-align: justify;'>{reseña}</p>", unsafe_allow_html=True)
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



def veintiseis_abril():
    st.title("Evento:  Aplicación de la Inteligencia Artificial y Conjuntos Rugosos de Participantes Geriátricos en las ENASEM 2018 y 2021: Modelos para el Cálculo de Riesgo de Sarcopenia")

    # Datos del autor
    foto = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/ArceoS.jpg"

    #foto = "ArceoS.jpg"  # Cambia esta ruta a la imagen del autor
    nombre = "Santiago Arceo Díaz"
    grado = "Dr. Ciencias (Astrofísica)"
    reseña = "Licenciatura y Maestría en Física y Doctor en Ciencias (Astrofísica), por las Universidades de Colima y Guanajuato, respectivamente. En su formación académica se especializó en la creación de modelos analíticos y numéricos, aplicados a las ciencias exactas y a la ingeniería aplicada. Dentro de la astrofísica, su área de investigación se centra en la evolución estelar y su relación con la tasa de producción de neutrinos y axiones, concretamente las estrellas gigantes rojas. También ha realizado trabajos en múltiples áreas de la ingeniería y la arquitectura (con simulaciones numéricas aplicadas a la sostenibilidad ambiental de las que se han realizado 6 tesis de maestría). Se encuentra realizando una estancia postdoctoral en la Universidad de Colima en la que se enfoca en el uso del machine learning para la clasificación de pacientes geriátricos, a partir de variables antropométricas."
    #st.markdown(f"<p style='text-align: justify;'>{reseña}</p>", unsafe_allow_html=True)
    correo = "santiagoarceo@ucol.mx"
    perfil_scholar = "https://scholar.google.com.mx/citations?user=SFgL-gkAAAAJ&hl=en"
    
    # Mostrar sección "Acerca del autor"
    mostrar_acerca_del_autor(foto, nombre, grado, reseña, correo, perfil_scholar)
    
    # Información sobre la plática
    resumen_platica = ("Se aborda el uso de inteligencia artificial y la teoría de conjuntos rugosos para evaluar el riesgo de sarcopenia en adultos mayores mexicanos, utilizando datos de las encuestas ENASEM 2018 y 2021. Se utilizaron conjuntos rugosos y árboles de decisión para clasificar y evaluar el riesgo de sarcopenia, basándose en variables como fuerza, caídas, y movilidad. Se analizaron subconjuntos de pacientes con respuestas idénticas, permitiendo extraer perfiles de riesgo. Los modelos permitieron clasificar pacientes con distintos niveles de riesgo de sarcopenia, mostrando una mayor prevalencia de riesgo en mujeres y en pacientes con hipertensión y diabetes. La clasificación mediante inteligencia artificial y conjuntos rugosos es efectiva para evaluar el riesgo de sarcopenia, incluso sin medidas antropométricas directas. Se observaron diferencias significativas en el riesgo entre hombres y mujeres, y la presencia de comorbilidades como hipertensión y diabetes aumenta el riesgo.")
    
    # Mostrar sección "Sobre la plática"
    mostrar_sobre_la_platica(resumen_platica)
    
    # Enlace directo al PDF
    enlace_pdf = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/seminario_26_abril_2024.pdf"  # Reemplaza con el enlace directo al PDF
    mostrar_diapositivas(enlace_pdf)
    
    # Botón para generar y descargar el PDF
    pdf = generar_pdf(foto, nombre, grado, reseña, correo, perfil_scholar, resumen_platica, enlace_pdf)
    st.download_button(
        label="Descargar PDF con los datos del evento",
        data=pdf,
        file_name="evento_24_abril.pdf",
        mime="application/pdf",
    )
    
    # Sección "Preguntas Clave"
    st.subheader("Preguntas Clave")
    st.write("""
    1. ¿Cómo cambiará la proporción de adultos mayores en México hacia el año 2050, y cuáles serán las consecuencias para la salud pública?
    2. ¿Cuál es la prevalencia de sarcopenia en las poblaciones de adultos mayores en México y cómo varía entre diferentes grupos (sin comorbilidades, con diabetes, con hipertensión, etc.)?
    3. ¿Cómo se utiliza la teoría de conjuntos rugosos y la inteligencia artificial para clasificar y evaluar el riesgo de sarcopenia en adultos mayores?
    4. ¿Cuáles son las preguntas o variables críticas en la ENASEM que se utilizan para evaluar el riesgo de sarcopenia (por ejemplo, fuerza de presión, caídas, movilidad)?
    5. ¿Cómo influyen las comorbilidades como la hipertensión y la diabetes en el riesgo de sarcopenia en adultos mayores?
    6. ¿Existen diferencias significativas en el riesgo de sarcopenia entre hombres y mujeres?
    7. ¿Cómo se pueden utilizar los modelos desarrollados para mejorar la detección y gestión de la sarcopenia en el ámbito clínico?
    8. ¿Qué revelan los datos de las encuestas ENASEM 2018 y 2021 sobre la distribución del riesgo de sarcopenia en la población mexicana mayor de 60 años?
    """)


def seis_de_septiembre():
    st.title("Evento: El arte de las presentaciones científicas: pasos críticos para tener éxito y errores críticos para evitar")

    # Datos del autor
    #foto = "rios.jpg"  # Cambia esta ruta a la imagen del autor
    foto = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/rios.jpg"

    nombre = "Mónica Ríos Silva"
    grado = "Dra. Ciencias Médicas"
    reseña = "Médica cirujana y partera con especialidad en Medicina Interna y Doctorado en Ciencias Médicas por la Universidad de Colima, médica especialista del Hospital Materno Infantil de Colima y PTC de la Facultad de Medicina de la Universidad de Colima. Es profesora de los posgrados en Ciencias Médicas, Ciencias Fisiológicas, Nutrición clínica y Ciencia ambiental global. Cuenta con 42 artículos científicos en revistas con factor de impacto con más de 400 citas, desde 2019 revisora de artículos en revistas internacionales con factor de impacto mayor de 1, asesoría de 31 tesis de especialidades médicas y de maestría y doctorado en la Universidad de Colima y la Universidad de Aguascalientes. Colaboraciones de investigación: en el Centro de Investigaciones Biomédicas de Occidente y las unidades estatales del Instituto Mexicano del Seguro Social así como con la Universidad Michoacana de San Nicolás de Hidalgo. Miembro del Sistema Nacional de Investigadores Nivel II."
    #st.markdown(f"<p style='text-align: justify;'>{reseña}</p>", unsafe_allow_html=True)
    correo = "mrios@ucol.mx"
    perfil_scholar = "https://scholar.google.com.mx/citations?hl=en&user=5mgGr3kAAAAJ"
    
    # Mostrar sección "Acerca del autor"
    mostrar_acerca_del_autor(foto, nombre, grado, reseña, correo, perfil_scholar)
    
    # Información sobre la plática
    resumen_platica = ("Te invitamos al seminario El arte de las presentaciones científicas, donde aprenderás los aspectos clave para desarrollar presentaciones efectivas y profesionales. Basado en la obra de Michael Alley, este seminario cubrirá cuatro pilares esenciales: el discurso, la estructura, las ayudas visuales y la entrega. Descubre cómo hacer tu discurso ameno utilizando ejemplos y analogías, cómo organizar tus ideas de manera lógica con transiciones claras, y cómo diseñar ayudas visuales que refuercen tu mensaje sin sobrecargar a la audiencia. Además, aprenderás a controlar los nervios, mantener la atención del público y anticipar problemas técnicos siguiendo la Ley de Murphy.")
    
    # Mostrar sección "Sobre la plática"
    mostrar_sobre_la_platica(resumen_platica)
    
    # Enlace directo al PDF
    enlace_pdf = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/El%20arte%20de%20las%20presentaciones%20cient%C3%ADficas310824_pdf.pdf"  # Reemplaza con el enlace directo al PDF
    mostrar_diapositivas(enlace_pdf)
    
    # Botón para generar y descargar el PDF
    pdf = generar_pdf(foto, nombre, grado, reseña, correo, perfil_scholar, resumen_platica, enlace_pdf)
    st.download_button(
        label="Descargar PDF con los datos del evento",
        data=pdf,
        file_name="evento_24_abril.pdf",
        mime="application/pdf",
    )
    
    # Sección "Preguntas Clave"
    st.subheader("Preguntas Clave")
    st.write("""
.
    """)



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
    elif selected_page == "26 de abril: Santiago Arceo":
        veintiseis_abril()
    elif selected_page == "06 de septiembre: Mónica Ríos":
        seis_de_septiembre()
    # Aquí añadirás funciones similares para cada una de las fechas/eventos

if __name__ == "__main__":
    main()
