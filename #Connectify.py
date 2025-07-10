# empresa Connectify
#Projeto fictício de uma loja de smartphone e acessórios chamada Connectify,
#ela atua em 2 endereços, um no RJ e outro em SP, e tem um presença online há quase 1 ano.

# criando de df para a empresa Connectify.

import pandas as pd
from tabulate  import tabulate

df_canal_vendas = pd.DataFrame ({
'id_loja' : [1,2,3 ],
'endereco': ['Botafogo Praia Shopping', 'Shopping Itaquera', 'Loja Online Connectify'],
'telefone': [ '21985856262', '11963632525', '21978454578']
})

df_funcionarios = pd.DataFrame({
    'id_funcionario': [1,2,3,4,5,6,7,8,9,10,11],
    'Nome': ['Jose Dias', 'Maycon Castro', 'Ana Beatriz', 'Lucas Mello', 'Bruna Costa', 'Marcos Lima', 'Carla Mendes', 'Tiago Rocha', 'Fernanda Alves', 'Ricardo Pinto', 'Juliana Ramos'],
    'idade': [28, 34, 25, 31, 29, 40, 27, 36, 33, 38, 30],
    'sexo': ['M', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
    'whatsapp': ['(21) 91234-5678', '(11) 99876-5432', '(31) 98765-4321', '(41) 97654-3210', '(51) 96543-2109', '(61) 95432-1098', '(71) 94321-0987', '(81) 93210-9876', '(91) 92109-8765', '(19) 91098-7654', '(27) 90987-6543']
})


df_funcionarios.to_csv('canais.csv', index=False)

df_produtos = pd.DataFrame ({
'id_produto' : [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],
'produtos' : ['iPhone 16 Pro Max', 'iPhone 16 Pro', 'iPhone 16', 'iPhone 16 Mini', 'Samsung Galaxy S25 Ultra', 'Samsung Galaxy S25+', 'Samsung Galaxy S25', 'Samsung Galaxy Buds Pro', 'Samsung Wireless Charger', 'Samsung Galaxy Watch 6', 'Apple AirPods Pro 3', 'Apple Watch Series 9', 'Apple Lightning Cable', 'Samsung Fast Cable', 'PowerLine USB-C Cable', 'Beats Studio Buds', 'Sony WH Headphones', 'JBL Tune Earbuds', 'Fitbit 4 Smartwatch', 'Garmin Forerunner 255', 'Apple MagSafe Charger', 'Samsung Galaxy SmartTag', 'Apple Lightning Cable', 'Samsung Galaxy Watch 6', 'Anker Wireless Charging Pad'],
'valor': [7999.99, 6999.99, 5999.99, 4999.99, 8999.99, 8499.99, 7999.99, 1299.99, 499.99, 1999.99, 1799.99, 3499.99, 149.99, 129.99, 99.99, 899.99, 1599.99, 749.99, 1399.99, 1299.99, 399.99, 299.99, 149.99, 2499.99, 399.99]
})

#Ler arquivo em excel
df_vendas = pd.read_excel(r"C:\Users\Lucas Santos\OneDrive\Desktop\ProjetoPython\Projeto Connectify\vendas c.xlsx")


# print(tabulate(df_produtos, headers= 'keys', tablefmt= 'grid'))
# print(tabulate(df_canal_vendas, headers= 'keys', tablefmt= 'grid'))
# print(tabulate(df_vendas, headers= 'keys', tablefmt= 'grid'))
print(df_vendas)


df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda']).dt.date
# df_filtrado = df_vendas[(df_vendas['id_venda'] >= 1) & (df_vendas['id_venda'] <= 100)]
# print(tabulate(df_filtrado, headers='keys', tablefmt='grid', showindex=True))
print(df_vendas)

# CONCATENADO ABAIXO
df_vendas.to_csv('vendas.csv', index=False)
df_produtos.to_csv('produtos.csv', index=False)
df_canal_vendas.to_csv('canais.csv', index=False)
df_funcionarios.to_csv('funcionarios.csv', index=False)