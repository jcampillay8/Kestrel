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

      <input type="checkbox" id="menu-toggle" class="menu-toggle" v-model="menuOpen" />
      <label for="menu-toggle" class="menu-icon">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </label>

      <div class="nav-container">
        <ul class="nav-links_personalizado">
          <li class="nav-item" :class="{ active: isActiveRoute('/') }">
            <router-link to="/" @click="closeMenu">{{ $t('home') }}</router-link>
          </li>
          <li class="nav-item" :class="{ active: isActiveRoute('/authentication/login') }">
            <router-link to="/authentication/login" @click="closeMenu">{{ $t('sign_in') }}</router-link>
          </li>
          <li class="nav-item" :class="{ active: isActiveRoute('/registration') }">
            <router-link to="/registration" @click="closeMenu">{{ $t('register_an_account') }}</router-link>
          </li>
          <li class="nav-item" :class="{ active: isActiveRoute('/reset-password') }">
            <router-link to="/reset-password" @click="closeMenu">{{ $t('forgot_password') }}</router-link>
          </li>

          <!-- Selector de Idioma -->
          <li class="nav-item">
            <div class="language-selector">
              <select id="language-select" @change="changeLanguage" :value="currentLanguage">
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
import { ref, watchEffect } from 'vue';
import { useI18n } from 'vue-i18n';
import { useRouter } from 'vue-router';
import { computed } from 'vue';

const { locale } = useI18n();
const router = useRouter();
const menuOpen = ref(false);

const currentLanguage = ref(locale.value);

watchEffect(() => {
  locale.value = currentLanguage.value;
});

function changeLanguage(event: Event) {
  const selectedLanguage = (event.target as HTMLSelectElement).value;
  currentLanguage.value = selectedLanguage;
  localStorage.setItem('language', selectedLanguage);
}

function isActiveRoute(path: string) {
  return computed(() => router.currentRoute.value.path === path).value;
}

function closeMenu() {
  menuOpen.value = false;
}
</script>

<style scoped>
/* Estilos previamente definidos */
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

/* Menú hamburguesa */
.menu-icon {
  display: none;
  cursor: pointer;
}

.menu-icon .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  margin: 4px auto;
  background-color: #f2f2f2;
}

.menu-toggle {
  display: none;
}

.menu-toggle:checked ~ .nav-container .nav-links_personalizado {
  display: block;
}

/* Responsivo */
@media (max-width: 768px) {
  .wrapper_personalizado {
    flex-direction: column;
    align-items: flex-start;
  }

  .wrapper_personalizado .logo_personalizado a {
    font-size: 24px;
    margin-bottom: 10px;
    white-space: normal; /* Permite el wrap del texto en pantallas pequeñas */
  }

  .nav-container {
    width: 100%;
  }

  .nav-links_personalizado {
    display: none;
    width: 100%;
    flex-direction: column;
    align-items: flex-start;
    background-color: #242526; /* Fondo para el menú desplegable */
    padding: 10px 0;
    margin-top: 10px; /* Espacio extra para separarlo del borde superior */
    border-radius: 5px; /* Redondea las esquinas del menú */
  }

  .menu-toggle:checked ~ .nav-container .nav-links_personalizado {
    display: flex;
    transform: translateY(0);
  }

  .nav-links_personalizado li {
    width: 100%;
    text-align: left;
    margin: 0;
  }

  .nav-links_personalizado li a {
    width: 100%;
    padding: 10px 20px;
    border-bottom: 1px solid #3a3b3c;
  }

  .menu-icon {
    display: block;
    position: absolute;
    top: 20px;
    right: 30px;
  }

  .nav-links_personalizado li:last-child a {
    border-bottom: none; /* Elimina la línea en el último elemento */
  }
}
</style>
