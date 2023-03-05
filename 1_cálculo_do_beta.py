"""Crie um programa em Python que receba um conjunto de dados de 
preços de ações e calcule o valor do beta para cada ação em relação ao mercado. 
O programa deve ser capaz de lidar com grandes volumes de dados e produzir 
resultados precisos e confiáveis."""

import numpy as np
from sklearn.linear_model import LinearRegression
import yfinance as yf

def beta(stocks: list, market: str, start_date: str, end_date: str):
    """
    Calcula o beta de uma lista de ações com relação ao mercado.
    Parâmetros:
    stocks (list): lista de ativos para calcular o beta.
    market (str): código do mercado.  
    start_date: data de início do período a calcular
    end_date: date final do período a calcular
    
    Retorno:
    dict: beta dos ativos.
    """
    df = yf.download(stocks+[market],
                      start=start_date,
                      end=end_date,
                      progress=False)

    df = df["Adj Close"].pct_change().tail(-1)
    
    beta = {}
    for stock in stocks:
        x = np.array(df[stock].dropna()).reshape((-1,1))
        y = np.array(df[[market]].tail(len(x)))
        model = LinearRegression().fit(x, y)
        print (f'{stock} Beta no período de {df.index[len(df[[market]])-len(df[stock].dropna())]} a {df.index[-1]} = {model.coef_[0][0]}')
        beta[stock] = {
            "start_date": df.index[len(df[market])-len(df[stock].dropna())],
            "end_date": df.index[-1],
            "beta": model.coef_[0][0],
        }
    return beta


stocks = ["ABEV3.SA", "BBDC4.SA", "EGIE3.SA", "PETR4.SA", "TAEE11.SA", "VALE3.SA", "WEGE3.SA", "IVVB11.SA", "BOVA11.SA"]
market = "^BVSP" #IBOV

print(beta(stocks, market, "2000-01-01", "2023-03-01"))