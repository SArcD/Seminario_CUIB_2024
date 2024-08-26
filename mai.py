import streamlit as st

# Configuración de la barra lateral para la selección de la página
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

# Función para mostrar el contenido de cada página
def show_page(page):
    if page == "Inicio":
        st.title("Calendario de Eventos Académicos")
        st.write("Selecciona una fecha en la barra lateral para ver más detalles.")
    elif page == "30 de agosto: Miguel Huerta":
        st.title("30 de agosto: Miguel Huerta")
        st.write("**Tema:** Creación y tipos de hipótesis")
    elif page == "06 de septiembre: Mónica Ríos":
        st.title("06 de septiembre: Mónica Ríos")
        st.write("**Tema:** Aspectos de la investigación científica")
    elif page == "13 de septiembre: Mariano, Julio y Minerva":
        st.title("13 de septiembre: Mariano, Julio y Minerva")
        st.write("**Tema:** Diseños experimentales")
    elif page == "20 de septiembre: Daniela Rios y Victoria García y Julián":
        st.title("20 de septiembre: Daniela Rios, Victoria García y Julián")
        st.write("**Tema:** Bioética y diseño experimental")
    elif page == "27 de septiembre: Julián":
        st.title("27 de septiembre: Julián")
        st.write("**Tema:** Diseño experimental: ejercicio")
    elif page == "04 de octubre: Fernanda y Cesar":
        st.title("04 de octubre: Fernanda y Cesar")
        st.write("**Tema:** Estudios transversales")
    elif page == "11 de octubre: Yoli y Mónica Ríos":
        st.title("11 de octubre: Yoli y Mónica Ríos")
        st.write("**Tema:** Casos y controles")
    elif page == "18 de octubre: Ricardo y Fernanda García":
        st.title("18 de octubre: Ricardo y Fernanda García")
        st.write("**Tema:** Estudios de cohorte")
    elif page == "25 de octubre: Liliana y Alondra":
        st.title("25 de octubre: Liliana y Alondra")
        st.write("**Tema:** Ensayos clínicos")
    elif page == "08 de noviembre: Paola García y Angie Del Toro":
        st.title("08 de noviembre: Paola García y Angie Del Toro")
        st.write("**Tema:** Investigación científica del cambio ambiental")
    elif page == "15 de noviembre: Xóchitl Trujillo":
        st.title("15 de noviembre: Xóchitl Trujillo")
        st.write("**Tema:** Aspectos de las publicaciones científicas y el emprendimiento")
    elif page == "22 de noviembre: Santiago Arceo":
        st.title("22 de noviembre: Santiago Arceo")
        st.write("**Tema:** Machine-learning en el análisis clínico")
    elif page == "29 de noviembre: Alberto Bricio y Ricardo Marentes y Valeria Ibarra":
        st.title("29 de noviembre: Alberto Bricio, Ricardo Marentes y Valeria Ibarra")
        st.write("**Tema:** Bioética e Investigación clínica y Retribución social")

# Mostrar el contenido de la página seleccionada
show_page(page)
