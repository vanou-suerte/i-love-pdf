from pypdf import PdfReader, PdfWriter
import argparse
import os

def split_pdf_by_page_count(input_path: str, pages_per_part: int =1, output_dir: str = "output_parts"):

    reader = PdfReader(input_path)
    total_pages = len(reader.pages)

    os.makedirs(output_dir, exist_ok=True)

    part_number = 1
    for start in range(0, total_pages, pages_per_part):
        writer = PdfWriter()
        end = min(start + pages_per_part, total_pages)

        for page_num in range(start, end):
            writer.add_page(reader.pages[page_num])

        output_path = os.path.join(output_dir, f"part_{part_number}.pdf")
        with open(output_path, "wb") as output_file:
            writer.write(output_file)

        print(f"Fichier gen : {output_path}")
        part_number += 1


def merge_pdfs(pdf_paths: list, output_path: str):

    writer = PdfWriter()

    for pdf in pdf_paths:
        reader = PdfReader(pdf)
        for page in reader.pages:
            writer.add_page(page)

    with open(output_path, "wb") as output_file:
        writer.write(output_file)

    print(f"pdf fusio : {output_path}")


def main():
    
    parser = argparse.ArgumentParser(
    description="Découpage et fusion de fichiers PDF"
    )
    
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    split_parser = subparsers.add_parser("split")
    
    split_parser.add_argument("input_pdf")
    split_parser.add_argument("-p", "--pages-per-part", type=int, default=1)
    split_parser.add_argument("-o", "--output-dir", default="output_parts", help="Dossier de sortie")
    

    merge_parser = subparsers.add_parser("merge")
    merge_parser.add_argument("pdfs",nargs="+")
    merge_parser.add_argument("-o", "--output", required=True, help="PDF de sortie")
    args = parser.parse_args()

    if args.command == "split":
        split_pdf_by_page_count(args.input_pdf, args.pages_per_part,args.output_dir)

    elif args.command == "merge":
        merge_pdfs(args.pdfs, args.output)

    # input_pdf = "CorentinGoat-leGoat.pdf"

    # split_pdf_by_page_count(input_pdf)

    # pdfs_to_merge = [
    #     "output_parts/part_1.pdf",
    #     "output_parts/part_2.pdf"
    # ]
    
    # merge_pdfs(pdfs_to_merge, "merged_output.pdf")


if __name__ == "__main__":
    main()