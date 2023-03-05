""""Questão 3) Suponha que você deseja precificar uma opção double digital, que 
paga  um valor fixo se o ativo subjacente estiver dentro de um determinado 
intervalo  no vencimento. Escreva um código em Python para calcular o preço 
teórico dessa opção, usando o modelo de Black-Scholes. Os inputs devem ser: os 
preços atuais dos ativos subjacentes, os preços de exercício da opção, a 
volatilidade, o tempo até o vencimento e a taxa livre de risco. O output deve 
ser o preço teórico da opção."""

from math import sqrt, log, exp
from scipy.stats import norm


def black_scholes_double_digital_price( S: float,
                                        S_1: float, 
                                        S_2: float,
                                        r: float, 
                                        sigma: float, 
                                        t: float,
                                        time_type: str):
    """
    Calcula o preço de uma opção double digital utilizando o modelo de Black-Scholes.
    Parâmetros:
    S (float): preço atual do ativo subjacente.
    S_1 (float): strike da opção de venda.
    S_2 (float): strike da opção de compra, maior que S_1.
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


    d_1_p = (log(S/S_1)+(r+sigma**2/2)*t)/(sigma*sqrt(t))
    d_2_p = d_1_p - sigma*sqrt(t)

    d_1_c = (log(S/S_2)+(r+sigma**2/2)*t)/(sigma*sqrt(t))
    d_2_c = d_1_c - sigma*sqrt(t)

    return 1 - norm.cdf(-d_2_p) - norm.cdf(d_2_c)



print(black_scholes_double_digital_price(60, 50, 70, 0, 0.2, 6, "months"))