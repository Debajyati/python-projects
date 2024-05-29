import PyPDF2
import sys


def copy_pages(input_pdf_path, output_pdf_path, from_page, to_page, destination_page):
    with open(input_pdf_path, "rb") as input_file:
        reader = PyPDF2.PdfReader(input_file)
        writer = PyPDF2.PdfWriter()

        # Check for valid page indexes
        if from_page < 0 or from_page >= len(reader.pages):
            raise ValueError(f"Invalid 'from_page' index: {from_page}")

        if to_page < from_page or to_page >= len(reader.pages):
            raise ValueError(f"Invalid 'to_page' index: {to_page}")

        if destination_page < 0 or destination_page > len(reader.pages):
            raise ValueError(f"Invalid 'destination_page' index: {destination_page}")

        # Copy pages to a new PDF
        for page_num in range(from_page, to_page + 1):
            page = reader.pages[page_num]
            writer.add_page(page)

        # Read the destination PDF file and insert the copied pages at the desired index
        with open(output_pdf_path, "rb") as output_file:
            destination_reader = PyPDF2.PdfReader(output_file)
            destination_writer = PyPDF2.PdfWriter()

            # Insert pages before the destination page index
            for page_num in range(destination_page):
                page = destination_reader.pages[page_num]
                destination_writer.add_page(page)

            # Insert the copied pages at the destination page index
            for page_num in range(len(writer.pages)):
                page = writer.pages[page_num]
                destination_writer.add_page(page)

            # Insert remaining pages after the destination page index
            for page_num in range(destination_page, len(destination_reader.pages)):
                page = destination_reader.pages[page_num]
                destination_writer.add_page(page)

            # Save the result to the output file
            with open(output_pdf_path, "wb") as output_file_final:
                destination_writer.write(output_file_final)


if __name__ == "__main__":
    try:
        # Grab all 4 arguments:
        input_pdf_path =  sys.argv[1] # PATH of the input pdf
        if input_pdf_path == "-h" or input_pdf_path == "--help" :
            helptext = '''
\033[36m Usage\033[0m:

╔═  ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════  ═╗

║                                                                                                                         ║
║   \033[32mpython PDFsplitter.py [input_pdf_path] [output_pdf_path] [from_page_index] [to_page_index] [destination_page_index]\033[0m   ║
║                                                                                                                         ║

╚═  ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════  ═╝

\033[36m Description\033[0m:

\033[33m This program allows you to copy a specified range of pages from an input PDF document and insert them into an existing output PDF document at a specified destination page index.\033[0m

\033[36m Arguments\033[0m:

1.\033[32m input_pdf_path\033[0m: Path to the input PDF document from which pages will be copied.
2.\033[32m output_pdf_path\033[0m: Path to the output PDF document where the copied pages will be inserted. Note that the output PDF must have at least one page.
3.\033[32m from_page_index\033[0m: 0-based index of the first page to copy from the input PDF.
4.\033[32m to_page_index\033[0m: 0-based index of the last page (inclusive) to copy from the input PDF.
5.\033[32m destination_page_index\033[0m: 0-based index at which to insert the copied pages into the output PDF.

            '''
            print(helptext)
        else:
            output_pdf_path = sys.argv[2] # PATH of the output pdf (The output pdf must have atleast 1 page. An entirely empty file with a `.pdf` extension won't work)
            from_page_index = int(sys.argv[3])  # Start copying from this page index (0-based)
            to_page_index = int(sys.argv[4])  # Copy pages up to this page index (inclusive)
        
            if len(sys.argv) > 5:
                destination_page_index = int(sys.argv[5])  # Insert the copied pages before this page index (0-based)
            else:
                destination_page_index = 0  # Default value if not provided 

            copy_pages(
                input_pdf_path,
                output_pdf_path,
                from_page_index,
                to_page_index,
                destination_page_index,
            )

    except:
        print("\033[32mUnexpected error occured.\033[0m")
        print('''
        To know how to use the program, run -
        `python3 PDFsplitter.py --help` or, python3 PDFsplitter.py -h
        ''')
