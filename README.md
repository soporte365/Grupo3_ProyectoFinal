# Título del Proyecto

_Desarrollo de una API con Python, FastAPI y base de datos PostgreSQL como backend para proceso de envió de remesas._

## Comenzando 🚀

_Utilizar las herramientas de git clone, ya sea desde tu ide, o descargando desde la web._

### Descripción del proyecto 📋

_El proyecto consiste en el desarrollo de una base de datos y una API (Application Programming Interface) basada en Python, utilizando el framework FastAPI y PostgreSQL como base de datos. Este software permitirá la creación de un servicio backend que podrá ser consumido por cualquier aplicaciones front-end creada. El propósito de la API y la base de datos es agilizar los procesos manuales llevados a cabo por la empresa de remesas, donde se aplicará seguridad y las cuatro operaciones básicas CRUD._

## Funcionalidades 🖇️


* Endpoints CRUD:
   _Crear, leer, actualizar y eliminar recursos (usuarios, tasas, países, emisores, beneficiarios y transacciones)_

* Autenticación y autorización:
   _Implementación de OAuth2 con JWT(JSON Web Token) para cada usuario._

* Validación de datos:
   _Uso de Pydantic para la validación automática de los datos de entrada y salida._

## La operatividad 📌

```
1-	Los Encargados o remeseros publican las tasas diariamente de los diferentes cambios de divisas, las cuales envían a los agentes y podrán registrarla en el sistema para su uso.
2-	El cliente se comunica por mensajes de WhatsAPP con un agente para envío de divisas.
3-	El agente responde enviando que primeramente deposite la cantidad enviada.
4-	Si el cliente realiza el abono, se procede con la solicitud de información de:
a-	País destino.
b-	Datos del emisor (nombre, documento, telf., correo).
c-	Datos del beneficiario o receptor (nombre, documento, telf., correo, banco, tipo de cuenta, numero de cuenta).
Nota: si el cliente necesita saber cuanto es el cambio, el agente desde el sistema podrá calcular usando el monto que desea enviar el cliente en conjunto con el tipo de cambio del día.
5-	Una vez obtenido esos datos se procederá a llenarlos en el sistema en conjunto con la solicitud del ticket o giro el cual tendrá la siguiente estructura:
a-	Titulo o descripción: Giro: País origen – País destino – correlativo
b-	Datos del emisor.
c-	Datos del beneficiario.
d-	Monto enviado
e-	 Tasa seleccionada según país origen – destino
f-	Monto a recibir (calculado)
g-	El agente quien está realizando el ticket.
6-	Se podrá generar un ticket y se deberá actualizar las tablas de emisor y receptor para no hacer registros por separados, mas puede ser modificados por separado.
7-	Los encargados de publicar las tasas son los que ejecutan las transacciones a los beneficiarios, por lo que ellos podrán acceder al sistema y validar los tickets que se mostrarán con un estado de pendiente, o en proceso.
8-	Luego de que los remeseros concluyan la transacción podrán actualizar el estado del giro que estará en pendiente a procesado y podrán enviarles el recibo de la transferencia realizada o el ticket generado, de manera resumida ya sea por correo o whatsAPP.

```

## Resultados 📄


** Con el sistema se podrá: **

```
* Generar una base de datos con los clientes, beneficiarios, tasas, países, usuarios (agentes y administradores), bancos, y el registro del tickets o transacción.
* Calculo de cambios según la tasa del día.
* Calculo de pago de % para cada agente.
* Envío de manera eficiente la información al cliente sobre su transferencia.
* Llevar mejor contabilidad de los montos recibidos y enviados.


```

### Pre-requisitos  🔧 

_El IDE  de tu preferncia y los componentes que necesites para que sea compatible en caso uses otro que no sea PyCharm_



## Construido con 🛠️


* [PyCharm](https://www.jetbrains.com/pycharm/download/?section=windows) - El IDE usado
* Las dependencias y librerias estan dentro del archivo requirements.txt


## Autores ✒️

_Aquí figuran todos aquellos que ayudaron a levantar el proyecto desde sus inicios, hasta la actualidad_

* **Carlos Torres** 
* **Jose Figuera** 
* **Rafael Perez** 

