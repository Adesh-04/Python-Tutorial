from bin_dec import bin_dec
from dec_oct import dec_oct
from dec_hex import dec_hex
from oct_dec import oct_dec
from dec_bin import dec_bin  ##Broken
from hex_dec import hex_dec

## binary to octal 

decimal = bin_dec(1001)
octal = dec_oct(decimal)
# print(octal)

## binary to hexadecimal

decimal = bin_dec(1001)
hexadecimal = dec_hex(decimal)
# print(hexadecimal)

## octal to binary 

decimal = oct_dec(11)
binary = dec_bin(decimal)
# print(binary)

## octal to hexadecimal

decimal = oct_dec(11)
hexadecimal = dec_hex(decimal)
# print(hexadecimal)

## hexadecimal to binary

decimal = hex_dec(11)
binary = dec_bin(decimal)
# print(binary)

## hexadecimal to octal

decimal = hex_dec(11)
octal = dec_oct(decimal)
# print(octal)
