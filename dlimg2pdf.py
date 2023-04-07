import os
import requests
from io import BytesIO
from PIL import Image
from fpdf import FPDF

# 画像のURLリスト
image_urls = [
    "https://domain/path/to/image/image-000001.jpg",
    "https://domain/path/to/image/image-000002.jpg",
    "https://domain/path/to/image/image-000003.jpg",
]

# 画像を保存するディレクトリ
image_dir = "./images"

# 画像をダウンロードし、PDFファイルを作成する関数
def create_pdf(image_urls, output_path):
    pdf = FPDF()

    for i, url in enumerate(image_urls):
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))

        # 画像を保存する
        img_path = os.path.join(image_dir, f"image_{i+1}.jpg")
        img.save(img_path)

        # PDFにページを追加する
        pdf.add_page()
        pdf.image(img_path)

    # PDFファイルを保存する
    pdf.output(output_path, "F")

    # 保存した画像を削除する
    for i in range(len(image_urls)):
        img_path = os.path.join(image_dir, f"image_{i+1}.jpg")
        os.remove(img_path)

# PDFファイルを生成する
create_pdf(image_urls, "output.pdf")
