
# Estas son funciones que compartian tanto instancias de login y register, entonces las dejo aca para que ambos compartan estas
# en el caso de registro, dicha clase tiene 3 metodos mas debido a que el registro tiene una entrada mas para confirmar la "Password"

# Los siguientes son metodos que agregan calidad, focus in and out para los entries que creé en clases de register y login

# Función para manejar el evento de enfoque del usuario
# tambien se encarga de eliminar espacios en blanco para eliminar sensibilidad 
def user_on_enter(entry):
    name = entry.get()
    entry.delete(0, 'end')
    if name == 'Username':
        entry.config(foreground='black')
    else:
        entry.insert(0, name.strip())

# Función para manejar el evento de desenfoque del usuario
def user_on_leave(entry):
    name = entry.get()
    if name == '':
        entry.config(foreground='gray')
        entry.insert(0, 'Username')

# Función para manejar el evento de enfoque de la contraseña
# tambien se encarga de eliminar espacios en blanco para eliminar sensibilidad 
def code_on_enter(entry):
    name = entry.get()
    entry.delete(0, 'end')
    if name == 'Password':
        entry.config(foreground='black')
    else:
        entry.insert(0, name.strip())

# Función para manejar el evento de desenfoque de la contraseña
def code_on_leave(entry):
    name = entry.get()
    if name == '':
        entry.config(foreground='gray')
        entry.insert(0, 'Password')

# cuando enfoco al entry, desaparece el "Confirm Password" en gris, escribo en negro 
# tambien se encarga de eliminar espacios en blanco para eliminar sensibilidad        
def confirm_on_enter(entry):
    name = entry.get()
    entry.delete(0, 'end')
    if name == 'Confirm Password':
        entry.config(foreground='black')
    else: entry.insert(0,name.strip())
    
# cuando desenfoco el entry, aparece el "Confirm Password" en gris (si no hay nada escrito)
def confirm_on_leave(entry):
    name = entry.get()
    if name == '':
        entry.config(foreground='gray')
        entry.insert(0, 'Confirm Password')