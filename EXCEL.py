import tabula

df = '/home/andre/projetos/pdf/2017.pdf'
output = '/home/andre/projetos/pdf/2017.json'

tabula.convert_into(df, output, output_format="json", pages="all")

##tabula.convert_into_by_batch(df, output_format="XLSX", pages="all")
