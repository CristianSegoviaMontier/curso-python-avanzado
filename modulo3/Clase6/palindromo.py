"""
palindromos:

radar
atar a la rata

"""



def palindromo(srt_input):
    str_original = str_input.replace(" ","").upper()
    str_reverso = str_original[::-1].replace(" ","").upper()

    if (str_reverso == str_original):
        print(f"La frase '{str_input}' SI es un palindramo")
    else:
        print(f"La frase '{str_input}' NO es un palindromo")

if __name__ == '__main__':
    str_input = input('Ingrese una frase :')
    palindromo(str_input)
