def calcular_valores(primer_banda, segunda_banda, tercer_banda, radio_tol):
    colores = {
        '0': '#000000',  # Negro
        '1': '#E6BF83',  # Marrón
        '2': '#FF6666',  # Rojo
        '3': '#FFB366',  # Naranja
        '4': '#FFFF99',  # Amarillo
        '5': '#66FF66',  # Verde
        '6': '#6666FF',  # Azul
        '7': '#6C4675 ',  # Morado
        '8': '#C0C0C0',  # Plata
        '9': '#FFFFFF'   # Blanco
    }

    multiplicador = {
        '1': '#000000', 
        '10': '#E6BF83', 
        '100': '#FF6666', 
        '1000': '#FFB366',
        '10000': '#FFFF99', 
        '100000': '#66FF66', 
        '1000000': '#6666FF',
        '10000000': '#6C4675',
        '100000000': '#C0C0C0', 
        '1000000000': '#FFFFFF'}

    tolerancia = int(primer_banda + segunda_banda) if primer_banda is not None and segunda_banda is not None else 0
    if tolerancia is not None and tercer_banda is not None:
        value = tolerancia * int(tercer_banda)
    else:
        value = 0

    value_tolerancia = 0
    color4 = ""

    if radio_tol == "oro":
        if value is not None:
            value_tolerancia = int(value * 0.05)
        else:
            value_tolerancia = 0
        color4 = "#DFCE00"
    elif radio_tol == "plata":
        if value is not None:
            value_tolerancia = int(value * 0.10)
        else:
            value_tolerancia = 0
        color4 = "#C9C9C9"


    max_value = value + value_tolerancia if value is not None else 0
    min_value = value - value_tolerancia if value is not None else 0
    color1, color2, color3 = colores.get(primer_banda, ""), colores.get(segunda_banda, ""), multiplicador.get(tercer_banda, "")

    return value, min_value, max_value, color1, color2, color3, color4
