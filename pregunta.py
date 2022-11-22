"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import numpy as np

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #
    # Inserte su código aquí
    #

    df.drop(['Unnamed: 0'], axis=1,inplace=True)
    df.drop_duplicates(inplace=True)
    df.dropna(axis=0,inplace=True)
    
    #Pre-procesamiento
    df['monto_del_credito'] = df['monto_del_credito'].str.replace("$ ","").str.replace(",","").str.replace(".00",'').astype(float)
    df['tipo_de_emprendimiento']=df['tipo_de_emprendimiento'].astype(str)
    df['tipo_de_emprendimiento']=df['tipo_de_emprendimiento'].str.lower()
    df['sexo']=df['sexo'].str.lower()
    df['idea_negocio'] = df['idea_negocio'].str.lower()
    df['idea_negocio'] = df['idea_negocio'].str.lambda x: x.replace(" ",'_').str.replace("-",'_')
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(float)
    df['barrio'] = df['barrio'].astype(str).str.lower().srt.replace("-",' ').str.replace("_",' ')
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], infer_datetime_format=True)
    df['línea_credito'] = df['línea_credito'].str.lower().str.replace(" ",'_').str.replace("-",'_')
                                                                 
    df.drop_duplicates(inplace=True)
    df.dropna(axis=0, inplace=True)
    
    return df
