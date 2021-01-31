import csv
import re

arquivo = open("2020.csv")

exemple_reader = csv.reader(arquivo)

lista = list(exemple_reader)



for row in lista:
    print(row)


# for row in exemple_reader:
#     # if texto or controle > 0:
#     #     print('Row #' + str(exemple_reader.line_num) + ' ' + str(row))
#     #
#     #     controle += 1
#     # ['Ordem', 'Entidade\nDevedora', 'Protocolo', 'Precatório', 'Situação', 'Proc. Originário', 'Natureza', 'Ano', 'Priori.', 'Valor Histórico', 'Pago']
#
#
#         #print('Row #' + str(exemple_reader.line_num) + ' ' + str(row))
# #    print(str(row).replace('[', '').replace(']', '').replace(r'\n', ''))
#     #if str(row)[0:3] != "['O":
#     if not bool(re.search(r'ordem|últimos|comum|idoso', str(row), re.IGNORECASE)) and str(row)[0:3] != "'',":
#         print(str(row).replace('[', '').replace(']', ''))
#

