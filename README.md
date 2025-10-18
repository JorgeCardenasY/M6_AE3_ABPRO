# Proyecto de Recetas con Django

Este proyecto de  aplicación web para gestionar y mostrar recetas de cocina está construido usando Python con el framework Django. A continuaciónAlgunas consideraciones importantes sobre el desarrollo son las siguientes:

## Descripción General del Proyecto

Este proyecto es una aplicación web que permite ver una lista de recetas, y también te da la posibilidad de añadir nuevas recetas a través de un panel de administración. Esta aplicación, si se implementara un desarrollo más completo permitiría aciones tipo CRUD (Create, Read, Update, Delete), aunque en este momento el desarrollo se ha centrado en cumplir el requerimiento de la tarea, y centrado en las partes de "Read" (leer) y "Create" (crear).

Se ha implementado con el framework **Django**, que es el framework de Python de alto nivel que se aborda en el BootCamp. Éste se basa en el patrón de diseño denominado **MVT (Modelo-Vista-Plantilla)**. Es muy parecido al MVC (Modelo-Vista-Controlador), pero con algunas diferencias en los nombres:

*   **Modelo:** Contiene la estructura de los datos. y se relaciona con la estructura de datos de la base de datos.
*   **Vista:** Es la lógica de la aplicación. Aquí es donde escribimos el código en Python que decide qué datos se le muestran al usuario y a través de qué documentos HTML se muestran.
*   **Plantilla (Template):** Es el archivo o documento HTML que ve el usuario. Se encarga de la presentación de los datos.

## La Aplicación: `apprecetas`

Es pertinente mencionar que en Django los proyectos se organizan en "aplicaciones": una aplicación es un módulo de Python que se encarga de una funcionalidad específica. En nuestro caso, tenemos una sola aplicación llamada `apprecetas`.

Separar el proyecto en aplicaciones nos ayuda a mantener el código ordenado y reutilizable. Si, en el futuro, se  quisiera añadir un blog al sitio, éste se podría crear en una nueva aplicación `blog` sin tener que mezclar todo el código.

## Datos: El Modelo `Receta`

El modelo es, sin duda, una de las partes más importantes de cualquier iniciativa de desarrollo de software. El modelo Define cómo se estructuran nuestros datos. En `apprecetas/models.py`, se ha definido nuestro modelo `Receta`.

```python
from django.db import models

class Receta(models.Model):
    nombre = models.CharField(max_length=200)
    ingredientes = models.TextField()
    instrucciones = models.TextField()
    imagen = models.ImageField(upload_to='recetas/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
```

Aquí estamos usando el **ORM (Object-Relational Mapping)** de Django. Esto nos permite definir la estructura de nuestra base de datos usando clases de Python, en lugar de escribir código SQL. Encargándose Django de la "traducción".

*   `class Receta(models.Model):`: A través de esto, Django establece que `Receta` es un modelo, por lo que debe crear una tabla en la base de datos para él.
*   `nombre = models.CharField(...)`: Un campo para texto corto, nombre de la receta.
*   `ingredientes = models.TextField(...)`: Un campo para texto largo, para la lista de ingredientes.
*   `imagen = models.ImageField(...)`: Un campo especial para subir imágenes. Django se encarga de gestionar la subida de archivos.
*   `fecha_creacion = models.DateTimeField(auto_now_add=True)`: Un campo de fecha y hora que se rellena automáticamente cuando se crea una nueva receta.

En un proyecto más complejo se podrían agregar campos como "etiquetas" o "palabras clave", que podrían utilizarse para esatadisticas descriptivas que pudieran ser aporte al desarrollo del negocio. Por ejemplo, si fuera una biblioteca, se podrían hacer análisis por tipos de libros, materiales, tipo de papel, fechas de publicación, entre otras que sean consideradas como criterios de toma de desición del negocio.

## Las Vistas: ¿Qué ve el usuario?

Las vistas son funciones de Python que reciben una petición del usuario (por ejemplo, cuando hace clic en un enlace) y devuelven una respuesta (normalmente, una página HTML).

En `apprecetas/views.py` tenemos varias vistas:

*   `index(request)`: Muestra la página de inicio.
*   `recetas(request)`: Obtiene todas las recetas de la base de datos y se las pasa a la plantilla `recetas.html` para que las muestre.
*   `detalle_receta(request, receta_id)`: Muestra los detalles de una receta específica.
*   `contacto(request)`: Muestra la página de contacto.

Todas estas vistas usan la función `render()`. Esta función de Django toma la petición del usuario, una plantilla HTML y un "contexto" (un diccionario de Python con los datos que queremos mostrar), y genera el HTML final que se envía al navegador.

## Panel de Administración: admin.py

Se ha immplementado un  panel de administración en '/admin/'. A éste panle se agregó la funcionalidad de  agregar recetas e imágenes. 

Como elementos futuros para el desarrollo de este proyecto en específico, se considera la creación de formularios a través de forms.py, el mejorar la estética del proyecto más allá de lo estricamente funcional, como es el caso del presente.

Atte.-<br>
__Jorge Cárdenas Yañez__