import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader


if __name__ == "__main__":
    df = pd.read_excel("sales_data.xlsx", sheet_name=0)
    df = df.dropna()
    print(df.shape)

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace(",", ".")
    .astype(float)
    )

    df = df[df["Quantity"] > 0]

    df = df.drop_duplicates()

    df = df.dropna()
    

    df["Total"] = df["Quantity"] * df["Price"]

    print(df.head())

    print("Total rows after cleaning: " + str(len(df)))






    category_sales = df.groupby("Category")["Total"].sum()

    plt.figure()
    category_sales.plot(kind="bar")
    plt.title("Total Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Sales (€)")
    plt.tight_layout()

    plt.savefig("sales_by_category.png")
    plt.close()





    pdf = canvas.Canvas("sales_report.pdf", pagesize=A4)
    width, height = A4

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, height - 50, "Sales Report")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, height - 80, f"Total sales: €{df['Total'].sum():.2f}")
    pdf.drawString(50, height - 100, f"Number of transactions: {len(df)}")








    img = ImageReader("sales_by_category.png")
    img_width, img_height = img.getSize()

    display_width = 400
    display_height = (display_width / img_width) * img_height

    x = (width - display_width) / 2
    y = (height - display_height) / 2 - 50

    pdf.drawImage(
        img,
        x,
        y,
        width=display_width,
        height=display_height
    )

    pdf.save()