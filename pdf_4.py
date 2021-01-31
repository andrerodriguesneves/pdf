import PyPDF2

pdf_file_obj = open("2017.pdf", 'rb')

pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

REMOCAO = 'OrdemEntidade DevedoraProtocoloPrecatórioSituaçãoProc. OriginárioNaturezaAnoPriori.Valor HistóricoPago'


for row in range(pdf_reader.numPages):
    pageobj = pdf_reader.getPage(row)
    print(pageobj.extractText().replace(REMOCAO, ''))
