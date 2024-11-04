import pandas as pd
import re

def pasar_a_limpito_ds(df):
    # WEIGHT
    df['Weight'] = df['Weight'].str.replace('kg', '').astype(float)

    # RAM
    df['Ram'] = df['Ram'].str.replace('GB', '').astype(int)
    
    # RESOLUTION PIXELES
    df[['ancho', 'alto']] = df['ScreenResolution'].str.extract(r'(\d+)x(\d+)').astype(float)
    df['Resolution'] = df['ancho'] * df['alto']
    df = df.drop(['ancho', 'alto'], axis=1)

    # IPS
    df['IPS_Panel'] = df['ScreenResolution'].str.contains('IPS Panel').astype(int)

    # TOUCHSCREEN
    df['Touchscreen'] = df['ScreenResolution'].str.contains('Touchscreen').astype(int)
    df = df.drop('ScreenResolution', axis=1)
    
    # ORDENAR ...
    df = df.sort_index()
    
    # COMPANY
    calidad_company_dict = {
        'Apple': 4, 'Razer': 4, 'Microsoft': 4, 'Huawei': 4,
        'Dell': 3, 'HP': 3, 'Lenovo': 3, 'MSI': 3, 'Asus': 3, 'Acer': 3,
        'Samsung': 2, 'Toshiba': 2, 'LG': 2,
        'Mediacom': 1, 'Xiaomi': 1, 'Chuwi': 1, 'Fujitsu': 1, 'Vero': 1, 'Google': 1}
    df['COMPANY'] = df['Company'].map(calidad_company_dict).fillna(0)
    df = df.drop('Company', axis=1)
    
    # GHZS ... NO FUNCIONAAAAAAAAAA AAA A A A A ...
    # df['Cpu'] = df['Cpu'].str.replace('GHz', '')
    # df['GHZ'] = df['Cpu'].str.extract(r'(\d+\.\d+)$').astype(float)
    # df = df.drop('GHZ', axis=1)
    
    # INTEL
    df['Intel'] = df['Cpu'].str.contains('Intel').astype(int)

    # AMD
    df['AMD'] = df['Cpu'].str.contains('AMD').astype(int)
    
    # PROCESADOR
    def clasificar_procesador(cpu):
        if 'i9' in cpu:
            return 6
        elif 'i7' in cpu or 'Xeon' in cpu:
            return 5
        elif 'i5' in cpu or 'Ryzen' in cpu:
            return 4
        elif 'i3' in cpu:
            return 3
        elif 'Pentium' in cpu:
            return 2
        elif 'A' in cpu and 'AMD' in cpu:  
            return 2
        elif 'Celeron' in cpu or 'Atom' in cpu:
            return 1
        else:
            return 0  
    df['PROCESADOR'] = df['Cpu'].apply(clasificar_procesador)
    df = df.drop(['Cpu', 'Product'], axis=1)
    
    # TYPENAME
    tipo_rendimiento_dict = {
        'Gaming': 5, 'Workstation': 5, 'Ultrabook': 4, 
        '2 in 1 Convertible': 3, 'Notebook': 3, 'Netbook': 2}
    df['Type_Name'] = df['TypeName'].map(tipo_rendimiento_dict)
    df = df.drop('TypeName', axis=1)
    
    # SISTEMA OPERATIVO
    sistema_rendimiento_dict = {
        'Windows 10': 5, 'macOS': 4, 'Mac OS X': 4,
        'Windows 7': 3, 'Windows 10 S': 3, 'Linux': 3,
        'Chrome OS': 2, 'Android': 1, 'No OS': 1}
    df['OP_SYS'] = df['OpSys'].map(sistema_rendimiento_dict)
    df = df.drop('OpSys', axis=1)
    
    # MEMORY
    def clasificar_almacenamiento(memory):
        if any(keyword in memory for keyword in ['512GB SSD + 1TB HDD', '256GB SSD + 1TB HDD', '1TB SSD', '2TB HDD', '512GB SSD', '1TB Hybrid', '1TB HDD + 1TB HDD']):
            return 3
        elif any(keyword in memory for keyword in ['256GB SSD', '128GB SSD + 1TB HDD', '512GB HDD', '256GB Flash Storage', '512GB SSD + 512GB SSD']):
            return 2
        elif any(keyword in memory for keyword in ['32GB Flash Storage', '64GB SSD', '128GB SSD', '500GB HDD', '32GB SSD', '64GB Flash Storage']):
            return 1
        return 1
    df['MEMORY'] = df['Memory'].apply(clasificar_almacenamiento)
    df = df.drop('Memory', axis=1)
    
    # GPU
    def clasificar_gpu(gpu):
        if any(keyword in gpu for keyword in ['GTX 1070', 'GTX 1080', 'GTX 980', 'GTX 970', 'Quadro M3000M', 'Quadro M2200', 'Quadro M2000M', 'RX 580', 'RX 560', 'RX 550', 'Radeon Pro', 'FirePro']):
            return 3
        elif any(keyword in gpu for keyword in ['GTX 1050', 'GTX 1050 Ti', 'GTX 965M', 'GTX 960M', 'MX150', 'MX130', 'Quadro M1000M', 'Quadro M520M', 'R7 M445', 'R7 M460', 'Radeon R5', 'Iris Plus']):
            return 2
        elif any(keyword in gpu for keyword in ['Intel HD', 'Intel UHD', 'Iris Graphics', 'GeForce 920M', 'GeForce 930MX', 'GeForce 940MX', 'Radeon R4', 'Radeon R2', 'Radeon R5 520', 'R5 M315']):
            return 1
        return 1
    df['GPU'] = df['Gpu'].apply(clasificar_gpu)
    df = df.drop('Gpu', axis=1)
    print(type(df))
    return df

import matplotlib.pyplot as plt  
import seaborn as sns

def crear_mapa_de_correlacion(df):
    
    # SOLO COLUMNAS NUMERICAS 
    numeric_df = df.select_dtypes(include=[float, int])

    plt.figure(figsize=(12, 10))
    sns.heatmap(numeric_df.corr(), annot=True, vmin=-1, vmax=1, cmap="coolwarm", annot_kws={"size": 8})
    plt.show()