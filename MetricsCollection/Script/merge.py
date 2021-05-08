# Importing libraries
import numpy as np # array and vector manipulation
import pandas as pd # data manipulation
import csv

countClasses = 0
countTests = 0

# Processing all projects
fileName = open('names.txt')
names = fileName.readlines()
for name in names:
    name = name.rstrip("\n")
    # Copy file class file with oo metrics and test files with test smells 
    testsmells_class_data = pd.read_csv("../Dados/"+name+"/testsmells-class.csv")
    class_data = pd.read_csv("../Dados/"+name+"/class.csv")
    test_data = pd.read_csv("../Dados/"+name+"/class.csv")
    
    # Removing all files that are not classes (e.g., enum and interface)
    class_data.drop(class_data[class_data["type"] != "class"].index, inplace=True)
    test_data.drop(test_data[test_data["type"] != "class"].index, inplace=True)
    
    # Columns of the dataframe
    class_data_lines = class_data.shape[0]
    test_data_lines = test_data.shape[0]
    testsmells_class_data_lines = testsmells_class_data.shape[0]

    
    # Removing the test classes
    class_data.drop(class_data[class_data["class"].str.contains("Test")].index, inplace=True)
    
    # Removing the production classes
    for i in range(test_data_lines):
        test_data.iat[i, 1] = test_data.iat[i, 1].split('.').pop()
    test_data.drop(test_data[~test_data["class"].str.contains("Test") ].index, inplace=True)
    print(test_data)

    # Renomeando coluna de nomes de classes do testsmells_class_data
    class_data = class_data.rename(columns={'file': 'ProductionFileName'})
    test_data = test_data.rename(columns={'class': 'TestFileName'})
    
    # Joining test smells and metrics
    joined_data_class = pd.merge(class_data, testsmells_class_data, on="ProductionFileName")
    joined_data_test = pd.merge(test_data, testsmells_class_data, on="TestFileName")
    
    # Removendo colunas duplicadas no JNose
    joined_data_test = joined_data_test.drop(['numberMethods'], axis=1)
    joined_data_test = joined_data_test.drop(['LOC'], axis=1)
    joined_data_test = joined_data_test.drop(['type'], axis=1)
    joined_data_class = joined_data_class.drop(['numberMethods'], axis=1)
    joined_data_class = joined_data_class.drop(['LOC'], axis=1)
    joined_data_class = joined_data_class.drop(['type'], axis=1)

    joined_data_class.to_csv(r'/home/luana-martins/Área de Trabalho/ML/ClassMetrics/'+name+'.csv', index = False, header=True)
    joined_data_test.to_csv(r'/home/luana-martins/Área de Trabalho/ML/TestClassMetrics/'+name+'.csv', index = False, header=True)
    countTests += len(joined_data_test.index)
    countClasses += len(joined_data_class.index)
    joined_data_class.to_csv('/home/luana-martins/Área de Trabalho/ML/ClassMetrics/TotalClass.csv', mode='a', index = False, header=True)
    joined_data_test.to_csv('/home/luana-martins/Área de Trabalho/ML/TestClassMetrics/TotalTest.csv', mode='a', index = False, header=True)
    

print(countTests)
print(countClasses)
