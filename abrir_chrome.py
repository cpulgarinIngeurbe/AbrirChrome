import subprocess
import sys

try:
    subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe"])
    print("Chrome abierto exitosamente")
except FileNotFoundError:
    # Intenta la ruta alternativa si existe
    try:
        subprocess.Popen([r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"])
        print("Chrome abierto exitosamente")
    except FileNotFoundError:
        print("No se encontró Chrome en las rutas estándar")
        sys.exit(1)
except Exception as e:
    print(f"Error al abrir Chrome: {e}")
    sys.exit(1)
