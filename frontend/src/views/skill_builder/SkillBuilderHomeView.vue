<template>
    <v-container>
      <v-row>
        <v-col cols="12">
          <h1>{{ $t('skill_builder.Skill_Builder_Home') }}</h1>
          <p>{{ $t('skill_builder.Skill_Builder_Description') }}</p>
        </v-col>
      </v-row>
  
      <v-row>
        <!-- Tarjeta de crear nuevas habilidades -->
        <v-col cols="12" md="6">
          <v-card>
            <v-card-title>{{ $t('skill_builder.Create_New_Skill') }}</v-card-title>
            <v-card-text>
              <p>{{ $t('skill_builder.Create_New_Skill_Description') }}</p>
              <v-btn color="primary">{{ $t('skill_builder.Create') }}</v-btn>
            </v-card-text>
          </v-card>
        </v-col>
  
        <!-- Tarjeta de habilidades recomendadas -->
        <v-col cols="12" md="6">
          <v-card>
            <v-card-title>{{ $t('skill_builder.Recommended_Skills') }}</v-card-title>
            <v-card-text>
              <p>{{ $t('skill_builder.Recommended_Skills_Description') }}</p>
              <!-- Puedes agregar una lista de habilidades recomendadas aquí -->
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script setup lang="ts">
  // Aquí puedes importar cualquier componente o funcionalidad adicional que necesites
  </script>
  
  <style scoped>
  /* Añade estilos personalizados para esta vista si lo necesitas */
  </style>
  