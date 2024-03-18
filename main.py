from fpdf import FPDF
import pandas as pd


def main():
    df = pd.read_csv("topics.csv")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False, margin=0)

    for index, row in df.iterrows():
        pdf.add_page()
        pdf.set_font(family="Times", style="BI", size=24)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="C", ln=1, border=0)
        pdf.line(10, 24, 200, 24)
        for n in range(24, 280, 15):
            pdf.line(10, n, 200, n)

        # Set the footer
        pdf.ln(260)
        pdf.set_font(family="Times", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        for i in range(row["Pages"] - 1):
            pdf.add_page()
            # Set the footer for the other pages
            pdf.ln(272)
            pdf.set_font(family="Times", size=8)
            pdf.set_text_color(180, 180, 180)
            pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
            for n in range(0, 280, 15):
                pdf.line(10, n, 200, n)

    pdf.output("output.pdf")


if __name__ == "__main__":
    main()
