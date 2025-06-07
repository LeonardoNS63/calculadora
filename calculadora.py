import tkinter as tk
import tkinter.ttk as ttk 
janela = tk.Tk() 
janela.title("calculadora")
janela.geometry("250x400")


def add_number9() :
    global cont_num1
    global cont_num2
    if cont_num2 <= 8 :
        if xxx != '[ ]' :
           numero2['text'] = numero2['text'] + '9'
           cont_num2 += 1
    if cont_num1 <= 8 :
        if xxx == '[ ]' :
            numero1['text'] = numero1['text'] + '9'
            cont_num1 += 1
    else :
        print('ERRO : number of caracters full')
def add_number8() :
    global cont_num1
    global cont_num2
    if cont_num2 <= 8 :
        if xxx != '[ ]' :
           numero2['text'] = numero2['text'] + '8'
           cont_num2 += 1
    if cont_num1 <= 8 :
        if xxx == '[ ]' :
            numero1['text'] = numero1['text'] + '8'
            cont_num1 += 1
    else :
        print('ERRO : number of caracters full')
def add_number7() :
    global cont_num1
    global cont_num2
    if cont_num2 <= 8 :
        if xxx != '[ ]' :
           numero2['text'] = numero2['text'] + '7'
           cont_num2 += 1
    if cont_num1 <= 8 :
        if xxx == '[ ]' :
            numero1['text'] = numero1['text'] + '7'
            cont_num1 += 1
    else :
        print('ERRO : number of caracters full')
def add_mais() :
    global xxx
    sinal_do_calculo['text'] =  '+'
    xxx = sinal_do_calculo['text'] 
def add_number6() :
    global cont_num1
    global cont_num2
    if cont_num2 <= 8 :
        if xxx != '[ ]' :
           numero2['text'] = numero2['text'] + '6'
           cont_num2 += 1
    if cont_num1 <= 8 :
        if xxx == '[ ]' :
            numero1['text'] = numero1['text'] + '6'
            cont_num1 += 1
    else :
        print('ERRO : number of caracters full')
def add_number5() :
    global cont_num1
    global cont_num2
    if cont_num2 <= 8 :
        if xxx != '[ ]' :
           numero2['text'] = numero2['text'] + '5'
           cont_num2 += 1
    if cont_num1 <= 8 :
        if xxx == '[ ]' :
            numero1['text'] = numero1['text'] + '5'
            cont_num1 += 1
    else :
        print('ERRO : number of caracters full')
def add_number4() :
    global cont_num1
    global cont_num2
    if cont_num2 <= 8 :
        if xxx != '[ ]' :
           numero2['text'] = numero2['text'] + '4'
           cont_num2 += 1
    if cont_num1 <= 8 :
        if xxx == '[ ]' :
            numero1['text'] = numero1['text'] + '4'
            cont_num1 += 1
    else :
        print('ERRO : number of caracters full')
def add_menos() :
    global xxx
    sinal_do_calculo['text'] =  '-'
    xxx = sinal_do_calculo['text'] 
def add_number3() :
    global cont_num1
    global cont_num2
    if cont_num2 <= 8 :
        if xxx != '[ ]' :
           numero2['text'] = numero2['text'] + '3'
           cont_num2 += 1
    if cont_num1 <= 8 :
        if xxx == '[ ]' :
            numero1['text'] = numero1['text'] + '3'
            cont_num1 += 1
    else :
        print('ERRO : number of caracters full')
def add_number2() :
    global cont_num1
    global cont_num2
    if cont_num2 <= 8 :
        if xxx != '[ ]' :
           numero2['text'] = numero2['text'] + '2'
           cont_num2 += 1
    if cont_num1 <= 8 :
        if xxx == '[ ]' :
            numero1['text'] = numero1['text'] + '2'
            cont_num1 += 1
    else :
        print('ERRO : number of caracters full')
def add_number1() :
    global cont_num1
    global cont_num2
    if cont_num2 <= 8 :
        if xxx != '[ ]' :
           numero2['text'] = numero2['text'] + '1'
           cont_num2 += 1
    if cont_num1 <= 8 :
        if xxx == '[ ]' :
            numero1['text'] = numero1['text'] + '1'
            cont_num1 += 1
    else :
        print('ERRO : number of caracters full')
def add_multi() :
    global xxx
    sinal_do_calculo['text'] =  'x'
    xxx = sinal_do_calculo['text'] 
def add_number0() :
    global cont_num1
    global cont_num2
    if cont_num2 <= 8 :
        if xxx != '[ ]' :
           numero2['text'] = numero2['text'] + '0'
           cont_num2 += 1
    if cont_num1 <= 8 :
        if xxx == '[ ]' :
            numero1['text'] = numero1['text'] + '0'
            cont_num1 += 1
    else :
        print('ERRO : number of caracters full')
def add_result() :
    global cont_num1
    global cont_num2
    global xxx
    valor1 = numero1['text']
    valor2 = numero2['text']
    valor1 = int(valor1)
    valor2 = int(valor2)
    if xxx == 'x' :
        result = valor1*valor2
    if xxx == '-' :
        result = valor1-valor2
    if xxx == '+' :
        result = valor1+valor2
    if xxx == '÷' :
        result = valor1/valor2
    resultado['text'] = result
    numero1['text'] = ''
    numero2['text'] = ''
    sinal_do_calculo['text'] = '[ ]'
    xxx = sinal_do_calculo['text']
    cont_num2 = 0
    cont_num1 = 0
def delete() :
    global cont_num1
    global cont_num2
    global xxx
    resultado['text'] = '0'
    numero1['text'] = ''
    numero2['text'] = ''
    sinal_do_calculo['text'] = '[ ]'
    xxx = sinal_do_calculo['text']
    cont_num2 = 0
    cont_num1 = 0
def add_division() :
    global xxx
    sinal_do_calculo['text'] =  '÷'
    xxx = sinal_do_calculo['text'] 


#entradas/resultado
numero1 = tk.Label(janela, text='', width=8)
sinal_do_calculo = tk.Label(janela, text='[ ]')
numero2 = tk.Label(janela,text='', width=8)
texto_do_resultado = tk.Label(janela,text='Result :', fg='green')
resultado = tk.Label(janela, text="0", bg='green', fg='white', width=8)
numero1.grid(row=1, column=0)
sinal_do_calculo.grid(row=1, column=1)
numero2.grid(row=1, column=2)
texto_do_resultado.grid(row=2, column=0)
resultado.grid(row=2, column=1)
#numeros 
b9 = tk.Button(janela,text='9', command=add_number9, width= 5, height= 5)
b8 = tk.Button(janela,text='8', command=add_number8, width= 5, height= 5)
b7 = tk.Button(janela,text='7', command=add_number7, width= 5, height= 5)
mais = tk.Button(janela,text='+', command=add_mais, width= 5, height= 5)
b6 = tk.Button(janela,text='6', command=add_number6, width= 5, height= 5)
b5 = tk.Button(janela,text='5', command=add_number5, width= 5, height= 5)
b4 = tk.Button(janela,text='4', command=add_number4, width= 5, height= 5)
menos = tk.Button(janela,text='-', command=add_menos, width= 5, height= 5)
b3 = tk.Button(janela,text='3', command=add_number3, width= 5, height= 5)
b2 = tk.Button(janela,text='2', command=add_number2, width= 5, height= 5)
b1 = tk.Button(janela,text='1', command=add_number1, width= 5, height= 5)
vezes = tk.Button(janela,text='X' , command=add_multi, width= 5, height= 5)
b0 = tk.Button(janela,text='0', command=add_number0, width= 5, height= 5)
divisao = tk.Button(janela, text='÷', command=add_division, width= 5, height= 5)
delete = tk.Button(janela, text='DEL', bg='red', fg='white', command=delete, width= 5, height= 5 )
dar_resultado = tk.Button(janela,text='=', command=add_result, width= 5, height= 5)
b9.grid(row=3 , column=0, padx=5)
b8.grid(row=3 , column=1, padx=5)
b7.grid(row=3 , column=2, padx=5)
mais.grid(row=3 , column=3, padx=5)
b6.grid(row=4, column=0, padx=5)
b5.grid(row=4, column=1, padx=5)
b4.grid(row=4, column=2, padx=5)
menos.grid(row=4, column=3, padx=5)
b3.grid(row=5, column=0, padx=5)
b2.grid(row=5, column=1, padx=5)
b1.grid(row=5, column=2, padx=5)
vezes.grid(row=5, column=3, padx=5)
b0.grid(row=6, column=1, padx=5)
delete.grid(row=6, column=0, padx=5)
dar_resultado.grid(row=6, column=2, padx=5)
divisao.grid(row=6, column=3, padx=5)

xxx = sinal_do_calculo['text']   
cont_num1 = 0
cont_num2 = 0

janela.mainloop()