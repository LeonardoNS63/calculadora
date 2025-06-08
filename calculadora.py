import tkinter as tk
import tkinter.ttk as ttk 
janela = tk.Tk() 
janela.title("calculadora")
janela.geometry("350x400")

def valida_numero(digito) :
    x = len(digito)
    if x >= 10 :
        return False
    if digito.isdigit():
        return True
    else:
        return False
def add_number(event) :
    global cont_num1
    global cont_num2
    numero = event.widget['text']
    if cont_num2 <= 8 :
        if xxx != '[ ]' :
           numero2.insert('end', numero)
           cont_num2 += 1
    if cont_num1 <= 8 :
        if xxx == '[ ]' :
            numero1.insert('end', numero)
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
    valor1 = numero1.get()
    valor2 = numero2.get()
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
    numero1.delete(0, 'end')
    numero2.delete(0, 'end')
    sinal_do_calculo['text'] = '[ ]'
    xxx = sinal_do_calculo['text']
    cont_num2 = 0
    cont_num1 = 0
def delete() :
    global cont_num1
    global cont_num2
    global xxx
    resultado['text'] = ''
    numero1.delete(0, 'end')
    numero2.delete(0, 'end')
    sinal_do_calculo['text'] = '[ ]'
    xxx = sinal_do_calculo['text']
    cont_num2 = 0
    cont_num1 = 0
def botao_resultado() :
    result = resultado['text']
    global cont_num1
    global cont_num2
    try :
        numero1.delete(0, 10)
        resultado['text'] = ''
        cont_num2 = 0
        cont_num1 = 0
    except resultado['text'] == '' :
        return 

#frames 
frame1=tk.Frame(janela)
frame1.pack()
frame2=tk.Frame(janela)
frame2.pack(pady=3)
frame3=tk.Frame(janela)
frame3.pack(pady=3)
frame4=tk.Frame(janela)
frame4.pack()
frame5=tk.Frame(janela)
frame5.pack()
frame6 =tk.Frame(janela)
frame6.pack()

#entradas/resultado
numero1 = tk.Entry(frame1, text='', width=10, font='10', border=5)
numero1.config(validate="key", validatecommand=(janela.register(valida_numero), "%P"))
sinal_do_calculo = tk.Label(frame1, text='[ ]')
numero2 = tk.Entry(frame1,text='', width=10, font='10', border=5)
numero2.config(validate="key", validatecommand=(janela.register(valida_numero), "%P"))
resultado = tk.Label(frame2, text='', bg='white', width=20, font='20')
numero1.pack(side='left')
sinal_do_calculo.pack(side='left')
numero2.pack(side='left')
resultado.pack(side='left')





b9 = tk.Button(frame3,text='9',  width= 5, height= 5)
b8 = tk.Button(frame3,text='8',  width= 5, height= 5)
b7 = tk.Button(frame3,text='7',  width= 5, height= 5)
mais = tk.Button(frame3,text='+', width= 5, height= 5)
b_result = tk.Button(frame3,text='RESULT', width= 5, height= 5, command=botao_resultado)
b6 = tk.Button(frame4,text='6',  width= 5, height= 5)
b5 = tk.Button(frame4,text='5',  width= 5, height= 5)
b4 = tk.Button(frame4,text='4',  width= 5, height= 5)
menos = tk.Button(frame4,text='-', width= 5, height= 5)
b3 = tk.Button(frame5,text='3',  width= 5, height= 5)
b2 = tk.Button(frame5,text='2',  width= 5, height= 5)
b1 = tk.Button(frame5,text='1',  width= 5, height= 5)
vezes = tk.Button(frame5,text='X',  width= 5, height= 5)
b0 = tk.Button(frame6,text='0',  width= 5, height= 5)
divisao = tk.Button(frame6, text='÷', width= 5, height= 5)
delete = tk.Button(frame6, text='DEL',command=delete, bg='red', fg='white', width= 5, height= 5)
dar_resultado = tk.Button(frame6,text='=',command=add_result, width= 5, height= 5)
b9.grid(row=3 , column=0)
b9.bind("<Button-1>", add_number) 
b8.grid(row=3 , column=1)
b8.bind("<Button-1>", add_number) 
b7.grid(row=3 , column=2)
b7.bind("<Button-1>", add_number) 
mais.grid(row=3 , column=3)
mais.bind("<Button-1>", add_sinal)
b_result.grid(row=3, column=4)
b6.grid(row=4, column=0)
b6.bind("<Button-1>", add_number) 
b5.grid(row=4, column=1)
b5.bind("<Button-1>", add_number) 
b4.grid(row=4, column=2)
b4.bind("<Button-1>", add_number) 
menos.grid(row=4, column=3)
menos.bind("<Button-1>", add_sinal)
b3.grid(row=5, column=0)
b3.bind("<Button-1>", add_number) 
b2.grid(row=5, column=1)
b2.bind("<Button-1>", add_number) 
b1.grid(row=5, column=2)
b1.bind("<Button-1>", add_number) 
vezes.grid(row=5, column=3)
vezes.bind("<Button-1>", add_sinal)
b0.grid(row=6, column=1)
b0.bind("<Button-1>", add_number) 
delete.grid(row=6, column=0)
dar_resultado.grid(row=6, column=2)
divisao.grid(row=6, column=3)
divisao.bind("<Button-1>", add_sinal)

xxx = sinal_do_calculo['text']   
cont_num1 = 0
cont_num2 = 0

janela.mainloop()