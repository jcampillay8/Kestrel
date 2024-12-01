<template>
  <v-row>
    <v-col cols="1"></v-col> <!-- Columna vacía a la izquierda -->
    <v-col cols="10">
      <h1 class="my-3">Generador y Evaluador de Oraciones</h1>

      <!-- Expansion Panels -->
      <v-expansion-panels
        v-model="panelActivo"
        class="expansion-panels-width-border"
      >
        <!-- Panel 1: Selectores y Descripción -->
        <v-expansion-panel>
          <v-expansion-panel-title class="custom-panel-title">
            Configuración
          </v-expansion-panel-title>
          <v-expansion-panel-text>
            <!-- Dropdown de Nivel -->
            <v-select
              v-model="selectedNivel"
              :items="niveles"
              label="Selecciona un nivel"
              outlined
            ></v-select>

            <!-- Dropdown de Contenido -->
            <v-select
              v-model="selectedContenido"
              :items="contenidos"
              label="Selecciona un contenido"
              outlined
              v-if="contenidos.length > 0"
            ></v-select>

            <!-- Dropdown de Temas -->
            <v-select
              v-model="selectedTema"
              :items="temas"
              label="Selecciona un tema"
              outlined
            ></v-select>

            <v-textarea
              v-model="descripcion"
              label="Escribe una descripción del tema (máximo 280 caracteres)"
              outlined
              rows="3"
              maxlength="280"
              placeholder="Escribe una descripción del tema (máximo 280 caracteres)"
              class="mt-4"
            ></v-textarea>
          </v-expansion-panel-text>
        </v-expansion-panel>

        <!-- Panel 2: Crear Oración y Evaluación -->
        <v-expansion-panel>
          <v-expansion-panel-title class="custom-panel-title">
            Generación y Evaluación
          </v-expansion-panel-title>
          <v-expansion-panel-text>
            <div class="d-flex align-center mb-3">
              <v-btn @click="crearOracion" color="primary" class="mt-4 mb-3">Crear Oración</v-btn>
            </div>

            <div v-if="oracionGenerada" class="mb-3">
              <p class="large-text">{{ oracionGenerada }}</p>
            </div>

            <v-textarea
              v-model="respuestaAlumno"
              label="Traduce la oración al inglés"
              outlined
              rows="3"
              placeholder="Traduce la oración al inglés"
              class="mb-3"
            ></v-textarea>

            <div class="d-flex align-center mb-3">
              <v-btn
                @click="revisarTraduccion"
                :disabled="disableRevisar"
                color="success"
              >
                Revisar
              </v-btn>
              <!-- Progress Circular -->
              <v-progress-circular
                v-if="loading"
                indeterminate
                color="green"
                class="ml-3"
              ></v-progress-circular>
            </div>

            <!-- Mostrar diferencias resaltadas -->
            <div v-if="highlightedDiff" class="mt-3">
              <p class="large-text" v-html="highlightedDiff"></p>
            </div>

            <!-- Mostrar el Score -->
            <div v-if="score" class="mt-2">
              <p class="large-text"><strong>Score:</strong> {{ score }}</p>
            </div>

            <!-- Mostrar el Feedback -->
            <div v-if="feedback" class="mt-2">
              <p class="large-text"><strong>Feedback:</strong> {{ feedback }}</p>
            </div>
          </v-expansion-panel-text>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-col>
    <v-col cols="1"></v-col> <!-- Columna vacía a la derecha -->
  </v-row>
</template>

<script>
import axios from "axios";
import { ref, onMounted, watch } from "vue";

export default {
  setup() {
    const panelActivo = ref(0); // Por defecto, el primer panel está abierto
    const niveles = ref([]);
    const selectedNivel = ref("");
    const contenidos = ref([]);
    const selectedContenido = ref("");
    const selectedTema = ref("");
    const temas = ref([]);
    const descripcion = ref("");
    const oracionGenerada = ref("");
    const respuestaAlumno = ref("");
    const highlightedDiff = ref(""); // Almacena las diferencias resaltadas
    const score = ref(""); // Almacena el score
    const feedback = ref(""); // Almacena el feedback
    const loading = ref(false); // Controla la visibilidad del Progress Circular
    const disableRevisar = ref(true); // Controla si el botón Revisar está deshabilitado

    const cargarNiveles = () => {
      try {
        axios
          .get("http://localhost:8000/skill_practice/niveles/")
          .then((response) => {
            niveles.value = response.data.map((nivel) => nivel.nombre);
          });
      } catch (error) {
        console.error("Error al cargar niveles:", error);
      }
    };

    const cargarTemas = () => {
      try {
        axios
          .get("http://localhost:8000/skill_practice/temas/")
          .then((response) => {
            temas.value = response.data.map((tema) => tema.value);
          });
      } catch (error) {
        console.error("Error al cargar temas:", error);
      }
    };

    const cargarContenidos = (nivel) => {
      try {
        axios
          .post("http://localhost:8000/skill_practice/contenidos/", { nivel })
          .then((response) => {
            contenidos.value = response.data.map((contenido) => contenido.value);
          });
      } catch (error) {
        console.error("Error al cargar contenidos:", error);
      }
    };

    watch(selectedNivel, (newNivel) => {
      if (newNivel) {
        cargarContenidos(newNivel);
      } else {
        contenidos.value = [];
      }
    });

    const crearOracion = () => {
      // Limpiar las variables antes de enviar la solicitud
      descripcion.value = "";
      respuestaAlumno.value = "";
      highlightedDiff.value = "";
      score.value = ""; // Limpiar el score
      feedback.value = ""; // Limpiar el feedback
      oracionGenerada.value = "";
      disableRevisar.value = false; // Habilitar el botón Revisar

      axios
        .post("http://localhost:8000/skill_practice/crear-oracion/", {
          nivel: selectedNivel.value,
          contenido: selectedContenido.value,
          tema: selectedTema.value,
          descripcion: descripcion.value,
        })
        .then((response) => {
          oracionGenerada.value = response.data.oracion;
        })
        .catch((error) => {
          console.error("Error al crear la oración:", error);
        });
    };

    const revisarTraduccion = () => {
      loading.value = true; // Mostrar el Progress Circular al hacer clic
      disableRevisar.value = true; // Deshabilitar el botón Revisar
      axios
        .post("http://localhost:8000/skill_practice/revisar-traduccion/", {
          oracion_generada: oracionGenerada.value,
          respuesta_alumno: respuestaAlumno.value,
        })
        .then((response) => {
          highlightedDiff.value = response.data.highlighted_diff; // Asignar diferencias resaltadas
          score.value = response.data.score; // Asignar el score
          feedback.value = response.data.feedback; // Asignar el feedback
        })
        .catch((error) => {
          console.error("Error al revisar la traducción:", error);
        })
        .finally(() => {
          loading.value = false; // Ocultar el Progress Circular cuando finalice
        });
    };

    onMounted(() => {
      cargarNiveles();
      cargarTemas();
    });

    return {
      panelActivo,
      niveles,
      selectedNivel,
      contenidos,
      selectedContenido,
      selectedTema,
      temas,
      descripcion,
      oracionGenerada,
      respuestaAlumno,
      highlightedDiff,
      score,
      feedback,
      loading,
      disableRevisar,
      cargarContenidos,
      crearOracion,
      revisarTraduccion,
    };
  },
};
</script>

<style scoped>
.my-3 {
  margin-top: 1rem;
  margin-bottom: 1rem;
}
.mt-4 {
  margin-top: 1.5rem;
}
.mb-3 {
  margin-bottom: 1rem;
}
.expansion-panels-width-border {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 16px;
}
.ml-3 {
  margin-left: 1rem;
}
.custom-panel-title {
  background-color: #161616; /* Fondo oscuro */
  color: #fff; /* Texto blanco */
  padding: 10px;
  border-radius: 5px;
}
.large-text {
  font-size: 1.3rem; /* Incrementar tamaño de texto */
  font-weight: 400; /* Peso del texto */
  line-height: 1.8; /* Espaciado entre líneas */
}
</style>
