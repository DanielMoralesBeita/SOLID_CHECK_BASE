import os

class SecurityGuard:
    @staticmethod
    def is_safe(file_path):
        MAX_SIZE = 2 * 1024 * 1024  # 2MB
        if not os.path.exists(file_path):
            return False, "El archivo no existe."
        if os.path.getsize(file_path) > MAX_SIZE:
            return False, "Archivo demasiado grande (Límite 2MB)."
        return True, "Safe"

class CodeLoader:
    @staticmethod
    def load_safely(file_path):
        is_safe, message = SecurityGuard.is_safe(file_path)
        if not is_safe:
            print(f"[!] Seguridad: {message}")
            return None
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.readlines()
        except Exception as e:
            print(f"[!] Error de lectura: {e}")
            return None