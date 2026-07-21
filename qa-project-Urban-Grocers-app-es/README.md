# Proyecto Sprint 8 
# Automatización de pruebas para la API de Urban Grocers

## Descripción del proyecto

Este proyecto corresponde al Sprint 8 del Bootcamp de QA Engineering de TripleTen.

El objetivo principal fue automatizar las pruebas de la API de **Urban Grocers**, específicamente del endpoint encargado de la creación de kits de productos (`/api/v1/kits`).

Para ello, se desarrolló una serie de pruebas automatizadas utilizando **Python**, **Pytest** y la librería **Requests**, con el fin de validar el comportamiento de la API frente a diferentes valores enviados en el parámetro **name** del cuerpo de la solicitud.

Las pruebas verifican que la API responda correctamente tanto para datos válidos como para datos inválidos, comprobando que los códigos de respuesta y los datos retornados coincidan con los requisitos funcionales establecidos.

---

# Objetivos

- Automatizar las pruebas del endpoint de creación de kits.
- Validar las restricciones del parámetro **name**.
- Verificar que la API responda con los códigos HTTP esperados.
- Confirmar que la información devuelta por la API sea correcta.
- Aplicar buenas prácticas de automatización de pruebas.

---

# Tecnologías utilizadas

- Python 3
- Pytest
- Requests
- Git
- GitHub
- PyCharm

---

# Estructura del proyecto

```
api_stand_tests/

│
├── configuration.py
├── data.py
├── sender_stand_request.py
├── create_kit_name_kit_test.py
├── README.md
└── .gitignore
```

### configuration.py

Contiene las constantes utilizadas por el proyecto, incluyendo:

- URL del servidor.
- Endpoints de la API.

---

### data.py

Almacena la información utilizada durante las solicitudes HTTP.

Incluye:

- Headers.
- Datos para crear usuarios.
- Datos para crear kits.

---

### sender_stand_request.py

Contiene las funciones encargadas de enviar solicitudes HTTP utilizando la librería Requests.

Entre ellas:

- Creación de usuarios.
- Obtención del token de autenticación.
- Creación de kits.

---

### create_kit_name_kit_test.py

Archivo que contiene todos los casos de prueba automatizados utilizando Pytest.

Cada prueba valida un escenario diferente relacionado con el parámetro **name**.

---

# Metodología de pruebas

Antes de crear un kit de productos, la aplicación crea automáticamente un nuevo usuario para obtener un **authToken** válido.

Posteriormente, este token se utiliza para autenticar la solicitud de creación del kit.

Cada caso de prueba envía un valor diferente para el campo **name** y verifica:

- Código de respuesta HTTP.
- Contenido de la respuesta.
- Valor devuelto del campo **name**, cuando corresponde.

---

# Lista de comprobación

| Nº | Caso de prueba | Datos enviados | Resultado esperado |
|----|----------------|----------------|--------------------|
| 1 | Longitud mínima permitida | `"a"` | Código 201 y el campo **name** coincide con el enviado. |
| 2 | Longitud máxima permitida (511 caracteres) | Texto de 511 caracteres | Código 201 y el campo **name** coincide con el enviado. |
| 3 | Longitud menor a la permitida (0 caracteres) | `""` | Código 400. |
| 4 | Longitud superior a la permitida (512 caracteres) | Texto de 512 caracteres | Código 400. |
| 5 | Caracteres especiales | `"№%@",` | Código 201 y el campo **name** coincide con el enviado. |
| 6 | Espacios permitidos | `" A Aaa "` | Código 201 y el campo **name** coincide con el enviado. |
| 7 | Valores numéricos como texto | `"123"` | Código 201 y el campo **name** coincide con el enviado. |
| 8 | Parámetro ausente | `{}` | Código 400. |
| 9 | Tipo de dato incorrecto | `123` | Código 400. |

---

# Validaciones realizadas

Las pruebas verifican que:

- El código HTTP sea el esperado.
- El kit se cree correctamente cuando los datos son válidos.
- El servidor rechace correctamente los datos inválidos.
- El valor del campo **name** devuelto por la API coincida con el enviado en la solicitud.
- La API valide correctamente la longitud del parámetro.
- La API valide el tipo de dato recibido.

---

# Ejecución de las pruebas

Instalar las dependencias necesarias:

```bash
pip install requests
pip install pytest
```

Ejecutar todas las pruebas:

```bash
pytest
```

Ejecutar una única clase de pruebas:

```bash
pytest create_kit_name_kit_test.py
```

Ejecutar las pruebas mostrando información detallada:

```bash
pytest -v
```

---

# Resultados esperados

Al ejecutar las pruebas, Pytest debe mostrar que cada caso de prueba ha sido ejecutado correctamente.

Ejemplo:

```
========= test session starts =========

collected 9 items

create_kit_name_kit_test.py .........

========= 9 passed =========
```

---

# Buenas prácticas implementadas

- Separación de la configuración del proyecto.
- Reutilización de funciones para las solicitudes HTTP.
- Uso de datos centralizados.
- Automatización mediante Pytest.
- Validación de respuestas HTTP.
- Organización modular del proyecto.
- Código reutilizable y fácil de mantener.

---

# Conclusiones

Este proyecto permitió aplicar conceptos fundamentales de automatización de pruebas de API utilizando Python.

Mediante la ejecución de pruebas positivas y negativas se comprobó que el endpoint de creación de kits valida correctamente las restricciones establecidas para el parámetro **name**, garantizando un comportamiento consistente de la API.

Además, el proyecto fortaleció conocimientos sobre autenticación mediante tokens, envío de solicitudes HTTP, validación de respuestas JSON y automatización de pruebas con Pytest.