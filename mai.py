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

def generar_pdf(titulo, foto_url, nombre, grado, reseña, correo, perfil_scholar, resumen_platica, enlace_pdf):
    # Crear el PDF
    pdf = FPDF()
    pdf.add_page()

    # Título en negritas
    #pdf.set_font("Times", "B", 16)
    #pdf.cell(200, 10, txt=titulo, ln=True, align='C')
    #pdf.ln(10)  # Añadir un espacio vertical después del título


    # Título en negritas usando multi_cell para manejar títulos largos y centrados
    pdf.set_font("Times", "B", 16)
    page_width = pdf.w - 2 * pdf.l_margin  # Calcular el ancho de la página
    pdf.multi_cell(page_width, 10, txt=titulo, align='C')  # Utilizar multi_cell para que el título largo se ajuste y esté centrado

    pdf.ln(10)  # Añadir un espacio vertical después del título

    # Acerca del autor en negritas
    pdf.set_font("Times", "B", 14)
    pdf.cell(200, 10, txt="Acerca del autor", ln=True)

    # Añadir la imagen del autor desde la URL
    response = requests.get(foto_url)
    img = Image.open(BytesIO(response.content))
    img.save("temp_image.jpg")  # Guardar temporalmente para usarla en FPDF
    
    # Posicionar la imagen del autor y asegurarse de que el texto esté alineado después de la imagen
    img_height = 40  # Ajustar la altura de la imagen
    pdf.image("temp_image.jpg", x=10, y=pdf.get_y() + 5, w=30, h=img_height)  # Imagen de tamaño ajustado

    # Ajustar la posición para que el texto comience después de la imagen
    pdf.set_y(pdf.get_y() + img_height + 5)  # Añadir espacio debajo de la imagen

    # Lista de etiquetas y contenido
    informacion = [
        ("Nombre", nombre),
        ("Grado", grado),
        ("Reseña", reseña),
        ("Correo", correo),
        ("Perfil", perfil_scholar)
    ]

    # Imprimir etiquetas y contenido con negritas
    for etiqueta, contenido in informacion:
        pdf.set_font("Times", "B", 14)  # Negritas para la etiqueta
        pdf.cell(40, 10, f"{etiqueta}: ")  # Usar cell para la etiqueta
        pdf.set_font("Times", "", 14)  # Texto normal para el contenido
        pdf.multi_cell(0, 10, contenido)  # Usar multi_cell para el contenido que puede ser largo

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
        pdf.cell(40, 10, "Ver diapositivas: ", ln=False)
        pdf.set_font("Times", "", 12)  # Texto normal para el enlace
        # Crear un enlace clicable
        pdf.cell(0, 10, txt=enlace_pdf, ln=True, link=enlace_pdf)

    
    # Descargar la imagen de la cintilla desde GitHub y agregarla en la parte inferior
    cintilla_url = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/udec.png"  # URL de la imagen
    response = requests.get(cintilla_url)
    cintilla_img = Image.open(BytesIO(response.content))
    cintilla_img.save("temp_cintilla.png")  # Guardar temporalmente la imagen de la cintilla
    
    # Añadir la cintilla (imagen) centrada en la parte inferior
    image_width = 90  # Ancho de la imagen cintilla
    pdf_width = 210
    x_position = (pdf_width - image_width) / 2  # Centrar la imagen
    y_position = 270  # Posición en la parte inferior, ajustada para la altura de la imagen

    pdf.image("temp_cintilla.png", x=x_position, y=y_position, w=image_width)

    return pdf.output(dest="S").encode("latin1")

import streamlit as st

def pagina_ejemplo():
    titulo = "Evento: Creación y tipos de hipótesis"
    st.title(titulo)

    # Datos del autor
    foto = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/DrHuerta.jpg"
    nombre = "Miguel Huerta"
    grado = "PhD en Ciencias"
    
    reseña = ("Doctor en Ciencias con especialidad en Fisiología y Biofísica. Es Profesor-Investigador "
              "Titular C del Centro Universitario de Investigaciones Biomédicas de la Universidad de Colima. "
              "Es miembro del Sistema Nacional de Investigadores en el nivel 3 emérito. Su campo de investigación "
              "es la Biomedicina, con énfasis en la fisiología y biofísica del sistema neuromuscular y la fisiopatología "
              "de la diabetes mellitus. Ha publicado más de cien artículos en revistas indizadas al Journal of Citation "
              "Reports y ha graduado a más de 40 Maestros y Doctores en Ciencias en programas SNP-CONAHCyT.")
    
    correo = "huertam@ucol.mx"
    perfil_scholar = "https://scholar.google.com.mx/citations?user=7jGGpnoAAAAJ&hl=en&oi=ao"
    
    # Mostrar la imagen del autor con tamaño ajustado
    st.markdown(f'''
    <div style="text-align: center;">
        <img src="{foto}" alt="{nombre}" style="width: 300px; border-radius: 10px;">
    </div>
    ''', unsafe_allow_html=True)
    
    # Mostrar la información de la plática con el texto justificado (Resumen de la plática antes de la reseña)
    resumen_platica = ("Esta plática abordará la creación y tipos de hipótesis en la investigación científica, "
                       "explorando las diferencias entre hipótesis nulas y alternativas, y cómo formularlas correctamente.")
    
    st.markdown(f'''
    <div style="text-align: justify; font-family: Times New Roman; font-size: 16px;">
    <strong>Resumen de la plática:</strong> {resumen_platica}
    </div>
    ''', unsafe_allow_html=True)
    
    # Mostrar la reseña del autor
    st.markdown(f'''
    <div style="text-align: justify; font-family: Times New Roman; font-size: 16px;">
    <strong>{nombre}</strong>, {grado}. {reseña} <br><br>
    Puedes contactar al autor por correo electrónico: <a href="mailto:{correo}">{correo}</a> <br>
    Perfil de Google Scholar: <a href="{perfil_scholar}" target="_blank">{perfil_scholar}</a>
    </div>
    ''', unsafe_allow_html=True)
    
    # Enlace directo al PDF
    enlace_pdf = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/asp.pdf"
    mostrar_diapositivas(enlace_pdf)
    
    # Botón para generar y descargar el PDF
    pdf = generar_pdf(titulo, foto, nombre, grado, reseña, correo, perfil_scholar, resumen_platica, enlace_pdf)
    st.download_button(
        label="Descargar PDF con los datos del evento",
        data=pdf,
        file_name="evento_30_agosto.pdf",
        mime="application/pdf",
    )
    
    # Agregar la imagen después del botón de descarga
    imagen_url = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/65e716285fa59ca5118574bc62a47521be9f5662/Dr_Huerta_hipotesis.jpg"
    st.image(imagen_url, caption="Dr. Huerta explicando hipótesis", use_column_width=True)
    
    # Añadir contenido sobre "Indicadores de argumentos" debajo
    contenido = '''
    <div style="text-align: justify; font-family: Times New Roman; font-size: 16px;">

    ### Indicadores de argumentos

    Los indicadores de argumentos son palabras o frases que señalan la presencia de una premisa o de una conclusión en un razonamiento. Ayudan a identificar la estructura del argumento, es decir, a distinguir qué enunciados sirven como soporte (premisas) y cuál es la idea principal que se quiere demostrar o sustentar (conclusión).

    #### Indicadores de premisas

    Algunas palabras sirven para señalar las premisas de un argumento. A estas se les llama <strong>indicadores de premisas</strong>. Aquí se presenta una lista de estos indicadores de premisas:

    - puesto que
    - porque
    - ya que
    - como
    - se sigue que
    - como lo muestra
    - dado que
    - como lo indica tal o cual
    - la razón es que
    - por la razón de que
    - puede inferirse que
    - puede derivarse de
    - puede deducirse de
    - en vista del hecho de que

    #### Indicadores de conclusión

    Podríamos determinar cuál de las proposiciones es la conclusión de un argumento y cuáles son sus premisas. Ciertamente, no puede uno confiarse en el orden en el que aparecen las proposiciones en un pasaje. Algunas palabras sirven para introducir la conclusión de un argumento y a estas se les llama <strong>indicadores de conclusión</strong>:

    - por lo tanto
    - de ahí que
    - así, así que
    - por consiguiente
    - en consecuencia
    - consecuentemente
    - prueba que
    - como resultado
    - por esta razón
    - por estas razones
    - se sigue que
    - concluyo que
    - lo que muestra que
    - lo que quiere decir que
    - lo que conlleva que
    - lo que implica que
    - lo que permite inferir que
    - lo que lleva a la conclusión
    - podemos inferir que

    #### Argumentos en contexto

    Las palabras y frases listadas pueden ayudar a reconocer la presencia de un argumento o a identificar sus premisas o su conclusión. Pero algunas veces solo es el significado de un pasaje o el contexto lo que indica la presencia de un argumento. Por ejemplo, durante el acalorado debate por el envío de tropas estadounidenses a Irak en 2007, un crítico del envío de tropas escribió:

    <em>"Mientras nosotros enviamos a tierras extranjeras nuestros hombres y mujeres jóvenes para imponer el orden en Irak, muchos de sus llamados líderes han abandonado sus puestos. Les hemos dado a los iraquíes una oportunidad para salvar sus diferencias y nos la han arrojado a la cara. Irak no merece nuestra ayuda."</em>

    En ese argumento no se emplea ningún indicador de premisa o conclusión y, aun así, es inequívoco. Otro ejemplo lo ofreció una academia en su respuesta a la crítica aguda a la arquitectura moderna, realizada por el novelista y ensayista Tom Wolfe:

    <em>"Tom Wolfe sugiere que los grandes arquitectos modernistas exigen dogmáticamente muros blancos, construcciones de acero y líneas rectas mientras que evitan materiales lujosos. Sin embargo, Mies van der Rohe utilizó mármol travertino y ónix en su afamado Pabellón de Barcelona, y el color es parte integral de la Unite d’Habitation de Le Corbusier, cuyas curvas esculturales son posibles por la construcción en concreto. El señor Wolfe perpetúa una impresión plana, exagerada y falsa del modernismo arquitectónico."</em>

    </div>
    '''
    
    st.markdown(contenido, unsafe_allow_html=True)




def veintiseis_abril():
    titulo = "Aplicación de la Inteligencia Artificial y Conjuntos Rugosos de Participantes Geriátricos en las ENASEM 2018 y 2021: Modelos para el Cálculo de Riesgo de Sarcopenia"
    st.title(titulo)
    
    # Datos del autor
    foto = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/ArceoS.jpg"
    nombre = "Santiago Arceo Díaz"
    grado = "Dr. Ciencias (Astrofísica)"
    
    reseña = ("Licenciatura y Maestría en Física y Doctor en Ciencias (Astrofísica), por las Universidades de Colima y Guanajuato, respectivamente. "
              "En su formación académica se especializó en la creación de modelos analíticos y numéricos, aplicados a las ciencias exactas y a la ingeniería aplicada. "
              "Dentro de la astrofísica, su área de investigación se centra en la evolución estelar y su relación con la tasa de producción de neutrinos y axiones, "
              "concretamente las estrellas gigantes rojas. También ha realizado trabajos en múltiples áreas de la ingeniería y la arquitectura (con simulaciones numéricas "
              "aplicadas a la sostenibilidad ambiental de las que se han realizado 6 tesis de maestría). Se encuentra realizando una estancia postdoctoral en la Universidad "
              "de Colima en la que se enfoca en el uso del machine learning para la clasificación de pacientes geriátricos, a partir de variables antropométricas.")
    
    correo = "santiagoarceo@ucol.mx"
    perfil_scholar = "https://scholar.google.com.mx/citations?user=SFgL-gkAAAAJ&hl=en"
    
    # Mostrar la información del autor con el texto justificado
    #st.image(foto, caption=nombre, use_column_width=True)

    #correo = "santiagoarceo@ucol.mx"
    #perfil_scholar = "https://scholar.google.com.mx/citations?user=SFgL-gkAAAAJ&hl=en"
    
    # Mostrar la imagen del autor con tamaño ajustado
    st.markdown(f'''
    <div style="text-align: center;">
        <img src="{foto}" alt="{nombre}" style="width: 300px; border-radius: 10px;">
    </div>
    ''', unsafe_allow_html=True)
    
    
    st.markdown(f'''
    <div style="text-align: justify; font-family: Times New Roman; font-size: 14px;">
    <strong>{nombre}</strong>, {grado}. {reseña} <br><br>
    Puedes contactar al autor por correo electrónico: <a href="mailto:{correo}">{correo}</a> <br>
    Perfil de Google Scholar: <a href="{perfil_scholar}" target="_blank">{perfil_scholar}</a>
    </div>
    ''', unsafe_allow_html=True)
    
    # Información sobre la plática
    resumen_platica = ("Se aborda el uso de inteligencia artificial y la teoría de conjuntos rugosos para evaluar el riesgo de sarcopenia en adultos mayores mexicanos, "
                       "utilizando datos de las encuestas ENASEM 2018 y 2021. Se utilizaron conjuntos rugosos y árboles de decisión para clasificar y evaluar el riesgo de "
                       "sarcopenia, basándose en variables como fuerza, caídas, y movilidad. Se analizaron subconjuntos de pacientes con respuestas idénticas, permitiendo "
                       "extraer perfiles de riesgo. Los modelos permitieron clasificar pacientes con distintos niveles de riesgo de sarcopenia, mostrando una mayor prevalencia "
                       "de riesgo en mujeres y en pacientes con hipertensión y diabetes. La clasificación mediante inteligencia artificial y conjuntos rugosos es efectiva para "
                       "evaluar el riesgo de sarcopenia, incluso sin medidas antropométricas directas. Se observaron diferencias significativas en el riesgo entre hombres y mujeres, "
                       "y la presencia de comorbilidades como hipertensión y diabetes aumenta el riesgo.")
    
    # Mostrar la información de la plática con el texto justificado
    st.markdown(f'''
    <div style="text-align: justify; font-family: Times New Roman; font-size: 14px;">
    <strong>Resumen de la plática:</strong> {resumen_platica}
    </div>
    ''', unsafe_allow_html=True)
    
    # Enlace directo al PDF
    enlace_pdf = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/seminario_26_abril_2024.pdf"
    mostrar_diapositivas(enlace_pdf)
    
    # Botón para generar y descargar el PDF
    pdf = generar_pdf(titulo, foto, nombre, grado, reseña, correo, perfil_scholar, resumen_platica, enlace_pdf)
    st.download_button(
        label="Descargar PDF con los datos del evento",
        data=pdf,
        file_name="evento_26_abril.pdf",
        mime="application/pdf",
    )
    
    # Sección "Preguntas Clave"
    st.subheader("Preguntas Clave")
    st.markdown('''
    <div style="text-align: justify; font-family: Times New Roman; font-size: 14px;">
    1. ¿Cómo cambiará la proporción de adultos mayores en México hacia el año 2050, y cuáles serán las consecuencias para la salud pública?<br>
    2. ¿Cuál es la prevalencia de sarcopenia en las poblaciones de adultos mayores en México y cómo varía entre diferentes grupos (sin comorbilidades, con diabetes, con hipertensión, etc.)?<br>
    3. ¿Cómo se utiliza la teoría de conjuntos rugosos y la inteligencia artificial para clasificar y evaluar el riesgo de sarcopenia en adultos mayores?<br>
    4. ¿Cuáles son las preguntas o variables críticas en la ENASEM que se utilizan para evaluar el riesgo de sarcopenia (por ejemplo, fuerza de presión, caídas, movilidad)?<br>
    5. ¿Cómo influyen las comorbilidades como la hipertensión y la diabetes en el riesgo de sarcopenia en adultos mayores?<br>
    6. ¿Existen diferencias significativas en el riesgo de sarcopenia entre hombres y mujeres?<br>
    7. ¿Cómo se pueden utilizar los modelos desarrollados para mejorar la detección y gestión de la sarcopenia en el ámbito clínico?<br>
    8. ¿Qué revelan los datos de las encuestas ENASEM 2018 y 2021 sobre la distribución del riesgo de sarcopenia en la población mexicana mayor de 60 años?<br>
    </div>
    ''', unsafe_allow_html=True)

# Llamada a la función para mostrar la página
#veintiseis_abril()



def seis_de_septiembre():
    titulo = "Evento: El arte de las presentaciones científicas: pasos críticos para tener éxito y errores críticos para evitar"
    st.title(titulo)

    # Datos del autor
    foto_autor = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/rios.jpg"
    foto_derecha = "https://github.com/SArcD/Seminario_CUIB_2024/blob/3c6cf85fdf45b0f666c86d74376a4468ef80b9c5/dramoni.PNG?raw=true"

    nombre = "Mónica Ríos Silva"
    grado = "Dra. Ciencias Médicas"
    reseña = ("Médica cirujana y partera con especialidad en Medicina Interna y Doctorado en Ciencias Médicas por la Universidad de Colima, "
              "médica especialista del Hospital Materno Infantil de Colima y PTC de la Facultad de Medicina de la Universidad de Colima. "
              "Es profesora de los posgrados en Ciencias Médicas, Ciencias Fisiológicas, Nutrición clínica y Ciencia ambiental global. "
              "Cuenta con 42 artículos científicos en revistas con factor de impacto con más de 400 citas, desde 2019 revisora de artículos "
              "en revistas internacionales con factor de impacto mayor de 1, asesoría de 31 tesis de especialidades médicas y de maestría y "
              "doctorado en la Universidad de Colima y la Universidad de Aguascalientes. Colaboraciones de investigación: en el Centro de "
              "Investigaciones Biomédicas de Occidente y las unidades estatales del Instituto Mexicano del Seguro Social así como con la "
              "Universidad Michoacana de San Nicolás de Hidalgo. Miembro del Sistema Nacional de Investigadores Nivel II.")
    correo = "mrios@ucol.mx"
    perfil_scholar = "https://scholar.google.com.mx/citations?hl=en&user=5mgGr3kAAAAJ"
    
    # Mostrar la imagen del autor y la segunda imagen en columnas
  #  col1, col2 = st.columns(2)
    
  #  with col1:
  #      # Mostrar la imagen del autor
  #      st.image(foto_autor, width=150)
    
  #  with col2:
  #      # Mostrar la imagen adicional a la derecha
  #      st.image(foto_derecha, width=300)

        # Usar tres columnas para ajustar la posición de la imagen de la derecha
    col1, col2, col3 = st.columns([2, 0.5, 1])  # Ajustar las proporciones de las columnas

    with col1:
        # Mostrar la imagen del autor
        st.image(foto_autor, width=150)
    
    with col2:
        # Mostrar la imagen adicional, desplazada ligeramente hacia la izquierda
        st.image(foto_derecha, width=300)  # Ajustar el tamaño



    
    # Mostrar detalles del autor
    st.subheader(nombre)
    st.write(f"**Grado:** {grado}")
    st.write(reseña)
    st.write(f"**Correo:** {correo}")
    st.write(f"**Perfil:** [Google Scholar]({perfil_scholar})")
    
    # Información sobre la plática
    resumen_platica = ("Te invitamos al seminario El arte de las presentaciones científicas, donde aprenderás los aspectos clave para desarrollar presentaciones efectivas y profesionales. "
                       "Basado en la obra de Michael Alley, este seminario cubrirá cuatro pilares esenciales: el discurso, la estructura, las ayudas visuales y la entrega. "
                       "Descubre cómo hacer tu discurso ameno utilizando ejemplos y analogías, cómo organizar tus ideas de manera lógica con transiciones claras, y cómo diseñar "
                       "ayudas visuales que refuercen tu mensaje sin sobrecargar a la audiencia. Además, aprenderás a controlar los nervios, mantener la atención del público y anticipar "
                       "problemas técnicos siguiendo la Ley de Murphy.")
    
    # Mostrar sección "Sobre la plática"
    mostrar_sobre_la_platica(resumen_platica)
    
    # Enlace directo al PDF
    enlace_pdf = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/El%20arte%20de%20las%20presentaciones%20cient%C3%ADficas310824_pdf.pdf"
    mostrar_diapositivas(enlace_pdf)
    
    # Botón para generar y descargar el PDF
    pdf = generar_pdf(titulo, foto_autor, nombre, grado, reseña, correo, perfil_scholar, resumen_platica, enlace_pdf)
    st.download_button(
        label="Descargar PDF con los datos del evento",
        data=pdf,
        file_name="evento_24_abril.pdf",
        mime="application/pdf",
    )
    
    # Sección "Preguntas Clave"
    st.subheader("Preguntas Clave")
    st.write("""
    1. ¿Cuáles son los principales errores que se deben evitar al dar una presentación científica?
    2. ¿Qué aspectos se deben cuidar en una presentación científica para asegurar su efectividad?
    3. ¿Qué ventajas y desventajas presentan las presentaciones científicas en comparación con otros métodos de comunicación?
    4. ¿Cómo se puede anticipar y manejar preguntas difíciles durante una presentación?
    5. ¿Cómo se debe estructurar el contenido de una presentación científica para mantener el interés del público?
    """)


    # Sección "Material de apoyo"
    st.subheader("Material de apoyo")
    st.markdown("""
    Para profundizar más en el tema, te recomendamos el siguiente libro:
    
    - [The Craft of Scientific Presentations: Critical Steps to Succeed and Critical Errors to Avoid](https://github.com/SArcD/Seminario_CUIB_2024/blob/a10ffac9338f31fbf68ce79e7629ba8155978cf2/Scientific-Presentation_book.pdf)
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
