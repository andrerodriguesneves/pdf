import tabula

df = '/home/andre/projetos/pdf/'
output = '/home/andre/projetos/pdf/2017.csv'

##tabula.convert_into(df, output, output_format="csv", pages="all")

tabula.convert_into_by_batch(df, output_format="csv", pages="all")
