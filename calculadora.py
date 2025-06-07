import tkinter as tk
import tkinter.ttk as ttk 
janela = tk.Tk() 
janela.title("calculadora")
janela.geometry("350x400")

def add_number(event) :
    global cont_num1
    global cont_num2
    numero = event.widget['text']
    if cont_num2 <= 8 :
        if xxx != '[ ]' :
           numero2['text'] = numero2['text'] + numero
           cont_num2 += 1
    if cont_num1 <= 8 :
        if xxx == '[ ]' :
            numero1['text'] = numero1['text'] + numero
            cont_num1 += 1
    else :
        print('ERRO : number of caracters full')
def add_sinal(event) :
    sinal = event.widget['text']
    global xxx
    sinal_do_calculo['text'] =  sinal
    xxx = sinal_do_calculo['text']

def add_result() :
    global cont_num1
    global cont_num2
    global xxx
    valor1 = numero1['text']
    valor2 = numero2['text']
    valor1 = int(valor1)
    valor2 = int(valor2)
    if xxx == 'X' :
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
    resultado['text'] = ''
    numero1['text'] = ''
    numero2['text'] = ''
    sinal_do_calculo['text'] = '[ ]'
    xxx = sinal_do_calculo['text']
    cont_num2 = 0
    cont_num1 = 0
def botao_resultado() :
    result = resultado['text']
    global cont_num1
    global cont_num2
    try :
        numero1['text'] = result
        resultado['text'] = ''
        cont_num2 = 0
        cont_num1 = 0
    except resultado['text'] == '' :
        return 
    

#entradas/resultado
numero1 = tk.Label(janela, text='', width=8)
sinal_do_calculo = tk.Label(janela, text='[ ]')
numero2 = tk.Label(janela,text='', width=8)
texto_do_resultado = tk.Label(janela,text='Result :', fg='green')
resultado = tk.Label(janela, text='', bg='green', fg='white', width=8)
numero1.grid(row=1, column=0)
sinal_do_calculo.grid(row=1, column=1)
numero2.grid(row=1, column=2)
texto_do_resultado.grid(row=2, column=0)
resultado.grid(row=2, column=1)
#numeros 
b9 = tk.Button(janela,text='9',  width= 5, height= 5)
b8 = tk.Button(janela,text='8',  width= 5, height= 5)
b7 = tk.Button(janela,text='7',  width= 5, height= 5)
mais = tk.Button(janela,text='+', width= 5, height= 5)
b6 = tk.Button(janela,text='6',  width= 5, height= 5)
b5 = tk.Button(janela,text='5',  width= 5, height= 5)
b4 = tk.Button(janela,text='4',  width= 5, height= 5)
menos = tk.Button(janela,text='-', width= 5, height= 5)
b3 = tk.Button(janela,text='3',  width= 5, height= 5)
b2 = tk.Button(janela,text='2',  width= 5, height= 5)
b1 = tk.Button(janela,text='1',  width= 5, height= 5)
vezes = tk.Button(janela,text='X',  width= 5, height= 5)
b0 = tk.Button(janela,text='0',  width= 5, height= 5)
divisao = tk.Button(janela, text='÷', width= 5, height= 5)
delete = tk.Button(janela, text='DEL',command=delete, bg='red', fg='white', width= 5, height= 5)
dar_resultado = tk.Button(janela,text='=',command=add_result, width= 5, height= 5)
b_result = tk.Button(janela,text='RESULT', width= 5, height= 5, command=botao_resultado)
# grid e bind dos botoes 
b9.grid(row=3 , column=0, padx=7)
b9.bind("<Button-1>", add_number) 
b8.grid(row=3 , column=1, padx=7)
b8.bind("<Button-1>", add_number) 
b7.grid(row=3 , column=2, padx=7)
b7.bind("<Button-1>", add_number) 
mais.grid(row=3 , column=3, padx=7)
mais.bind("<Button-1>", add_sinal)
b_result.grid(row=3 , column=4, padx=7)
b6.grid(row=4, column=0, padx=7)
b6.bind("<Button-1>", add_number) 
b5.grid(row=4, column=1, padx=7)
b5.bind("<Button-1>", add_number) 
b4.grid(row=4, column=2, padx=7)
b4.bind("<Button-1>", add_number) 
menos.grid(row=4, column=3, padx=7)
menos.bind("<Button-1>", add_sinal)
b3.grid(row=5, column=0, padx=7)
b3.bind("<Button-1>", add_number) 
b2.grid(row=5, column=1, padx=7)
b2.bind("<Button-1>", add_number) 
b1.grid(row=5, column=2, padx=7)
b1.bind("<Button-1>", add_number) 
vezes.grid(row=5, column=3, padx=7)
vezes.bind("<Button-1>", add_sinal)
b0.grid(row=6, column=1, padx=7)
b0.bind("<Button-1>", add_number) 
delete.grid(row=6, column=0, padx=7)
dar_resultado.grid(row=6, column=2, padx=7)
divisao.grid(row=6, column=3, padx=7)
divisao.bind("<Button-1>", add_sinal)

xxx = sinal_do_calculo['text']   
cont_num1 = 0
cont_num2 = 0

janela.mainloop()