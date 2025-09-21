import PyPDF2
import os

# List of PDFs to merge
pdfs = [  r"E:\Learning\Project Python\Documents\enigma-trainee-muhammad-alwansyah-mardika-java-spring-boot---reactjs--react-native-1709799780767.pdf",  r"E:\Learning\Project Python\Documents\TraineeScoring_Muhammad Alwansyah Mardika.docx.pdf"]

merger = PyPDF2.PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged_output.pdf")
merger.close()

#  Try Modifying:  
# - Add GUI using Tkinter  
# - Sort files by name or date  
# - Allow user input for file selection