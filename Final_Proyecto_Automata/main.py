from tkinter import *
from tkinter import messagebox
import webbrowser  

raiz = Tk()
raiz.title("Inicio de sesión")
raiz.geometry('925x500+300+200')
raiz.configure(bg="#fff")
raiz.resizable(False, False)

#Alfabeto que se utilizará para codificar mensaje
alfabeto_en_signos = {
    'a': 'α', 'b': 'β', 'c': '¢', 'd': '∂', 'e': '3', 'f': '∫',
    'g': 'ϱ', 'h': '∞', 'i': '1', 'j': '√', 'k': 'κ', 'l': '|',
    'm': 'μ', 'n': 'η', 'o': '0', 'p': 'π', 'q': 'ψ', 'r': 'ρ',
    's': '5', 't': '7', 'u': 'υ', 'v': 'ν', 'w': 'ω', 'x': 'ξ',
    'y': 'γ', 'z': 'ζ', ' ': ' '  
}

#función de codificación de mensaje
def codificar(texto):
    codificacion = ""
    for letra in texto.lower():  # normalización de texto a minusculas
        if letra in alfabeto_en_signos: #Recorre la letra actual para validar si se encuentra en el alfabeto
            codificacion += alfabeto_en_signos[letra] 
        else:
            codificacion += letra  # si la letra no posee un signo de cambio, se mantendrá igual
    return codificacion

#Alfabeto que se utilizará para descodificar mensaje
alfabeto_normal = {
    'α': 'a', 'β': 'b', '¢': 'c', '∂': 'd', '3': 'e', '∫': 'f',
    'ϱ': 'g', '∞': 'h', '1': 'i', '√': 'j', 'κ': 'k', '|': 'l',
    'μ': 'm', 'η': 'n', '0': 'o', 'π': 'p', 'ψ': 'q', 'ρ': 'r',
    '5': 's', '7': 't', 'υ': 'u', 'ν': 'v', 'ω': 'w', 'ξ': 'x',
    'γ': 'y', 'ζ': 'z', ' ': ' '  
}

#función para descodificar mennsaje
def descodificar(texto):
    descodificacion = ""
    for letra in texto.lower():  # normalización de texto a minusculas
        if letra in alfabeto_normal: #Recorre la letra actual para validar si se encuentra en el alfabeto
            descodificacion += alfabeto_normal[letra] 
        else:
            descodificacion += letra  # si la letra no posee un signo de cambio, se mantendrá igual
    return descodificacion

#AFD para validar un mensaje previo a la codificación
class afdPreCod():
    def init(self):
        self.alfabeto = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','¿','?','¡','!','.',' ',}
        self.estados = {'s0','s1','s2','s3','s4','s5','s6','s7','s8','s9'}
        self.estadoInicial = 's0'
        self.estadosFinales = {'s6','s8','s9'}
        self.transiciones = {
            "s0":{'A':'s8','B':'s8','C':'s8','D':'s8','E':'s8','F':'s8','G':'s8','H':'s8','I':'s8','J':'s8','K':'s8','L':'s8','M':'s8','N':'s8','O':'s8','P':'s8','Q':'s8','R':'s8','S':'s8','T':'s8','U':'s8','V':'s8','W':'s8','X':'s8','Y':'s8','Z':'s8','¿':'s1','?':'s4','¡':'s2','!':'s4','.':'s4',' ':'s4'},
            "s1":{'A':'s3','B':'s3','C':'s3','D':'s3','E':'s3','F':'s3','G':'s3','H':'s3','I':'s3','J':'s3','K':'s3','L':'s3','M':'s3','N':'s3','O':'s3','P':'s3','Q':'s3','R':'s3','S':'s3','T':'s3','U':'s3','V':'s3','W':'s3','X':'s3','Y':'s3','Z':'s3','¿':'s4','?':'s4','¡':'s4','!':'s4','.':'s4',' ':'s4'},
            "s2":{'A':'s5','B':'s5','C':'s5','D':'s5','E':'s5','F':'s5','G':'s5','H':'s5','I':'s5','J':'s5','K':'s5','L':'s5','M':'s5','N':'s5','O':'s5','P':'s5','Q':'s5','R':'s5','S':'s5','T':'s5','U':'s5','V':'s5','W':'s5','X':'s5','Y':'s5','Z':'s5','¿':'s4','?':'s4','¡':'s4','!':'s4','.':'s4',' ':'s4'},
            "s3":{'A':'s3','B':'s3','C':'s3','D':'s3','E':'s3','F':'s3','G':'s3','H':'s3','I':'s3','J':'s3','K':'s3','L':'s3','M':'s3','N':'s3','O':'s3','P':'s3','Q':'s3','R':'s3','S':'s3','T':'s3','U':'s3','V':'s3','W':'s3','X':'s3','Y':'s3','Z':'s3','¿':'s4','?':'s6','¡':'s4','!':'s4','.':'s4',' ':'s1'},
            "s4":{'A':'s4','B':'s4','C':'s4','D':'s4','E':'s4','F':'s4','G':'s4','H':'s4','I':'s4','J':'s4','K':'s4','L':'s4','M':'s4','N':'s4','O':'s4','P':'s4','Q':'s4','R':'s4','S':'s4','T':'s4','U':'s4','V':'s4','W':'s4','X':'s4','Y':'s4','Z':'s4','¿':'s4','?':'s4','¡':'s4','!':'s4','.':'s4',' ':'s4'},
            "s5":{'A':'s5','B':'s5','C':'s5','D':'s5','E':'s5','F':'s5','G':'s5','H':'s5','I':'s5','J':'s5','K':'s5','L':'s5','M':'s5','N':'s5','O':'s5','P':'s5','Q':'s5','R':'s5','S':'s5','T':'s5','U':'s5','V':'s5','W':'s5','X':'s5','Y':'s5','Z':'s5','¿':'s4','?':'s4','¡':'s4','!':'s6','.':'s4',' ':'s2'},
            "s6":{'A':'s4','B':'s4','C':'s4','D':'s4','E':'s4','F':'s4','G':'s4','H':'s4','I':'s4','J':'s4','K':'s4','L':'s4','M':'s4','N':'s4','O':'s4','P':'s4','Q':'s4','R':'s4','S':'s4','T':'s4','U':'s4','V':'s4','W':'s4','X':'s4','Y':'s4','Z':'s4','¿':'s4','?':'s4','¡':'s4','!':'s4','.':'s4',' ':'s7'},
            "s7":{'A':'s8','B':'s8','C':'s8','D':'s8','E':'s8','F':'s8','G':'s8','H':'s8','I':'s8','J':'s8','K':'s8','L':'s8','M':'s8','N':'s8','O':'s8','P':'s8','Q':'s8','R':'s8','S':'s8','T':'s8','U':'s8','V':'s8','W':'s8','X':'s8','Y':'s8','Z':'s8','¿':'s1','?':'s4','¡':'s2','!':'s4','.':'s4',' ':'s4'},
            "s8":{'A':'s8','B':'s8','C':'s8','D':'s8','E':'s8','F':'s8','G':'s8','H':'s8','I':'s8','J':'s8','K':'s8','L':'s8','M':'s8','N':'s8','O':'s8','P':'s8','Q':'s8','R':'s8','S':'s8','T':'s8','U':'s8','V':'s8','W':'s8','X':'s8','Y':'s8','Z':'s8','¿':'s4','?':'s4','¡':'s4','!':'s4','.':'s9',' ':'s7'},
            "s9":{'A':'s4','B':'s4','C':'s4','D':'s4','E':'s4','F':'s4','G':'s4','H':'s4','I':'s4','J':'s4','K':'s4','L':'s4','M':'s4','N':'s4','O':'s4','P':'s4','Q':'s4','R':'s4','S':'s4','T':'s4','U':'s4','V':'s4','W':'s4','X':'s4','Y':'s4','Z':'s4','¿':'s4','?':'s4','¡':'s4','!':'s4','.':'s9',' ':'s7'}
        }
        self.actual=self.estadoInicial
    
    def reinicio(self):
        self.actual = self.estadoInicial

    def procesar(self, cadena):
        self.reinicio()
        for palabra in cadena:
            palabra = palabra.upper()

            self.actual = self.transiciones[self.actual][palabra]
    
        if self.actual in self.estadosFinales:
            print(codificar(cadena))
        else:
            return False, print('Palabra Invalida')#Agregar mensaje en front end visual

class afdPreDesCod():
    def init(self):
        self.alfabeto = {'α','β','¢','∂','3','∫','ϱ','∞','1','√','κ','|','μ','η','0','π','ψ','ρ','5','7','υ','ν','ω','ξ','γ','ζ','¿','?','¡','!','.',' ',}
        self.estados = {'s0','s1','s2','s3','s4','s5','s6','s7','s8','s9'}
        self.estadoInicial = 's0'
        self.estadosFinales = {'s6','s8','s9'}
        self.transiciones = {
            "s0":{'α':'s8','β':'s8','¢':'s8','∂':'s8','3':'s8','∫':'s8','ϱ':'s8','∞':'s8','1':'s8','√':'s8','κ':'s8','|':'s8','μ':'s8','η':'s8','0':'s8','π':'s8','ψ':'s8','ρ':'s8','5':'s8','7':'s8','υ':'s8','ν':'s8','ω':'s8','ξ':'s8','γ':'s8','ζ':'s8','¿':'s1','?':'s4','¡':'s2','!':'s4','.':'s4',' ':'s4'},
            "s1":{'α':'s3','β':'s3','¢':'s3','∂':'s3','3':'s3','∫':'s3','ϱ':'s3','∞':'s3','1':'s3','√':'s3','κ':'s3','|':'s3','μ':'s3','η':'s3','0':'s3','π':'s3','ψ':'s3','ρ':'s3','5':'s3','7':'s3','υ':'s3','ν':'s3','ω':'s3','ξ':'s3','γ':'s3','ζ':'s3','¿':'s4','?':'s4','¡':'s4','!':'s4','.':'s4',' ':'s4'},
            "s2":{'α':'ss','β':'ss','¢':'ss','∂':'ss','3':'ss','∫':'ss','ϱ':'ss','∞':'ss','1':'ss','√':'ss','κ':'ss','|':'ss','μ':'ss','η':'ss','0':'ss','π':'ss','ψ':'ss','ρ':'ss','5':'ss','7':'ss','υ':'ss','ν':'ss','ω':'ss','ξ':'ss','γ':'ss','ζ':'ss','¿':'s4','?':'s4','¡':'s4','!':'s4','.':'s4',' ':'s4'},
            "s3":{'α':'s3','β':'s3','¢':'s3','∂':'s3','3':'s3','∫':'s3','ϱ':'s3','∞':'s3','1':'s3','√':'s3','κ':'s3','|':'s3','μ':'s3','η':'s3','0':'s3','π':'s3','ψ':'s3','ρ':'s3','5':'s3','7':'s3','υ':'s3','ν':'s3','ω':'s3','ξ':'s3','γ':'s3','ζ':'s3','¿':'s4','?':'s6','¡':'s4','!':'s4','.':'s4',' ':'s1'},
            "s4":{'α':'s4','β':'s4','¢':'s4','∂':'s4','3':'s4','∫':'s4','ϱ':'s4','∞':'s4','1':'s4','√':'s4','κ':'s4','|':'s4','μ':'s4','η':'s4','0':'s4','π':'s4','ψ':'s4','ρ':'s4','5':'s4','7':'s4','υ':'s4','ν':'s4','ω':'s4','ξ':'s4','γ':'s4','ζ':'s4','¿':'s4','?':'s4','¡':'s4','!':'s4','.':'s4',' ':'s4'},
            "ss":{'α':'ss','β':'ss','¢':'ss','∂':'ss','3':'ss','∫':'ss','ϱ':'ss','∞':'ss','1':'ss','√':'ss','κ':'ss','|':'ss','μ':'ss','η':'ss','0':'ss','π':'ss','ψ':'ss','ρ':'ss','5':'ss','7':'ss','υ':'ss','ν':'ss','ω':'ss','ξ':'ss','γ':'ss','ζ':'ss','¿':'s4','?':'s4','¡':'s4','!':'s6','.':'s4',' ':'s2'},
            "s6":{'α':'s4','β':'s4','¢':'s4','∂':'s4','3':'s4','∫':'s4','ϱ':'s4','∞':'s4','1':'s4','√':'s4','κ':'s4','|':'s4','μ':'s4','η':'s4','0':'s4','π':'s4','ψ':'s4','ρ':'s4','5':'s4','7':'s4','υ':'s4','ν':'s4','ω':'s4','ξ':'s4','γ':'s4','ζ':'s4','¿':'s4','?':'s4','¡':'s4','!':'s4','.':'s4',' ':'s7'},
            "s7":{'α':'s8','β':'s8','¢':'s8','∂':'s8','3':'s8','∫':'s8','ϱ':'s8','∞':'s8','1':'s8','√':'s8','κ':'s8','|':'s8','μ':'s8','η':'s8','0':'s8','π':'s8','ψ':'s8','ρ':'s8','5':'s8','7':'s8','υ':'s8','ν':'s8','ω':'s8','ξ':'s8','γ':'s8','ζ':'s8','¿':'s1','?':'s4','¡':'s2','!':'s4','.':'s4',' ':'s4'},
            "s8":{'α':'s8','β':'s8','¢':'s8','∂':'s8','3':'s8','∫':'s8','ϱ':'s8','∞':'s8','1':'s8','√':'s8','κ':'s8','|':'s8','μ':'s8','η':'s8','0':'s8','π':'s8','ψ':'s8','ρ':'s8','5':'s8','7':'s8','υ':'s8','ν':'s8','ω':'s8','ξ':'s8','γ':'s8','ζ':'s8','¿':'s4','?':'s4','¡':'s4','!':'s4','.':'s9',' ':'s7'},
            "s9":{'α':'s4','β':'s4','¢':'s4','∂':'s4','3':'s4','∫':'s4','ϱ':'s4','∞':'s4','1':'s4','√':'s4','κ':'s4','|':'s4','μ':'s4','η':'s4','0':'s4','π':'s4','ψ':'s4','ρ':'s4','5':'s4','7':'s4','υ':'s4','ν':'s4','ω':'s4','ξ':'s4','γ':'s4','ζ':'s4','¿':'s4','?':'s4','¡':'s4','!':'s4','.':'s9',' ':'s7'}
        }
        self.actual=self.estadoInicial
    
    def reinicio(self):
        self.actual = self.estadoInicial

    def procesar(self, cadena):
        self.reinicio()
        for palabra in cadena:

            self.actual = self.transiciones[self.actual][palabra]
    
        if self.actual in self.estadosFinales:
            print(descodificar(cadena))
        else:
            return False, print('Palabra Invalida')#Agregar mensaje en front end visual

def signin():
    username = user.get()
    password = code.get()

    if username == "admin" and password == "1234":
        screen = Toplevel(raiz)
        screen.title("App")
        screen.geometry("400x300+300+200")  
        screen.config(bg="white")
        
        
        Label(screen, text="Bienvenido", bg="white", font=("Microsoft YaHei UI Light", 15, "bold")).pack(pady=10)

        
        Label(screen, text="Escribe tu mensaje:", bg="white", font=("Microsoft YaHei UI Light", 10)).pack(pady=10)
        message_entry = Entry(screen, width=30, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        message_entry.pack(pady=5)
        Frame(screen, width=295, height=2, bg="black").pack(pady=5)

        
        Button(screen, text="Quiero enviar un mensaje codificado", bg="#57a1f8", fg="white", border=0, width=30,
                command=lambda: enviar_a_whatsapp(codificar(message_entry.get()))).pack(pady=10)

        
        Button(screen, text="Quiero descodificar un mensaje", bg="#57a1f8", fg="white", border=0, width=30,
                command=lambda: mostrar_resultado("Decodificado", descodificar(message_entry.get()))).pack(pady=10)

    elif username != "admin" and password != "1234":
        messagebox.showerror("Error", "Usuario y contraseña inválidos")

    elif password != "1234":
        messagebox.showerror("Error", "Contraseña inválida")


def mostrar_resultado(tipo, resultado):
    messagebox.showinfo(f"Resultado {tipo}", resultado)


def enviar_a_whatsapp(mensaje_codificado):
    
    numero = '00000000'
    mensaje = mensaje_codificado
    url = f"https://wa.me/{numero}?text={mensaje}"  
    webbrowser.open(url)  


img = PhotoImage(file='Images/logo1.png')
Label(raiz, image=img, bg='white').place(x=30, y=30)

frame = Frame(raiz, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text="Ingresa", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=130, y=5)

def on_enter(e):
    user.delete(0, "end")

def on_leave(e):
    name = user.get()
    if name == "":
        user.insert(0, "Usuario")

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, "Usuario")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

def on_enter(e):
    code.delete(0, "end")

def on_leave(e):
    name = code.get()
    if name == "":
        code.insert(0, "Contraseña")

code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
code.place(x=30, y=150)
code.insert(0, "Contraseña")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

Button(frame, width=42, pady=7, text="Sign in", bg="#57a1f8", fg="white", border=0, command=signin).place(x=35, y=204)
label = Label(frame, text="¿No tienes cuenta?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text="Sign up", border=0, bg="white", cursor="hand2", fg="#57a1f8")
sign_up.place(x=215, y=270)

raiz.mainloop()