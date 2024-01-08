import PyPDF2
import os

def split_pdf(input_pdf, pages_per_section):

    if not os.path.exists(input_pdf):
        print("The specified file does not exist")
        return

    pdf_file = open(input_pdf, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    total_pages = len(pdf_reader.pages)
    sections = total_pages // pages_per_section

    for i in range(sections):
        pdf_writer = PyPDF2.PdfWriter()


        start_page = i * pages_per_section
        end_page = start_page + pages_per_section

        for page_num in range(start_page, min(end_page, total_pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)


        output_filename = f'sections/output_section_{i+1}.pdf'
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)

        print(f'Created: {output_filename}')

    pdf_file.close()

# Replace 'input.pdf' with the path to your PDF, and 10 with the desired number of pages per split
split_pdf('2024GameManual.pdf', 10)
