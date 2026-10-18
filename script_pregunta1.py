#se importan en un inicio las librerias necesarias para el funcionamiento del programa
import numpy as np
import time

def costo_minimo_perdidas(n, vals):
    assert n >= 0
    if n == 0:
        return 0.0
    dp = np.zeros(n + 1)    
    try:
        dp[1] = float(vals[0])

        for i in range(2, n + 1):
            costo = float(vals[i - 1])
            dp[i] = min(dp[i - 1] + costo, dp[i - 2] + costo * 0.8)

        return dp[n]

    except (TypeError, ValueError, IndexError):
        print("Alerta: datos inválidos en los sensores SCADA")
        return None

