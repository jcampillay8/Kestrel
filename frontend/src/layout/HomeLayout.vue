<!-- src/layout/HomeLayout.vue -->
<template>
    <v-app class="home-layout">
      <v-navigation-drawer app>
        <!-- Contenido del menú lateral (navigation drawer) -->
        <v-list>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>{{ $t('home') }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <!-- Agrega más ítems de navegación aquí -->
        </v-list>
      </v-navigation-drawer>
  
      <v-app-bar app>
        <!-- Contenido de la barra superior -->
        <v-toolbar-title>My App</v-toolbar-title>
  
        <!-- Selector de idioma -->
        <v-spacer></v-spacer>
        <v-select
          v-model="selectedLocale"
          :items="locales"
          item-text="text"
          item-value="value"
          @change="changeLocale"
          label="Language"
          hide-details
          dense
          outlined
        ></v-select>
      </v-app-bar>
  
      <v-main>
        <v-container class="home-content">
          <router-view />
        </v-container>
      </v-main>
  
      <v-footer app>
        <!-- Contenido del pie de página -->
        <span>&copy; 2024 My App</span>
      </v-footer>
    </v-app>
  </template>
  
  <script setup>
  import { useI18n } from 'vue-i18n';
  import { ref } from 'vue';
  
  // Uso del composable de internacionalización
  const { locale } = useI18n();
  
  // Locales disponibles
  const locales = ref([
    { text: 'English', value: 'en' },
    { text: 'Español', value: 'es-LA' }
  ]);
  
  // Variable reactiva para almacenar el idioma seleccionado
  const selectedLocale = ref(locale.value);
  
  // Función para cambiar el idioma
  const changeLocale = (newLocale) => {
    locale.value = newLocale;
    localStorage.setItem('selectedLocale', newLocale); // Guardar la selección en el localStorage para persistirla
  };
  
  // Recuperar el idioma seleccionado al cargar el componente
  if (localStorage.getItem('selectedLocale')) {
    selectedLocale.value = localStorage.getItem('selectedLocale');
    changeLocale(selectedLocale.value);
  }
  </script>
  
  <style scoped>
  .home-layout {
    display: flex;
    min-height: 100vh;
  }
  
  .home-content {
    padding-top: 16px;
  }
  </style>
  