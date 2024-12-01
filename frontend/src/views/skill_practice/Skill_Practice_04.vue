<template>
  <v-row justify="center">
    <v-col cols="12" md="10">
      <h1 class="my-3 text-h3">Generador y Evaluador de Oraciones</h1>

      <!-- Botón para generar una oración -->
      <v-btn
        color="primary"
        class="mb-3"
        :disabled="loading"
        @click="crearOracion"
      >
        Crear Oración Aleatoria
      </v-btn>

      <!-- Mostrar Tema Seleccionado -->
      <div v-if="temaSeleccionado" class="mb-3 text-h6 font-weight-bold">
        <strong>Tema seleccionado:</strong> {{ temaSeleccionado }}
      </div>

      <!-- Mostrar Relación Seleccionada -->
      <div v-if="relacionSeleccionada" class="mb-3 text-h6 font-weight-bold">
        <strong>Relación seleccionada:</strong> {{ relacionSeleccionada }}
      </div>

      <!-- Mostrar Oración Generada -->
      <div v-if="oracionGenerada" class="mb-3 text-h5">
        <strong>Oración generada:</strong> {{ oracionGenerada }}
      </div>

      <v-textarea
        v-model="respuestaAlumno"
        outlined
        placeholder="Traduce la oración al inglés"
        class="mb-3 large-textarea"
        :disabled="loading"
      ></v-textarea>

      <!-- Botón para revisar la traducción -->
      <v-btn
        color="success"
        class="mb-3"
        :disabled="!oracionGenerada || !respuestaAlumno || loading"
        @click="revisarTraduccion"
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

      <!-- Resultados -->
      <v-card class="mt-4" v-if="resultadoRevision">
        <v-card-title class="text-h6 font-weight-bold">
          Puntaje y Feedback
        </v-card-title>
        <v-card-text>
          <p class="text-h6"><strong>Diferencias resaltadas:</strong></p>
          <div v-html="resultadoRevision.highlightedDiff" class="text-h6"></div>
          <br />
          <p class="text-h6"><strong>Puntaje:</strong> {{ resultadoRevision.score }}/10</p>
          <br />
          <pre class="text-h6">{{ resultadoRevision.key_areas }}</pre>
          <br />
          <p class="text-h6">{{ resultadoRevision.note }}</p>
          <br />
          <p class="text-h6"><strong>Feedback:</strong> {{ resultadoRevision.feedback }}</p>

        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      temaSeleccionado: "",
      relacionSeleccionada: "",
      oracionGenerada: "",
      respuestaAlumno: "",
      resultadoRevision: null,
      loading: false, // Estado de carga
    };
  },
  methods: {
    async crearOracion() {
      try {
        this.loading = true; // Inicia el estado de carga
        const response = await axios.post(
          "http://127.0.0.1:8000/skill_builder/crear-oracion/"
        );
        this.temaSeleccionado = response.data.tema_seleccionado;
        this.relacionSeleccionada = response.data.relacion_seleccionada;
        this.oracionGenerada = response.data.oracion_generada;
        this.respuestaAlumno = ""; // Reinicia el campo de respuesta
        this.resultadoRevision = null; // Limpia los resultados previos
      } catch (error) {
        console.error("Error al crear la oración:", error);
        alert("Hubo un error al crear la oración. Inténtalo nuevamente.");
      } finally {
        this.loading = false; // Finaliza el estado de carga
      }
    },
    async revisarTraduccion() {
      try {
        this.loading = true; // Inicia el estado de carga
        const response = await axios.post(
          "http://127.0.0.1:8000/skill_builder/revisar-traduccion/",
          {
            oracion_generada: this.oracionGenerada,
            respuesta_alumno: this.respuestaAlumno,
          }
        );
        this.resultadoRevision = {
          score: response.data.score,
          feedback: response.data.feedback,
          highlightedDiff: response.data.highlighted_diff,
          key_areas: response.data.key_areas,
          note: response.data.note,
        };
      } catch (error) {
        console.error("Error al revisar la traducción:", error);
        alert("Hubo un error al revisar la traducción. Inténtalo nuevamente.");
      } finally {
        this.loading = false; // Finaliza el estado de carga
      }
    },
  },
};
</script>

<style>
.font-weight-bold {
  font-weight: bold;
}
.large-textarea textarea {
  font-size: 1.25rem; /* Aumenta el tamaño del texto */
  line-height: 2rem; /* Ajusta el interlineado si es necesario */
}
</style>
