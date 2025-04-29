from flask import Flask, request, render_template
from funcoes_corretas import (
    decimal_para_binario,
    decimal_para_octal,
    binario_para_decimal,
    decimal_para_hexadecimal,
    hexadecimal_para_decimal,
    octal_para_decimal,
    octal_para_hexadecimal,
    hexadecimal_para_octal,
    hexadecimal_para_binario
)

app = Flask(__name__)

def configurar_rotas(app):
    @app.route('/', methods=['GET', 'POST'])
    def index() -> str:
        numero = ""
        tipo = ""
        resultado = ""

        if request.method == "POST":
            numero = request.form.get("numero", "")
            tipo = request.form.get("tipo", "")

            try:
                numero = numero.replace(',', '.')  # Ajuste de separador decimal universal

                if tipo == "decimal_para_binario":
                    resultado = decimal_para_binario(numero)
                elif tipo == "decimal_para_hexadecimal":
                    resultado = decimal_para_hexadecimal(numero)
                elif tipo == "hexadecimal_para_decimal":
                    resultado = hexadecimal_para_decimal(numero)
                elif tipo == "octal_para_decimal":
                    resultado = octal_para_decimal(numero)
                elif tipo == "octal_para_hexadecimal":
                    resultado = octal_para_hexadecimal(numero)
                elif tipo == "hexadecimal_para_octal":
                    resultado = hexadecimal_para_octal(numero)
                elif tipo == "decimal_para_octal":
                    resultado = decimal_para_octal(numero)
                elif tipo == "hexadecimal_para_binario":
                    resultado = hexadecimal_para_binario(numero)
                elif tipo == "binario_para_decimal":
                    resultado = binario_para_decimal(numero)
                else:
                    resultado = "Tipo de conversão inválido."
            
            except ValueError:
                resultado = "Erro: Valor numérico inválido para a base selecionada."
            except Exception as e:
                resultado = f"Erro inesperado: {str(e)}"

        return render_template('index.html', resultado=resultado, numero=numero, tipo=tipo)

# Configura as rotas
configurar_rotas(app)

if __name__ == '__main__':
    app.run(debug=True)