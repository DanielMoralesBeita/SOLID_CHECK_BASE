
# Copyright (c) 2026 Daniel Alberto Morales Beita
# Licensed under the MIT License. 
# See LICENSE file in the project root for full license information.

from core import CodeLoader
from rules import SRP_MethodCountRule, LongFunctionRule
from reporter import HTMLReporter  # Importamos el nuevo reportero



class AnalyzerPMV:
    def __init__(self):
        self.rules = [
            SRP_MethodCountRule(limit=10),
            LongFunctionRule(line_limit=50)
        ]

    def analyze(self, file_to_scan):
        lines = CodeLoader.load_safely(file_to_scan)
        if lines is None: return

        results = []
        for rule in self.rules:
            try:
                results.append(rule.evaluate(lines))
            except Exception as e:
                results.append({"principle": "Error", "status": "FAIL", "detail": str(e)})
        
        # Generamos el reporte HTML
        report_path = HTMLReporter.generate(file_to_scan, results)
        print(f"✅ Análisis completado. Reporte generado en: {report_path}")

if __name__ == "__main__":
    scanner = AnalyzerPMV()
    scanner.analyze("snake.py")