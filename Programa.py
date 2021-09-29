import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy

#carregar o modelo de DL
from keras.models import load_model
model = load_model('my_model.h5')

#classes existentes de sinais de transito
classes = { 1:'Limite de velocidade (20km/h)',
            2:'Limite de velocidade (30km/h)',      
            3:'Limite de velocidade (50km/h)',       
            4:'Limite de velocidade (60km/h)',      
            5:'Limite de velocidade (70km/h)',    
            6:'Limite de velocidade (80km/h)',      
            7:'Fim do limite de velocidade (80km/h)',     
            8:'Limite de velocidade (100km/h)',    
            9:'Limite de velocidade (120km/h)',     
           10:'Proibição de ultrapassar',   
           11:'Proibição de ultrapassar para automóveis pesados',     
           12:'Cruzamento com via sem prioridade',     
           13:'Via com prioridade',    
           14:'Cedência de passagem',     
           15:'Stop',       
           16:'Trânsito proibido',       
           17:'Trânsito proibido a automóveis de mercadorias',       
           18:'Sentido proibido',       
           19:'Outros perigos',     
           20:'Curva à esquerda',      
           21:'Curva à direita',   
           22:'Curva à esquerda e contracurva',      
           23:'Lomba ou depressão',     
           24:'Pavimento escorregadio',       
           25:'Passagem estreita',  
           26:'Trabalhos na via',    
           27:'Sinalização luminosa',      
           28:'Travessia de peões',     
           29:'Crianças',     
           30:'Saída de ciclistas',       
           31:'Neve ou gelo',
           32:'Animais selvagens',      
           33:'Fim de todas as proibições',      
           34:'Virar à direita',     
           35:'Virar à esquerda',       
           36:'Seguir em frente',      
           37:'Seguir em frente ou virar à direita',      
           38:'Seguir em frente ou virar à esquerda',      
           39:'Contornar pela direita',     
           40:'Contornar pela esquerda',      
           41:'Rotunda',     
           42:'Fim da proibição de ultrapassar',      
           43:'Fim da proibição de ultrapassar para automóveis pesados' }
                 
#inicializar interface
top=tk.Tk()
top.geometry('800x600')
top.title('RAST - Reconhecimento Automático de Sinais de Trânsito')
top.configure(background='#CDCDCD')
#BG do Label
label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(top)

def classificar(caminho):
    global label_packed
    image = Image.open(caminho)
    image = image.resize((30,30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    print(image.shape)
    pred = model.predict_classes([image])[0]
    sign = classes[pred+1]
    print(sign)
    label.configure(foreground='#375636', text=sign) 
   

def mostrar_botao_classificacao(caminho):
    classify_b=Button(top,text="Classificar Sinal", command=lambda: classificar(caminho),padx=10,pady=5)
    classify_b.configure(background='#375636', foreground='white',font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_imagem():
    try:
        caminho=filedialog.askopenfilename()
        uploaded=Image.open(caminho)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        mostrar_botao_classificacao(caminho)
    except:
        pass

upload=Button(top,text="Selecionar Imagem",command=upload_imagem,padx=10,pady=5)
upload.configure(background='#375636', foreground='white',font=('arial',10,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Reconhecimento Automático de Sinais de Trânsito",pady=20, font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()


