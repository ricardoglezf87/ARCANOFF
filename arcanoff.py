import ctypes
import time

# Definir la función para prevenir la suspensión del sistema
def prevenir_suspension():
    ES_CONTINUOUS = 0x80000000
    ES_SYSTEM_REQUIRED = 0x00000001
    ES_DISPLAY_REQUIRED = 0x00000002
    
    # Llamada a la API de Windows
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED)

# Ejecutar la función en un bucle
try:
    while True:
        prevenir_suspension()
        time.sleep(60)  # Mantener la pantalla activa cada 60 segundos
except KeyboardInterrupt:
    pass
