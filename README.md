Este repositorio contiene una aplicación simple de gestión de tareas desarrollada en Python,
implementada utilizando los principios de la Arquitectura Hexagonal. El objetivo principal de 
este proyecto es demostrar cómo aplicar una arquitectura centrada en el dominio, manteniendo 
el código desacoplado de las capas externas (interfaces de usuario, base de datos, etc.).

Características
CRUD básico para la gestión de tareas.
Arquitectura Hexagonal: Separación clara entre el dominio, los puertos y los adaptadores.
Diseño orientado a objetos con una clase Task que representa la lógica de negocio central.
Interfaz de línea de comandos para interactuar con la aplicación.
Adaptadores para persistir datos fácilmente integrables (puedes cambiar entre bases de datos en memoria o persistentes).
