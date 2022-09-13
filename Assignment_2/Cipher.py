from cgitb import small
import math
import sys
# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def encrypt ( strng ):

  # The below block of code is designed to create variables 
  # in preparation of creating a table
  input_len = len(strng)
  smallest_square = 1
  while input_len > (smallest_square ** 2):
    smallest_square += 1

  # The below block of code creates an empty 2d list with
  # the given variables above
  encrypt_list = []
  for row in range(smallest_square):
      encrypt_row = []
      for col in range(smallest_square):
        encrypt_row.append(0)
      encrypt_list.append(encrypt_row)

  # The below block of code updates the empty list with 
  # the string input value and fills empty spaces with
  # an asterisk
  strng_value = 0
  for row in range(smallest_square):
    for col in range(smallest_square):
      if strng_value >= input_len:
        encrypt_list[row][col] = '*'
      else:
        encrypt_list[row][col] = strng[strng_value]
        strng_value += 1

  # The below block of code is designed to create an empty 
  # list for the use of rotation
  rotate_list = []
  for row in range(smallest_square):
      encrypt_row = []
      for col in range(smallest_square):
        encrypt_row.append(0)
      rotate_list.append(encrypt_row)

  # The below block of code adds the contents of the original
  # 2d list into the new list rotated 90 degrees
  encrypt_row = smallest_square - 1
  for rotate_col in range(smallest_square):
    encrypt_word = encrypt_list[encrypt_row]
    for rotate_row in range(smallest_square):
      rotate_list[rotate_row][rotate_col] = encrypt_word[rotate_row]
    encrypt_row -= 1

  # The below block of code converts the rotated 2d list 
  # into a string omitting the asterisk
  encrypt_word = ''
  for row in range(smallest_square):
    for col in range(smallest_square):
      if rotate_list[row][col] == '*':
        pass
      else:
        encrypt_word += rotate_list[row][col]

  return encrypt_word


#########################################################################


# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns a decrypted string 
def decrypt ( strng ):

  # The below block of code is designed to create variables 
  # in preparation of creating a table
  input_len = len(strng)
  smallest_square = 1
  while input_len > (smallest_square ** 2):
    smallest_square += 1

  # The below block of code creates an empty 2d list with
  # the given variables above
  decrypt_list = []
  for rows in range(smallest_square):
      decrypt_rows = []
      for column in range(smallest_square):
        decrypt_rows.append(0)
      decrypt_list.append(decrypt_rows)

  # The below block of code updates the empty list with 
  # the string input value and fills empty spaces with
  # an asterisk
  strng_value = 0
  for column in range(smallest_square):
    for rows in range(smallest_square):
      if strng_value >= input_len:
        decrypt_list[column][rows] = '*'
      else:
        decrypt_list[column][rows] = strng[strng_value]
        strng_value += 1

  # The below block of code is designed to create an empty 
  # list for the use of rotation
  rotate_list = []
  for column in range(smallest_square):
      decrypt_column = []
      for column in range(smallest_square):
        decrypt_column.append(0)
      rotate_list.append(decrypt_column)


 # The below block of code adds the contents of the original
 # 2d list into the new list rotated 90 degrees


  decrypt_rows = smallest_square - 1
  for rotate_rows in range(smallest_square):
    decrypt_word = decrypt_list[decrypt_column]
    for rotate_column in range(smallest_square):
      rotate_list[rotate_column][rotate_rows] = decrypt_word[rotate_column]
    decrypt_column -= 1


  # The below block of code converts the rotated 2d list 
  # into a string omitting the asterisk
  decrypt_word = ''
  for rows in range(smallest_square):
    for column in range(smallest_square):
      if rotate_list[rows][column] == '*':
        pass
      else:
        decrypt_word += rotate_list[rows][column]

  return decrypt_word

def main():
  # read the strings P and Q from standard input
  input_data = sys.stdin.read()
  global data_list
  data_list = list(input_data.split())

  # encrypt the string P
  encrypt_p = encrypt(data_list[0])

  # decrypt the string Q
  decrypt_q = decrypt(data_list[1])

  # print the encrypted string of P
  print(encrypt_p)
  # and the decrypted string of Q
  print(decrypt_q)

if __name__ == "__main__":
  main()