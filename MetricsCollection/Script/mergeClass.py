# Pre-processamento de dados não estruturados

import numpy as np # array and vector manipulation
import pandas as pd # data manipulation
import csv
a = "zxing"
testsmells_class_data = pd.read_csv("../Dados/"+a+"/testsmells-class.csv")
class_data = pd.read_csv("../Dados/"+a+"/class.csv")

# Removendo instâncias $Anonymous
class_data.drop(class_data[class_data["type"] != "class"].index, inplace=True)
# Obtendo tamanho atual das linhas
class_data_lines = class_data.shape[0]
testsmells_class_data_lines = testsmells_class_data.shape[0]

  
# Removendo instâncias de classes de teste
class_data.drop(class_data[class_data["class"].str.contains("Test")].index, inplace=True)

# Renomeando coluna de nomes de classes do testsmells_class_data
testsmells_class_data = testsmells_class_data.rename(columns={'ProductionFileName': 'file'})

# Removendo coluna App
testsmells_class_data = testsmells_class_data.drop(['App'], axis=1)

# Unindo dados das duas tabelas
joined_data = pd.merge(class_data, testsmells_class_data, on="file")

# Removendo colunas duplicadas no JNose
joined_data = joined_data.drop(['numberMethods'], axis=1)
joined_data = joined_data.drop(['LOC'], axis=1)
joined_data = joined_data.drop(['type'], axis=1)

print(joined_data)
joined_data.to_csv(r'/home/luana-martins/Área de Trabalho/ML/ClassMetrics/'+a+'.csv', index = False, header=True)
