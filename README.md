## MODO DE USO 

Para poder utilizar el script es necesario :

* Tener instalado [python 3](https://www.python.org/downloads/)

* Instalar los paquetes necesarios, de preferencia con [pip](https://pip.pypa.io/en/stable/installation/)
```
    pip install paramiko psycopg2
```

* Generar el archivo de configuración __config.ini__, con la siguiente estructura: 

```
    [general]
    remote_mode = no 

    [postgresql]
    host = dominioServidorOIP 
    database = nombreDeLaBD 
    user = nombreDelUsuario 
    password = contraseñaDeLaBD 
    port = 5432

    [paths]
    from = /var/lib/odoo/.local/share/Odoo/filestore/baseConLasFotosOdoo
    to = /var/lib/odoo/.local/share/Odoo/filestore/baseDestinoOdoo/fotos
    local = rutaParaAlmacenarLocalmente 

    [ssh]
    hostname = dominioServidorOIP
    username = nombreDelUsuarioSSH
    port = 22
    password = contraseñaDelUsuario 
    look_for_keys = True
```

* Donde:
    * __[general]__: En está sección se define el funcionamiento general de la aplicación 
        * __remote_mode__: Define si los archivos se copiaran en el mismo servidor o si serán descargados.
            * __no__: Descarga los archivos a la ubicación definida en la variable _local_ dentro de la sección __[paths]__
            * __yes__: Copia los archivos dentro del mismo servidor a la ubicación definida en la variable _to_ dentro de la sección __[paths]__

    * __[postgresql]__: Sección donde se definen los datos de conexión a la base de datos de Odoo
        * __host__: Dominio del servidor o ip
        * __database__: Nombre de la base de datos a la cual se conectará
        * __user__: Usuario de la base de datos
        * __password__: Contraseña de la base de datos
        * __port__: Puerto de acceso a la base de datos, por defecto es _5432_

    * __[paths]__: Sección en donde se defines las ubicaciones absolutas de los directorios a trabajar
        * __from__: Ubicación del almacenamiento de archivos dentro del servidor, la ruta por defecto es */var/lib/odoo/.local/share/Odoo/filestore/__nombreDeLaBdDeOdoo__*
        * __to__: Ubicación en la cual se pegaran los archivos dentro del mismo servidor, solo en caso de que la variable _remote\_mode_ dentro de la sección _[general]_ sea _yes_
        * __local__: Ubicación en la que se descargarán los archivos, solo en caso de que la variable _remote\_mode_ dentro de la sección _[general]_ sea _no_

    * __[ssh]__: Configuración para la conexión por SSH
        * __hostname__: Dominio del servidor o ip 
        * __username__: Nombre del usuario que tenga permiso para conectarse por SSH
        * __port__: Puerto de acceso para SSH, por defecto es _22_
        * __password__: Contraseña del usuario SSH
        * __look_for_keys__: Configuración de paramiko, siempre debe ser el valor _True_
