<template>
    <v-row>
      <!-- Columna vacía a la izquierda -->
      <v-col cols="12" md="1"></v-col>
  
      <!-- Columna principal con las cards -->
      <v-col cols="12" md="10">
        <!-- Cuadro de búsqueda y filtros -->
        <v-row class="mb-4">
          <v-col cols="12" md="5">
            <v-text-field
              v-model="searchQuery"
              label="Buscar por Title Name, Description, Topic Father o Topic Son"
              outlined
              clearable
              @input="fetchItems"
            ></v-text-field>
          </v-col>
  
          <v-col cols="12" md="3">
            <v-select
              v-model="selectedLanguage"
              :items="languages"
              label="Filtrar por Language"
              outlined
              clearable
              @change="fetchItems"
            ></v-select>
          </v-col>
  
          <v-col cols="12" md="2">
            <v-select
              v-model="selectedCEFR"
              :items="cefrLevels"
              label="Filtrar por CEFR Level"
              outlined
              clearable
              @change="fetchItems"
            ></v-select>
          </v-col>
        </v-row>
  
        <!-- Cards -->
        <v-row>
          <v-col
            v-for="(item, index) in paginatedItems"
            :key="item.id"
            cols="12"
            sm="6"
            md="3"
          >
            <v-card>
              <v-img
                height="200"
                src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
                cover
              ></v-img>
              <v-card-title>{{ item.Title_Name }}</v-card-title>
              <v-card-subtitle>{{ item.Language }} - {{ item.Level_CEFR }}</v-card-subtitle>
              <v-card-text>
                <p>{{ item.Description }}</p>
                <p><strong>{{ item.Topic_Father }}:</strong> {{ item.Topic_Son }}</p>
                <v-rating
                  :model-value="item.rating || 0"
                  color="amber"
                  readonly
                ></v-rating>
                <div>{{ item.number_votes }} votes</div>
              </v-card-text>
              <!-- Botón GO PRACTICE -->
              <v-card-actions>
                <v-btn
                  color="#f66b37"
                  dark
                  :to="{ name: 'Practice', params: { id: item.id } }"
                >
                  GO PRACTICE
                </v-btn>

              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
  
        <!-- Paginación -->
        <v-pagination
          v-if="items.length > itemsPerPage"
          v-model="currentPage"
          :length="pageCount"
          color="primary"
        ></v-pagination>
      </v-col>
  
      <!-- Columna vacía a la derecha -->
      <v-col cols="12" md="1"></v-col>
    </v-row>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        items: [],
        searchQuery: '', // Campo para almacenar la consulta de búsqueda
        selectedLanguage: '', // Filtro de idioma
        selectedCEFR: '', // Filtro de nivel CEFR
        languages: ['Spanish', 'English', 'French', 'German'], // Idiomas disponibles
        cefrLevels: ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'], // Niveles CEFR
        itemsPerPage: 12,
        currentPage: 1,
      };
    },
    computed: {
      pageCount() {
        return Math.ceil(this.items.length / this.itemsPerPage);
      },
      paginatedItems() {
        const start = (this.currentPage - 1) * this.itemsPerPage;
        const end = start + this.itemsPerPage;
        return this.items.slice(start, end);
      },
    },
    methods: {
      fetchItems() {
        const params = {
          search: this.searchQuery,
        };
  
        if (this.selectedLanguage) {
          params.language = this.selectedLanguage;
        }
  
        if (this.selectedCEFR) {
          params.level_cefr = this.selectedCEFR;
        }
  
        axios
          .get('http://localhost:8000/skill_practice/tableform03/', { params })
          .then((response) => {
            if (response.data && Array.isArray(response.data.results)) {
              this.items = response.data.results;
            } else {
              console.error('Unexpected response structure:', response.data);
            }
          })
          .catch((error) => {
            console.error('Error fetching items:', error.response || error.message || error);
          });
      },
      goPractice(item) {
        // Implementa la acción para "GO PRACTICE"
        console.log('GO PRACTICE clicked for:', item);
        // Aquí puedes redirigir al usuario a otra página o iniciar una acción
      },
    },
    mounted() {
      this.fetchItems();
    },
  };
  </script>
  