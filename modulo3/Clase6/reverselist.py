"""
2. Given a list of strings, write a function that prints a reverse version of each string:

For example:
>A = [ "Helio World", "Hello Python", "1 2 3 4 5 6 7 8"]
>magic_function(A)
['dlroW olleH', 'nohtyP olleH', '8 7 6 5 4 3 2 1']

"""

# forma tradicial con for para cada miembro de la lista dada:
# def magif_funcion(list_input):
#     list_output =[]
#     for a in list_input:
#         list_output.append(a[::-1])
#     return(list_output)


# fomra con LIST COMPREHENSION
def magif_funcion(list_input):
    list_output = [a[::-1] for a in list_input] # LIST COMPREHENSION
    return list_output

if __name__ == '__main__':
    A = [ "Helio World", "Hello Python", "1 2 3 4 5 6 7 8"]
    B = magif_funcion(A)
    print(B)



