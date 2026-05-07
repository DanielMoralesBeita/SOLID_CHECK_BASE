from abc import ABC, abstractmethod

class AnalysisRule(ABC):
    @abstractmethod
    def evaluate(self, lines):
        pass

class SRP_MethodCountRule(AnalysisRule):
    """Detecta si una clase tiene demasiados métodos (Responsabilidad Única)."""
    def __init__(self, limit=15):
        self.limit = limit

    def evaluate(self, lines):
        count = sum(1 for line in lines if line.strip().startswith(('def ', 'function ')))
        if count > self.limit:
            return {"principle": "SRP", "status": "FAIL", "detail": f"{count} métodos detectados."}
        return {"principle": "SRP", "status": "PASS", "detail": "Conteo de métodos bajo el límite."}

class LongFunctionRule(AnalysisRule):
    """Detecta funciones que exceden un número saludable de líneas."""
    def __init__(self, line_limit=40):
        self.line_limit = line_limit

    def evaluate(self, lines):
        # Implementación simplificada para el PMV
        current_func_lines = 0
        violations = 0
        for line in lines:
            if line.strip().startswith(('def ', 'function ')):
                if current_func_lines > self.line_limit:
                    violations += 1
                current_func_lines = 0
            current_func_lines += 1
        
        if violations > 0:
            return {"principle": "Clean Code", "status": "WARN", "detail": f"{violations} funciones muy largas."}
        return {"principle": "Clean Code", "status": "PASS", "detail": "Funciones con longitud adecuada."}