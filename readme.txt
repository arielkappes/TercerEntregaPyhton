Proyecto de Administración de Bienes (Vehículos)
Este proyecto consiste en una aplicación de gestión de bienes, específicamente vehículos, desarrollada en Python utilizando bases de datos. La aplicación incluye funcionalidades CRUD (Crear, Leer, Actualizar, Eliminar) para las tablas de bienes, personal, áreas y rubros, así como funcionalidades de inicio de sesión, cierre de sesión y modificación de tablas y perfiles de usuarios.

Instalación
Clona este repositorio en tu máquina local:

bash
Copy code
git clone https://github.com/tu_usuario/proyecto-admin-bienes.git
Accede al directorio del proyecto:

bash
Copy code
cd proyecto-admin-bienes
Instala las dependencias utilizando pip:

Copy code
pip install -r requirements.txt
Configura el archivo de configuración config.py con los detalles de tu base de datos.

Uso
Ejecuta el archivo main.py para iniciar la aplicación:

css
Copy code
python main.py
La aplicación mostrará un menú de opciones desde donde puedes acceder a las diferentes funcionalidades, como CRUD para bienes, personal, áreas y rubros, así como opciones para iniciar sesión, cerrar sesión y modificar tablas y perfiles de usuarios.

Estructura del Proyecto
aplicacion: Archivo principal que contiene la lógica de la aplicación y el menú principal.
biene.py: Módulo que maneja las operaciones CRUD para la tabla de bienes (vehículos).
personal.py: Módulo que maneja las operaciones CRUD para la tabla de personal.
areas.py: Módulo que maneja las operaciones CRUD para la tabla de áreas.
rubros.py: Módulo que maneja las operaciones CRUD para la tabla de rubros.
auth.py: Módulo que maneja la autenticación de usuarios y la gestión de perfiles.
database.py: Módulo que contiene funciones para interactuar con la base de datos.
config.py: Archivo de configuración donde se pueden especificar detalles de la base de datos.
requirements.txt: Archivo que lista las dependencias del proyecto.
Contribución
¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, no dudes en abrir un problema o enviar una solicitud de extracción con tus cambios propuestos.

Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.

