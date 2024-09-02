<template>
    <section id="menu_personalizado">
      <div class="wrapper_personalizado">
        <div class="logo-container">
          <div class="logo_personalizado">
            <router-link to="/">
              Aurora Kestrel Language
            </router-link>
          </div>
        </div>

        <div class="nav-container">
          <ul class="nav-links_personalizado">
            <li class="nav-item" :class="{ active: isActiveRoute('/') }">
              <router-link to="/">{{ $t('home') }}</router-link>
            </li>
            <li class="nav-item" :class="{ active: isActiveRoute('/authentication/login') }">
              <router-link to="/authentication/login">{{ $t('sign_in') }}</router-link>
            </li>
            <li class="nav-item" :class="{ active: isActiveRoute('/registration') }">
              <router-link to="/registration">{{ $t('register_an_account') }}</router-link>
            </li>
            <li class="nav-item" :class="{ active: isActiveRoute('/reset-password') }">
              <router-link to="/reset-password">{{ $t('forgot_password') }}</router-link>
            </li>

            <!-- Selector de Idioma -->
            <li class="nav-item">
              <div class="language-selector">
                <select id="language-select" @change="changeLanguage($event)" :value="currentLanguage">
                  <option value="en-US">English</option>
                  <option value="es-LA">Español</option>
                </select>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </section>
  </template>

<script setup lang="ts">
import { useI18n } from 'vue-i18n';
import { useRouter } from 'vue-router';
import { computed } from 'vue';

const { locale } = useI18n();
const router = useRouter();

const currentLanguage = locale.value;

function changeLanguage(event: Event) {
    const selectedLanguage = (event.target as HTMLSelectElement).value;
    locale.value = selectedLanguage;
    localStorage.setItem('language', selectedLanguage);
}

function isActiveRoute(path: string) {
    return computed(() => router.currentRoute.value.path === path).value;
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
}

/* Menú personalizado */
#menu_personalizado {
    z-index: 999;
    background: #242526;
    height: 120px;
    padding-top: 20px;
    position: relative;
    width: 100%;
}

.wrapper_personalizado {
    position: relative;
    width: 100%;
    height: 70px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.logo-container {
    position: absolute;
    left: 30px;
}

.nav-container {
    position: absolute;
    right: 30px;
    display: flex;
    align-items: center;
}

.nav-links_personalizado {
    display: flex;
    align-items: center;
    list-style: none;
    margin: 0;
    padding: 0;
}

.nav-links_personalizado li {
    margin-left: 10px;
}

.nav-links_personalizado li a {
    color: #f2f2f2;
    text-decoration: none;
    font-size: 22px;
    font-weight: 600;
    padding: 5px 10px;
    border-radius: 5px;
    transition: all 0.3s ease;
}

.nav-links_personalizado li a:hover {
    background: #3a3b3c;
}

/* Color de la página seleccionada */
.nav-item.active a {
    color: #ff561e;
}

/* Estilo para Aurora Kestrel Language */
.logo_personalizado a {
    color: #f2f2f2;
    font-size: 30px;
    font-weight: 700;
    text-decoration: none;
    transition: color 0.3s ease;
}

.logo_personalizado a:hover {
    color: #ff561e;
}

/* Selector de idioma estilizado como los enlaces de navegación */
.language-selector select {
    color: #f2f2f2;
    background: transparent;
    border: none;
    font-size: 22px;
    font-weight: 600;
    padding: 5px 10px;
    border-radius: 5px;
    transition: all 0.3s ease;
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    text-align-last: center;
}

.language-selector select:hover {
    background: #3a3b3c;
}

/* Estilo para el desplegable */
.language-selector select option {
    background: #0f1425;
    color: #f2f2f2;
}
</style>
