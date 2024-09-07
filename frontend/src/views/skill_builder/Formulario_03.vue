<template>
  <v-row justify="center">
    <!-- Columna vacía a la izquierda -->
    <v-col cols="12" md="1"></v-col>

    <!-- Columna principal con el formulario -->
    <v-col cols="12" md="10">
      <h1>Create New Skill - Formulario 03</h1>
      <v-form>
        <!-- Seleccionador de lenguajes -->
        <v-select
          :label="$t('skill_builder.Select_Language')" 
          :items="languages"
          v-model="selectedLanguage"
          filterable
          item-text="language"
          item-value="language"
          class="mt-4"
        ></v-select>

        <!-- Campo de texto para el nombre de la habilidad -->
        <v-text-field :label="$t('skill_builder.Skill_Name')" v-model="skillName"></v-text-field>

        <!-- Segundo dropdown (Topic Father) -->
        <v-select
          :label="$t('skill_builder.Topic_Father')"
          :items="topicFathers"
          v-model="selectedTopicFather"
          filterable
        ></v-select>

        <!-- Campo de texto para ingresar múltiples valores -->
        <v-text-field
          :label="$t('skill_builder.Enter_multiple_topic_son')"
          v-model="multipleValues"
          :hint="$t('skill_builder.Use_commas_to_separate_values')"
          persistent-hint
        ></v-text-field>

        <v-textarea
          :label="$t('skill_builder.Description')"
          v-model="skillDescription"
          rows="4"
          outlined
          class="mt-4"
        ></v-textarea>

        <!-- Primer dropdown (CEFR Level) -->
        <v-select
          :label="$t('skill_builder.CEFR_Level')"
          :items="cefr_levels"
          v-model="selectedCEFRLevel"
        ></v-select>

        <v-select
          :label="$t('skill_builder.Select_number_tokens')"
          :items="tokens"
          v-model="selectedNumTokens"
          filterable
          item-text="tokens"
          item-value="tokens"
          class="mt-4"
        ></v-select>

        <!-- Mensaje de alerta -->
        <v-alert v-if="alertMessage" :type="alertType" class="mt-4">
          {{ alertMessage }}
        </v-alert>

        <!-- Botón de envío, desaparece si aparece el botón de continuar -->
        <v-btn v-if="!showContinueButton" color="primary" @click="submitForm">{{ $t('skill_builder.Submit') }}</v-btn>

        <!-- Botón de continuar y resubmit, visibles cuando aparece el botón de continuar -->
        <v-row v-if="showContinueButton" class="mt-4">
          <v-col>
            <v-btn color="success" @click="continueAction">{{ $t('skill_builder.Continue') }}</v-btn>
          </v-col>
          <v-col>
            <v-btn color="warning" @click="submitForm">{{ $t('skill_builder.Resubmit') }}</v-btn>
          </v-col>
        </v-row>
      </v-form>

      <!-- Tabla editable con las oraciones generadas -->
      <v-table v-if="generatedSentences.length > 0" class="mt-4">
        <thead>
          <tr>
            <th>{{ $t('skill_builder.Setence') }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(sentence, index) in generatedSentences" :key="index">
            <td>
              <v-confirm-edit v-model="generatedSentences[index]">
                <template v-slot:default="{ model: proxyModel, actions }">
                  <v-card class="mx-auto" max-width="1600">
                    <template v-slot:text>
                      <v-text-field
                        v-model="proxyModel.value"
                        label="Modify my value"
                        class="wrapped-text"
                      ></v-text-field>
                    </template>

                    <template v-slot:actions>
                      <v-spacer></v-spacer>
                      <component :is="actions"></component>
                    </template>
                  </v-card>
                </template>
              </v-confirm-edit>
            </td>
          </tr>
        </tbody>
      </v-table>
    </v-col>

    <!-- Columna vacía a la derecha -->
    <v-col cols="12" md="1"></v-col>
  </v-row>
</template>

<script>
import axios from 'axios';
import { ref, onMounted, watch } from 'vue';
import { useI18n } from 'vue-i18n';  // Importar la función de i18n

export default {
  setup() {
    // Iniciar el uso de i18n
    const { t, locale } = useI18n();

    // Declaraciones de variables reactivas dentro de setup
    const skillName = ref('');
    const skillDescription = ref('');
    const selectedCEFRLevel = ref(null);
    const selectedTopicFather = ref(null);
    const cefr_levels = ref([]);  // Para los CEFR Levels
    const topicFathers = ref([]); // Para los Topic Fathers

    // Declaraciones adicionales para el resto del formulario
    const selectedLanguage = ref('');
    const multipleValues = ref('');
    const selectedNumTokens = ref(100); // Valor preseleccionado por defecto
    const languages = ref([
      'English',
      'Spanish',
      'French',
      'Japanese',
      'German',
      'Chinese',
    ]);
    const tokens = ref([100, 250, 500, 750, 1000]); // Lista de tokens disponibles
    const alertMessage = ref('');
    const alertType = ref('error');
    const generatedSentences = ref([]); // Almacena las oraciones generadas
    const showContinueButton = ref(false); // Controla la visibilidad del botón de continuar

    // Función para cargar los Topic Fathers según el idioma seleccionado
    const loadTopicFathers = () => {
  // Obtén solo el código de idioma (ej. 'en' en lugar de 'en-US')
  const languageCode = locale.value.split('-')[0]; 
  console.log('Language being sent to backend:', languageCode);  // Verifica el valor de idioma
  axios
    .get('http://localhost:8000/skill_builder/topics/', {
      params: {
        language: languageCode  // Enviar el idioma al backend
      }
    })
    .then((response) => {
      console.log('Response data from backend:', response.data);  // Verifica la estructura de la respuesta
      topicFathers.value = response.data.map((topic) => Object.values(topic)[0]); // Ajustar al idioma seleccionado
    })
    .catch((error) => {
      console.error('Error loading topic fathers:', error);
    });
};

    // Cargar datos cuando el componente esté montado
    onMounted(() => {
      cefr_levels.value = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'];
      loadTopicFathers(); // Cargar los topic fathers iniciales
    });

    // Escuchar cambios en el idioma y recargar los Topic Fathers
    watch(locale, loadTopicFathers);

    const submitForm = async () => {
      if (!selectedLanguage.value || !multipleValues.value || !selectedNumTokens.value) {
        alertMessage.value = t('skill_builder.errors.fill_required_fields');  // Mensaje traducido
        alertType.value = 'error';
        return;
      }

      const words = multipleValues.value.split(',').map(word => word.trim()).filter(word => word);

      try {
        const params = new URLSearchParams();
        params.append('language', selectedLanguage.value);
        words.forEach(word => {
          params.append('words[]', word);
        });
        params.append('num_tokens', selectedNumTokens.value);
        params.append('topic_father', selectedTopicFather.value);
        params.append('description', skillDescription.value);
        params.append('cefr_level', selectedCEFRLevel.value);

        const response = await axios.get('http://localhost:8000/skill_builder/check_spelling/', {
          params: params
        });

        alertMessage.value = response.data.status === 'error'
          ? t('skill_builder.errors.misspelled_words', { words: response.data.message })
          : t('success.sentences_generated');  // Mensajes traducidos
        alertType.value = response.data.status === 'error' ? 'warning' : 'success';

        if (response.data.status === 'success') {
          generatedSentences.value = response.data.sentences;
        }

        showContinueButton.value = true;
      } catch (error) {
        console.error('Error checking spelling:', error);
        alertMessage.value = t('skill_builder.errors.spell_check_failed');  // Mensaje traducido
        alertType.value = 'error';
      }
    };

    const continueAction = async () => {
      try {
        const params = new URLSearchParams();
        params.append('language', selectedLanguage.value);
        multipleValues.value.split(',').map(word => word.trim()).forEach(word => {
          params.append('words[]', word);
        });
        params.append('num_tokens', selectedNumTokens.value);
        params.append('topic_father', selectedTopicFather.value);
        params.append('description', skillDescription.value);
        params.append('cefr_level', selectedCEFRLevel.value);
        params.append('skip_spell_check', 'true');

        const response = await axios.get('http://localhost:8000/skill_builder/check_spelling/', {
          params: params
        });

        alertMessage.value = t('skill_builder.success.sentences_generated');  // Mensaje traducido
        alertType.value = 'success';
        generatedSentences.value = response.data.sentences;
      } catch (error) {
        console.error('Error omitting spell checking:', error);
        alertMessage.value = t('skill_builder.errors.omit_spell_check_failed');  // Mensaje traducido
        alertType.value = 'error';
      }
    };

    const saveSentence = (index) => {
      console.log(`Sentence at index ${index} saved:`, generatedSentences.value[index]);
    };
    
    return {
      skillName,
      skillDescription,
      selectedCEFRLevel,
      selectedTopicFather,
      cefr_levels,
      topicFathers,
      selectedLanguage,
      multipleValues,
      languages,
      tokens,
      selectedNumTokens,
      submitForm,
      alertMessage,
      alertType,
      generatedSentences,
      saveSentence,
      showContinueButton,
      continueAction
    };
  },
};
</script>



<style scoped>
.wrapped-text {
  word-wrap: break-word;
  white-space: normal;
}
</style>
