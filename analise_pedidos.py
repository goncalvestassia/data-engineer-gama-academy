# crie um script que leia 2 arquivos no python utilizando pandas, "clientes.csv" e "pedidos.csv" 
# depois relacione os dos arquivos carregados no dataframe pelos campos cliente_df["id"] = pedidos_df["id"] 
# mostrando um relatório agrupado com a soma total de pedidos por clientes

import pandas as pd

clientes_df = pd.read_csv("clientes.csv")
pedidos_df = pd.read_csv("pedidos.csv")

merged_df = pd.merge(clientes_df, pedidos_df, left_on='id', right_on='cliente_id')
# merged_df = clientes_df.merge(pedidos_df, left_on='id', right_on='cliente_id')

grouped_df_count = merged_df.groupby(['nome']).agg({'valor_total':'count'}) # quantidade de pedidos por cliente
grouped_df_sum = merged_df.groupby(['nome']).agg({'valor_total':'sum'})  # valor total vendido por cliente
grouped_df_max = merged_df.groupby(['nome']).agg({'valor_total':'max'})  # valor maior vendido por cliente
grouped_df_min = merged_df.groupby(['nome']).agg({'valor_total':'min'})  # valor minimo vendido por cliente

print("-" * 60)
print(grouped_df_count)
print("-" * 60)
print(grouped_df_sum)
print("-" * 60)
print(grouped_df_max)
print("-" * 60)
print(grouped_df_min)


print(merged_df.describe())