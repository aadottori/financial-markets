"""Crie um programa em Python que utilize o modelo de precificação de opções
BlackScholes para avaliar o preço de uma opção de compra ou venda. O programa deve
ser capaz de receber informações sobre o preço atual do ativo subjacente, a taxa livre de
risco, a volatilidade do ativo e o tempo restante até o vencimento da opção."""

from math import sqrt, log, exp
from scipy.stats import norm


def black_scholes_option_price(put_or_call: str,
                                S: float, 
                                K: float,
                                r: float, 
                                sigma: float, 
                                t: float,
                                time_type: str):
    """
    Calcula o preço de uma opção de compra ou venda utilizando o modelo de Black-Scholes.
    Parâmetros:
    put_or_call (str): 'call' para opção de compra, 'put' para opção de venda.
    S (float): preço atual do ativo subjacente.
    K (float): preço de exercício da opção.
    r (float): taxa livre de risco.
    sigma (float): volatilidade do ativo subjacente.
    t (float): tempo restante até o vencimento da opção.
    time_type (str): 'days' para dias, 'months' para meses, 'years' para anos.
    
    Retorno:
    float: preço da opção.
    """

    if time_type == "days":
        t = t/360
    elif time_type == "months":
        t = t/12
    elif time_type == "years":
        t = t
    else:
        raise ValueError("as opções possíveis são days, months ou years")


    d1 = (log(S/K)+(r+sigma**2/2)*t)/(sigma*sqrt(t))
    d2 = d1 - sigma*sqrt(t)


    if put_or_call == "put":
        return K*exp(-r*t)*norm.cdf(-d2) - S*norm.cdf(-d1)
    elif put_or_call == "call":
        return S*norm.cdf(d1) - K*exp(-r*t)*norm.cdf(d2)
    else:
        raise ValueError("as opções possíveis são call e put")



print(black_scholes_option_price("call", 60, 50, 0, 0.2, 6, "months"))