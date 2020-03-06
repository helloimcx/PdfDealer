# encodeing-utf8
from PyPDF2 import PdfFileReader, PdfFileWriter

def verticalCut(filename: str):
    if len(filename) == 0:
        return
    # 获取一个 PdfFileReader 对象,加strict是让其不要报错
    pdf_input1 = PdfFileReader(open(filename, 'rb'), strict = False)
    pdf_input2 = PdfFileReader(open(filename, 'rb'), strict = False)
    # 获取 PDF 的页数
    page_count = pdf_input1.getNumPages()
    page1 = pdf_input1.getPage(0)

    # 获取pdf文件的宽度
    old_width = page1.mediaBox.getUpperRight_x()

    ''' 处理要输出的pdf文件'''
    # 生成一个 PdfFileWriter 对象，用于输出pdf
    pdf_output = PdfFileWriter()
    # 垂直裁剪pdf并复制到输出对象中
    for i in range(page_count):
        page1 = pdf_input1.getPage(i)
        page2 = pdf_input2.getPage(i)
        page1.mediaBox.lowerRight = (float(old_width) * 0.5, 0)
        page2.mediaBox.lowerLeft = (float(old_width) * 0.5, 0)
        pdf_output.addPage(page1)
        pdf_output.addPage(page2)

    '''将修改后的pdf文件输出'''
    with open('{}_cut.pdf'.format(filename[:-4]), "wb") as outputFile:
        pdf_output.write(outputFile)

    print("done!")
