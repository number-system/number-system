# Function to convert decimal to binary number
def decimalToBinary(decimal):  
    return format(decimal , '08b')

# Function to convert binary to octal number 
def decimalToOctal(decimal):
    octal = 0
    i = 1
    while (decimal != 0):
        octal = octal + (decimal % 8) * i
        decimal = int(decimal / 8)
        i = i * 10
    return octal

# Function to convert decimal to hexadecimal 
def decimalToHexa(decimal):
    return f'{int(decimal):X}'

# Function to convert binary to decimal number 
def binaryToDecimal(binary): 
    return int(binary, 2)

# Function to convert binary to hexadecimal number 
def binaryToHexa(binary):
    return f'{int(binary, 2):X}'

# function to create map between binary number and its equivalent octal 
def createMap(binary_oct_map): 
	binary_oct_map["000"] = '0'
	binary_oct_map["001"] = '1'
	binary_oct_map["010"] = '2'
	binary_oct_map["011"] = '3'
	binary_oct_map["100"] = '4'
	binary_oct_map["101"] = '5'
	binary_oct_map["110"] = '6'
	binary_oct_map["111"] = '7'

# Function to find octal equivalent of binary 
def binaryToOctal(binary): 
	l = len(binary)	
	# length of string before '.' 
	t = -1
	if '.' in binary: 
		t = binary.index('.') 
		len_left = t 
	else: 
		len_left = l 
	# add min 0's in the beginning to make left substring length divisible by 3 
	for i in range(1, (3 - len_left % 3) % 3 + 1): 
		binary = '0' + binary
	
	# if decimal point exists 
	if (t != -1): 
		# length of string after '.' 
		len_right = l - len_left - 1
		# add min 0's in the end to make right substring length divisible by 3 
		for i in range(1, (3 - len_right % 3) % 3 + 1): 
			binary = binary + '0'
	# create dictionary between binary and its equivalent octal code 
	binary_oct_map = {} 
	createMap(binary_oct_map) 
	i = 0
	octal = "" 
	while (True) : 
		# one by one extract from left, substring of size 3 and add its octal code 
		octal += binary_oct_map[binary[i:i + 3]] 
		i += 3
		if (i == len(binary)): 
			break
		# if '.' is encountered add it to result 
		if (binary[i] == '.'): 
			octal += '.'
			i += 1
	# required octal number 
	return octal

# Function to convert octal to decimal number
def octalToDecimal(octal):
    num = int(octal) 
    decimal_value = 0 
    base = 1
    while (num): 
        last_digit = num % 10
        num = int(num / 10)
        decimal_value += last_digit * base
        base = base * 8  
    return decimal_value

# Function to convert octal to binary number
def octalToBinary(octal):
    binary = "" # initializing bin as String While loop to extract each digit
    octal = int(octal)
    while octal != 0: 
		# extracting each digit 
        d = octal % 10
        if d == 0: 
			# concatenation of string using join function 
            binary = "".join(["000", binary]) 
        elif d == 1: 
			# concatenation of string using join function 
            binary = "".join(["001", binary])
        elif d == 2: 
			# concatenation of string using join function 
            binary = "".join(["010", binary])
        elif d == 3: 
			# concatenation of string using join function 
            binary = "".join(["011", binary]) 
        elif d == 4: 
			# concatenation of string using join function 
            binary = "".join(["100", binary]) 
        elif d == 5: 
			# concatenation of string using join function 
            binary = "".join(["101", binary]) 
        elif d == 6: 
			# concatenation of string using join function 
            binary = "".join(["110",binary]) 
        elif d == 7: 
			# concatenation of string using join function 
            binary = "".join(["111", binary]) 
        else: 
			# an option for invalid input 
            binary = "Invalid Octal Digit"
            break
		# updating the oct for while loop 
        octal = int(octal / 10) 
	# returning the string binary that stores binary equivalent of the number 
    return binary

# Function to convert octal to hexadecimal number
def octalToHexa(octal):
    return f'{int(octal, 8):X}'


# Function to convert hexadecimal to decimal number
def hexaToDecimal(hexa):
    return int(hexa, 16)

# Function to convert hexadecimal to binary number
def hexaToBinary(hexa):
    return "{0:08b}".format(int(hexa, 16))

# Function to convert hexadecimal to octal number
def hexaToOctal(hexa):
    decimal = hexaToDecimal(hexa)
    octal = decimalToOctal(decimal)
    return octal
