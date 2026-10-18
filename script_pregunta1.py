# Librerías necesarias para el funcionamiento del programa
import numpy as np


def costo_minimo_perdidas(n_nodos: int, perdidas_nodo: list) -> float | None:
    """Calcula el costo mínimo de pérdida de potencia en un alimentador.

    Args:
        n_nodos: Cantidad de nodos del alimentador (no negativa).
        perdidas_nodo: Pérdida de potencia medida en cada nodo .

    Returns:
        El costo mínimo acumulado, 0.0 si no hay nodos, o None si los
        datos de entrada están corruptos.
    """
    # La cantidad de nodos no puede ser negativa
    assert n_nodos >= 0

    # Caso base
    if n_nodos == 0:
        return 0.0

    # Tabla de costos acumulados
    costo_acumulado = np.zeros(n_nodos + 1)

    try:
        # Caso base: el costo del primer nodo es su propia pérdida
        costo_acumulado[1] = float(perdidas_nodo[0])

        # Se llena la tabla de izquierda a derecha
        for i in range(2, n_nodos + 1):
            perdida = float(perdidas_nodo[i - 1])
            costo_acumulado[i] = min(
                costo_acumulado[i - 1] + perdida,
                costo_acumulado[i - 2] + perdida * 0.8,
            )

        return costo_acumulado[n_nodos]

    except (TypeError, ValueError):
        # Datos corruptos o insuficientes:se genera una alerta, pero no detiene el código
        print("Alerta: datos inválidos en los sensores SCADA")
        return None


# Prueba 1: datos válidos, el valor retornado debería ser 40
datos_validos = [10, 20, 15, 30]
resultado = costo_minimo_perdidas(len(datos_validos), datos_validos)
print("Prueba 1 (datos válidos):", resultado)
