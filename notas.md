# VIDEO 1
# Explicación Paso a Paso del Comando `sudo npm create vue@latest`

## 1. Comando inicial: `sudo npm create vue@latest`
- **Descripción:** Estás utilizando el comando `create-vue`, que es un comando oficial de Vue.js para inicializar un nuevo proyecto basado en Vue.js. Al especificar `@latest`, aseguras que se utilice la versión más reciente del generador de proyectos Vue.
- **Implicancia:** Estás creando un nuevo proyecto Vue.js con la configuración más actualizada. El uso de `sudo` puede indicar que necesitas permisos elevados para instalar los paquetes globalmente en tu sistema, lo que no siempre es necesario y depende de cómo esté configurado tu sistema.

## 2. Instalación de `create-vue`
- **Descripción:** Si no tienes instalado `create-vue` previamente, npm te preguntará si deseas instalar el paquete necesario. En este caso, `create-vue@3.10.4`.
- **Implicancia:** Instalar `create-vue` permite que se generen los archivos y la estructura inicial de un proyecto Vue.js. Al proceder con "y", confirmas que deseas instalar este paquete y continuar con la creación del proyecto.

## 3. Nombre del Proyecto: `frontend`
- **Descripción:** Se te pide un nombre para tu proyecto. Aquí lo llamaste `frontend`.
- **Implicancia:** El nombre del proyecto determinará la carpeta en la que se creará la estructura del proyecto Vue.js. Este nombre es importante porque a menudo se utiliza como referencia en la configuración del proyecto y en scripts futuros.

## 4. Selección de TypeScript: `No`
- **Descripción:** Se te pregunta si deseas usar TypeScript, un superset de JavaScript que agrega tipado estático.
- **Implicancia:** Al seleccionar "No", decides usar JavaScript en lugar de TypeScript. Esto significa que no tendrás los beneficios del tipado estático, pero la configuración del proyecto será más simple y directa.

## 5. Soporte para JSX: `No`
- **Descripción:** JSX es una sintaxis de JavaScript que permite escribir HTML dentro de JavaScript. Es más común en React, pero también es compatible con Vue.
- **Implicancia:** Al seleccionar "No", indicas que no necesitas el soporte para JSX, lo que simplifica la configuración y evita dependencias adicionales.

## 6. Añadir Vue Router: `Yes`
- **Descripción:** Vue Router es la biblioteca oficial de Vue.js para manejar el enrutamiento en aplicaciones de una sola página (SPA).
- **Implicancia:** Al seleccionar "Yes", estás configurando tu proyecto para soportar múltiples vistas y navegación entre ellas, lo cual es esencial para aplicaciones complejas.

## 7. Añadir Pinia: `Yes`
- **Descripción:** Pinia es la librería oficial para la gestión del estado en Vue.js, similar a lo que era Vuex en versiones anteriores.
- **Implicancia:** Al añadir Pinia, decides utilizar una solución robusta y moderna para manejar el estado global de tu aplicación, lo que es útil para aplicaciones con múltiples componentes que necesitan compartir datos.

## 8. Añadir Vitest para pruebas unitarias: `Yes`
- **Descripción:** Vitest es una herramienta de pruebas unitarias rápida y ligera que se integra bien con Vue.
- **Implicancia:** Al seleccionar "Yes", estás preparando tu proyecto para incluir pruebas unitarias desde el principio, lo cual es una buena práctica de desarrollo para asegurar la calidad del código.

## 9. Solución de pruebas end-to-end: `No`
- **Descripción:** Las pruebas end-to-end (E2E) verifican el comportamiento de la aplicación en su totalidad, simulando la interacción del usuario.
- **Implicancia:** Al seleccionar "No", decides no configurar esta herramienta ahora, lo que simplifica la configuración inicial, pero podrías añadirla más adelante si lo necesitas.

## 10. Añadir ESLint: `Yes`
- **Descripción:** ESLint es una herramienta para identificar y reportar patrones en el código JavaScript, promoviendo un código más limpio y uniforme.
- **Implicancia:** Al seleccionar "Yes", añades una capa de verificación de la calidad del código, lo que es crucial en equipos grandes o proyectos complejos.

## 11. Añadir Prettier: `Yes`
- **Descripción:** Prettier es un formateador de código que asegura que el código siga un estilo consistente.
- **Implicancia:** Al seleccionar "Yes", decides mantener un formato consistente en tu código, lo que facilita la colaboración y la revisión de código.

## 12. Añadir Vue DevTools 7 (experimental): `Yes`
- **Descripción:** Vue DevTools es una extensión de navegador para depurar aplicaciones Vue.js. La versión 7 es una versión experimental que ofrece nuevas funcionalidades.
- **Implicancia:** Al seleccionar "Yes", optas por utilizar herramientas avanzadas para depuración, lo que puede mejorar la productividad en el desarrollo, aunque puede ser inestable por ser experimental.

## 13. Creación del proyecto y comandos finales
- **Descripción:** Una vez que todas las opciones son seleccionadas, el scaffolding del proyecto ocurre en la carpeta designada (`frontend`). Se te instruye a correr tres comandos: 
  - `cd frontend`: Navega a la carpeta del proyecto.
  - `npm install`: Instala todas las dependencias seleccionadas y necesarias para el proyecto.
  - `npm run format`: Formatea el código utilizando Prettier.
  - `npm run dev`: Inicia el servidor de desarrollo para ver tu aplicación en el navegador.
- **Implicancia:** Estos comandos finalizan la configuración inicial y te preparan para comenzar a trabajar en tu proyecto. `npm run dev` inicia la aplicación en modo desarrollo, permitiéndote hacer cambios en tiempo real.

# Resumen
Este proceso de creación de un proyecto Vue.js es altamente configurable y las decisiones que tomas afectan directamente cómo se desarrollará tu proyecto. Al seleccionar ciertas herramientas y características, como Vue Router, Pinia, Vitest, ESLint, y Prettier, estás preparando un entorno de desarrollo robusto, orientado a la calidad y la eficiencia en el desarrollo de aplicaciones web modernas con Vue.js.

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

## Comando: `sudo npm install vite --save-dev`

### Descripción
El comando `sudo npm install vite --save-dev` se utiliza para instalar `Vite`, que es una herramienta de desarrollo extremadamente rápida y ligera, especialmente diseñada para mejorar la experiencia de desarrollo de aplicaciones web modernas. `Vite` es conocido por su capacidad para ofrecer un servidor de desarrollo con recarga instantánea de módulos (HMR - Hot Module Replacement) y una construcción eficiente para la producción.

### Componentes del Comando
- **`sudo`:** Este prefijo se usa para ejecutar el comando con privilegios de superusuario o administrador. En muchos sistemas, especialmente en Unix y Linux, esto es necesario cuando necesitas permisos elevados para realizar ciertas tareas, como instalar paquetes globalmente o modificar archivos del sistema.
- **`npm`:** Es el gestor de paquetes para Node.js. Se utiliza para instalar, compartir, y administrar dependencias (bibliotecas y herramientas) en proyectos de JavaScript.
- **`install`:** Esta es la acción principal del comando, indicando que deseas instalar un paquete (o paquetes) especificado.
- **`vite`:** Este es el nombre del paquete que se desea instalar. En este caso, `Vite` es la herramienta de desarrollo que se está añadiendo al proyecto.
- **`--save-dev`:** Este indicador especifica que el paquete `Vite` debe ser guardado como una dependencia de desarrollo en el archivo `package.json`. Las dependencias de desarrollo son aquellas que solo se necesitan durante la fase de desarrollo y no son requeridas cuando la aplicación se ejecuta en producción.

### ¿Qué es `Vite`?
`Vite` es una herramienta de construcción de aplicaciones web que se enfoca en la rapidez y eficiencia. Entre sus características clave se encuentran:
- **Servidor de desarrollo ultrarrápido:** Gracias a su enfoque basado en ES Modules y un servidor nativo, `Vite` puede iniciar rápidamente, incluso en proyectos grandes.
- **Hot Module Replacement (HMR):** Proporciona una experiencia de desarrollo en la que los módulos se actualizan en tiempo real sin necesidad de recargar toda la página.
- **Optimización para producción:** Cuando preparas tu aplicación para producción, `Vite` se encarga de agrupar, minimizar, y optimizar el código para un rendimiento óptimo.

### Implicancias de su Instalación
- **Disponibilidad en el Proyecto:** Una vez instalado, `Vite` estará disponible como una herramienta de desarrollo en tu proyecto. Esto significa que puedes utilizarlo para iniciar un servidor de desarrollo rápido y realizar compilaciones eficientes de tu aplicación para producción.
- **Registro en `package.json`:** Al utilizar el flag `--save-dev`, `Vite` se registrará en la sección de `devDependencies` de tu archivo `package.json`. Esto asegura que otras personas que trabajen en el mismo proyecto (o tú mismo en otro momento) puedan instalar todas las herramientas de desarrollo necesarias simplemente ejecutando `npm install`.
- **Privilegios Elevados con `sudo`:** El uso de `sudo` implica que necesitas permisos administrativos para completar la instalación. Esto puede ser necesario en sistemas donde las carpetas de instalación de `npm` requieren privilegios de superusuario. Sin embargo, esto también puede significar que estás instalando `Vite` globalmente en tu sistema (aunque `--save-dev` normalmente lo instala en el proyecto local), por lo que es importante tener cuidado para no modificar el sistema de forma no intencionada.

### ¿Por qué `Vite` es importante?
- **Optimización del Flujo de Trabajo:** `Vite` es especialmente útil en proyectos donde la velocidad y la eficiencia del desarrollo son cruciales. Con su capacidad para manejar grandes bases de código y realizar HMR instantáneo, mejora significativamente la productividad de los desarrolladores.
- **Compatibilidad con Herramientas Modernas:** `Vite` se integra bien con herramientas modernas y frameworks como Vue.js, React, y otros, lo que lo convierte en una opción versátil para una amplia gama de proyectos de desarrollo web.

### Resumen
El comando `sudo npm install vite --save-dev` es una potente instrucción para agregar `Vite` a tu proyecto como una dependencia de desarrollo, asegurando que esté disponible para optimizar el entorno de desarrollo. El uso de `sudo` permite la instalación con permisos elevados, lo que puede ser necesario dependiendo de la configuración de tu sistema. Al finalizar, `Vite` te ayudará a desarrollar y construir aplicaciones web de manera más eficiente y rápida.


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

## Comando: `sudo npm i vuetify`

### Descripción
El comando `sudo npm i vuetify` se utiliza para instalar `Vuetify`, que es una popular biblioteca de componentes UI para Vue.js basada en Material Design. Este comando agrega Vuetify a tu proyecto Vue.js, permitiéndote usar una amplia gama de componentes visuales predefinidos y estilos consistentes, basados en las directrices de diseño de Material Design de Google.

### Componentes del Comando
- **`sudo`:** Este prefijo se usa para ejecutar el comando con privilegios de superusuario o administrador. Es posible que necesites estos permisos elevados para instalar paquetes en ciertos sistemas, dependiendo de la configuración de tu entorno de desarrollo.
- **`npm`:** Es el gestor de paquetes para Node.js, utilizado para instalar, actualizar y gestionar dependencias de proyectos JavaScript.
- **`i`:** Es una abreviatura de `install`, lo que significa que estás instalando un paquete. Es una forma común y abreviada de escribir `npm install`.
- **`vuetify`:** Es el nombre del paquete que se está instalando. `Vuetify` proporciona una colección de componentes de interfaz de usuario (UI) que siguen los principios de diseño de Material Design, lo que permite construir interfaces de usuario consistentes y atractivas de manera rápida y eficiente.

### ¿Qué es `Vuetify`?
`Vuetify` es una biblioteca de componentes de interfaz de usuario (UI) para Vue.js que implementa las pautas de Material Design. Ofrece una amplia gama de componentes que están listos para usar y personalizar, lo que facilita la creación de interfaces de usuario profesionales y consistentes.

### Ventajas de Usar `Vuetify`
- **Componentes Preconstruidos:** `Vuetify` ofrece una gran variedad de componentes, como botones, formularios, tablas, diálogos, entre otros, que están listos para ser utilizados en tus proyectos.
- **Consistencia en el Diseño:** Al adherirse a las pautas de Material Design, `Vuetify` garantiza que los componentes sigan un estilo visual coherente y atractivo.
- **Flexibilidad y Personalización:** Aunque los componentes de Vuetify siguen un estándar, puedes personalizarlos fácilmente para que se adapten a las necesidades específicas de tu proyecto.
- **Documentación Completa:** `Vuetify` cuenta con una documentación exhaustiva que facilita la integración y el uso de sus componentes.

### Implicancias de la Instalación
- **Disponibilidad en el Proyecto:** Una vez instalado, `Vuetify` estará disponible en tu proyecto, permitiéndote importar y utilizar sus componentes en las vistas de tu aplicación Vue.js.
- **Registro en `package.json`:** `Vuetify` se añadirá a la sección de dependencias en el archivo `package.json`, lo que asegura que la instalación se pueda replicar en otros entornos de desarrollo o por otros desarrolladores que trabajen en el mismo proyecto.
- **Privilegios Elevados con `sudo`:** El uso de `sudo` implica que necesitas permisos administrativos para completar la instalación, lo que podría ser necesario dependiendo de cómo esté configurado tu entorno de desarrollo.

### Resultado de la Instalación
- **Paquetes Añadidos y Auditados:** 
  - **`added 1 package`:** Se ha agregado un paquete nuevo a tu proyecto, que es `Vuetify`.
  - **`audited 348 packages`:** `npm` ha revisado un total de 348 paquetes en tu proyecto, lo que incluye las dependencias de `Vuetify` y las existentes en tu proyecto.
  
- **Paquetes Buscando Financiamiento:**
  - **`82 packages are looking for funding`:** De los paquetes auditados, 82 están buscando financiamiento. Puedes obtener más detalles sobre cómo contribuir financieramente a estos paquetes ejecutando `npm fund`.
  - **Implicancia:** Aunque esto no afecta directamente al funcionamiento del proyecto, indica que algunos de los paquetes que utilizas son mantenidos por desarrolladores que buscan apoyo financiero para continuar con su desarrollo.

- **Vulnerabilidades Encontradas:**
  - **`found 0 vulnerabilities`:** No se encontraron vulnerabilidades en los paquetes instalados o auditados.
  - **Implicancia:** La instalación es segura y no introduce riesgos de seguridad conocidos en tu proyecto, lo cual es importante para mantener la integridad y seguridad de tu aplicación.

### Resumen
El comando `sudo npm i vuetify` es utilizado para instalar `Vuetify`, una poderosa y flexible biblioteca de componentes de UI para Vue.js, basada en Material Design. La instalación fue exitosa, añadiendo Vuetify a tu proyecto sin vulnerabilidades de seguridad. El uso de `sudo` asegura que la instalación se realice con los permisos adecuados, y aunque algunos paquetes relacionados buscan financiamiento, esto no afecta directamente el uso de Vuetify en tu proyecto.

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

### main.ts (antes)
```typescript
import './assets/main.css'

// Vuetify
import 'vuetify/styles'
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
```

### maint.ts (después)
```typescript
import './assets/main.css'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)

const vuetify = createVuetify({
    components,
    directives,
})

app.use(vuetify)

app.mount('#app')

```


## Descripción de los Cambios Realizados

### 1. Importación de Vuetify y sus Componentes/Directivas:

- **Antes:** Sólo importabas los estilos de Vuetify (`vuetify/styles`), pero no estabas utilizando realmente los componentes o directivas de Vuetify.
- **Ahora:** Has añadido importaciones para `createVuetify`, así como para todos los componentes (`vuetify/components`) y directivas (`vuetify/directives`) de Vuetify.
- **Implicancia:** Estas nuevas importaciones permiten que tu aplicación use los componentes y directivas de Vuetify. Esto es crucial para aprovechar las características visuales y de interacción que ofrece esta biblioteca. Por ejemplo, componentes como botones, formularios, tarjetas, etc., y directivas como `v-show`, `v-model`, etc., ahora estarán disponibles.

### 2. Creación de la Instancia de Vuetify:

- **Antes:** No había una instancia de Vuetify creada ni utilizada en la aplicación.
- **Ahora:** Has creado una instancia de Vuetify mediante `createVuetify({ components, directives })`.
- **Implicancia:** Al crear esta instancia y pasarle los componentes y directivas, estás configurando Vuetify para que sea utilizado globalmente en tu aplicación. Esto significa que todos los componentes y directivas de Vuetify estarán disponibles para su uso en cualquier parte de tu aplicación.

### 3. Integración de Vuetify en la Aplicación Vue:

- **Antes:** Vuetify no estaba integrado con tu aplicación Vue.
- **Ahora:** Has añadido `app.use(vuetify)` para integrar Vuetify en tu aplicación Vue.
- **Implicancia:** Este paso asegura que Vuetify se registre correctamente como un plugin en tu aplicación Vue, permitiendo que los estilos y componentes de Vuetify estén disponibles en toda la aplicación. Sin este paso, aunque importaras Vuetify, no podrías utilizar sus características en tu aplicación.

## Resumen

En resumen, los cambios realizados añaden Vuetify como una biblioteca de UI completamente funcional dentro de tu proyecto Vue.js. Ahora, no solo estás importando los estilos de Vuetify, sino que también has configurado y registrado todos los componentes y directivas de Vuetify, lo que te permite utilizarlos en cualquier parte de tu aplicación. Esto mejora significativamente las capacidades de tu aplicación al integrar una rica biblioteca de componentes basados en Material Design.


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

## Comando: `sudo touch vue.d.ts`

### Descripción
El comando `sudo touch vue.d.ts` se utiliza para crear un archivo vacío llamado `vue.d.ts` en el directorio actual (`~/Proyectos/Django_Vue/Vue-Django-Auth/Version_01/frontend/src`). El uso de `sudo` indica que se requieren permisos de superusuario para realizar esta acción, lo cual podría ser necesario si el directorio o el sistema de archivos tiene restricciones de permisos.

### Implicancia
- **Creación del Archivo:** El archivo `vue.d.ts` es un archivo de declaración de TypeScript. Este tipo de archivo se utiliza para definir tipos que TypeScript pueda reconocer durante la compilación. En este caso, se está preparando para definir cómo se deben tratar los archivos `.vue` dentro de un proyecto que utiliza TypeScript.
- **Uso de `sudo`:** Indica que el directorio o sistema de archivos puede tener permisos restringidos, lo que requiere privilegios elevados para modificar o crear archivos en esa ubicación.

### Contenido del Archivo `vue.d.ts`
Una vez creado el archivo, se agrega el siguiente contenido:

```typescript
declare module '*.vue' {
    import { DefineComponent } from 'vue';
    const component: DefineComponent<{}, {}, any>;
    export default component;
}

```

## Descripción del Contenido

### 1. `declare module '*.vue'`
- **Descripción:** Esta declaración le dice a TypeScript cómo manejar la importación de archivos `.vue`. Sin esta declaración, TypeScript no sabría cómo interpretar los archivos `.vue`, lo que podría resultar en errores durante la compilación.

### 2. `import { DefineComponent } from 'vue'`
- **Descripción:** Se importa el tipo `DefineComponent` desde Vue. Este tipo describe los componentes de Vue, proporcionando a TypeScript la información necesaria sobre cómo debe tratar los componentes dentro de los archivos `.vue`.

### 3. `const component: DefineComponent<{}, {}, any>;`
- **Descripción:** Esta línea define que cualquier archivo `.vue` importado será tratado como un componente Vue con una estructura genérica (sin props, sin métodos, y sin datos específicos). El tipo `any` permite cualquier tipo de dato, proporcionando flexibilidad.

### 4. `export default component;`
- **Descripción:** Finalmente, esta línea exporta el componente como el valor por defecto, lo que es consistente con cómo normalmente se exportan los componentes en los archivos `.vue`.

## Implicancia del Contenido

### 1. Compatibilidad con TypeScript
- **Descripción:** Este archivo es crucial para proyectos Vue que usan TypeScript, ya que permite que TypeScript entienda y trabaje correctamente con los archivos `.vue`. Sin esta declaración, el compilador de TypeScript no podría manejar las importaciones de archivos `.vue`, lo que generaría errores.

### 2. Flexibilidad en los Componentes
- **Descripción:** Al utilizar `DefineComponent<{}, {}, any>`, se mantiene la flexibilidad para definir componentes con cualquier estructura, lo que es útil en proyectos donde los componentes pueden variar ampliamente en su definición.

## Resumen

El comando `sudo touch vue.d.ts` crea un archivo de declaración de TypeScript necesario para que TypeScript pueda manejar correctamente los archivos `.vue` en un proyecto que utiliza Vue.js y TypeScript. El contenido agregado a este archivo proporciona a TypeScript la información necesaria para interpretar y trabajar con componentes de Vue, asegurando la compatibilidad y evitando errores de compilación.

## Comando: `sudo npm install @mdi/font`

### Descripción
El comando `sudo npm install @mdi/font` se utiliza para instalar el paquete `@mdi/font`, que incluye la fuente de iconos Material Design Icons (MDI). Estos iconos son ampliamente utilizados en aplicaciones web y móviles para representar acciones, objetos, y conceptos de manera visualmente intuitiva. El uso de `sudo` indica que se requieren permisos de superusuario para ejecutar el comando, lo que puede ser necesario dependiendo de los permisos de tu entorno de desarrollo.

### Resultado de la Instalación
- **Paquetes Añadidos y Auditados:**
  - **`added 1 package`:** Se ha añadido un paquete nuevo, que es `@mdi/font`.
  - **`audited 349 packages`:** Se auditaron 349 paquetes en total, incluyendo el nuevo paquete instalado y las dependencias ya presentes en el proyecto.

- **Paquetes Buscando Financiamiento:**
  - **`82 packages are looking for funding`:** De los paquetes auditados, 82 están buscando financiamiento. Puedes ejecutar `npm fund` para obtener más detalles sobre cómo contribuir financieramente a estos paquetes.

- **Vulnerabilidades Encontradas:**
  - **`found 0 vulnerabilities`:** No se encontraron vulnerabilidades en los paquetes instalados o auditados, lo que significa que la instalación es segura y no introduce riesgos de seguridad en tu proyecto.

### Modificación del Archivo `main.ts`

Después de instalar `@mdi/font`, se ha modificado el archivo `main.ts` de la siguiente manera:

#### Código Original:
```typescript
import './assets/main.css'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)

const vuetify = createVuetify({
    components,
    directives,
})

app.use(vuetify)

app.mount('#app')
```


## Comando: `sudo npm install @vuelidate/core @vuelidate/validators`

### Descripción
El comando `sudo npm install @vuelidate/core @vuelidate/validators` se utiliza para instalar `Vuelidate`, una librería de validación ligera y flexible para Vue.js. Este comando instala tanto el núcleo de Vuelidate (`@vuelidate/core`) como su conjunto de validadores (`@vuelidate/validators`). El uso de `sudo` indica que se requieren permisos de superusuario para realizar la instalación, lo que puede ser necesario dependiendo de los permisos de tu entorno de desarrollo.

### Componentes Instalados
- **`@vuelidate/core`:** Es el núcleo de Vuelidate. Proporciona la infraestructura necesaria para la validación reactiva en aplicaciones Vue.js.
- **`@vuelidate/validators`:** Contiene un conjunto de validadores predefinidos que se pueden usar para realizar comprobaciones comunes, como la validación de campos obligatorios, longitud mínima/máxima, y formatos específicos como correos electrónicos.

### Resultado de la Instalación
- **Paquetes Añadidos y Auditados:**
  - **`added 4 packages`:** Se han añadido cuatro paquetes nuevos a tu proyecto, que incluyen `@vuelidate/core`, `@vuelidate/validators` y sus dependencias.
  - **`audited 353 packages`:** Se han auditado un total de 353 paquetes, incluyendo los ya existentes en tu proyecto.

- **Paquetes Buscando Financiamiento:**
  - **`83 packages are looking for funding`:** De los paquetes auditados, 83 están buscando financiamiento. Puedes ejecutar `npm fund` para obtener más detalles sobre cómo contribuir financieramente a estos paquetes.

- **Vulnerabilidades Encontradas:**
  - **`found 0 vulnerabilities`:** No se encontraron vulnerabilidades en los paquetes instalados o auditados, lo que indica que la instalación es segura y no introduce riesgos de seguridad en tu proyecto.

### Implicancias de la Instalación
- **Validación Reactiva:** Con Vuelidate instalado, puedes añadir validaciones reactivas a tus formularios en Vue.js de manera sencilla y eficiente. Esto te permite verificar la entrada del usuario en tiempo real y proporcionar retroalimentación inmediata.
- **Uso de Validadores Predefinidos:** `@vuelidate/validators` te ofrece una variedad de validadores comunes que puedes aplicar directamente a tus formularios, lo que acelera el proceso de desarrollo y asegura que los datos del usuario sean válidos antes de enviarlos al servidor.

### Resumen

El comando `sudo npm install @vuelidate/core @vuelidate/validators` instala la librería Vuelidate y sus validadores en tu proyecto Vue.js, permitiéndote implementar validaciones reactivas en tus formularios de manera sencilla y efectiva. La instalación fue exitosa, sin vulnerabilidades de seguridad, y 83 paquetes auditados están buscando financiamiento. Vuelidate es una herramienta poderosa para asegurar que los datos de los formularios sean válidos antes de ser procesados.

**visitar** https://vuetifyjs.com/en/components/forms/#vee-validate
**Pegar código en HomeView.vue**

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

## Comando: `sudo npm install vue-i18n@9`

### Descripción
El comando `sudo npm install vue-i18n@9` se utiliza para instalar `vue-i18n` en su versión 9, una popular librería para la internacionalización (i18n) en aplicaciones Vue.js. Esta librería permite gestionar múltiples idiomas en tu aplicación, proporcionando una forma sencilla de traducir textos y manejar localizaciones. El uso de `sudo` indica que se requieren permisos de superusuario para realizar la instalación, lo que puede ser necesario dependiendo de los permisos de tu entorno de desarrollo.

### Proceso de Instalación
- **`sudo` y Contraseña:** El uso de `sudo` requiere la introducción de la contraseña del usuario. Si la contraseña se ingresa incorrectamente, se te pedirá que lo intentes de nuevo. Esto es parte de la seguridad del sistema para asegurarse de que los comandos que requieren privilegios elevados sean autorizados por el usuario.
  
### Resultado de la Instalación
- **Paquetes Añadidos y Auditados:**
  - **`added 4 packages`:** Se han añadido cuatro paquetes nuevos a tu proyecto, que incluyen `vue-i18n` y sus dependencias.
  - **`audited 357 packages`:** Se han auditado un total de 357 paquetes en tu proyecto, lo que incluye tanto los nuevos como los ya existentes.

- **Paquetes Buscando Financiamiento:**
  - **`87 packages are looking for funding`:** De los paquetes auditados, 87 están buscando financiamiento. Puedes ejecutar `npm fund` para obtener más detalles sobre cómo contribuir financieramente a estos paquetes.

- **Vulnerabilidades Encontradas:**
  - **`found 0 vulnerabilities`:** No se encontraron vulnerabilidades en los paquetes instalados o auditados, lo que indica que la instalación es segura y no introduce riesgos de seguridad en tu proyecto.

### Implicancias de la Instalación
- **Internacionalización (i18n):** Con `vue-i18n` instalado, puedes gestionar múltiples idiomas y localizaciones en tu aplicación Vue.js de manera eficiente. Esto incluye la capacidad de traducir textos, formatear fechas, números y manejar pluralización en diferentes idiomas.
- **Versión Específica (`@9`):** La instalación específica de la versión 9 de `vue-i18n` asegura que estés utilizando una versión concreta de la librería, lo que puede ser importante para compatibilidad con otras partes de tu proyecto o dependencias.

### Resumen

El comando `sudo npm install vue-i18n@9` instala la versión 9 de `vue-i18n`, una librería esencial para manejar la internacionalización en aplicaciones Vue.js. La instalación fue exitosa, sin vulnerabilidades de seguridad, y 87 paquetes auditados están buscando financiamiento. `Vue-i18n` te permitirá gestionar múltiples idiomas en tu aplicación, facilitando la creación de aplicaciones multilingües con una experiencia de usuario mejorada en diferentes regiones.


**Crear carpeta src/lang**
--> cd/lang
--> sudo touch es-US.json

```json
{

}
```

#### Código Original:
```vue
<template>
  <form>
    <v-text-field
      v-model="state.name"
      :counter="10"
      :error-messages="v$.name.$errors.map(e => e.$message)"
      label="Name"
      required
      @blur="v$.name.$touch"
      @input="v$.name.$touch"
    ></v-text-field>

    <v-text-field
      v-model="state.email"
      :error-messages="v$.email.$errors.map(e => e.$message)"
      label="E-mail"
      required
      @blur="v$.email.$touch"
      @input="v$.email.$touch"
    ></v-text-field>

    <v-select
      v-model="state.select"
      :error-messages="v$.select.$errors.map(e => e.$message)"
      :items="items"
      label="Item"
      required
      @blur="v$.select.$touch"
      @change="v$.select.$touch"
    ></v-select>

    <v-checkbox
      v-model="state.checkbox"
      :error-messages="v$.checkbox.$errors.map(e => e.$message)"
      label="Do you agree?"
      required
      @blur="v$.checkbox.$touch"
      @change="v$.checkbox.$touch"
    ></v-checkbox>

    <v-btn
      class="me-4"
      @click="v$.$validate"
    >
      submit
    </v-btn>
    <v-btn @click="clear">
      clear
    </v-btn>
  </form>
</template>
<script setup>
  import { reactive } from 'vue'
  import { useVuelidate } from '@vuelidate/core'
  import { email, required } from '@vuelidate/validators'

  const initialState = {
    name: '',
    email: '',
    select: null,
    checkbox: null,
  }

  const state = reactive({
    ...initialState,
  })

  const items = [
    'Item 1',
    'Item 2',
    'Item 3',
    'Item 4',
  ]

  const rules = {
    name: { required },
    email: { required, email },
    select: { required },
    items: { required },
    checkbox: { required },
  }

  const v$ = useVuelidate(rules, state)

  function clear () {
    v$.value.$reset()

    for (const [key, value] of Object.entries(initialState)) {
      state[key] = value
    }
  }
</script>
```
# Código modificado

```vue
<template>
  <form>
    <v-text-field
      v-model="state.name"
      :counter="10"
      :error-messages="v$.name.$errors.map(e => e.$message)"
      label="Name"
      required
      @blur="v$.name.$touch"
      @input="v$.name.$touch"
    ></v-text-field>

    <v-text-field
      v-model="state.email"
      :error-messages="v$.email.$errors.map(e => e.$message)"
      label="E-mail"
      required
      @blur="v$.email.$touch"
      @input="v$.email.$touch"
    ></v-text-field>

    <v-select
      v-model="state.select"
      :error-messages="v$.select.$errors.map(e => e.$message)"
      :items="items"
      label="Item"
      required
      @blur="v$.select.$touch"
      @change="v$.select.$touch"
    ></v-select>

    <v-checkbox
      v-model="state.checkbox"
      :error-messages="v$.checkbox.$errors.map(e => e.$message)"
      label="Do you agree?"
      required
      @blur="v$.checkbox.$touch"
      @change="v$.checkbox.$touch"
    ></v-checkbox>

    <v-btn
      class="me-4"
      @click="v$.$validate"
    >
      {{ $t('submit') }}
    </v-btn>
    <v-btn @click="clear">
      clear
    </v-btn>
  </form>
</template>
<script setup>
  import { reactive } from 'vue'
  import { useVuelidate } from '@vuelidate/core'
  import { email, required } from '@vuelidate/validators'

  const initialState = {
    name: '',
    email: '',
    select: null,
    checkbox: null,
  }

  const state = reactive({
    ...initialState,
  })

  const items = [
    'Item 1',
    'Item 2',
    'Item 3',
    'Item 4',
  ]

  const rules = {
    name: { required },
    email: { required, email },
    select: { required },
    items: { required },
    checkbox: { required },
  }

  const v$ = useVuelidate(rules, state)

  function clear () {
    v$.value.$reset()

    for (const [key, value] of Object.entries(initialState)) {
      state[key] = value
    }
  }
</script>
```


```typescript
import './assets/main.css'
import '@mdi/font/css/materialdesignicons.css';
// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import en from './lang/en-US.json';

import { createI18n } from 'vue-i18n'

const i18n = createI18n({
    legacy: false,
    locale: "en",
    messages: {
        en
    }
})

const app = createApp(App)

app.use(createPinia())
app.use(router)

const vuetify = createVuetify({
    components,
    directives,
})

app.use(vuetify);

app.use(i18n); // Corrección aquí

app.mount('#app')
```
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

## Explicación del Código Relacionado con `i18n`

### 1. Importación de `vue-i18n`
```javascript
import { createI18n } from 'vue-i18n'
```

**Descripción:** Se importa la función createI18n desde la librería vue-i18n. Esta función es utilizada para configurar e inicializar la funcionalidad de internacionalización (i18n) en una aplicación Vue.js. vue-i18n facilita la gestión de múltiples idiomas en una aplicación, permitiendo traducir textos y manejar otros aspectos de localización, como el formato de fechas y números.

### 2. Importación de Archivos de Traducción

```typescript
import en from './lang/en-US.json';
```
**Descripción:** Se importa el archivo en-US.json, que contiene las traducciones en inglés para la aplicación. Este archivo generalmente está estructurado como un objeto JSON donde las claves representan las cadenas de texto en la aplicación y los valores son las traducciones correspondientes.

Ejemplo de un archivo JSON típico:

```json
{
  "welcome": "Welcome",
  "submit": "Submit"
}
```
3. Creación de la Instancia de i18n

```javascript
const i18n = createI18n({
    legacy: false,
    locale: "en",
    messages: {
        en
    }
})
```

**Descripción:** Se crea una instancia de i18n usando la función createI18n. Esta instancia es la que se va a utilizar para gestionar la internacionalización en toda la aplicación.

**Parámetros de Configuración:**

**legacy:** false: Indica que estás usando la nueva API de composición de vue-i18n en lugar de la API heredada.
**locale:** "en": Especifica el idioma por defecto de la aplicación, en este caso, inglés (en). Esto significa que la aplicación mostrará los textos en inglés por defecto.
**messages: { en }:** Define los mensajes de traducción disponibles, utilizando el objeto importado desde en-US.json, lo que permite a la aplicación acceder a las traducciones en inglés.

**4. Uso de i18n en la Aplicación**
javascript
Copy code
app.use(i18n);
**Descripción:** La instancia i18n se registra como un plugin en la aplicación Vue mediante app.use(i18n);. Esto permite que la funcionalidad de internacionalización esté disponible en toda la aplicación, permitiendo el uso de las funciones de traducción ($t) en los componentes Vue.

¿Qué Permite Hacer vue-i18n?
**Traducción de Textos:** Con vue-i18n configurado, puedes utilizar la función $t en tus componentes para traducir textos dinámicamente según el idioma seleccionado.
**Ejemplo:**

```vue
Copy code
<template>
  <p>{{ $t('welcome') }}</p>
</template>
```

Este código mostraría "Welcome" si el idioma actual es inglés (en).

Gestión de Múltiples Idiomas: Puedes expandir el objeto messages para incluir múltiples idiomas y cambiar dinámicamente el idioma en la aplicación.

**Resumen**
El código relacionado con i18n agrega soporte para internacionalización en tu aplicación Vue.js, configurando un idioma por defecto (inglés) y permitiendo que la aplicación muestre textos en diferentes idiomas utilizando un archivo JSON de traducciones. Con vue-i18n, puedes fácilmente expandir y gestionar múltiples idiomas en tu aplicación, mejorando la accesibilidad y experiencia de usuario en distintas regiones lingüísticas.

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

- sudo mkdir src/ --> mkdir layout
- cd layout
- touch AuthLayout.vue

## Creación del Archivo `AuthLayout.vue`

En el directorio `~/Proyectos/Django_Vue/Vue-Django-Auth/Version_01/frontend/src/layout`, se creó un nuevo archivo llamado `AuthLayout.vue` utilizando el siguiente comando:

```bash
touch AuthLayout.vue
```
Contenido del Archivo AuthLayout.vue
Dentro de este archivo, se añadió el siguiente contenido:

```vue
Copy code
<template>
    <router-view/>
</template>

<style scoped>
</style>
```

**Descripción:**

**```<template>```**: Contiene la estructura principal del componente. En este caso, se utiliza **```<router-view/>```** para renderizar el componente correspondiente a la ruta actual dentro del layout de autenticación.

**```<style scoped>```**: Se incluye una sección de estilos scoped, lo que significa que los estilos definidos aquí solo afectarán a este componente en particular. Actualmente, esta sección está vacía, pero está lista para añadir estilos específicos para este layout en el futuro.


## Explicación de los Cambios en el Código de Configuración de Rutas en Vue Router

### Código Original

```typescript
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router

```

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################


## Explicación del Código

El código proporcionado utiliza **Vuetify**, un framework basado en **Vue.js** que proporciona componentes de interfaz de usuario listos para usar. Aquí te explico cada parte del código:

```vue
<template>
    <v-app>
        <router-view/>
    </v-app>
</template>
```

**```<v-app>```**: Este es el componente principal de Vuetify que actúa como el contenedor raíz de tu aplicación. Es necesario para que los demás componentes de Vuetify funcionen correctamente. Proporciona el contexto del tema, gestiona la disposición de la interfaz y maneja la responsividad de la aplicación.

**```<router-view/>```**: Este es un componente de Vue Router que renderiza el componente asociado con la ruta actual. En otras palabras, muestra la vista correspondiente según la URL en la que te encuentres.

El Estilo:
```vue
<style scoped>
    .v-application {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        background-color: #274384;
    }
</style>
```
**.v-application:** Es una clase que Vuetify aplica automáticamente al elemento raíz de la aplicación. En este código, estás sobrescribiendo algunos estilos de esta clase:

display: flex;: Define un contenedor flexible. Esto hace que los elementos dentro de .v-application sigan un modelo de diseño flexible (flexbox), permitiendo que se alineen y distribuyan de manera eficiente en el espacio disponible.

justify-content: center;: Centra horizontalmente el contenido dentro del contenedor.

align-items: center;: Centra verticalmente el contenido dentro del contenedor.

min-height: 100vh;: Establece la altura mínima del contenedor para que ocupe el 100% de la altura de la ventana del navegador (viewport).

background-color: #274384;: Define un color de fondo específico para toda la aplicación. En este caso, un color azul oscuro (#274384).

**Resumen**
El código configura una aplicación de Vuetify donde el contenido se centra tanto vertical como horizontalmente en la página, con un color de fondo azul oscuro. El uso de flexbox y el ajuste de la altura mínima garantizan que el contenido esté siempre centrado y se ajuste perfectamente a la ventana del navegador.

## Explicación del Código

### Código sin corregir

El código original configura un enrutador básico en una aplicación **Vue 3** utilizando **Vue Router**. A continuación, se detalla lo que hace cada parte:

```typescript
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router
```
## `createRouter` y `createWebHistory`

- Se importan estas funciones desde **vue-router** para configurar el enrutador de la aplicación.
- **`createWebHistory`** se usa para crear un historial de navegación compatible con HTML5, utilizando la URL base definida en `import.meta.env.BASE_URL`.

## Rutas

- La configuración del enrutador define dos rutas:
  - La ruta `'/'`, que carga el componente **HomeView**.
  - La ruta `'/about'`, que carga el componente **AboutView** de forma dinámica (**lazy-loaded**), generando un chunk separado para optimizar la carga.

## Código nuevo

En el código nuevo, se introduce una arquitectura diferente para la gestión de rutas, integrando un **layout** para mejorar la organización y estructura de la aplicación.


```typescript
import { createRouter, createWebHistory } from 'vue-router'
import AuthLayout from '@/layout/AuthLayout.vue';
import HomeView from '../views/HomeView.vue'
import { components } from 'vuetify/dist/vuetify-labs.js';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: AuthLayout,
      children: [
        { path: '', component: HomeView }
      ]
    },
  ]
})

export default router

```

## AuthLayout

- Se ha importado un nuevo componente de layout (**AuthLayout**), que se utiliza como contenedor para otras rutas. Esto es útil para mantener una estructura consistente a lo largo de diferentes vistas que comparten el mismo layout.

## Rutas con Layout

- La ruta `'/'` ahora utiliza **AuthLayout** como componente principal.
- Dentro de **AuthLayout**, la vista **HomeView** se carga como un **child route**. Esto permite que todas las rutas dentro de **AuthLayout** compartan un layout común, mientras que el contenido específico de la ruta se carga dentro del layout.

## Mejoras

- La utilización de **layouts** mejora la estructura de la aplicación y facilita la adición de nuevas vistas que deben compartir un mismo layout.
- La organización de rutas como **child routes** también ayuda a mantener el código más limpio y manejable.

## Resumen

El código nuevo introduce un patrón más avanzado para la gestión de rutas en una aplicación **Vue 3**, utilizando **layouts** para estructurar mejor las vistas y mantener consistencia en la interfaz de usuario. Este enfoque es útil en aplicaciones más complejas donde diferentes vistas comparten un diseño común.


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

```bash
> sudo npm install -D sass
> mkdir styles
.
├── logo.svg
└── styles
    ├── animations
    │   ├── _animation.rotate.scss
    │   ├── _animations.index.scss
    │   └── _animation.top_to_bottom.scss
    ├── auth
    │   └── _main.scss
    └── general
        ├── _general.colors.scss
        ├── _general.fonts.scss
        └── _general.index.scss

```



```bash
> sudo touch frontend/src/views/SignInView.vue

```

```typescript
<script setup lang="ts">
import { reactive } from 'vue';
import { useVuelidate } from '@vuelidate/core';
import { required, email } from '@vuelidate/validators';

const initialState = {
  email: '',
  password: ''
}

const state = reactive({
  ...initialState,
});

const rules = {
  email: { required, email },
  password: { required }
}

const v$ = useVuelidate(rules, state);

</script>
<template>
    <v-main>
      <v-container>
        <form @submit.prevent="handleSubmit">
          <v-row>
            <v-col cols="12">
              <h3>{{ $t('sign_in_to_my_app') }}</h3>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <v-text-field
                v-model="state.email"
                :error-messages="v$.email.$errors.map((e) => e.$message)"
                :label="$t('email')"
                variant="outlined"
                autocomplete="new-email"
                @blur="v$.email.$touch"
                @input="v$.email.$touch"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <v-text-field
                v-model="state.password"
                :counter="20"
                :error-messages="v$.password.$errors.map((e) => e.$message)"
                :label="$t('password')"
                variant="outlined"
                autocomplete="new-password"
                @blur="v$.password.$touch"
                @input="v$.password.$touch"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row class="mb-0">
            <v-col cols="6">
              <v-checkbox v-model="state.rememberMe" :label="$t('remember_me')"></v-checkbox>
            </v-col>
            <v-col cols="6" class="text-right">
              <router-link to="/reset-password" class="auth-reset-password">
                {{ $t('forgot_password') }}
              </router-link>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <v-btn
                type="submit"
                class="auth-btn"
                @click="v$.$validate"
                :class="{ 'auth-submitting-active-btn': isLoading }"
              >
                {{ $t('sign_in') }}
                <span class="mdi mdi-arrow-right-bold auth-main-form-submit-icon"></span>
                <span class="mdi mdi-cached rotate-animation auth-main-form-submitting-icon"></span>
              </v-btn>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <div class="auth-main-form-alerts">
                <div
                  class="auth-main-form-alert-success top-to-bottom-animation"
                  role="alert"
                  v-if="successMessage"
                >
                  <span class="mdi mdi-bell-outline auth-main-form-alert-success-icon"></span>
                  <p>{{ successMessage }}</p>
                </div>
                <div
                  class="auth-main-form-alert-error top-to-bottom-animation"
                  role="alert"
                  v-else-if="errorMessage"
                >
                  <span class="mdi mdi-bell-outline auth-main-form-alert-error-icon"></span>
                  <p>{{ errorMessage }}</p>
                </div>
              </div>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <div class="auth-additional-link">
                <p>
                  {{ $t('dont_have_an_account') }}
                  <router-link to="/registration" class="inline-block auth-main-form-reset-link">
                    {{ $t('register_an_account') }}
                  </router-link>
                </p>
              </div>
            </v-col>
          </v-row>
        </form>
      </v-container>
    </v-main>
  </template>
  <style>
  @import '@/assets/styles/auth/_main.scss';
  </style>
```

Modificar archivo **frontend/src/router/index.ts**

```typescript

import { createRouter, createWebHistory } from 'vue-router'
import AuthLayout from '@/layout/AuthLayout.vue';
import HomeView from '../views/HomeView.vue'
import SignInView from '../views/SignInView.vue'
import { components } from 'vuetify/dist/vuetify-labs.js';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: AuthLayout,
      children: [
        { path: '', component: SignInView }
      ]
    },

  ]
})

export default router

```

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

```bash
> sudo touch frontend/src/views/RegistrationView.vue
```

```typescript
import { createRouter, createWebHistory } from 'vue-router'
import AuthLayout from '@/layout/AuthLayout.vue';
import SignInView from '../views/SignInView.vue'
import RegistrationView from '../views/RegistrationView.vue'
import { components } from 'vuetify/dist/vuetify-labs.js';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: AuthLayout,
      children: [
        { path: '', component: SignInView },
        { path: 'registration', component: RegistrationView }
      ]
    },
  ]
})

export default router
```

## RegistrationView.vue

```typescript
<script setup lang="ts">
import { reactive } from 'vue';
import { useVuelidate } from '@vuelidate/core';
import { required, email } from '@vuelidate/validators';

const initialState = {
  email: '',
  password: ''
}

const state = reactive({
  ...initialState,
});

const rules = {
  email: { required, email },
  password: { required }
}

const v$ = useVuelidate(rules, state);

</script>
<template>
    <v-main>
      <v-container>
        <form @submit.prevent="handleSubmit">
          <v-row>
            <v-col cols="12">
              <h3>{{ $t('sign_up_to_my_app') }}</h3>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <v-text-field
                v-model="state.email"
                :error-messages="v$.email.$errors.map((e) => e.$message)"
                :label="$t('email')"
                variant="outlined"
                autocomplete="new-email"
                @blur="v$.email.$touch"
                @input="v$.email.$touch"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <v-text-field
                v-model="state.password"
                :counter="20"
                :error-messages="v$.password.$errors.map((e) => e.$message)"
                :label="$t('password')"
                variant="outlined"
                autocomplete="new-password"
                @blur="v$.password.$touch"
                @input="v$.password.$touch"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row class="mb-0">
            <v-col cols="6">
              <v-checkbox v-model="state.rememberMe" :label="$t('remember_me')"></v-checkbox>
            </v-col>
            <v-col cols="6" class="text-right">
              <router-link to="/reset-password" class="auth-reset-password">
                {{ $t('forgot_password') }}
              </router-link>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <v-btn
                type="submit"
                class="auth-btn"
                @click="v$.$validate"
                :class="{ 'auth-submitting-active-btn': isLoading }"
              >
                {{ $t('sign_up') }}
                <span class="mdi mdi-arrow-right-bold auth-main-form-submit-icon"></span>
                <span class="mdi mdi-cached rotate-animation auth-main-form-submitting-icon"></span>
              </v-btn>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <div class="auth-main-form-alerts">
                <div
                  class="auth-main-form-alert-success top-to-bottom-animation"
                  role="alert"
                  v-if="successMessage"
                >
                  <span class="mdi mdi-bell-outline auth-main-form-alert-success-icon"></span>
                  <p>{{ successMessage }}</p>
                </div>
                <div
                  class="auth-main-form-alert-error top-to-bottom-animation"
                  role="alert"
                  v-else-if="errorMessage"
                >
                  <span class="mdi mdi-bell-outline auth-main-form-alert-error-icon"></span>
                  <p>{{ errorMessage }}</p>
                </div>
              </div>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <div class="auth-additional-link">
                <p>
                  {{ $t('do_you_have_an_account') }}
                  <router-link to="/" class="inline-block auth-main-form-reset-link">
                    {{ $t('sign_in') }}
                  </router-link>
                </p>
              </div>
            </v-col>
          </v-row>
        </form>
      </v-container>
    </v-main>
  </template>
  <style>
  @import '@/assets/styles/auth/_main.scss';
  </style>
```

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

> mkdir backend

> pip install django

> django-admin startproject core .

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

> pip install djangorestframework

**Application definition**

```python

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_APPS = [
    'rest_framework',
]

PROJECT_APPS = [
    'apps.authentication',
]

INSTALLED_APPS = BASE_APPS + THIRD_APPS + PROJECT_APPS

```

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

> python manage.py startapp authentication apps/authentication

**core/urls.py**

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/',include(('apps.authentication.urls','authentication'), namespace='authentication')),
]
```

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

> touch apps/authentication/serializers.py

## `models.py`

Este archivo define los modelos que representan las entidades de tu aplicación en la base de datos. Se ha realizado una modificación en el modelo `CustomUser` para evitar conflictos con las relaciones inversas (`reverse accessors`) que Django crea automáticamente.

### `CustomUserManager`

Esta clase hereda de `BaseUserManager` y proporciona métodos personalizados para crear usuarios.

- **`create_user`**: Método que se encarga de crear un usuario con un correo electrónico y contraseña. Valida que el campo de correo electrónico esté presente y lo normaliza antes de crear el usuario.

```python
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

```

## `CustomUser`

Esta clase hereda de `AbstractUser`, pero se personaliza para usar el correo electrónico en lugar del nombre de usuario (`username`). Además, se han añadido campos para gestionar grupos y permisos de manera personalizada.

- **`username = None`**: Se elimina el campo `username` de la clase base `AbstractUser`.
- **`email`**: Se define el campo de correo electrónico como obligatorio y único.
- **`groups`**: Se redefine el campo `groups` para evitar conflictos con la relación inversa generada por Django. Se añade un `related_name` único (`customuser_groups`) y `related_query_name` (`customuser`) para personalizar la relación.
- **`user_permissions`**: De manera similar, se redefine el campo `user_permissions` para evitar conflictos. Se añade un `related_name` único (`customuser_user_permissions`) y `related_query_name` (`customuser`).
- **`USERNAME_FIELD`**: Especifica que el campo de correo electrónico se utilizará como identificador único para el usuario.
- **`objects = CustomUserManager()`**: Asigna el `CustomUserManager` como administrador del modelo, lo que permite utilizar los métodos personalizados para crear usuarios.
- **`__str__`**: Método que devuelve el correo electrónico del usuario como su representación en cadena.

```python
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups',  # Cambia el nombre de la relación inversa
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_query_name='customuser'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_user_permissions',  # Cambia el nombre de la relación inversa
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_query_name='customuser'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


```


## Explicación de los Cambios:

### `groups` y `user_permissions`:

- Se añaden campos personalizados para gestionar las relaciones **Many-to-Many** con los modelos `Group` y `Permission`.
- **`related_name`**: Personaliza el nombre de la relación inversa para evitar conflictos con el modelo de usuario predeterminado de Django.
- **`related_query_name`**: Define un nombre de consulta relacionado único, permitiendo que las consultas se realicen sin problemas.

### Motivo de los Cambios:

- Estos cambios se realizan para evitar conflictos entre las relaciones inversas (**reverse accessors**) que Django intenta crear automáticamente para el modelo `CustomUser` y el modelo predeterminado `User`. 
- Al personalizar `related_name` y `related_query_name`, se evita que Django intente crear relaciones con nombres duplicados, lo que podría causar errores en el sistema.

### Resumen

- El modelo `CustomUser` ha sido modificado para personalizar las relaciones **Many-to-Many** con los modelos `Group` y `Permission`, evitando conflictos con el modelo de usuario predeterminado de Django.
- Estos cambios aseguran que tu aplicación pueda manejar de manera eficiente la gestión de usuarios, grupos y permisos, respetando la estructura personalizada que has implementado.


## `serializers.py`

Este archivo define los serializadores, que son responsables de transformar los datos complejos de Django en formatos que se puedan renderizar en JSON, y viceversa.

### `UserSocialRegistrationSerializer`

- **`email` y `password`**: Campos definidos en el serializador, donde `password` tiene reglas de validación adicionales como ser solo de escritura y ser tratado como un campo de contraseña.

- **`Meta`**: Define qué modelo se está serializando (`CustomUser`) y qué campos se incluyen (`email`, `password`, `role`).

- **`validate_email`**: Método que valida si el correo electrónico ya existe, si está vacío o si tiene un formato inválido.

- **`validate_password`**: Método que valida la longitud y formato de la contraseña, asegurando que esté entre 8 y 20 caracteres y que no contenga espacios.

- **`create`**: Método que crea un nuevo usuario utilizando los datos validados.

```python
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from .models import CustomUser

class UserSocialRegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=20, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}}
        }

    def validate_email(self, email):
        """
        Validate the email
        """
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError(_('This email address is already registered.'))

        if not email.strip():
            raise serializers.ValidationError(_('Email address cannot be blank.'))

        import re
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise serializers.ValidationError(_('Enter a valid email address.'))

        return email

    def validate_password(self, password):
        """
        Validate the password
        """
        min_length: int = 8
        max_length: int = 20

        if len(password) < min_length or len(password) > max_length:
            raise serializers.ValidationError(_('The password must be between 8 and 20 characters long.'))

        if ' ' in password:
            raise serializers.ValidationError(_('The password cannot contain spaces.'))

        return password

    def create(self, validated_data):
        """
        Create the user
        """
        user: CustomUser = CustomUser.objects.create_user(**validated_data)
        return user

```

## `urls.py`

Este archivo define las rutas de la aplicación `authentication`.

- **`app_name = 'authentication'`**: Establece un namespace para las URLs de la aplicación, lo que facilita su referenciación en otras partes del proyecto.

- **`urlpatterns`**: Lista de rutas definidas para la aplicación.

  - **`path('registration', CreateAccountView.as_view(), name='registration')`**: Define una ruta para la creación de cuentas, vinculando la URL `/registration` a la vista `CreateAccountView`.

```python
from django.urls import path
from .views import CreateAccountView

app_name = 'authentication'

urlpatterns = [
    path('registration', CreateAccountView.as_view(), name='registration')
]
```

## `views.py`

Este archivo contiene las vistas que manejan las solicitudes HTTP para la aplicación `authentication`. Las vistas son responsables de procesar las solicitudes entrantes, interactuar con los modelos y serializadores, y devolver una respuesta adecuada.

### `CreateAccountView`

- **Descripción**:
  - Esta vista hereda de `CreateAPIView`, que es una vista genérica proporcionada por Django Rest Framework para manejar la creación de nuevos registros en la base de datos. En este caso, la vista se utiliza para registrar nuevos usuarios en la aplicación.

- **`serializer_class = UserSerializer`**:
  - Define el serializador que se utilizará para validar y crear el usuario. El serializador (`UserSerializer`) convierte los datos JSON enviados en la solicitud en un objeto `CustomUser`, validando campos como el correo electrónico y la contraseña antes de guardarlo en la base de datos.

- **`permission_classes = [IsNotAuthenticated]`**:
  - Establece que solo los usuarios no autenticados pueden acceder a esta vista. Es decir, si un usuario ya está autenticado (por ejemplo, si ha iniciado sesión), no podrá acceder a esta vista para crear una nueva cuenta. Esta clase de permiso es útil para evitar que usuarios autenticados intenten crear cuentas adicionales.

- **`post`**:
  - Método que maneja la solicitud HTTP POST para crear un nuevo usuario. Este método:
    1. **Serialización**: Toma los datos del cuerpo de la solicitud y los pasa al serializador definido (`UserSerializer`).
    2. **Validación**: Verifica si los datos proporcionados son válidos. Si hay errores específicos relacionados con el correo electrónico o la contraseña, se manejan de manera personalizada para proporcionar mensajes de error claros.
    3. **Creación**: Si los datos son válidos, el método `save` del serializador se llama para crear un nuevo usuario en la base de datos.
    4. **Respuesta**: Devuelve una respuesta JSON con un mensaje de éxito si el usuario se crea correctamente. Si ocurre algún error durante el proceso, se devuelve un mensaje de error apropiado.

```python
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer
from .permissions import IsNotAuthenticated

# Create Account
class CreateAccountView(CreateAPIView):
    queryset = None
    serializer_class = UserSerializer
    permission_classes = [IsNotAuthenticated]
    
    def post(self, request):
        # Obtener información sobre la serialización
        serializer = self.get_serializer(data=request.data)

        # Verificar si los datos recibidos son correctos
        if not serializer.is_valid():
            # Mensaje de error predeterminado
            errorMsg = _('An error has occurred.')

            # Verificar si el error está relacionado con el correo electrónico
            if serializer.errors.get('email') is not None:
                errorMsg = serializer.errors['email'][0].capitalize()
            elif serializer.errors.get('password') is not None:
                errorMsg = serializer.errors['password'][0].capitalize()

            # Devolver mensaje personalizado
            return Response(
                {
                    "success": False,
                    "message": errorMsg
                },
                status=status.HTTP_200_OK
            )

        # Intentar crear el usuario
        try:
            serializer.save()
        except Exception:
            # Devolver mensaje personalizado en caso de error
            return Response(
                {
                    "success": False,
                    "message": _('An unknown error occurred.')
                },
                status=status.HTTP_200_OK
            )             

        # Devolver mensaje de éxito
        return Response(
            {
                "success": True,
                "message": _('The account was created successfully.')
            },
            status=status.HTTP_201_CREATED
        )
```

## `permissions.py`

Este archivo define las clases de permisos que se usan para restringir el acceso a ciertas vistas en tu aplicación Django Rest Framework. Los permisos son esenciales para controlar quién puede acceder a qué partes de tu aplicación, asegurando que solo los usuarios adecuados puedan realizar ciertas acciones.

### `IsNotAuthenticated`

- **Descripción**:
  - Esta clase hereda de `BasePermission`, que es una clase base de Django Rest Framework para implementar permisos personalizados. El objetivo de `IsNotAuthenticated` es restringir el acceso a las vistas solo a usuarios que no están autenticados, es decir, usuarios que no han iniciado sesión.

- **`has_permission`**:
  - Este método es el núcleo de cualquier clase de permisos en Django Rest Framework. En `IsNotAuthenticated`, el método **retorna `True` si el usuario no está autenticado** (es decir, si `request.user.is_authenticated` es `False`).
  - Si el usuario está autenticado (es decir, si ha iniciado sesión), el método retorna `False`, lo que deniega el acceso a la vista protegida por este permiso.

- **Uso**:
  - Este permiso se utiliza típicamente en vistas como formularios de registro o de inicio de sesión, donde no tiene sentido permitir que los usuarios que ya están autenticados accedan nuevamente a estas vistas.

```python
from rest_framework.permissions import BasePermission

class IsNotAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_authenticated
```


> **POST** http://127.0.0.1:8000/api/auth/registration

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

> **Agregar la siguiente linea en settings.py**

AUTH_USER_MODEL = 'authentication.CustomUser'

## `AUTH_USER_MODEL = 'authentication.CustomUser'`

### Explicación

Esta línea en `settings.py` le dice a Django que utilice un modelo de usuario personalizado en lugar del modelo de usuario predeterminado (`auth.User`) que Django proporciona.

### Detalles

- **`AUTH_USER_MODEL`**: Esta es la configuración que Django utiliza para saber cuál es el modelo de usuario que debe emplear para la autenticación, manejo de permisos, y otras funcionalidades relacionadas con usuarios.

- **`'authentication.CustomUser'`**:
  - **`authentication`**: Es el nombre de la aplicación donde se encuentra el modelo de usuario personalizado. En este caso, la aplicación `authentication` está ubicada en `apps/authentication`.
  - **`CustomUser`**: Es el nombre del modelo de usuario personalizado que has definido en `models.py`.

### ¿Qué hace esta línea?

- **Sustituye el Modelo de Usuario Predeterminado**: Al definir `AUTH_USER_MODEL`, Django utilizará `CustomUser` en lugar de `auth.User` para todas las operaciones relacionadas con usuarios, como autenticación, manejo de permisos, y gestión de perfiles de usuario.

- **Integración Completa**: Esto significa que cualquier referencia al usuario en tu proyecto, como en vistas, formularios, o serializadores, usará tu modelo personalizado `CustomUser` en lugar del modelo de usuario predeterminado.

### Importancia

- **Flexibilidad**: Definir un modelo de usuario personalizado te permite agregar campos y funcionalidades específicas a tus necesidades, como usar el correo electrónico en lugar del nombre de usuario (`username`) para la autenticación.

- **Evita Conflictos**: Esta configuración asegura que Django siempre utilice el modelo correcto, evitando posibles conflictos o errores si se intentara usar el modelo de usuario predeterminado y el personalizado en el mismo proyecto.

### Resumen

La línea `AUTH_USER_MODEL = 'authentication.CustomUser'` es esencial cuando has definido un modelo de usuario personalizado y quieres que Django lo use en lugar de su modelo predeterminado. Esto asegura que todas las operaciones relacionadas con usuarios en tu proyecto empleen tu modelo personalizado.

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

## Explicación

Esta línea en `settings.py` configura Django Rest Framework (DRF) para utilizar una función personalizada para manejar excepciones en tu aplicación.

### `EXCEPTION_HANDLER`

- **`EXCEPTION_HANDLER`**: Es una configuración de Django Rest Framework que permite especificar una función personalizada que será llamada cada vez que ocurra una excepción no manejada en las vistas de tu API.

### `'core.exceptions.custom_exception_handler'`

- **`'core.exceptions.custom_exception_handler'`**: Es la ruta que apunta a la función que has definido en `core/exceptions.py` para manejar las excepciones. Esta función reemplaza el manejador de excepciones predeterminado de DRF, permitiéndote personalizar las respuestas de error.

### Código en `settings.py`

```python
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'core.exceptions.custom_exception_handler'
}
```

## Código en `exceptions.py`

### Archivo `exceptions.py`

Este archivo contiene la función personalizada que se utilizará para manejar las excepciones en tu aplicación. Aquí está el código:

```python
# System Utils
from django.http import JsonResponse

# Installed Utils
from rest_framework.views import exception_handler
from rest_framework.response import Response  # Asegúrate de importar Response

def custom_exception_handler(exc, context):
    """
    Custom the exceptions
    messages
    """
    response = exception_handler(exc, context)
    
    if response is not None:
        response.data['status_code'] = response.status_code
        
    if hasattr(exc, 'detail'):
        return JsonResponse(  # Cambiado de `response(...)` a `JsonResponse(...)`
            {
                "success": False,
                "message": exc.detail
            },
            status=response.status_code  # Asegúrate de incluir el código de estado
        )      
    else:
        return JsonResponse({
            'success': False,  # Corregido 'sucess' a 'success'
            'message': 'An unknown error occurred.'
        }, status=500)

```

## Explicación

### `exception_handler(exc, context)`

- Llama al manejador de excepciones predeterminado de Django Rest Framework. Esto permite que DRF maneje las excepciones de la manera usual antes de aplicar cualquier personalización adicional.

### `response.data['status_code'] = response.status_code`

- Si el manejador de excepciones predeterminado devuelve una respuesta (`response`), se añade el código de estado HTTP (`status_code`) al cuerpo de la respuesta.

### `hasattr(exc, 'detail')`

- Verifica si la excepción (`exc`) tiene un atributo `detail`. Esto generalmente indica que la excepción es una instancia de una excepción estándar de DRF (como `ValidationError`, `PermissionDenied`, etc.).

### `JsonResponse` con `exc.detail`

- Si la excepción tiene un `detail`, se devuelve una respuesta JSON personalizada con un formato específico que incluye un campo `"success": False` y el detalle del mensaje de error (`"message": exc.detail`).

### Respuesta genérica para excepciones desconocidas

- Si la excepción no tiene un `detail` (es decir, es una excepción inesperada o desconocida), se devuelve una respuesta JSON genérica con un mensaje de error predeterminado y un código de estado 500 (Error interno del servidor).

## Resumen

La configuración en `settings.py` y la función en `exceptions.py` permiten personalizar cómo se manejan y se devuelven las excepciones en tu aplicación Django Rest Framework. Esto te da control sobre la forma en que los errores se comunican a los clientes de la API, asegurando que las respuestas sean consistentes y que los detalles sensibles no se expongan innecesariamente.


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

> sudo npm install axios

## Comando: `sudo npm install axios`

### Explicación

Este comando se utiliza para instalar el paquete `axios` en un proyecto Node.js. A continuación, se detalla qué hace cada parte del comando:

- **`sudo`**:
  - Ejecuta el comando con privilegios de superusuario (administrador). Esto es necesario si estás instalando paquetes en un entorno donde se requieren permisos elevados, como en directorios del sistema.

- **`npm`**:
  - Es el gestor de paquetes de Node.js. `npm` se utiliza para instalar, actualizar, y gestionar dependencias (paquetes) en proyectos Node.js.

- **`install`**:
  - Es el comando que le indica a `npm` que instale uno o más paquetes. En este caso, se está instalando el paquete `axios`.

- **`axios`**:
  - Es el nombre del paquete que se va a instalar. **Axios** es una biblioteca basada en promesas que se utiliza para realizar solicitudes HTTP desde el navegador o desde Node.js. Es comúnmente utilizada para interactuar con APIs, enviar y recibir datos JSON, y manejar peticiones HTTP de manera sencilla y eficiente.

### Resultado del Comando

- Al ejecutar este comando, `npm` descarga e instala el paquete `axios` y todas sus dependencias en el proyecto actual.
- **Axios** se agregará a la lista de dependencias en el archivo `package.json` del proyecto.
- Una vez instalado, podrás importar y usar `axios` en tu código para realizar solicitudes HTTP.

### Ejemplo de Uso de `axios`

```javascript
const axios = require('axios');

axios.get('https://api.example.com/data')
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
```

> mkdir src/composables

> touch src/composables/useAuth.ts

> mkdir src/interfaces

> touch src/interfaces/ user.ts

## Explicación de los Archivos y su Comunicación

### 1. `useAuth.ts`

Este archivo es un **composable** en Vue 3 que maneja la autenticación de usuarios (registro o inicio de sesión). Utiliza las APIs reactivas de Vue y la biblioteca `axios` para enviar solicitudes HTTP al backend. A continuación se detalla qué hace cada parte del código:

#### **Importaciones**

- **`ref` de Vue**:
  - `ref` es una función de Vue que crea referencias reactivas. En este archivo, `ref` se utiliza para crear variables reactivas (`successMessage`, `errorMessage`, `isLoading`) que actualizarán automáticamente la interfaz de usuario cuando sus valores cambien.

- **`axios` y `AxiosResponse`**:
  - `axios` es una biblioteca para realizar solicitudes HTTP. `AxiosResponse` es un tipo de TypeScript que define la estructura de las respuestas HTTP que `axios` maneja.
  
- **Tipos de Interfaces Importadas**:
  - `BaseUser`: Es una interfaz importada desde `user.ts`, que define la estructura básica de un usuario (correo electrónico y contraseña).
  - `ApiResponse`: Es una interfaz importada desde `apiResponse.ts`, que define la estructura de la respuesta esperada del servidor.

#### **Función `useAuth`**

- **Propósito**:
  - `useAuth` es una función que encapsula la lógica de autenticación, permitiendo a los componentes Vue reutilizarla fácilmente.

- **Variables Reactivas**:
  - **`successMessage`**: Almacena un mensaje de éxito si la autenticación es exitosa.
  - **`errorMessage`**: Almacena un mensaje de error si algo sale mal.
  - **`isLoading`**: Indica si se está realizando una solicitud de autenticación (utilizada para mostrar indicadores de carga en la interfaz).

- **Método `authRequest`**:
  - **Propósito**: Este método maneja la lógica de la solicitud de autenticación (registro o inicio de sesión).
  - **Funcionamiento**:
    1. **Inicia la Carga**: Activa `isLoading` para mostrar un indicador de carga en la interfaz.
    2. **Resetea Mensajes**: Limpia los mensajes de éxito y error antes de enviar la solicitud.
    3. **Envía la Solicitud**: Usa `axios` para enviar una solicitud POST al servidor con los datos del usuario.
    4. **Maneja la Respuesta**:
       - Si la respuesta es exitosa (`response.data.success` es `true`), almacena el mensaje de éxito en `successMessage`.
       - Si la respuesta no es exitosa, almacena el mensaje de error en `errorMessage`.
    5. **Manejo de Errores**: Si ocurre un error durante la solicitud, se captura y almacena el mensaje en `errorMessage`.
    6. **Finaliza la Carga**: Desactiva `isLoading` para ocultar el indicador de carga.

- **Retorno**: `useAuth` devuelve los métodos y variables reactivas (`authRequest`, `successMessage`, `errorMessage`, `isLoading`) para ser usados en los componentes Vue.

```typescript
import { ref } from 'vue';
import axios, { type AxiosResponse } from 'axios';
import type { BaseUser } from '@/interfaces/user';
import type ApiResponse from '@/interfaces/apiResponse';

export const useAuth = () => {
  const successMessage = ref('');
  const errorMessage = ref('');
  const isLoading = ref<boolean>(false);

  const authRequest = async (url: string, user: BaseUser) => {
    isLoading.value = true;
    successMessage.value = errorMessage.value = '';

    try {
      const response: AxiosResponse<ApiResponse<null>> = await axios.post(url, user);
      if (response.data.success) {
        successMessage.value = response.data.message;
      } else {
        errorMessage.value = response.data.message;
      }
    } catch (error) {
      errorMessage.value = error instanceof Error ? error.message : 'An error has occurred.';
    } finally {
      isLoading.value = false;
    }
  };

  return { authRequest, successMessage, errorMessage, isLoading };
};

```

## 2. `apiResponse.ts`

Este archivo define una interfaz de TypeScript llamada `ApiResponse` que estructura la respuesta que se espera recibir del servidor después de una solicitud HTTP.

### Interfaz `ApiResponse<T>`

- **`content: T | null`**:
  - Representa el contenido principal de la respuesta. El tipo genérico `T` permite flexibilidad, lo que significa que `content` puede ser de cualquier tipo (por ejemplo, un objeto, una lista, etc.) o `null` si no hay contenido.

- **`success: boolean`**:
  - Indica si la solicitud fue exitosa (`true`) o no (`false`).

- **`message: string`**:
  - Proporciona un mensaje informativo, como una confirmación en caso de éxito o un mensaje de error en caso de fallo.

### Propósito

Esta interfaz permite que las respuestas del servidor sean consistentes y predecibles, facilitando la manipulación de los datos en el frontend. Al estructurar las respuestas de esta manera, se asegura que el frontend pueda manejar adecuadamente tanto los datos recibidos como los mensajes de error o éxito.

### Código de `apiResponse.ts`

```typescript
export default interface ApiResponse<T> {
  content: T | null;
  success: boolean;
  message: string;
}

```
## 3. `user.ts`

Este archivo define una interfaz de TypeScript llamada `BaseUser` que describe la estructura básica de un usuario en el sistema.

### Interfaz `BaseUser`

- **`email: string`**:
  - Representa la dirección de correo electrónico del usuario.
  
- **`password: string`**:
  - Representa la contraseña del usuario.

### Propósito

Esta interfaz se usa para garantizar que los objetos que representan usuarios tengan siempre un formato consistente, lo que facilita la validación y manipulación de datos de usuarios.

### Código de `user.ts`

```typescript
export interface BaseUser {
  email: string;
  password: string;
}

```

## Comunicación entre los Archivos

### `useAuth.ts`

- **Importación de `BaseUser` desde `user.ts`**:
  - `useAuth.ts` importa la interfaz `BaseUser` desde `user.ts` para tipar el objeto `user` que se envía en la solicitud de autenticación. Esto garantiza que los datos del usuario (correo electrónico y contraseña) tengan un formato consistente y predefinido.

- **Importación de `ApiResponse` desde `apiResponse.ts`**:
  - `useAuth.ts` también importa la interfaz `ApiResponse` desde `apiResponse.ts` para tipar la respuesta esperada de la solicitud HTTP realizada con `axios`. Esto permite manejar de manera consistente las respuestas del servidor, asegurando que se sigan siempre las mismas estructuras de datos.

### `apiResponse.ts` y `user.ts`

- **Definición de Estructuras de Datos**:
  - Estos archivos (`apiResponse.ts` y `user.ts`) definen las estructuras de datos clave que son utilizadas por `useAuth.ts` para manejar tanto la autenticación como las respuestas del servidor. 
  - `user.ts` define la estructura de los datos del usuario, mientras que `apiResponse.ts` define cómo se espera que sean las respuestas del servidor.

### Propósito

- **Eficiencia y Estructura**:
  - En conjunto, estos archivos permiten que tu aplicación maneje la autenticación de usuarios de manera eficiente y estructurada, garantizando que los datos se envíen y reciban en los formatos correctos.
  - Además, aseguran que los mensajes de error o éxito se manejen de manera clara y consistente, mejorando la experiencia del usuario y la mantenibilidad del código.


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

## Explicación del Código

Este código define un composable en Vue 3 que maneja la lógica de autenticación de usuarios, específicamente el registro o inicio de sesión, utilizando `axios` para realizar solicitudes HTTP. A continuación, se describe cada parte del código:

### Importaciones

- **`ref` de Vue:**
  - `ref` es una función de Vue que crea referencias reactivas. Estas referencias se utilizan para manejar estados que cambian en la interfaz de usuario, como los mensajes de éxito, error y el estado de carga.

- **`useRouter` de `vue-router`:**
  - `useRouter` permite acceder al router de Vue, lo que facilita la navegación programática dentro de la aplicación, como redirigir al usuario a otra página después de un registro exitoso.

- **`axios` y `AxiosResponse`:**
  - `axios` es una biblioteca popular para realizar solicitudes HTTP desde el frontend. `AxiosResponse` es un tipo de TypeScript que describe la estructura de la respuesta HTTP que se espera de `axios`.

- **Interfaces `BaseUser` y `ApiResponse`:**
  - Estas interfaces se utilizan para definir los tipos de datos que se envían en la solicitud (`BaseUser`) y los que se reciben en la respuesta (`ApiResponse`). Esto proporciona seguridad de tipos y ayuda a evitar errores relacionados con tipos de datos incorrectos.

### Función `useAuth`

- **Propósito:**
  - `useAuth` es un composable que encapsula toda la lógica relacionada con la autenticación de usuarios. Proporciona métodos y estados reactivos que pueden ser reutilizados en los componentes de Vue.

- **Variables Reactivas:**
  - **`successMessage`**: Almacena un mensaje de éxito si la solicitud HTTP es exitosa.
  - **`errorMessage`**: Almacena un mensaje de error si la solicitud HTTP falla.
  - **`isLoading`**: Indica si se está realizando una solicitud HTTP en ese momento, lo que puede ser utilizado para mostrar un indicador de carga en la interfaz.

- **Método `authRequest`:**
  - **Propósito:** Realiza la solicitud de autenticación al servidor (registro o inicio de sesión).
  - **Flujo de Trabajo:**
    1. **Iniciar la Carga:** Activa `isLoading` para indicar que se está realizando una operación.
    2. **Resetear Mensajes:** Limpia los mensajes de éxito y error antes de realizar la solicitud.
    3. **Enviar Solicitud:** Utiliza `axios.post` para enviar los datos del usuario al servidor.
    4. **Manejo de Respuesta:**
       - Si la respuesta indica éxito (`response.data.success`), almacena el mensaje de éxito en `successMessage` y, después de 2 segundos, redirige al usuario a la página principal (`'/'`).
       - Si la solicitud falla, almacena el mensaje de error en `errorMessage`.
    5. **Manejo de Errores:** Si ocurre un error durante la solicitud (por ejemplo, problemas de red), se captura y se establece en `errorMessage`.
    6. **Finalizar la Carga:** Desactiva `isLoading` para indicar que la operación ha finalizado.

- **Retorno:**
  - La función `useAuth` devuelve un objeto que incluye `authRequest`, `successMessage`, `errorMessage`, e `isLoading`, los cuales pueden ser utilizados en los componentes de Vue para gestionar la autenticación.

### Código Completo

```typescript
// System Utils
import { ref } from 'vue';

// Installed Utils
import { useRouter } from 'vue-router';
import axios, { type AxiosResponse } from 'axios';

// App Utils
import type { BaseUser } from '@/interfaces/user';
import type ApiResponse from '@/interfaces/apiResponse';

// Register the users
export const useAuth = () => {

   // Use the router
   const router = useRouter();

  // Reactive reference for success messages
  const successMessage = ref('');

  // Reactive reference for error messages
  const errorMessage = ref('');

  // Loading marker
  const isLoading = ref<boolean>(false);

  // Sign in or register a user
  const authRequest = async (url: string, user: BaseUser) => {
    
    // Enable the loading
    isLoading.value = true;

    // Reset the error and success messages
    successMessage.value = errorMessage.value = '';

    try {
      // Send request
      const response: AxiosResponse<ApiResponse<null>> = await axios.post(url, user);

      // Check if the message is success
      if (response.data.success) {
        // Set message
        successMessage.value = response.data.message;
        // Wait for 2 seconds
        setTimeout(() => {
            router.push('/');
        }, 2000);
      } else {
        // Set error message
        errorMessage.value = response.data.message;
      }
    } catch (error) {
      // Set error
      errorMessage.value = error instanceof Error ? error.message : 'An error has occurred.';
    } finally {
      // Disable the loading
      isLoading.value = false;
    }
  }

  return { authRequest, successMessage, errorMessage, isLoading }
}

```

## Explicación del Código

Este código es un componente de Vue 3 escrito en TypeScript que gestiona la lógica de un formulario de registro de usuarios utilizando `Vuetify` para la interfaz de usuario, `Vuelidate` para la validación de formularios, y un composable personalizado (`useAuth`) para manejar la autenticación. A continuación, se detalla cada parte del código:

### Importaciones en el Script

- **`reactive` de Vue:**
  - `reactive` es una función de Vue que convierte un objeto en reactivo, lo que significa que las propiedades del objeto se vuelven reactivas y se actualizarán automáticamente en la interfaz de usuario cuando cambien.

- **`useVuelidate` de `@vuelidate/core`:**
  - `useVuelidate` es un composable que se utiliza para gestionar la validación de formularios. Permite definir reglas de validación y aplicarlas a los campos del formulario de manera reactiva.

- **`required` y `email` de `@vuelidate/validators`:**
  - Estos son validadores predefinidos que aseguran que los campos sean obligatorios (`required`) y que el campo de correo electrónico tenga un formato válido (`email`).

- **`useAuth` de '@/composables/useAuth':**
  - `useAuth` es un composable personalizado que encapsula la lógica de autenticación (registro o inicio de sesión) y proporciona métodos y estados para manejar la solicitud de autenticación.

### Configuración del Estado y Validación

- **`initialState`:**
  - Este objeto define los valores iniciales de los campos del formulario (`email` y `password`).

- **`state`:**
  - `state` es un objeto reactivo basado en `initialState`. Este objeto es el que se vincula a los campos del formulario, permitiendo que sus valores sean reactivos y se actualicen automáticamente en la interfaz de usuario.

- **`rules`:**
  - `rules` define las reglas de validación para los campos del formulario. Aquí se especifica que `email` debe ser un campo obligatorio y tener un formato de correo electrónico válido, y que `password` debe ser un campo obligatorio.

- **`v$`:**
  - `v$` es una referencia a la validación configurada con `Vuelidate`. Se utiliza para verificar si los campos son válidos y para acceder a los mensajes de error.

### Uso del Composable `useAuth`

- **Desestructuración de `useAuth`:**
  - Se desestructuran `authRequest`, `successMessage`, `errorMessage`, e `isLoading` del composable `useAuth`. Estos se utilizan para manejar la solicitud de autenticación, así como para gestionar los estados de éxito, error y carga.

### Manejo del Envío del Formulario

- **`handleSubmit`:**
  - `handleSubmit` es una función que se ejecuta cuando se envía el formulario. Esta función realiza las siguientes tareas:
    1. **Verificar Errores:** Usa `v$` para verificar si hay errores en los campos del formulario. Si los hay, la función se detiene.
    2. **Registrar al Usuario:** Llama a `authRequest` pasando la URL y los datos del formulario (`state`). Esto realiza la solicitud HTTP para registrar al usuario.

### Estructura del Template

- **Formulario de Registro:**
  - El formulario está construido con componentes de Vuetify, como `v-text-field` para los campos de entrada y `v-btn` para el botón de envío. Se utiliza la validación y los mensajes de error de `Vuelidate` para proporcionar feedback en tiempo real a los usuarios.

- **Mensajes de Éxito y Error:**
  - Si `successMessage` tiene un valor, se muestra un mensaje de éxito. Si `errorMessage` tiene un valor, se muestra un mensaje de error. Esto proporciona una retroalimentación clara al usuario sobre el estado de su solicitud de registro.

### Código Completo

```typescript
<script setup lang="ts">
// System Utils
import { reactive } from 'vue';

// Installed Utils
import { useVuelidate } from '@vuelidate/core';
import { required, email } from '@vuelidate/validators';

// App Utils
import { useAuth } from '@/composables/useAuth';

// Default fields value
const initialState = {
  email: '',
  password: ''
}

// Make the fields reactive
const state = reactive({
  ...initialState,
});

// Rules for Vuelidate
const rules = {
  email: { required, email },
  password: { required }
}

// Configure Vuelidate
const v$ = useVuelidate(rules, state);

// Use auth variables
const { authRequest, successMessage, errorMessage, isLoading } = useAuth();

// Handle the form submit
const handleSubmit = async () => {
  // Verify if errors exist
  if (v$.value.$invalid) {
    return;
  }

  // Register the user
  authRequest('http://127.0.0.1:8000/api/auth/registration', state);
};
</script>

<template>
  <v-main>
    <v-container>
      <form @submit.prevent="handleSubmit">
        <v-row>
          <v-col cols="12">
            <h3>{{ $t('sign_up_to_my_app') }}</h3>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
            <v-text-field
              v-model="state.email"
              :error-messages="v$.email.$errors.map((e) => e.$message)"
              :label="$t('email')"
              variant="outlined"
              autocomplete="new-email"
              @blur="v$.email.$touch"
              @input="v$.email.$touch"
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
            <v-text-field
              type="password"
              v-model="state.password"
              :counter="20"
              :error-messages="v$.password.$errors.map((e) => e.$message)"
              :label="$t('password')"
              variant="outlined"
              autocomplete="new-password"
              @blur="v$.password.$touch"
              @input="v$.password.$touch"
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
            <v-btn type="submit" class="auth-btn" @click="v$.$validate" :class="{'auth-submitting-active-btn': isLoading }">
              {{ $t('sign_up') }}
              <span class="mdi mdi-arrow-right-bold auth-main-form-submit-icon"></span>
              <span class="mdi mdi-cached rotate-animation auth-main-form-submitting-icon"></span>
            </v-btn>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
            <div class="auth-main-form-alerts">
              <div
                class="auth-main-form-alert-success top-to-bottom-animation"
                role="alert"
                v-if="successMessage"
              >
                <span class="mdi mdi-bell-outline auth-main-form-alert-success-icon"></span>
                <p>{{ successMessage }}</p>
              </div>
              <div
                class="auth-main-form-alert-error top-to-bottom-animation"
                role="alert"
                v-else-if="errorMessage"
              >
                <span class="mdi mdi-bell-outline auth-main-form-alert-error-icon"></span>
                <p>{{ errorMessage }}</p>
              </div>
            </div>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
            <div class="auth-additional-link">
              <p>
                {{ $t('do_you_have_an_account') }}
                <router-link to="/" class="inline-block auth-main-form-reset-link">
                  {{ $t('sign_in') }}
                </router-link>
              </p>
            </div>
          </v-col>
        </v-row>
      </form>
    </v-container>
  </v-main>
</template>

<style>
@import '@/assets/styles/auth/_main.scss';
</style>
```

> **POST** http://127.0.0.1:8000/api/auth/registration

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

## Explicación de la Configuración de `django-cors-headers` en Django

`django-cors-headers` es una biblioteca que permite manejar **CORS (Cross-Origin Resource Sharing)** en proyectos Django. CORS es un mecanismo de seguridad que permite o restringe las solicitudes HTTP provenientes de otros dominios, algo común en aplicaciones web donde el frontend y el backend están en diferentes servidores o puertos.

### Instalación de `django-cors-headers`

Primero, se instala el paquete `django-cors-headers` utilizando `pip`:

```bash
pip install django-cors-headers
```

> pip install django-cors-headers

## Configuración en `settings.py`

Después de la instalación, se deben realizar algunas configuraciones en el archivo `settings.py` de tu proyecto Django para habilitar y configurar el manejo de CORS.

**settings.py**
```python 

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_APPS = [
    'rest_framework',
    'corsheaders',
]

PROJECT_APPS = [
    'apps.authentication',

]

INSTALLED_APPS = BASE_APPS + THIRD_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:3000"
]
```

## Explicación de la Configuración de `django-cors-headers`

- **`corsheaders`:** Este es el paquete recién instalado que se añade a `INSTALLED_APPS` bajo `THIRD_APPS`. Al agregarlo aquí, habilitas la funcionalidad de CORS en tu proyecto Django.

- **`corsheaders.middleware.CorsMiddleware`:** Este middleware se añade en la lista de `MIDDLEWARE`. Es responsable de interceptar las solicitudes HTTP y añadir los encabezados necesarios para habilitar CORS, dependiendo de la configuración que se establezca más adelante.

### Configuración de `CORS_ALLOWED_ORIGINS`

- **`CORS_ALLOWED_ORIGINS`:** Es una lista de URLs que se permiten realizar solicitudes a tu servidor Django desde otro dominio o puerto. En este ejemplo, se están permitiendo las solicitudes desde `http://localhost:5173` (que podría ser un frontend corriendo en Vite) y `http://localhost:3000` (otro posible frontend o herramienta como React).

### Resumen

Con la adición de `django-cors-headers` y su configuración en `settings.py`:

- **`corsheaders` en `INSTALLED_APPS`:** Habilita el uso de CORS en tu proyecto Django.
- **`CorsMiddleware` en `MIDDLEWARE`:** Intercepta las solicitudes y añade los encabezados necesarios para permitir o denegar las solicitudes CORS.
- **`CORS_ALLOWED_ORIGINS`:** Define específicamente qué dominios pueden hacer solicitudes a tu API, protegiendo tu aplicación de solicitudes no autorizadas desde otros orígenes.

Esta configuración es crucial cuando tu frontend y backend no están alojados en el mismo dominio o puerto, lo cual es común en el desarrollo de aplicaciones modernas.

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

## Explicación de la Configuración con `.env` y `import.meta.env`

### Creación del Archivo `.env`

Has creado un archivo llamado `.env` en tu proyecto, que contiene la siguiente línea:

```env
VITE_APP_API_URL=http://127.0.0.1:8000/
```

## Explicación de la Configuración con `.env` y `import.meta.env`

### **`VITE_APP_API_URL`**

- **`VITE_APP_API_URL`:** Es una variable de entorno que define la URL base para tu API. Esta variable es utilizada por Vite, la herramienta de construcción que estás usando para tu proyecto frontend en Vue 3. Definir la URL en un archivo `.env` te permite manejar configuraciones específicas para diferentes entornos (desarrollo, producción, etc.) sin necesidad de modificar directamente el código fuente.

### Uso de la Variable de Entorno en `RegistrationView.vue`

Luego, has reemplazado la ruta directa en el archivo `RegistrationView.vue` por la variable de entorno:

```typescript
authRequest(import.meta.env.VITE_APP_API_URL + 'api/auth/registration', state);
```

## Explicación de la Configuración con `import.meta.env.VITE_APP_API_URL`

### **`import.meta.env.VITE_APP_API_URL`**

- **`import.meta.env.VITE_APP_API_URL`:** Esta es la forma en que Vite accede a las variables de entorno definidas en el archivo `.env`. `import.meta.env` es un objeto que contiene todas las variables de entorno cargadas por Vite. En este caso, estás accediendo a `VITE_APP_API_URL`, que has definido como `http://127.0.0.1:8000/`.

### Concatenación de la URL

- **Concatenación de la URL:** Estás concatenando la URL base (`VITE_APP_API_URL`) con la ruta específica para la solicitud de registro (`api/auth/registration`). Esto permite que tu código sea más flexible y fácil de mantener, ya que si necesitas cambiar la URL base, solo tienes que actualizar el archivo `.env` sin modificar el código fuente.

### Beneficios de Esta Configuración

1. **Flexibilidad:** Puedes cambiar la URL base para diferentes entornos (por ejemplo, desarrollo, prueba, producción) simplemente modificando el archivo `.env`.

2. **Mantenibilidad:** Al centralizar la configuración de la URL en un archivo `.env`, reduces el riesgo de errores al tener múltiples lugares en el código donde se define la URL.

3. **Seguridad:** Las variables de entorno pueden manejar información sensible y se pueden configurar para que no se incluyan en el control de versiones (por ejemplo, agregando `.env` a `.gitignore`).

### Resumen

Esta configuración mejora la flexibilidad y mantenibilidad de tu aplicación, permitiendo que las URLs del backend sean fácilmente configurables sin necesidad de modificar directamente el código fuente.


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

## Explicación del Código en `views.py` y `serializers.py`

### `views.py`

Este archivo contiene la lógica que maneja la autenticación de usuarios cuando intentan iniciar sesión en la aplicación. Aquí te explico el código:

```python
# System Utils
from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate

# Installed Utils
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

# APP Utils
from .serializers import UserSerializer, SignInAccountSerializer
from .permissions import IsNotAuthenticated

# Sign In
class SignInAccountView(APIView):
    permission_classes = [IsNotAuthenticated]

    def post(self, request):
        # Get information about serialization
        serializer = SignInAccountSerializer(data=request.data)

        # Check if the received data is correct
        if not serializer.is_valid():
            # Default error message
            errorMsg: str = _('An error has occurred.')

            # Check if the error is for email
            if serializer.errors.get('email') is not None:
                errorMsg = serializer.errors['email'][0].capitalize()
            elif serializer.errors.get('password') is not None:
                errorMsg = serializer.errors['password'][0].capitalize()

            # Return custom message
            return Response(
                {
                    "success": False,
                    "message": errorMsg
                },
                status=status.HTTP_200_OK
            )
        
        # Get email
        email = serializer.validated_data.get('email')
        
        # Get password
        password = serializer.validated_data.get('password')

        # Let's login
        user = authenticate(email=email, password=password)

        # Check if login is successful
        if user:
            # Delete existing token if it exists
            Token.objects.filter(user=user).delete()

            # Create a new token
            token = Token.objects.create(user=user)

            # Return custom message
            return Response(
                {
                    "success": True,
                    "message": _('You have successfully signed in.'),
                    "user": {
                        "user_id": user.id,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "email": user.email,
                        "token": token.key
                    }
                },
                status=status.HTTP_201_CREATED
            )
        
        else:
            # Return custom message
            return Response(
                {
                    "success": False,
                    "message": _('The email or password is not correct.')
                },
                status=status.HTTP_200_OK
            )
```

## Explicación del Código en `views.py`

### `SignInAccountView`

- **`SignInAccountView`:** 
  - Es una subclase de `APIView` que maneja la autenticación de usuarios mediante un método POST.

- **`permission_classes`:** 
  - Restringe el acceso a esta vista a solo usuarios no autenticados, utilizando la clase de permisos `IsNotAuthenticated`.

### `post` Method

- **Serialización de Datos:**
  - Los datos enviados en la solicitud (`request`) se serializan utilizando `SignInAccountSerializer`.

- **Validación de Datos:**
  - Si los datos no son válidos, se genera un mensaje de error basado en los errores específicos encontrados (ya sea en el campo de correo electrónico o en el campo de contraseña) y se devuelve un mensaje personalizado.

- **Autenticación:**
  - Los datos validados (`email` y `password`) se usan para autenticar al usuario utilizando `authenticate`.

- **Generación de Token:**
  - Si la autenticación es exitosa, se elimina cualquier token anterior asociado al usuario y se genera un nuevo token.
  - Se devuelve un mensaje de éxito junto con la información del usuario y el nuevo token.

- **Manejo de Errores:**
  - Si la autenticación falla, se devuelve un mensaje de error indicando que el correo electrónico o la contraseña son incorrectos.

## `serializers.py`

Este archivo define cómo se deben serializar y validar los datos de entrada cuando un usuario intenta iniciar sesión.

```python
# System Utils
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from apps.authentication.models import CustomUser

# Serializer for login
class SignInAccountSerializer(serializers.ModelSerializer):

    # Fields for serialization
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20, write_only=True)

    # Specify the user's fields used for serialization
    class Meta:
        model = CustomUser
        fields = ['email', 'password']

        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}}
        }
```

## `serializers.py`

Este archivo define cómo se deben serializar y validar los datos de entrada cuando un usuario intenta iniciar sesión.

```python
# System Utils
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from apps.authentication.models import CustomUser

# Serializer for login
class SignInAccountSerializer(serializers.ModelSerializer):

    # Fields for serialization
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20, write_only=True)

    # Specify the user's fields used for serialization
    class Meta:
        model = CustomUser
        fields = ['email', 'password']

        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}}
        }

```

## Explicación de la Configuración en `settings.py` y su Relación con `views.py` y `serializers.py`

### Adición de `'rest_framework.authtoken'` a `INSTALLED_APPS`

```python
THIRD_APPS = [
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
]
```

### `'rest_framework.authtoken'`

Este módulo proporciona un sistema de autenticación basado en tokens para Django Rest Framework (DRF). Al incluirlo en `INSTALLED_APPS`, habilitas la funcionalidad que permite generar y manejar tokens de autenticación para usuarios en tu aplicación. Estos tokens son utilizados para autenticar a los usuarios en lugar de las credenciales tradicionales (usuario y contraseña) en solicitudes posteriores.

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication'],
}
```

### `DEFAULT_AUTHENTICATION_CLASSES`

Aquí estás definiendo que el método predeterminado de autenticación para tu API será `TokenAuthentication`. Esto significa que cualquier vista que utilice la autenticación requerirá que el cliente proporcione un token de autenticación en las solicitudes para verificar la identidad del usuario.

### Relación con el Código en `views.py` y `serializers.py`

#### En `views.py`

En la clase `SignInAccountView`, después de que un usuario ha sido autenticado con éxito mediante su correo electrónico y contraseña, se genera un **token** con el siguiente código:

```python
# Check if login is successful
if user:
    # Delete existing token if it exists
    Token.objects.filter(user=user).delete()

    # Create a new token
    token = Token.objects.create(user=user)

    # Return custom message
    return Response(
        {
            "success": True,
            "message": _('You have successfully signed in.'),
            "user": {
                "user_id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "token": token.key
            }
        },
        status=status.HTTP_201_CREATED
    )
```

### Generación de Token

- El token se genera utilizando el modelo `Token` que proviene de `rest_framework.authtoken.models`. Este token se asocia al usuario que ha iniciado sesión y se envía al cliente como parte de la respuesta JSON.

### Autenticación en Solicitudes Futuras

- Una vez que el cliente recibe el token, lo incluirá en el encabezado de las solicitudes futuras para autenticarse. La configuración de `TokenAuthentication` en `DEFAULT_AUTHENTICATION_CLASSES` asegura que DRF utilice este token para validar la identidad del usuario en todas las solicitudes autenticadas.

### En `serializers.py`

- El archivo `serializers.py` no interactúa directamente con los tokens, pero es fundamental para validar las credenciales del usuario (correo electrónico y contraseña) antes de generar el token en `views.py`.


```python
class SignInAccountSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password']

```
### Validación de Credenciales

- `SignInAccountSerializer` asegura que los datos proporcionados por el usuario (correo electrónico y contraseña) sean válidos. Solo después de esta validación, el usuario puede ser autenticado en `views.py` y se puede generar un token.

### Resumen

- **`rest_framework.authtoken`:** Proporciona la funcionalidad de autenticación basada en tokens.
- **`TokenAuthentication`:** Se utiliza como el método predeterminado de autenticación en tu API, lo que requiere que los usuarios proporcionen un token en las solicitudes autenticadas.

### Relación con `views.py` y `serializers.py`

- **`views.py`:** Maneja la autenticación de usuarios y genera tokens tras la validación exitosa de credenciales, mientras que `serializers.py` valida esas credenciales.

Esta configuración permite que tu API utilice tokens como método seguro de autenticación, protegiendo las rutas y asegurando que solo los usuarios autenticados puedan acceder a los recursos protegidos.


> python manage.py makemigrations
> python manage.py migrate

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

### `django_ratelimit`

`django_ratelimit` es una librería para Django que implementa la funcionalidad de limitación de tasas (rate limiting) en las vistas de tu aplicación web. La limitación de tasas es una técnica que se utiliza para controlar el número de solicitudes que un usuario o cliente puede hacer a una API o servicio en un período de tiempo determinado. Esto es útil para prevenir abusos como ataques de fuerza bruta, DDoS, o simplemente para limitar el uso excesivo de un recurso.

#### Funcionalidades Clave:

- **Configuración Sencilla**: Te permite aplicar la limitación de tasas fácilmente a las vistas de Django mediante decoradores o middleware.
- **Personalización**: Puedes configurar los límites de tasa por IP, por usuario autenticado, o basados en cualquier criterio que necesites.
- **Integración**: Se integra de manera nativa con las vistas de Django, lo que permite una implementación rápida y eficiente.

#### Ejemplo de Uso:

Una vez instalada, puedes usar `django_ratelimit` en tus vistas para limitar la cantidad de solicitudes:

```python
from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='5/m', method='POST', block=True)
def my_view(request):
    # Esta vista solo permitirá 5 solicitudes POST por minuto desde la misma IP.
    ...
```

### Explicación de la Línea de Código:

```python
@method_decorator(ratelimit(key='ip', rate='5/m', block=True))
```

### ¿Qué es lo que hace?

Esta línea de código utiliza el decorador `@method_decorator` de Django para aplicar la funcionalidad de limitación de tasa (rate limiting) proporcionada por `django_ratelimit` a un método en una clase de vista basada en Django Rest Framework.

### Componentes de la Línea:

- **`@method_decorator`**:
  - Este es un decorador que permite aplicar otros decoradores a métodos dentro de clases en Django. En este caso, se utiliza para aplicar el decorador `ratelimit` a la función `post` dentro de la clase `SignInAccountView`.

- **`ratelimit`**:
  - Este es el decorador proporcionado por la librería `django_ratelimit`. Se utiliza para limitar la cantidad de solicitudes que se pueden hacer a una vista específica desde una misma fuente (por ejemplo, la misma dirección IP) en un período de tiempo determinado.

### Parámetros del Decorador `ratelimit`:

- **`key='ip'`**:
  - Define la clave por la cual se aplicará la limitación de tasa. En este caso, `ip` significa que las solicitudes se limitarán por la dirección IP del cliente.

- **`rate='5/m'`**:
  - Establece el límite de la tasa de solicitudes. Aquí, `'5/m'` indica que solo se permiten 5 solicitudes por minuto desde la misma dirección IP.

- **`block=True`**:
  - Si se establece en `True`, las solicitudes que excedan el límite configurado serán bloqueadas automáticamente y no se procesarán. El servidor responderá con un error `429 Too Many Requests`.

### ¿Cómo se Aplica en el Contexto de `SignInAccountView`?

En el contexto de la vista `SignInAccountView`, esta línea asegura que cualquier cliente (identificado por su dirección IP) solo pueda intentar iniciar sesión hasta 5 veces por minuto. Si un cliente excede este límite, las solicitudes adicionales se bloquearán automáticamente, evitando posibles ataques de fuerza bruta o abusos en el sistema de inicio de sesión.

### Beneficios de Utilizar `ratelimit`:

- **Seguridad**: Protege tu aplicación de intentos masivos de inicio de sesión (por ejemplo, ataques de fuerza bruta).
- **Control de Abuso**: Evita que un solo usuario sobrecargue tu sistema con demasiadas solicitudes en un corto período de tiempo.
- **Facilidad de Implementación**: Se integra fácilmente en las vistas existentes mediante el uso de decoradores.

### Resumen

Esta línea de código es crucial para implementar una capa de seguridad adicional en tu aplicación, asegurando que las operaciones sensibles, como el inicio de sesión, estén protegidas contra abusos y ataques.


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

```bash

> mkdir frontend/src/views/auth
> mkdir frontend/src/views/dashboard


views
├── auth
│   ├── RegistrationView.vue
│   └── SignInView.vue
└── dashboard
    └── MainView.vue
```


## Explicación del Código

Este código implementa un formulario de inicio de sesión utilizando Vue 3 con TypeScript, Vuetify para el diseño de la interfaz de usuario, y Vuelidate para la validación de formularios. A continuación, se describe qué hace cada parte del código:

### Script Setup (`<script setup lang="ts">`)

#### **Importaciones**

- **`reactive`, `watch`, `onUnmounted`**:
  - Estas funciones de Vue 3 permiten crear referencias reactivas, observar cambios en los datos y limpiar recursos cuando se desmonta el componente.

- **`useRouter`**:
  - Importado desde `vue-router`, se utiliza para redirigir al usuario a diferentes rutas en la aplicación.

- **`useVuelidate`**:
  - Una función que activa la validación de formularios utilizando las reglas definidas.

- **`required`, `email`**:
  - Validadores de Vuelidate que aseguran que los campos sean obligatorios y tengan un formato de correo electrónico válido.

- **`useAuth`**:
  - Un composable personalizado que maneja la lógica de autenticación del usuario.

#### **Estado Reactivo**

```typescript
const initialState = {
  email: '',
  password: ''
};

const state = reactive({
  ...initialState,
});
```

### `initialState`

- Define los valores iniciales para los campos del formulario. Esto sirve como la estructura básica y los valores predeterminados para los datos que el usuario ingresará.

### `state`

- Convierte los valores iniciales en un objeto reactivo utilizando `reactive` de Vue 3. Esto significa que cualquier cambio en `state` se reflejará automáticamente en la interfaz de usuario, permitiendo una actualización en tiempo real del formulario basado en los datos ingresados por el usuario.

### Reglas de Validación
- Define las reglas que se aplican a los campos del formulario, como asegurar que el correo electrónico tenga un formato válido y que la contraseña sea un campo obligatorio. Estas reglas son esenciales para garantizar que los datos enviados sean correctos y completos.


```typescript
const rules = {
  email: { required, email },
  password: { required }
};

const v$ = useVuelidate(rules, state);

```

### `rules`

- Define las reglas de validación para los campos del formulario. `email` debe ser un correo electrónico válido y `password` es un campo obligatorio.

### `v$`

- Es la instancia de Vuelidate que se encarga de validar los datos del formulario en base a las reglas definidas en `rules`.

### Manejo de Autenticación y Redirección

- Se manejan las operaciones de autenticación y la lógica de redirección después de un inicio de sesión exitoso o en caso de error.



```typescript
const { authRequest, successMessage, errorMessage, isLoading } = useAuth();
const router = useRouter();
let timeoutId;

```
### `authRequest`, `successMessage`, `errorMessage`, `isLoading`

- Estos son valores y métodos devueltos por el composable `useAuth`, que maneja la lógica de autenticación.

### `router`

- Se utiliza para redirigir al usuario después de un inicio de sesión exitoso.

### `timeoutId`

- Almacena el ID del temporizador que se utiliza para retrasar la redirección.

### Manejo del Envío del Formulario

- Contiene la lógica para manejar el envío del formulario, incluyendo validaciones y la solicitud de autenticación.

```typescript
const handleSubmit = async () => {
  if (v$.value.$invalid) {
    return;
  }

  authRequest(import.meta.env.VITE_APP_API_URL + 'api/auth/sign-in', state);
};

```

### `handleSubmit`

- Esta función se activa cuando se envía el formulario. Verifica si el formulario es válido antes de intentar autenticar al usuario. Si la validación es exitosa, llama a `authRequest` para autenticar al usuario.



```typescript
watch(successMessage, () => {
  timeoutId = setTimeout(() => {
    router.push('/dashboard');
  }, 2000);
});

```
### `watch(successMessage, ...)`

- Observa los cambios en `successMessage`. Si el mensaje de éxito cambia (lo que indica un inicio de sesión exitoso), se configura un temporizador para redirigir al usuario al dashboard después de 2 segundos.




```typescript
onUnmounted(() => {
  if (timeoutId) {
    clearTimeout(timeoutId);
  }
});

```
### `onUnmounted`

- Se asegura de que el temporizador se cancele si el componente se desmonta antes de que expire el temporizador, evitando posibles errores.


```typescript
<template>
  <v-main>
    <v-container>
      <form @submit.prevent="handleSubmit">
        <!-- Form fields and layout -->
      </form>
    </v-container>
  </v-main>
</template>

```
### Template (`<template>`)

- Este bloque define la estructura visual del formulario utilizando componentes de Vuetify.

#### Formulario

- El formulario incluye campos para `email` y `password`, con validación en tiempo real. Al enviar el formulario, se llama a `handleSubmit`.

#### Botones y Mensajes

- Incluye un botón de envío que muestra un indicador de carga si `isLoading` es `true`. También muestra mensajes de éxito o error basados en los valores de `successMessage` y `errorMessage`.


```typescript
<style>
@import '@/assets/styles/auth/_main.scss';
</style>

```

### Estilo (`<style>`)

#### `@import`

- Importa estilos específicos para el formulario de autenticación desde un archivo SCSS.

### Resumen

- Este código configura un formulario de inicio de sesión con validación, manejo de estado reactivo, y autenticación, integrando la lógica de redirección y limpieza de recursos para asegurar una experiencia de usuario fluida y segura.

## SignInView.vue
```typescript
<script setup lang="ts">
// System Utils
import { reactive, watch, onUnmounted } from 'vue';

// Installed Utils
import { useRouter } from 'vue-router';
import { useVuelidate } from '@vuelidate/core';
import { required, email } from '@vuelidate/validators';

// App Utils
import { useAuth } from '@/composables/useAuth';

// Default fields value
const initialState = {
  email: '',
  password: ''
}

// Make the fields reactive
const state = reactive({
  ...initialState,
});

// Rules for Vuelidate
const rules = {
  email: { required, email },
  password: { required }
}

// Configure Vuelidate
const v$ = useVuelidate(rules, state);

// Use auth variables
const { authRequest, successMessage, errorMessage, isLoading } = useAuth();

// Use the router
const router = useRouter();

// Timeout ID for cleanup
let timeoutId;

// Handle the form submit
const handleSubmit = async () => {

  // Verify if errors exists
  if (v$.value.$invalid) {
    return;
  }

  // Register the user
  authRequest(import.meta.env.VITE_APP_API_URL + 'api/auth/sign-in', state);

};

// Watch the successMessage for message change
watch(successMessage, () => {
  // Wait for 2 seconds
  timeoutId = setTimeout(() => {
    router.push('/dashboard');
  }, 2000);
});

// Cleanup on component unmount
onUnmounted(() => {
  if (timeoutId) {
    clearTimeout(timeoutId);
  }
});

</script>
<template>
    <v-main>
      <v-container>
        <form @submit.prevent="handleSubmit">
          <v-row>
            <v-col cols="12">
              <h3>{{ $t('sign_in_to_my_app') }}</h3>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <v-text-field
                v-model="state.email"
                :error-messages="v$.email.$errors.map((e) => e.$message)"
                :label="$t('email')"
                required
                variant="outlined"
                autocomplete="new-email"
                @blur="v$.email.$touch"
                @input="v$.email.$touch"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <v-text-field
                type="password",
                v-model="state.password"
                :counter="20"
                :error-messages="v$.password.$errors.map((e) => e.$message)"
                :label="$t('password')"
                variant="outlined"
                autocomplete="new-password"
                @blur="v$.password.$touch"
                @input="v$.password.$touch"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row class="mb-0">
            <v-col cols="6">
              <v-checkbox v-model="state.rememberMe" :label="$t('remember_me')"></v-checkbox>
            </v-col>
            <v-col cols="6" class="text-right">
              <router-link to="/reset-password" class="auth-reset-password">
                {{ $t('forgot_password') }}
              </router-link>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <v-btn
                type="submit"
                class="auth-btn"
                @click="v$.$validate"
                :class="{ 'auth-submitting-active-btn': isLoading }"
              >
                {{ $t('sign_in') }}
                <span class="mdi mdi-arrow-right-bold auth-main-form-submit-icon"></span>
                <span class="mdi mdi-cached rotate-animation auth-main-form-submitting-icon"></span>
              </v-btn>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <div class="auth-main-form-alerts">
                <div
                  class="auth-main-form-alert-success top-to-bottom-animation"
                  role="alert"
                  v-if="successMessage"
                >
                  <span class="mdi mdi-bell-outline auth-main-form-alert-success-icon"></span>
                  <p>{{ successMessage }}</p>
                </div>
                <div
                  class="auth-main-form-alert-error top-to-bottom-animation"
                  role="alert"
                  v-else-if="errorMessage"
                >
                  <span class="mdi mdi-bell-outline auth-main-form-alert-error-icon"></span>
                  <p>{{ errorMessage }}</p>
                </div>
              </div>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <div class="auth-additional-link">
                <p>
                  {{ $t('dont_have_an_account') }}
                  <router-link to="/registration" class="inline-block auth-main-form-reset-link">
                    {{ $t('register_an_account') }}
                  </router-link>
                </p>
              </div>
            </v-col>
          </v-row>
        </form>
      </v-container>
    </v-main>
  </template>
  <style>
  @import '@/assets/styles/auth/_main.scss';
  </style>

```

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

> pip install python-decouple

> sudo npm install dompurify

> sudo npm install @vueuse/head