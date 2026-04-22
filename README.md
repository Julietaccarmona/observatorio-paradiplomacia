Funcionalidades y Roles del Sistema del Observatorio de Paradiplomacia

Proyecto: Observatorio Web de Paradiplomacia Provincial en Argentina

Aplicación web desarrollada con Django para registrar y analizar convenios internacionales de provincias argentinas.

## Tecnologías

- Python
- Django

## Funcionalidades

- Registro de convenios
- Clasificación por actor
- Consulta de estudios académicos
- API en JSON

Finalidad del Sistema

Esta plataforma permite registrar, organizar y visualizar información sobre la acción internacional de actores subnacionales en Argentina, centralizando datos sobre convenios internacionales y estudios académicos vinculados a la paradiplomacia.

Objetivo Principal

Proporcionar una herramienta digital de consulta y análisis que sistematice información dispersa sobre política internacional subnacional, facilitando su acceso tanto a usuarios generales como a investigadores.

Beneficios Clave

Para usuarios: acceso claro y organizado a información sobre convenios internacionales
Para investigadores: herramienta de sistematización y análisis
Para el administrador: gestión centralizada de datos y actualización del sistema
Definición de Roles y Responsabilidades

1. Usuario/Visitante

Persona que accede al observatorio de forma pública

¿Quién es?
Estudiantes, investigadores o público general
Personas interesadas en relaciones internacionales o política subnacional
Usuarios que desean consultar información sobre convenios y estudios
¿Qué puede hacer?

✅ Ver convenios internacionales registrados
✅ Filtrar información por provincia, país, tipo de acuerdo o actor
✅ Consultar estudios académicos por provincia
✅ Acceder desde cualquier dispositivo
✅ Visualizar información organizada y actualizada

¿Qué NO puede hacer?

❌ No puede modificar información
❌ No puede acceder al panel administrativo
❌ No necesita registrarse
❌ No puede cargar nuevos datos

Flujo de Uso Típico
Accede al sitio web del observatorio
Navega por la sección de convenios
Filtra por provincia (ej: Río Negro)
Consulta información detallada
Accede a estudios relacionados 2. Administrador del Sistema

Encargado de gestionar y mantener el observatorio

¿Quién es?
Desarrollador o responsable del sistema
Usuario con acceso completo al backend
¿Qué puede hacer?

✅ Gestionar Convenios

Crear nuevos registros
Editar información existente
Eliminar convenios

✅ Gestionar Actores

Clasificar convenios según tipo de actor
Crear nuevas categorías (provincial, municipal, universidades, etc.)

✅ Gestionar Provincias

Registrar provincias
Asociarlas a convenios y estudios

✅ Gestionar Estudios

Cargar artículos, papers o informes
Asociarlos a provincias
Incluir enlaces externos

✅ Acceder al Panel Administrativo

Uso del panel de administración de Django
Gestión completa de la base de datos
¿Qué NO debería hacer?

❌ No cargar información sin verificación
❌ No modificar datos sin criterio académico

Flujo de Trabajo Típico
Accede al panel admin
Carga nuevos convenios o estudios
Actualiza información existente
Mantiene la base de datos organizada
Matriz de Permisos
Acción Usuario Admin
Ver convenios ✅ ✅
Filtrar información ✅ ✅
Ver estudios ✅ ✅
Crear/editar convenios ❌ ✅
Crear/editar estudios ❌ ✅
Acceder panel admin ❌ ✅
Gestionar base de datos ❌ ✅
Flujo Completo del Sistema
Carga de Información
El administrador accede al panel
Registra convenios y estudios
Los datos se almacenan en la base de datos
Uso del Sistema
El usuario accede al sitio web
Consulta información disponible
Aplica filtros según sus intereses
Visualiza resultados en pantalla
Arquitectura y Funcionamiento

La aplicación funcionará bajo el siguiente esquema:

👉 Usuario → interfaz web → servidor en Django → base de datos

Funcionamiento interno
El usuario accede a una URL
El sistema procesa la solicitud
Se ejecuta una vista (lógica del sistema)
Se consulta la base de datos mediante el ORM
Se devuelve la información en formato:
HTML (para visualización)
JSON (para interoperabilidad)
Interoperabilidad

El sistema incluirá una API básica que permitirá acceder a los datos en formato JSON.

Ejemplo de endpoint:
/api/convenios/
/api/estudios/

Esto permitirá que:

otros sistemas reutilicen los datos
se integren aplicaciones externas
se facilite el análisis automatizado
Paradigma de Diseño
Enfoque del sistema

El sistema implementa un enfoque basado en:

centralización de datos dispersos
estructura clara y relacional
acceso público a la información
Diseño de interfaz
Interfaz simple y funcional
Navegación por secciones (convenios, estudios)
Filtros por provincia, actor y tipo de acuerdo
Visualización clara orientada a consulta
Resumen de Responsabilidades
Usuario → Consulta información

Accede a datos sin modificar el sistema

Administrador → Gestiona el sistema

Carga, edita y mantiene la información

Conclusión

El sistema propone una solución tecnológica que permite organizar y analizar la acción internacional subnacional, combinando herramientas de desarrollo web con una aplicación concreta en el campo de las Relaciones Internacionales.
