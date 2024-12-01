<template>
  
    <!-- Título principal -->
    <v-row>
      <v-col cols="12">
        <h1 class="text-center mb-5">Construye tu Roadmap para Aprender Inglés</h1>
      </v-col>
    </v-row>

    <!-- Preguntas -->
    <v-row v-for="(question, index) in questions" :key="index" class="mb-5">
      <v-col cols="12" md="2"></v-col>
      <v-col cols="12" md="8">
        <h4 class="mb-3">{{ index + 1 }}. {{ question.label }}</h4>
        <v-textarea
          v-model="answers[index]"
          :label="question.placeholder"
          outlined
          rows="5"
          :placeholder="question.example"
          @input="limitCharacters(index)"
        ></v-textarea>
        <!-- Contador de caracteres -->
        <p class="text-right text-muted">{{ answers[index].length }} / 100</p>
      </v-col>
      <v-col cols="12" md="2"></v-col>
    </v-row>

    <!-- Botón de enviar -->
    <v-row>
      <v-col cols="12" class="text-center">
        <v-btn color="primary" class="mt-4" @click="submitAnswers">Enviar Respuestas</v-btn>
      </v-col>
    </v-row>

    <!-- Respuesta del roadmap -->
    <v-row v-if="roadmap" class="mt-5">
      <v-col cols="12" md="2"></v-col>
      <v-col cols="12" md="8">
        <h3 class="mb-4">Tu mensaje de motivación y Roadmap:</h3>
        <v-card>
          <v-card-text>
            <pre>{{ roadmap }}</pre>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" md="2"></v-col>
    </v-row>
  
</template>

<script setup lang="ts">
import { ref } from "vue";
import axios from "axios";

// Lista de preguntas
const questions = [
  {
    label: "¿Cuál es la razón principal por la que deseas aprender inglés?",
    placeholder: "Ejemplo: Trabajo, Estudios, Viajar, Placer personal...",
    example: "Escribe algo como: 'Quiero mejorar mis habilidades para entrevistas de trabajo'.",
  },
  {
    label: "¿Qué esperas lograr en los próximos 6 meses?",
    placeholder: "Ejemplo: Mejorar en entrevistas de trabajo, Viajar y comunicarme con facilidad...",
    example: "Escribe algo como: 'Quiero poder dar una presentación en inglés en mi empresa'.",
  },
  {
    label: "Imagina que dominas este idioma. ¿Qué harías primero?",
    placeholder: "Ejemplo: Postularme a un trabajo internacional, Tener una conversación fluida...",
    example: "Escribe algo como: 'Me postularía a trabajos en empresas internacionales'.",
  },
];

// Respuestas del usuario
const answers = ref(["", "", ""]);
const roadmap = ref(""); // Aquí se almacena la respuesta del backend

// Función para enviar respuestas al backend
const submitAnswers = async () => {
  try {
    const response = await axios.post("http://localhost:8000/user/roadmap-motivation/", {
      answers: answers.value,
    });
    roadmap.value = response.data.roadmap; // Almacena el roadmap devuelto
  } catch (error) {
    console.error("Error al obtener el roadmap:", error);
    roadmap.value = "Hubo un error al generar el roadmap. Intenta de nuevo.";
  }
};

// Función para limitar la longitud de los caracteres
const limitCharacters = (index: number) => {
  if (answers.value[index].length > 100) {
    answers.value[index] = answers.value[index].slice(0, 100);
  }
};
</script>

<style scoped>
.text-muted {
  font-size: 0.9rem;
}
</style>
