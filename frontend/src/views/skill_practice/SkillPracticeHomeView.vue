<template>
  <div class="skill-practice-home">
    <h1>Welcome to Skill Practice</h1>
    <p>This is the home view where you can practice your skills.</p>
    
    <div v-if="loading">
      <p>Loading skills...</p>
    </div>

    <div v-else>
      <ul>
        <li v-for="skill in skills" :key="skill.id">
          {{ skill.name }} - Level: {{ skill.level }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SkillPracticeHomeView',
  data() {
    return {
      skills: [],
      loading: true
    };
  },
  created() {
    this.fetchSkills();
  },
  methods: {
    async fetchSkills() {
      try {
        const response = await axios.get('/api/skills/');
        this.skills = response.data;
      } catch (error) {
        console.error('Error fetching skills:', error);
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>

<style scoped>
.skill-practice-home {
  padding: 20px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  padding: 10px 0;
  border-bottom: 1px solid #ccc;
}
</style>
