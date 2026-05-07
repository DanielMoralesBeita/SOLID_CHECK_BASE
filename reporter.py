import datetime

class HTMLReporter:
    @staticmethod
    def generate(file_name, results):
        html_template = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>Reporte de Calidad de Código</title>
            <style>
                body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 40px; background-color: #f4f7f6; }}
                .container {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
                h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
                .meta {{ color: #7f8c8d; font-size: 0.9em; margin-bottom: 20px; }}
                table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
                th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }}
                th {{ background-color: #3498db; color: white; }}
                .PASS {{ color: #27ae60; font-weight: bold; }}
                .FAIL {{ color: #e74c3c; font-weight: bold; }}
                .WARN {{ color: #f39c12; font-weight: bold; }}
                .footer {{ margin-top: 30px; font-size: 0.8em; color: #bdc3c7; text-align: center; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Reporte de Análisis: {file_name}</h1>
                <p class="meta">Generado el: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                
                <table>
                    <thead>
                        <tr>
                            <th>Principio / Regla</th>
                            <th>Estado</th>
                            <th>Detalle del Hallazgo</th>
                        </tr>
                    </thead>
                    <tbody>
                        {"".join(f'''
                        <tr>
                            <td>{res.get('principle', 'N/A')}</td>
                            <td class="{res.get('status', '')}">{res.get('status', 'ERROR')}</td>
                            <td>{res.get('detail', 'N/A')}</td>
                        </tr>
                        ''' for res in results)}
                    </tbody>
                </table>
                
                <div class="footer">
                    "Hecho con Amor y IA , por Daniel Morales Beita. Yo lo merezco, soy un imán de oportunidades."
                </div>
            </div>
        </body>
        </html>
        """
        
        output_file = f"reporte_{file_name.replace('.', '_')}.html"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_template)
        return output_file
