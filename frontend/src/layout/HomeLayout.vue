<template>
  <v-app :theme="theme">
    <v-app-bar app dense color="#152763">
      <v-toolbar-title class="white--text">Aurora Kestrel Language</v-toolbar-title>
      <v-spacer></v-spacer>

      <!-- Botones en pantallas grandes -->
      <v-btn
        text
        class="d-none d-md-flex"
        :class="{ 'selected-link': isActive('/dashboard') }"
        @click="navigateTo('/dashboard')"
      >
        {{ $t('menu_home.Home') }}
      </v-btn>
      <v-btn
        text
        class="d-none d-md-flex"
        :class="{ 'selected-link': isActive('/dashboard/skill-practice') }"
        @click="navigateTo('/dashboard/skill-practice')"
      >
        {{ $t('menu_home.Skill Practice') }}
      </v-btn>
      <v-btn
        text
        class="d-none d-md-flex"
        :class="{ 'selected-link': isActive('/dashboard/skill-builder') }"
        @click="navigateTo('/dashboard/skill-builder')"
      >
        {{ $t('menu_home.Skill Builder') }}
      </v-btn>
      <v-btn
        text
        class="d-none d-md-flex"
        :class="{ 'selected-link': isActive('/dashboard/progress-tracking') }"
        @click="navigateTo('/dashboard/progress-tracking')"
      >
        {{ $t('menu_home.Progress Tracking') }}
      </v-btn>
      <v-btn
        text
        class="d-none d-md-flex"
        :class="{ 'selected-link': isActive('/dashboard/about') }"
        @click="navigateTo('/dashboard/about')"
      >
        {{ $t('menu_home.About') }}
      </v-btn>
      <v-btn
        text
        class="d-none d-md-flex"
        :class="{ 'selected-link': isActive('/dashboard/contact') }"
        @click="navigateTo('/dashboard/contact')"
      >
        {{ $t('menu_home.Contact') }}
      </v-btn>

      <!-- Selector de idioma -->
      <div class="language-selector d-none d-md-flex">
        <select
          id="language-select"
          @change="changeLanguage"
          v-model="currentLanguage"
          :class="[theme === 'dark' ? 'dark-text' : 'light-text']"
        >
          <option value="en-US">English</option>
          <option value="es-LA">Español</option>
        </select>
      </div>

      <!-- Botón Luna/Sol para cambiar de tema -->
      <v-btn icon @click="toggleTheme" class="white--text">
        <v-icon>{{ theme === 'dark' ? 'mdi-weather-night' : 'mdi-weather-sunny' }}</v-icon>
      </v-btn>

      <!-- Menú para pantallas pequeñas -->
      <v-btn icon @click="drawer = true" class="d-flex d-md-none white--text">
        <v-icon>mdi-menu</v-icon>
      </v-btn>
    </v-app-bar>

    <!-- Menú lateral (sidebar) -->
    <v-navigation-drawer v-model="drawer" app temporary absolute color="#0c32e6">
      <v-list>
        <v-list-item @click="navigateTo('/dashboard')">
          <v-list-item-title :class="{ 'selected-link': isActive('/dashboard') }">{{ $t('menu_home.Home') }}</v-list-item-title>
        </v-list-item>
        <v-list-item @click="navigateTo('/dashboard/skill-practice')">
          <v-list-item-title :class="{ 'selected-link': isActive('/dashboard/skill-practice') }">{{ $t('menu_home.Skill Practice') }}</v-list-item-title>
        </v-list-item>
        <v-list-item @click="navigateTo('/dashboard/skill-builder')">
          <v-list-item-title :class="{ 'selected-link': isActive('/dashboard/skill-builder') }">{{ $t('menu_home.Skill Builder') }}</v-list-item-title>
        </v-list-item>
        <v-list-item @click="navigateTo('/dashboard/progress-tracking')">
          <v-list-item-title :class="{ 'selected-link': isActive('/dashboard/progress-tracking') }">{{ $t('menu_home.Progress Tracking') }}</v-list-item-title>
        </v-list-item>
        <v-list-item @click="navigateTo('/dashboard/about')">
          <v-list-item-title :class="{ 'selected-link': isActive('/dashboard/about') }">{{ $t('menu_home.About') }}</v-list-item-title>
        </v-list-item>
        <v-list-item @click="navigateTo('/dashboard/contact')">
          <v-list-item-title :class="{ 'selected-link': isActive('/dashboard/contact') }">{{ $t('menu_home.Contact') }}</v-list-item-title>
        </v-list-item>

        <!-- Selector de idioma para pantallas pequeñas -->
        <v-list-item>
          <select
            v-model="currentLanguage"
            @change="changeLanguage"
            style="color: white !important;"
          >
            <option value="en-US">English</option>
            <option value="es-LA">Español</option>
          </select>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <!-- Contenido principal -->
    <v-main>
      <div class="home-content">
        <router-view />
      </div>
    </v-main>

    <!-- Footer -->
    <v-footer app>
      <span>&copy; 2024 Aurora Kestrel Language. All rights reserved.</span>
    </v-footer>
  </v-app>
</template>

<script setup lang="ts">
import { ref, watchEffect } from 'vue';
import { useI18n } from 'vue-i18n';
import { useRouter } from 'vue-router';

const { locale } = useI18n();
const router = useRouter();
const drawer = ref(false);
const theme = ref('dark'); // Inicializa el tema en modo oscuro

const languages = [
  { value: 'en-US', text: 'English' },
  { value: 'es-LA', text: 'Español' },
];

const currentLanguage = ref(locale.value);

watchEffect(() => {
  locale.value = currentLanguage.value;
});

function changeLanguage(event: Event) {
  const selectedLanguage = (event.target as HTMLSelectElement).value;
  currentLanguage.value = selectedLanguage;
  localStorage.setItem('language', selectedLanguage);
}

function navigateTo(route: string) {
  router.push(route);
}

function isActive(route: string) {
  return router.currentRoute.value.path === route;
}

function toggleTheme() {
  theme.value = theme.value === 'dark' ? 'light' : 'dark';
}
</script>

<style scoped>
.language-selector {
  margin-right: 16px;
}

#language-select {
  padding: 4px;
  font-size: 14px;
  color: white;
}

.language-selector select {
  background: transparent;
  border: none;
  font-size: 22px;
  font-weight: 600;
  padding: 5px 10px;
  border-radius: 5px;
  transition: all 0.3s ease;
  appearance: none;
  text-align-last: center;
}

.language-selector select:hover {
  background: #3a3b3c;
}

/* Clases dinámicas para cambiar color según el tema */
.dark-text {
  color: white;
}

.light-text {
  color: black;
}

.home-content {
  padding-top: 16px;
}

.selected-link {
  color: #f66b37 !important;
}

/* Estilos adicionales para el fondo del menú desplegable */
select {
  background-color: inherit; /* Utiliza el color de fondo actual */
}

option {
  background-color: white;
  color: black;
}

.dark-text option {
  background-color: black;
  color: white;
}

.light-text option {
  background-color: white;
  color: black;
}
</style>
