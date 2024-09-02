<!-- AuthLayout.vue -->
<template>
    <v-app class="auth-layout">
      <WelcomeHeaderView />
      <div class="content">
        <router-view />
      </div>
      <!-- Reemplaza GOOD BYE con el contenido de WelcomeFooterView -->
      <WelcomeFooterView />
    </v-app>
  </template>
  
  <script setup lang="ts">
  import WelcomeHeaderView from '@/components/WelcomeHeaderView.vue';
  import WelcomeFooterView from '@/components/WelcomeFooterView.vue';
  </script>
  
  <style scoped>
  .auth-layout {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }
  
  .content {
    flex-grow: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    background-image: url('@/assets/img/kestrel.jpg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
  }

  /* Media query para ajustar la posición de la imagen en pantallas pequeñas */
  @media (max-width: 768px) {
    .content {
      background-position: center right 30%; /* Desplaza la imagen hacia la derecha */
    }
  }
  
  .footer {
    margin-top: auto;
    background-color: #242526;
  }
  </style>
