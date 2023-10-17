import decimal

num1 = decimal.Decimal('10.345')
num2 = decimal.Decimal('5.678')

suma = num1 + num2
print('Suma :', suma)

resta = num1 - num2
print('Resta :', resta)

division = num1 / num2
print('Division con Decimal :', division)

print('Division sin Decimal :', 10.345/5.678)

redondeo_2 = division.quantize(decimal.Decimal('0.00'))
print('Dicision redondeo dos decimales', redondeo_2)

redondeo_alza = division.quantize(decimal.Decimal('1.00000'), rounding=decimal.ROUND_CEILING)
redondeo_baja = division.quantize(decimal.Decimal('1.00000'), rounding=decimal.ROUND_FLOOR)
redondeo_cercano = division.quantize(decimal.Decimal('1.00000'), rounding=decimal.ROUND_HALF_EVEN)
redondeo_cercano_mas_decimales = division.quantize(decimal.Decimal('1.00000000000000'), rounding=decimal.ROUND_HALF_EVEN)

print('Redondeo hacia arriba :', redondeo_alza)
print('Redondeo hacia abajo :', redondeo_baja)
print('Redondeo cercano :', redondeo_cercano)
print('Redondeo cercano mas decimales:', redondeo_cercano_mas_decimales)
