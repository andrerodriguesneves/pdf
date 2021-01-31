import tabula

df = '/home/andre/projetos/pdf/2017.pdf'


df_2 = tabula.read_pdf(df, pages="all")

print(df_2)