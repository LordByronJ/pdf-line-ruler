
import sys
import pdfplumber

def calculate_total_edge_length(pdf_path):
    total_length = 0.0
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            for edge in page.edges:
                # Only considers edges that are rect_edge and curve_edge
                if edge["object_type"] == "rect_edge":
                    # Straight line segment
                    start_x, start_y = edge["x0"], edge["y0"]
                    end_x, end_y = edge["x1"], edge["y1"]
                elif edge["object_type"] == "curve_edge":
                    # Approximate length of cuved line using diag line:
                    start_x, start_y = edge["x0"], edge["top"]
                    end_x, end_y = edge["x1"], edge["bottom"]
                # Calculate Euclidean distance
                length = ((end_x - start_x) ** 2 + (end_y - start_y) ** 2) ** 0.5
                total_length += length
    return total_length

if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print('Usage: python3 main.py <Path to PDF file> <Optional: Path to known length PDF file> <Optional: time takes to cut PDF file in any time units>')
        exit(1)
    pdf_file = sys.argv[1]
    total_edge_length = calculate_total_edge_length(pdf_file)
    total_edge_length_inches = total_edge_length/72
    print(f"Total length of edges in {pdf_file}: {total_edge_length:.2f} pixels, {total_edge_length_inches:.2f} inches")
    if len(sys.argv) < 4:
        exit(0)
    known_length_pdf_file = sys.argv[2]
    known_total_edge_length = calculate_total_edge_length(known_length_pdf_file)
    time_to_cut = float(sys.argv[3])
    print(f"Total time to cut {pdf_file}: {time_to_cut / known_total_edge_length * total_edge_length:.2f}")
