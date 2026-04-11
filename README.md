SISTEMA DE GESTION DE INVENTARIO Y VENTAS

Un sistema web completo para gestionar productos, clientes y ventas de forma eficiente.
Desarrollado con Flask, SQLAlchemy y SQLite.

CARACTERISTICAS

- Gestión de productos con CRUD completo
- Gestión de clientes con registro y edición
- Sistema de ventas con control automático de stock
- Interfaz web responsive y moderna
- Base de datos SQLite integrada
- Validación de datos en servidor y cliente
- Panel de control con estadísticas en tiempo real
- Historial de ventas con fecha y monto

TECNOLOGIAS UTILIZADAS

- Python 3.8+
- Flask (framework web)
- SQLAlchemy (ORM para base de datos)
- SQLite (base de datos)
- HTML5 (estructura)
- CSS3 (estilos)
- JavaScript (funcionalidad frontend)


REQUISITOS

Python 3.8 o superior
pip (administrador de paquetes de Python)

DEPENDENCIAS

Flask==2.3.0
Flask-SQLAlchemy==3.0.5
SQLAlchemy==2.0.0
Werkzeug==2.3.0

INSTALACION

1. Clonar el repositorio

git clone https://github.com/tu-usuario/sistema-inventario.git
cd sistema-inventario

2. Dirigirse a la carpeta backend

cd backend

3. Crear un ambiente virtual

# En Linux/Mac
python3 -m venv venv
source venv/bin/activate

# En Windows
python -m venv venv
venv\Scripts\activate

4. Instalar las dependencias

pip install -r requirements.txt

5. Ejecutar la aplicación

python app.py

La aplicación estará disponible en http://localhost:5000

USO DEL SISTEMA

PAGINA DE INICIO

Al abrir la aplicación, verás el panel de control con:
- Total de productos registrados
- Total de clientes registrados
- Total de ventas realizadas
- Total de ingresos generados
- Accesos rápidos a cada sección

GESTION DE PRODUCTOS

Crear producto: Completa el formulario con tipo, cantidad y precio
Listar productos: Se muestra en una tabla con todas las propiedades
Editar producto: Haz clic en el botón "Editar" para modificar datos
Eliminar producto: Haz clic en "Eliminar" para borrar un producto

Validaciones:
- Tipo de producto obligatorio
- Cantidad debe ser un numero >= 0
- Precio debe ser un numero >= 0

GESTION DE CLIENTES

Crear cliente: Completa el formulario con todos los datos obligatorios
Selecciona tipo de identificación: CC, CE, NIT, PEP, TI, DNI
Listar clientes: Tabla con información completa del cliente
Editar cliente: Modifica nombre, apellido, telefono y email
Eliminar cliente: Borra permanentemente el cliente del sistema

Validaciones:
- Email unico en el sistema
- Identificación unica
- Telefono es obligatorio
- Email con formato válido

REGISTRO DE VENTAS

Registrar venta: Selecciona producto y cliente, ingresa cantidad
El sistema calcula automáticamente el total
Control de stock: Se reduce automáticamente el inventario
Historial: Ver todas las ventas con fecha y monto
Eliminar venta: Deshace la venta y devuelve el stock

MODELOS DE BASE DE DATOS

PRODUCTO

id (Primary Key)
tipo (String) - Nombre del producto
cantidad (Integer) - Stock disponible
precio (Float) - Precio unitario
fecha_creacion (DateTime) - Fecha de registro

CLIENTE

id (Primary Key)
tipo_identificacion (String) - Tipo de documento
identificacion (String) - Numero de documento
nombre (String) - Nombre del cliente
apellido (String) - Apellido del cliente
numero_Telefonico (String) - Telefono de contacto
email (String) - Email del cliente
fecha_registro (DateTime) - Fecha de registro

VENTA

id (Primary Key)
id_producto (Foreign Key) - Referencia al producto
id_cliente (Foreign Key) - Referencia al cliente
cantidad (Integer) - Cantidad vendida
fecha (DateTime) - Fecha de la venta
total (Float) - Monto total de la venta

CONFIGURACION

1. Base de datos

La base de datos se crea automáticamente al ejecutar la aplicación.
Se utiliza SQLite, un archivo llamado productos.db en la carpeta backend.

Para reiniciar la base de datos:

rm productos.db
python app.py

SOLUCION DE PROBLEMAS

Problema: "No such column"

Solucion: Elimina la base de datos y crea una nueva
rm productos.db
python app.py

Problema: "ModuleNotFoundError: No module named 'flask'"

Solucion: Instala las dependencias
pip install -r requirements.txt

Problema: "Port 5000 already in use"

Solucion: Cambia el puerto en app.py (ultima linea):
app.run(debug=True, port=8000)

Problema: El server no inicia

Solucion: Verifica que estes en la carpeta backend
Verifica que el ambiente virtual este activado
Verifica que Python 3.8+ este instalado



LICENCIA

Este proyecto esta bajo la licencia MIT. Ver el archivo LICENSE para mas detalles.



REFERENCIAS

- Documentacion oficial de Flask: https://flask.palletsprojects.com/
- Documentacion de SQLAlchemy: https://docs.sqlalchemy.org/
- MDN Web Docs: https://developer.mozilla.org/
- Python Documentation: https://docs.python.org/3/
