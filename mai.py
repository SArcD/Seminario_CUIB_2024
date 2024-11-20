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
    "04 de octubre: Fernanda y Michel": "04 de octubre: Fernanda y Michel",
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
        # Espacio vertical entre el resumen y la sección "Acerca del autor"
    st.write("")
    st.write("")
    
    perfil_scholar = "https://scholar.google.com.mx/citations?user=7jGGpnoAAAAJ&hl=en&oi=ao"
    
    # Mostrar la imagen del autor con tamaño ajustado
    st.markdown(f'''
    <div style="text-align: center;">
        <img src="{foto}" alt="{nombre}" style="width: 300px; border-radius: 10px;">
    </div>
    ''', unsafe_allow_html=True)

    # Espacio antes del resumen de la plática
    st.write("")
    
    # Mostrar la información de la plática con el texto justificado (Resumen de la plática antes de la reseña)
    resumen_platica = ("Esta plática abordará la creación y tipos de hipótesis en la investigación científica, "
                       "explorando las diferencias entre hipótesis nulas y alternativas, y cómo formularlas correctamente.")
    
    st.markdown(f'''
    <div style="text-align: justify; font-family: Times New Roman; font-size: 16px;">
    <strong>Resumen de la plática:</strong> {resumen_platica}
    </div>
    ''', unsafe_allow_html=True)

    # Espacio vertical entre el resumen y la sección "Acerca del autor"
    st.write("")
    st.write("")

    # Mostrar la sección "Acerca del autor"
    st.markdown(f'''
    <div style="text-align: justify; font-family: Times New Roman; font-size: 16px;">
    <strong>Acerca del autor</strong><br><br>
    <strong>{nombre}</strong>, {grado}. {reseña} <br><br>
    <strong>Puedes contactar al autor por correo electrónico:</strong> <a href="mailto:{correo}">{correo}</a> <br>
    <strong>Perfil de Google Scholar:</strong> <a href="{perfil_scholar}" target="_blank">{perfil_scholar}</a>
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

def septiembre_trece():
    titulo = "Diseños experimentales con animales: modelo de diabetes y modelo de preeclampsia"
    st.title(titulo)
    
    # Datos del primer autor
    foto1 = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/Foto_Julio.jpg"
    nombre1 = "Julio César Alcaraz Siqueiros"
    grado1 = "Maestro en Ingeniería de Procesos"
    reseña1 = " Es matemático de formación y después realizó un posgrado en Ingeniería de Procesos enfocado en Bioingeniería, ambos por la Universidad de Colima. Durante su desarrollo profesional y académico he tenido la experiencia en trabajo experimental y teórico aplicado a biología matemática, donde ha realizado modelos matemáticos predictivos basados en ecuaciones diferenciales y matriciales que describen procesos biológicos y químicos, haciendo simulaciones por computadora (MATLAB, R y Python), y comprobando las predicciones de manera experimental. Su formación le ha dado habilidades en el manejo de instrumentos de laboratorio tales como, monitoreo en línea y fuera de línea de biorreactores, caracterización y extracción de enzimas extracelulares, bioprocesos de los azúcares y trabajo experimental con animales. Además de la recolección, análisis e interpretación de datos usando herramientas estadísticas, probabilísticas y de programación para la realización de modelos predictivos de un proceso. Lo anterior lo llevó a continuar sus estudios de doctorado. Actualmente es estudiante del Doctorado en Ciencias Fisiológicas en el Laboratorio de Fiosiología del Músculo Esquelético de la Universidad de Colima, también se desempeña como profesor por horas en la Facultad de Ciencias Biológicas y Agropecuarias de la misma universidad, y además es miembro activo de la asociación civil DAYIN A.C. (Desarrollo y Ayuda con Investigación)."
    correo1 = "julio_siqueiros@ucol.mx"
    perfil_scholar1 = "https://www.researchgate.net/profile/Julio-Alcaraz-Siqueiros-2"
    
    # Datos del segundo autor
    foto2 = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/Expo_septiembre_trece.jpg"
    nombre2 = "Héctor Mariano Jiménez Leal"
    grado2 = ""
    reseña2 = ""
    correo2 = "hectormariano_jimenez@ucol.mx"
    perfil_scholar2 = "https://scholar.google.com.mx/citations?user=SFgL-gkAAAAJ&hl=en"
    
    # Datos del tercer autor
    foto3 = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/Expo_septiembre_trece.jpg"
    nombre3 = "Minerva Silvia Márquez Villar"
    grado3 = ""
    reseña3 = ""
    correo3 = "mmarquez20@ucol.mx"
    perfil_scholar3 = "https://scholar.google.com.mx/citations?user=SFgL-gkAAAAJ&hl=en"
    
    # Mostrar información de los autores
    autores = [(foto1, nombre1, grado1, reseña1, correo1, perfil_scholar1),
               (foto2, nombre2, grado2, reseña2, correo2, perfil_scholar2),
               (foto3, nombre3, grado3, reseña3, correo3, perfil_scholar3)]
    
    for foto, nombre, grado, reseña, correo, perfil_scholar in autores:
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
    resumen_platica = ("En la charla se presentaron las características principales y los principios fundamentales que involucran la planificación de experimentos científicos. El enfoque principal se centró en los diseños experimentales que involucran animales, destacando la importancia de la definición de grupos a partir de las variables, el control e influencia de variables externas y la importancia de cuidar la validez y confiabilidad de las medicoones con el objetivo de lograr la replicabilidad y validez estadística de los resultados. Se mencionaron brevemente las consideraciones éticas que deben considerarse para llevar a cabo experimentos con animales. Posteriormente, se abordó de manera específica el tema de los experimentos en animales utilizando dos modelos patológicos: el modelo de diabetes y el modelo de preeclampsia. En el caso de la diabetes, se explicó como es la inducción de la enfermedad en ratas, las consideraciones para clasificar el tipo de diabetes inducida, y como este modelo permite estudiar los efectos de diferentes tratamientos y comprender mejor los mecanismos fisiológicos involucrados en esta enfermedad. Para el modelo de preeclampsia, se destacaron los síntomas y características que destacan en esta enfermedad, así como los desafíos y metodologías específicas empleadas para simular esta complicación del embarazo en modelos animales, todo con el objetivo de evaluar terapias preventivas de este padecimiento.")
    
    # Mostrar la información de la plática con el texto justificado
    st.markdown(f'''
    <div style="text-align: justify; font-family: Times New Roman; font-size: 14px;">
    <strong>Resumen de la plática:</strong> {resumen_platica}
    </div>
    ''', unsafe_allow_html=True)
    
    # Enlace directo al PDF
    enlace_pdf = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/SeminarioInterno_13Sep2024_completo.pdf"
    mostrar_diapositivas(enlace_pdf)
    
    # Botón para generar y descargar el PDF
    pdf = generar_pdf(titulo, foto1, nombre1, grado1, reseña1, correo1, perfil_scholar1, resumen_platica, enlace_pdf)
    st.download_button(
        label="Descargar PDF con los datos del evento",
        data=pdf,
        file_name="evento_13_septiembre.pdf",
        mime="application/pdf",
    )

    # Agregar la imagen después del botón de descarga
    imagen_url = "Expo_septiembre_trece.jpg"
    st.image(imagen_url, caption="Ponentes del 13 de septiembre: Mariano, Minerva y Julio César (de izquierda a derecha)", use_column_width=True)
    
    # Sección "Preguntas Clave"
    st.subheader("Preguntas Clave")
    st.markdown('''
    <div style="text-align: justify; font-family: Times New Roman; font-size: 14px;">
    1. ¿Cuáles son las características principales de la planificación de experimentos científicos que se destacaron en la charla?<br>
    2. ¿Qué importancia tienen los diseños experimentales que involucran animales en la investigación científica?<br>
    3. ¿Cómo se debe definir y controlar las variables en un experimento para asegurar la validez y confiabilidad de las mediciones?<br>
    4. ¿Por qué es esencial controlar las variables externas en los experimentos científicos?<br>
    5. ¿Qué aspectos éticos se deben considerar al realizar experimentos con animales?<br>
    6. ¿Cómo se induce la diabetes en modelos animales, como las ratas, y qué tipos de diabetes se pueden clasificar en estos experimentos?<br>
    7. ¿Qué desafíos presenta la simulación de la preeclampsia en modelos animales y cómo se emplean para evaluar terapias preventivas?<br>
    8. ¿Cuál es la relevancia de estudiar diferentes tratamientos en modelos animales para entender los mecanismos fisiológicos de enfermedades como la diabetes?<br>
    </div>
    ''', unsafe_allow_html=True)

# Llamada a la función para mostrar la página
#veintiseis_abril()

def octubre_cuatro():
    titulo = "Estudios transversales."
    st.title(titulo)
    
    # Datos del primer autor
    nombre1 = "Michel Baltazar César"
    grado1 = " "
    reseña1 = (" ")
    correo1 = "cmichel@ucol.mx"
    
    # Datos del segundo autor
    foto2 = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/valdez_aguilar.PNG"
    nombre2 = "Fernanda Edith Valdez Aguilar"
    grado2 = "Química Farmacéutica Bióloga"
    reseña2 = ("Fernanda Edith Valdez Aguilar, Química Farmacéutica Bióloga egresada de la Universidad de Colima. "
               "Durante su desarrollo académico en la facultad obtuvo experiencia en el ámbito de la experimentación con animales. "
               "Actualmente es estudiante de la Maestría en Ciencias Médicas de la Universidad de Colima.")
    correo2 = "fvaldez2@ucol.mx"
    
    # Lista de autores
    autores = [
        {"foto": None, "nombre": nombre1, "grado": grado1, "reseña": reseña1, "correo": correo1, "perfil_scholar": None},
        {"foto": foto2, "nombre": nombre2, "grado": grado2, "reseña": reseña2, "correo": correo2, "perfil_scholar": None}
    ]
    
    for autor in autores:
        # Si hay una foto, mostrarla
        if autor["foto"]:
            st.markdown(f'''
            <div style="text-align: center;">
                <img src="{autor['foto']}" alt="{autor['nombre']}" style="width: 300px; border-radius: 10px;">
            </div>
            ''', unsafe_allow_html=True)
    
        # Mostrar la información del autor con un espacio antes del resumen
        st.markdown(f'''
        <div style="margin-top: 20px; text-align: justify; font-family: Times New Roman; font-size: 14px;">
        <strong>{autor['nombre']}</strong>{", " + autor['grado'] if autor['grado'] else ""}. 
        {autor['reseña'] if autor['reseña'] else ""} <br><br>
        Puedes contactar al autor por correo electrónico: <a href="mailto:{autor['correo']}">{autor['correo']}</a> 
        </div>
        ''', unsafe_allow_html=True)
    
    # Información sobre la plática
    resumen_platica = ("Los estudios transversales son un tipo de investigación observacional que recopila datos de una población en un único momento del tiempo. "
                       "Su principal objetivo es medir la prevalencia de una enfermedad o condición y evaluar posibles relaciones entre variables en ese momento específico. "
                       "Existen tres tipos principales: Descriptivos, Analíticos y Seriados. Son estudios rápidos y económicos, pero tienen limitaciones como la imposibilidad de determinar la temporalidad entre causa y efecto.")
    
    # Mostrar la información de la plática con el texto justificado
    st.markdown(f'''
    <div style="text-align: justify; font-family: Times New Roman; font-size: 14px;">
    <strong>Resumen de la plática:</strong> {resumen_platica}
    </div>
    ''', unsafe_allow_html=True)
    
    # Enlace directo al PDF
    enlace_pdf = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/SeminarioInterno_04octubre2024_completo.pdf"
    mostrar_diapositivas(enlace_pdf)
    
    # Botón para generar y descargar el PDF
    #pdf = generar_pdf(titulo, nombre1, correo1, None, resumen_platica, enlace_pdf)
    #st.download_button(
    #    label="Descargar PDF con los datos del evento",
    #    data=pdf,
    #    file_name="evento_04_octubre.pdf",
    #    mime="application/pdf",
    #)
    
    # Sección "Preguntas Clave"
    st.subheader("Preguntas Clave")
    st.write("""
    1. ¿Qué es un estudio transversal y cuál es su principal objetivo?
    2. ¿Qué diferencias existen entre los estudios transversales descriptivos y analíticos?
    3. ¿Cuáles son las ventajas de los estudios transversales en términos de tiempo y costos?
    4. ¿Qué limitaciones tienen los estudios transversales al intentar establecer relaciones causales?
    5. ¿Cómo se mide la prevalencia de una condición o enfermedad en un estudio transversal?
    6. ¿Qué tipos de variables son más adecuadas para analizar en estudios transversales?
    7. ¿Qué retos presenta la selección de la muestra en los estudios transversales para garantizar la representatividad de la población?
    8. ¿Cómo se pueden utilizar los estudios transversales seriados para observar cambios en una población a lo largo del tiempo?
    """)

    # Sección "Material complementario"
    st.subheader("Material complementario")

    # Imagen 1
    st.write("""Los estudios transversales miden los casos de sujetos con una enfermedad o evento de interés en un punto temporal específico, como si se tratase de tomar una fotografía para capturar un momento determinado. Esto los diferencia de los estudios longitudinales, donde se incluye el seguimiento a través del tiempo de los individuos.
    
    """)
    
    
    st.image("https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/va_00.PNG", caption="Figura 1: Onjetivo de un estudio transversal.")

    st.write("""
    Los estudios transversales se emplean para la determinación de prevalencias, las cuales son la frecuencia de una enfermedad o evento de interés en una población. Además, pueden explorar posibles asociaciones entre exposiciones y eventos de interés, que pueden estudiarse posteriormente a través de distintos diseños de estudio. Una de sus aplicaciones es identificar la frecuencia de factores de riesgo de enfermedades. Debido a que la exposición y el desenlace se miden en una sola ocasión, este tipo de investigación no presenta pérdidas de seguimiento. Asimismo, son relativamente sencillos, poco consumidores de tiempo y de bajo costo monetario.
    """)
    
    # Imagen 2
    st.image("https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/va_01.PNG", caption="Figura 2: Ventajas de los estudios transversales.")

    st.write("""
    La principal característica de los estudios transversales es asimismo una desventaja, ya que al medir la exposición y el evento de interés o enfermedad simultáneamente no es posible determinar si la exposición precedió al evento. Por lo tanto, estos estudios son incapaces de establecer una relación de causa y efecto, solo detectar si existe asociación entre ambos.
    Estos pueden estar sujetos a sesgos, como lo son el sesgo de información, de selección y de confusión, los cuales pueden distorsionar los resultados. Además. tienen la desventaja de que, en casos donde la enfermedad sea de corta duración o tenga una gran letalidad, puede llegar a subestimar los resultados al no capturar a los pacientes si estos se curan o fallecen antes de ser incluidos en el estudio. Por otro lado, si una enfermedad o evento de interés es muy raro, difícilmente podría capturarse un caso en el estudio.
    """)
    
    # Imagen 3
    st.image("https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/va_02.PNG", caption="Figura 3: Desventajas de los estudios transversales.")

    # Imagen 4
    st.image("https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/va_03.PNG", caption="Figura 4: Conclusiones.")

    st.write(""" En resumen, los estudios transversales pueden emplearse para la determinación de prevalencias (descriptivos) o para identificar si existe asociación entre variables y generar nuevas hipótesis (analíticos). Se caracterizan por medir la exposición y el evento de interés al mismo tiempo, por lo que pueden determinar si existe asociación entre estos pero no es posible establecer causalidad. Debido a esto, suelen ser un paso previo para investigaciones más rigurosas.
    """)

def octubre_dieciocho():
    titulo = "Estudios de Cohorte"
    st.title(titulo)
    
    # Datos del primer autor
    nombre1 = "Ricardo García Rodríguez"
    grado1 = "Maestro en Piscología"
    reseña1 = (" ")
    correo1 = "ricardo_garcia@ucol.mx"
    
    # Datos del segundo autor
    #foto2 = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/valdez_aguilar.PNG"
    nombre2 = "María Fernanda García"
    grado2 = "Maestra en Ciencias"
    reseña2 = (" ")
    correo2 = "mgarcia109@ucol.mx"
    
    # Lista de autores
    autores = [
        {"foto": None, "nombre": nombre1, "grado": grado1, "reseña": reseña1, "correo": correo1, "perfil_scholar": None},
        {"foto": None, "nombre": nombre2, "grado": grado2, "reseña": reseña2, "correo": correo2, "perfil_scholar": None}
    ]
    
    for autor in autores:
        # Si hay una foto, mostrarla
        if autor["foto"]:
            st.markdown(f'''
            <div style="text-align: center;">
                <img src="{autor['foto']}" alt="{autor['nombre']}" style="width: 300px; border-radius: 10px;">
            </div>
            ''', unsafe_allow_html=True)
        
        # Mostrar la información del autor
        st.markdown(f'''
        <div style="text-align: justify; font-family: Times New Roman; font-size: 14px;">
        <strong>{autor['nombre']}</strong>{", " + autor['grado'] if autor['grado'] else ""}. 
        {autor['reseña'] if autor['reseña'] else ""} <br><br>
        Puedes contactar al autor por correo electrónico: <a href="mailto:{autor['correo']}">{autor['correo']}</a> 
        </div>
        ''', unsafe_allow_html=True)
    
    # Información sobre la plática
    resumen_platica = ("Un diseño de cohorte es un tipo de estudio observacional que se utiliza para investigar la relación entre una exposición (como un factor de riesgo o una intervención) y un resultado a lo largo del tiempo. En este diseño, se selecciona un grupo de individuos que no presentan la condición o enfermedad de interés al inicio del estudio, pero que están expuestos o no a un factor de riesgo específico. Luego, se sigue a estos individuos durante un periodo de tiempo para observar la aparición de la enfermedad o el resultado de interés.")
    
    # Mostrar la información de la plática con el texto justificado
    st.markdown(f'''
    <div style="text-align: justify; font-family: Times New Roman; font-size: 14px;">
    <strong>Resumen de la plática:</strong> {resumen_platica}
    </div>
    ''', unsafe_allow_html=True)
    

    enlace_pdf = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/Dise%C3%B1os%20de%20cohorte%20FINAL.pdf"

    # Mostrar el enlace como texto clicable
    st.markdown(f'[Haz clic aquí para ver las diapositivas]({enlace_pdf})')
    
    # Botón para generar y descargar el PDF
    #pdf = generar_pdf(titulo, nombre1, correo1, None, resumen_platica, enlace_pdf)
    #st.download_button(
    #    label="Descargar PDF con los datos del evento",
    #    data=pdf,
    #    file_name="evento_04_octubre.pdf",
    #    mime="application/pdf",
    #)
from fpdf import FPDF
import requests
from PIL import Image
from io import BytesIO

def convertir_a_rgb(imagen):
    """Convierte una imagen a RGB, rellenando la transparencia si existe."""
    if imagen.mode == "RGBA":
        fondo = Image.new("RGB", imagen.size, (255, 255, 255))  # Fondo blanco
        fondo.paste(imagen, mask=imagen.split()[3])  # Aplicar máscara de transparencia
        return fondo
    else:
        return imagen.convert("RGB")

def generar_pdf(titulo, foto1, imagen_derecha_url, nombre1, grado1, reseña1, correo1, perfil_scholar1, resumen_platica, enlace_pdf):
    # Crear el PDF
    pdf = FPDF()
    pdf.add_page()

    # Título en negritas y centrado
    pdf.set_font("Times", "B", 16)
    page_width = pdf.w - 2 * pdf.l_margin  # Ancho de la página
    pdf.multi_cell(page_width, 10, txt=titulo, align='C')
    pdf.ln(10)  # Espacio debajo del título

    # Descargar y agregar la imagen del autor (izquierda)
    response_foto = requests.get(foto1)
    if response_foto.status_code == 200:
        img_foto = Image.open(BytesIO(response_foto.content))
        img_foto = convertir_a_rgb(img_foto)  # Convertir a RGB manejando transparencia
        img_foto.save("temp_image.jpg")  # Guardar temporalmente
        img_height = 40  # Altura ajustada de la imagen
        img_width = 30  # Proporción ajustada
        pdf.image("temp_image.jpg", x=50, y=pdf.get_y(), w=img_width, h=img_height)
    else:
        print("Error al descargar la imagen izquierda.")

        # Descargar y agregar la imagen derecha
    response_derecha = requests.get(imagen_derecha_url)
    if response_derecha.status_code == 200:
        img_derecha = Image.open(BytesIO(response_derecha.content))
        img_derecha = convertir_a_rgb(img_derecha)
        img_derecha.save("temp_image_derecha.jpg")
        aspect_ratio = img_derecha.width / img_derecha.height
        img_derecha_width = img_height * aspect_ratio  # Calcular ancho basado en la altura
        pdf.image("temp_image_derecha.jpg", x=90, y=pdf.get_y(), w=img_derecha_width, h=img_height)
    else:
        print("Error al descargar la imagen derecha.")


    # Ajustar posición del texto "Acerca de la autora" debajo de las imágenes
    pdf.set_y(pdf.get_y() + img_height + 5)  # Mover hacia abajo para que no se superponga con las imágenes
    pdf.set_font("Times", "B", 14)
    pdf.cell(200, 10, txt="Acerca de la autora", ln=True)
    #pdf.ln(5)  # Espacio entre el título y el contenido

    # Información del autor
    informacion = [
        ("Nombre", nombre1),
        ("Grado", grado1),
        ("Reseña", reseña1),
        ("Correo", correo1),
        ("Perfil", perfil_scholar1)
    ]

    for etiqueta, contenido in informacion:
        pdf.set_font("Times", "B", 12)  # Negritas para las etiquetas
        pdf.cell(40, 10, f"{etiqueta}: ", ln=False)
        pdf.set_font("Times", "", 12)  # Texto normal para el contenido
        pdf.multi_cell(0, 10, contenido)  # Multi-cell para contenido largo

    pdf.ln(10)  # Espacio debajo de la información del autor

    # Sección "Sobre la plática"
    pdf.set_font("Times", "B", 14)
    pdf.cell(200, 10, txt="Sobre la plática", ln=True)

    pdf.set_font("Times", "", 12)  # Texto normal
    pdf.multi_cell(0, 10, resumen_platica)
    #pdf.ln(10)  # Espacio debajo de la sección "Sobre la plática"

    # Enlace a las diapositivas
    if enlace_pdf:
        pdf.set_font("Times", "B", 14)
        pdf.cell(40, 10, "Ver diapositivas: ", ln=False)
        pdf.set_font("Times", "", 12)
        pdf.cell(0, 10, txt=enlace_pdf, ln=True, link=enlace_pdf)

    # Descargar y agregar la cintilla
    cintilla_url = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/udec.png"
    response_cintilla = requests.get(cintilla_url)
    cintilla_img = Image.open(BytesIO(response_cintilla.content))
    cintilla_img.save("temp_cintilla.png")  # Guardar temporalmente la imagen

    image_width = 90  # Ancho de la cintilla
    pdf_width = 210  # Ancho de la página
    x_position = (pdf_width - image_width) / 2  # Centrar la imagen
    y_position = 270  # Altura ajustada para la parte inferior

    pdf.image("temp_cintilla.png", x=x_position, y=y_position, w=image_width)

    # Retornar el PDF como bytes para descargar
    return pdf.output(dest="S").encode("latin1")



def noviembre_quince():
    import streamlit as st

    titulo = "Seminario del 15 de noviembre: Publicación para principiantes"
    st.title(titulo)

    # Datos del autor
    foto1 = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/FotoXochitl.jpg"
    imagen_derecha_url = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/XARTT_0.PNG"
    nombre1 = "Xóchitl Angélica Rosio Trujillo Trujillo"
    grado1 = "Doctora en Ciencias Fisiológicas"
    reseña1 = (
        "Bióloga, Maestra y Doctora en Ciencias Fisiológicas con especialidad en Fisiología. "
        "Es Profesora-Investigadora de Tiempo Completo de la Universidad de Colima. Cuenta con perfil deseable "
        "y es miembro del Sistema Nacional de Investigadores en el nivel 3. Su línea de investigación es en Biomedicina "
        "con una producción científica de más de noventa artículos en revistas internacionales."
    )
    correo1 = "rosio@ucol.mx"
    perfil_scholar1 = "https://scholar.google.com.mx/citations?hl=en&user=NRAT-KwAAAAJ"

    # Mostrar la imagen del autor
    st.markdown(f'''
    <div style="text-align: center;">
        <img src="{foto1}" alt="{nombre1}" style="width: 300px; border-radius: 10px;">
        <div style="font-family: Times New Roman; font-size: 14px; margin-top: 5px;">
            <em>Dra. Xóchitl Trujillo</em>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    # Título de la sección "Acerca del autor" debajo de la imagen
    st.markdown(f'''
    <div style="text-align: center; font-family: Times New Roman; font-size: 16px; font-weight: bold; margin-top: 10px;">
        Acerca de la autora
    </div>
    ''', unsafe_allow_html=True)

    st.markdown(f'''
    <div style="text-align: center; font-family: Times New Roman; font-size: 16px; font-weight: bold;">
        
    </div>
    <div style="margin-top: 10px; text-align: justify; font-family: Times New Roman; font-size: 14px;">
        
    </div>
    ''', unsafe_allow_html=True)
    
    # Mostrar la reseña del autor y contacto
    st.markdown(f'''
    <div style="text-align: justify; font-family: Times New Roman; font-size: 14px;">
        <strong>{nombre1}</strong>{", " + grado1 if grado1 else ""}. 
        {reseña1 if reseña1 else ""} <br><br>
        <strong>Puedes contactar al autor por correo electrónico:</strong> <a href="mailto:{correo1}">{correo1}</a> <br><br>
        <strong>Perfil en Google Scholar:</strong> <a href="{perfil_scholar1}" target="_blank">{perfil_scholar1}</a>
    </div>
    ''', unsafe_allow_html=True)


    st.markdown(f'''
    <div style="text-align: center; font-family: Times New Roman; font-size: 16px; font-weight: bold;">
        
    </div>
    <div style="margin-top: 10px; text-align: justify; font-family: Times New Roman; font-size: 14px;">
        
    </div>
    ''', unsafe_allow_html=True)
    
    # Información sobre la plática
    resumen_platica = (
        "Esta plática aborda la importancia de las publicaciones científicas en el ámbito académico, destacando el proceso de redacción, envío, revisión y publicación de artículos. Se comienza por dar algunos consejos para facilitar la redacción del artículo (desde reglas básicas de estilo hasta la descripción de cada sección). Después se dan recomendaciones para la selección de la revista y se describen aspectos importantes de la revisión por pares. Por último, se abordan las consideraciones éticas relacionadas con la publicación de un artículo científico y el uso de la inteligencia artificial en la redacción. "
    )
    
    enlace_pdf = "https://acortar.link/aS2bXR"
    #https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/Publicacion%20para%20principiantes-LAB.pdf"

    st.markdown(f'''
    <div style="text-align: center; font-family: Times New Roman; font-size: 16px; font-weight: bold;">
        Resumen de la plática
    </div>
    <div style="margin-top: 10px; text-align: justify; font-family: Times New Roman; font-size: 14px;">
        {resumen_platica}
    </div>
    ''', unsafe_allow_html=True)


#st.markdown(f'''
#<div style="text-align: center; font-family: Times New Roman; font-size: 16px; font-weight: bold;">
#    Resumen de la plática
#</div>
#<div style="margin-top: 10px; text-align: justify; font-family: Times New Roman; font-size: 14px;">
#    {resumen_platica}
#</div>
#''', unsafe_allow_html=True)

    
    st.markdown(f'[Haz clic aquí para ver las diapositivas]({enlace_pdf})')

    # Generar y descargar el PDF
    #pdf = generar_pdf(titulo, nombre1, correo1, grado1, resumen_platica, enlace_pdf)
    #pdf = generar_pdf(titulo, foto1, nombre1, grado1, reseña1, correo1, perfil_scholar1, resumen_platica, enlace_pdf)
    pdf = generar_pdf(titulo, foto1, imagen_derecha_url, nombre1, grado1, reseña1, correo1, perfil_scholar1, resumen_platica, enlace_pdf)

    st.download_button(
        label="Descargar PDF con los datos del evento",
        data=pdf,
        file_name="evento_15_noviembre.pdf",
        mime="application/pdf",
    )

    # Sección "Preguntas Clave"
    st.subheader("Preguntas Clave")
    st.write("""
1. **¿Por qué es importante publicar los resultados de una investigación científica y qué impacto tiene en la carrera de un investigador?**
2. **¿Cuáles son los principales tipos de revisión por pares y qué ventajas y desventajas ofrece cada uno?**
3. **¿Qué criterios utiliza una persona revisora para evaluar la calidad y relevancia de un manuscrito científico?**
4. **¿Qué prácticas éticas deben seguirse al momento de preparar y someter un manuscrito científico para publicación?**
5. **¿Qué elementos deben incluirse en las secciones esenciales de un manuscrito, como introducción, métodos, resultados y discusión?**
6. **¿Qué características definen una revista científica de calidad y cómo se pueden identificar revistas predatorias?**
7. **¿Cuáles son las razones comunes por las que un manuscrito puede ser rechazado por una revista científica?**
8. **¿Cómo deben manejarse las disputas de autoría y qué medidas pueden tomarse para prevenirlas desde el inicio del proyecto?**
9. **¿Qué recomendaciones específicas se ofrecen para responder a los comentarios de los revisores tras el proceso de revisión por pares?**
10. **¿Cómo se debe utilizar la inteligencia artificial en la elaboración y análisis de manuscritos científicos según las recomendaciones actuales?**
    """)

    # Sección "Material complementario"
    st.subheader("Material complementario")

    # Imagen 1
    #st.write("""Esta diapositiva habla acerca de que existen diversos tipos de cohorte categorizados de acuerdo a 4 grandes parámetros.    
    #""")
    
    
    st.image("https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/XARTT_1.PNG", caption="Figura 1: Aspectos importantes de la publicación científica.")

    #st.write("""
    #Relata una división general acerca de los análisis estadísticos necesarios para un estudio de cohorte.
    #""")
    
    # Imagen 2
    st.image("https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/XARTT_2.PNG", caption="Figura 2: El papel del revisor en la publicación científica.")

    # Imagen 3
    st.image("https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/XARTT_2b.PNG", caption="Figura 3: Como planear tu primer artículo.")

    # Imagen 4
    st.image("https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/XARTT_3.PNG", caption="Figura 4: Tips para contar una buena historia.")

    # Imagen 5
    st.image("https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/XARTT_4.PNG", caption="Figura 5: Tips para sobrevivir a la revisión por pares.")


    # Enlace adicional
    st.write("### Lucha contra las revistas y los congresos predadores")
    st.markdown(
    '[Haz clic aquí para acceder al documento](https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/Summary%20report.pdf)',
    unsafe_allow_html=True)

def noviembre_dosdos():
    import streamlit as st

    titulo = "Seminario del 22 de noviembre: Análisis de marcadores antropométricos de sarcopenia utilizando modelos de aprendizaje supervisado "
    st.title(titulo)

    # Datos del autor
    foto1 = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/Arceo_S.jpg"
    imagen_derecha_url = "https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/SARC_0.PNG"
    nombre1 = "Santiago Arceo Díaz"
    grado1 = "Doctor en Ciencias (Astrofísica)"
    reseña1 = ("Licenciatura y Maestría en Física y Doctor en Ciencias (Astrofísica), por las Universidades de Colima y Guanajuato, respectivamente. "
              "En su formación académica se especializó en la creación de modelos analíticos y numéricos, aplicados a las ciencias exactas y a la ingeniería aplicada. "
              "Dentro de la astrofísica, su área de investigación se centra en la evolución estelar y su relación con la tasa de producción de neutrinos y axiones, "
              "concretamente las estrellas gigantes rojas. También ha realizado trabajos en múltiples áreas de la ingeniería y la arquitectura (con simulaciones numéricas "
              "aplicadas a la sostenibilidad ambiental de las que se han realizado 6 tesis de maestría). Se encuentra realizando una estancia postdoctoral en la Universidad "
              "de Colima en la que se enfoca en el uso del machine learning para la clasificación de pacientes geriátricos, a partir de variables antropométricas.")
    
    correo1 = "santiagoarceo@ucol.mx"
    perfil_scholar1 = "https://scholar.google.com.mx/citations?user=SFgL-gkAAAAJ&hl=en"

    
    # Mostrar la imagen del autor
    st.markdown(f'''
    <div style="text-align: center;">
        <img src="{foto1}" alt="{nombre1}" style="width: 300px; border-radius: 10px;">
        <div style="font-family: Times New Roman; font-size: 14px; margin-top: 5px;">
            <em>Dr. Santiago Arceo Díaz</em>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    # Título de la sección "Acerca del autor" debajo de la imagen
    st.markdown(f'''
    <div style="text-align: center; font-family: Times New Roman; font-size: 16px; font-weight: bold; margin-top: 10px;">
        Acerca de la autora
    </div>
    ''', unsafe_allow_html=True)

    st.markdown(f'''
    <div style="text-align: center; font-family: Times New Roman; font-size: 16px; font-weight: bold;">
        
    </div>
    <div style="margin-top: 10px; text-align: justify; font-family: Times New Roman; font-size: 14px;">
        
    </div>
    ''', unsafe_allow_html=True)
    
    # Mostrar la reseña del autor y contacto
    st.markdown(f'''
    <div style="text-align: justify; font-family: Times New Roman; font-size: 14px;">
        <strong>{nombre1}</strong>{", " + grado1 if grado1 else ""}. 
        {reseña1 if reseña1 else ""} <br><br>
        <strong>Puedes contactar al autor por correo electrónico:</strong> <a href="mailto:{correo1}">{correo1}</a> <br><br>
        <strong>Perfil en Google Scholar:</strong> <a href="{perfil_scholar1}" target="_blank">{perfil_scholar1}</a>
    </div>
    ''', unsafe_allow_html=True)


    st.markdown(f'''
    <div style="text-align: center; font-family: Times New Roman; font-size: 16px; font-weight: bold;">
        
    </div>
    <div style="margin-top: 10px; text-align: justify; font-family: Times New Roman; font-size: 14px;">
        
    </div>
    ''', unsafe_allow_html=True)
    
    # Información sobre la plática
    resumen_platica = (
        "Se muestran los resultados mediante algoritmos de aprendizaje no supervisado a una muestra de derechohabientes de las Delegaciones Sur y Norte del Instituto Mexicano del Seguro Social. Particularmente, se describe una estrategia para generar un diagnóstico inicial de sarcopenia a partir de las medidas antropométricas y de desempeño físico de las personas adultas mayores. Se comparan dos estrategias: una en la que se recurre al cribado secuencial de pacientes (siguiendo las recomendaciones del Grupo Europeo de trabajo para el estudio de sarcopenia en personas ancianas, EWGSOP2) y otra en la que se clasifica para los pacientes utilizado simultáneamente la fuerza de agarre, el índice de masa muscular esquelética y la velocidad de marcha. Además, se discute la incidencia de algunas comorbilidades en los grupos de pacientes con sarcopenia descartada y no descartada.")
    
    enlace_pdf = "https://acortar.link/aS2bXR"
    #https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/Publicacion%20para%20principiantes-LAB.pdf"

    st.markdown(f'''
    <div style="text-align: center; font-family: Times New Roman; font-size: 16px; font-weight: bold;">
        Resumen de la plática
    </div>
    <div style="margin-top: 10px; text-align: justify; font-family: Times New Roman; font-size: 14px;">
        {resumen_platica}
    </div>
    ''', unsafe_allow_html=True)


#st.markdown(f'''
#<div style="text-align: center; font-family: Times New Roman; font-size: 16px; font-weight: bold;">
#    Resumen de la plática
#</div>
#<div style="margin-top: 10px; text-align: justify; font-family: Times New Roman; font-size: 14px;">
#    {resumen_platica}
#</div>
#''', unsafe_allow_html=True)

    
    st.markdown(f'[Haz clic aquí para ver las diapositivas]({enlace_pdf})')

    # Generar y descargar el PDF
    #pdf = generar_pdf(titulo, nombre1, correo1, grado1, resumen_platica, enlace_pdf)
    #pdf = generar_pdf(titulo, foto1, nombre1, grado1, reseña1, correo1, perfil_scholar1, resumen_platica, enlace_pdf)
    pdf = generar_pdf(titulo, foto1, imagen_derecha_url, nombre1, grado1, reseña1, correo1, perfil_scholar1, resumen_platica, enlace_pdf)

    st.download_button(
        label="Descargar PDF con los datos del evento",
        data=pdf,
        file_name="evento_22_noviembre.pdf",
        mime="application/pdf",
    )

    # Sección "Preguntas Clave"
    st.subheader("Preguntas Clave")
    st.write("""
1. **¿Cuáles son las principales comorbilidades asociadas con la sarcopenia en la muestra de participantes y cómo varían entre hombres y mujeres?**

2. **¿Qué métodos de diagnóstico y evaluación de severidad se utilizan para identificar la sarcopenia según el consenso EWGSOP2?**

3. **¿Cómo se valida la ecuación IMMEA y cuáles son las variables antropométricas principales utilizadas en su cálculo?**

4. **¿Qué resultados principales se obtuvieron al aplicar modelos de clustering a los datos de fuerza de agarre, IMMEA y velocidad de marcha?**

5. **¿Cuáles son los puntos de corte antropométricos sugeridos para diagnosticar sarcopenia en hombres y mujeres?**

6. **¿Qué diferencias significativas se observaron entre los pacientes con sarcopenia grave y los pacientes clasificados como no graves en términos de fuerza, IMMEA y velocidad de marcha?**

7. **¿Qué rol desempeñan los modelos de árboles de decisión en la clasificación de pacientes con sarcopenia y cómo coinciden con los puntos de corte propuestos por el consenso?**

8. **¿Qué proporción de la muestra total corresponde a pacientes con sarcopenia y cómo están distribuidos en las categorías de severidad?**

9. **¿Qué variables adicionales, como circunferencia de pantorrilla, cintura y brazo, pueden servir como discriminadores de sarcopenia según estudios complementarios?**

10. **¿Qué limitaciones o discrepancias se encontraron al comparar los datos de desempeño físico (velocidad de marcha) con los valores de fuerza e IMMEA para clasificar sarcopenia?**
    """)

    # Sección "Material complementario"
    st.subheader("Material complementario")

    # Imagen 1
    #st.write("""Esta diapositiva habla acerca de que existen diversos tipos de cohorte categorizados de acuerdo a 4 grandes parámetros.    
    #""")
    
    
    st.image("https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/XARTT_1.PNG", caption="Figura 1: Aspectos importantes de la publicación científica.")

    #st.write("""
    #Relata una división general acerca de los análisis estadísticos necesarios para un estudio de cohorte.
    #""")
    
    # Imagen 2
    st.image("https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/XARTT_2.PNG", caption="Figura 2: El papel del revisor en la publicación científica.")

    # Imagen 3
    st.image("https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/XARTT_2b.PNG", caption="Figura 3: Como planear tu primer artículo.")

    # Imagen 4
    st.image("https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/XARTT_3.PNG", caption="Figura 4: Tips para contar una buena historia.")

    # Imagen 5
    st.image("https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/XARTT_4.PNG", caption="Figura 5: Tips para sobrevivir a la revisión por pares.")


    # Enlace adicional
    st.write("### Lucha contra las revistas y los congresos predadores")
    st.markdown(
    '[Haz clic aquí para acceder al documento](https://raw.githubusercontent.com/SArcD/Seminario_CUIB_2024/main/Summary%20report.pdf)',
    unsafe_allow_html=True)






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
    **Correo:** santiagoarceo@ucol.mx
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
    elif selected_page == "13 de septiembre: Mariano, Julio y Minerva":
        septiembre_trece()
    elif selected_page == "04 de octubre: Fernanda y Michel":
        octubre_cuatro()
    elif selected_page == "18 de octubre: Ricardo y Fernanda García":
        octubre_dieciocho()
    elif selected_page == "15 de noviembre: Xóchitl Trujillo":
        noviembre_quince()
    elif selected_page == "22 de noviembre: Santiago Arceo":
        noviembre_dosdos()
    # Aquí añadirás funciones similares para cada una de las fechas/eventos

if __name__ == "__main__":
    main()
