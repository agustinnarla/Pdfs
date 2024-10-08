import streamlit as st
import PyPDF2

#Asignamos la ruta donde se va a guardar el pdf final
output_pdf = 'documents/pdf_final.pdf'

def unir_pdf(output_path, documentos):
    pdf_final = PyPDF2.PdfMerger()

    for documento in documentos:
        pdf_final.append(documento)

    pdf_final.write(output_path)



st.header("Unir pdf")
st.subheader("Subir los pdf a unir")

pdf_adjuntados = st.file_uploader(label= "",accept_multiple_files=True)

unir = st.button(label="Unir")

if unir:
    #Comprobamos que se hayan subido al menos 2 pdf
    if len(pdf_adjuntados) <- 1:
        st.error("Debes subir al menos 2 pdf")
    else:
        unir_pdf(output_pdf, pdf_adjuntados)

        st.success("PDF unidos correctamente")
        #Abrimos el pdf en formato de lectura
        with open(output_pdf, "rb") as file:
            #Leemos el pdf
            pdf_data = file.read()
            #Descargamos el pdf
        st.download_button(
            label="Descargar PDF",
            data=pdf_data,
            file_name=output_pdf,
        )
