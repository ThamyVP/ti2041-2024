# ti2041-2024
# Descripcion App
Aplicación web sencilla que permite a los administradores registrar y consultar datos básicos de los productos.
# Requisitos:
Python 3.10 (o superior)
Django 5.1
Git
# Ejecucion: 
una vez instalado los requisitos, debe:
clonar el repositorio desde su conexion de Github,
abrir la terminal,
escribir el comando (py manage.py runserver),
al cargar el comando arrojara el link correspondiente a la app la cual lo llevara a la pagina principal login,
debe ingresar con el user:admin contrasena:inacap2024, con esto podra ingresar a la lista de los productos, a la administracion de la pagina y poder agregar, eliminar y editar productos a su preferencia.
# Metodo seguridad:
El metodo de seguridad utilizado fue "Proteccion contra CSRF (Cross-Site Request Forgery)
el cual evita que un intruso use sesiones activas para enviar peticiones maliciosas.
Verifica que este habilitada la proteccion CSRF la cual fue dada por Django, inclue el token {%csrf_token%} en los formularios y para proteger las vistas que tengan solicitudes POST, se agrego el decorador @login_required para verificar el usuario.