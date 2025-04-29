def bits_dinamicos_necessarios(valor_absoluto: int):
    if valor_absoluto == 0:
        return 8
    bits =  valor_absoluto.bit_length() + 1
    return ((bits + 7) // 8) * 8

def aplicar_complemento_de_dois(binario: str, bits: int = 8): 
    if '.' in binario:
        parte_inteira, parte_fracionaria = binario.split('.')
    else:
        parte_inteira, parte_fracionaria = binario, ""

    parte_inteira = parte_inteira.zfill(bits)
    parte_inteira_revertida = ''.join('1' if b == '0' else '0' for b in parte_inteira)
    n = int(parte_inteira_revertida, 2) + 1
    parte_inteira_resultado = bin(n)[2:].zfill(bits)

    if parte_fracionaria:
        parte_fracionaria_invertida = ''.join('1' if b == '0' else '0' for b in parte_fracionaria)
        return parte_inteira_resultado + '.' + parte_fracionaria_invertida
    else:
        return parte_inteira_resultado

def converter_oct_f_hex(octal):
    negativo = octal.startswith('-')
    if negativo:
        octal = octal[1:]

    if '.' in octal:
        parte_inteira, parte_fracionaria = octal.split('.')
    else:
        parte_inteira = octal
        parte_fracionaria = ""

    # Parte inteira em decimal
    decimal_inteiro = int(parte_inteira, 8)

    # Parte fracionária em decimal
    decimal_fracionaria = 0
    for i, dig in enumerate(parte_fracionaria):
        decimal_fracionaria += int(dig, 8) / (8 ** (i + 1))

    decimal_total = decimal_inteiro + decimal_fracionaria

    if negativo:
        decimal_total = -decimal_total

    # Converter para hexadecimal
    inteiro_hex = hex(int(abs(decimal_total)))[2:].upper()

    frac = abs(decimal_total) - int(abs(decimal_total))
    if frac > 0:
        frac_hex = ""
        precisao = 10
        for _ in range(precisao):
            frac *= 16
            dig = int(frac)
            frac_hex += hex(dig)[2:].upper()
            frac -= dig
        sinal = "-" if negativo else ""
        return f"{sinal}{inteiro_hex}.{frac_hex}"
    else:
        sinal = "-" if negativo else ""
        return f"{sinal}{inteiro_hex}"


#Conversão de número hexadecimal para binário
def converter_hex_f_bin(hexadecimal):
    hexadecimal = hexadecimal.upper()
    negativo = hexadecimal.startswith('-')
    
    if negativo:
        hexadecimal = hexadecimal[1:]

    decimal = converter_hex_f_decim(hexadecimal)
    inteiro = int(abs(decimal))
    fracionario = abs(decimal) - inteiro

    bin_inteiro = ""
    if inteiro == 0:
        bin_inteiro = "0"
    else:
        while inteiro > 0:
            bin_inteiro = str(inteiro % 2) + bin_inteiro
            inteiro //= 2

    bin_fracionario = ""
    count = 0
    temp_fracionario = fracionario
    while temp_fracionario > 0 and count < 10:
        temp_fracionario *= 2
        bit = int(temp_fracionario)
        bin_fracionario += str(bit)
        temp_fracionario -= bit
        count += 1

    if bin_fracionario:
        binario = f"{bin_inteiro}.{bin_fracionario}"
    else:
        binario = bin_inteiro

    if negativo:
        bits = bits_dinamicos_necessarios(int(abs(decimal)))
        binario = aplicar_complemento_de_dois(binario, bits)

    return binario