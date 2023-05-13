# Direccion de donde se extrajo el codigo
# https://medium.com/python-in-plain-english/extracting-data-from-pdf-files-with-python-and-pdfquery-de84e9232b62
#
#	Otra pagina interesante para estudiar es:
#
#	Python — Working with PDF file : https://medium.com/@olabisisulaiman/python-working-with-pdf-file-4e78c5b6bae2
#

import pdfquery
import pandas as pd

pdf_files = ['patient1pdf.pdf','patient2pdf.pdf','patient3pdf.pdf']

def clean_text_data(text):
  return text.split(':')[1]


def pdf_to_df(pdf_files):

        patient_data = {"Patient Number": [],
                       "Patient Name": [],
                       "DOB": [],
                       "Diagnosis": [],
                       "Treatment": [],
                       "Recommendation": []}

        for i in pdf_files: 
                pdf = pdfquery.PDFQuery(i)
                pdf.load()

                patient_data["Patient Number"].append(clean_text_data(pdf.pq('LTText\LineHorizontal:contains("Patient Number")').text()))

                patient_data["Patient Name"].append(clean_text_data(pdf.pq('LTText\LineHorizontal:contains("Patient Name")').text()))

                patient_data["DOB"].append(clean_text_data(pdf.pq('LTText\LineHorizontal:contains("DOB")').text()))

                patient_data["Diagnosis"].append(clean_text_data(pdf.pq('LTText\LineHorizontal:contains("Diagnosis")').text()))

                patient_data["Treatment"].append(clean_text_data(pdf.pq('LTText\LineHorizontal:contains("Treatment")').text()))
				                                         
                patient_data["Recommendation"].append(clean_text_data(pdf.pq('LTText\LineHorizontal:contains("Recommendation")').text()))


        columns=["Patient Number","Patient Name","DOB","Diagnosis","Treatment","Recommendation"]

        pdata = pd.DataFrame.from_dict(patient_data)
        pdata = pdata[columns]
        
        return pdata 	 

pdata = pdf_to_df(pdf_files)
