// Installed Utils
import { createRouter, createWebHistory } from 'vue-router';
import DOMPurify from 'dompurify';

// App Utils
import { useToken } from '@/composables/useToken';
import { useUserStore } from '@/stores/useUserStore';
import { useSocialStore } from '@/stores/useSocialStore';
import AuthLayout from '../layout/AuthLayout.vue';
import HomeLayout from '../layout/HomeLayout.vue'; // Importa HomeLayout
import SignInView from '../views/auth/SignInView.vue';
import RegistrationView from '../views/auth/RegistrationView.vue';
import ResetPasswordView from '../views/auth/ResetPasswordView.vue';
import ChangePasswordView from '../views/auth/ChangePasswordView.vue';
import GoogleConnectView from '../views/auth/GoogleConnectView.vue';
import MainView from '../views/dashboard/MainView.vue';

// Importa las vistas que mencionaste
import SkillPracticeHomeView from '../views/skill_practice/SkillPracticeHomeView.vue';
import SkillBuilderView from '../views/skill_builder/SkillBuilderHomeView.vue';
import ProgressTrackingView from '../views/progress_tracking/ProgressTrackingHomeView.vue';
import AboutView from '../views/about/AboutHomeView.vue';
import ContactView from '../views/contact/ContactHomeView.vue';

import Formulario01 from '../views/skill_builder/Formulario_01.vue';
import Formulario02 from '../views/skill_builder/Formulario_02.vue';
import Formulario03 from '../views/skill_builder/Formulario_03.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: '',
      component: AuthLayout,
      children: [
        { path: '', component: SignInView, meta: { noAuth: true } },
        { path: 'registration', component: RegistrationView, meta: { noAuth: true } },
        { path: 'reset-password', component: ResetPasswordView, meta: { noAuth: true } },
        { path: 'change-password/:token', component: ChangePasswordView, meta: { noAuth: true } },
        {
          path: 'google/connect',
          component: GoogleConnectView,
          meta: { socialAuth: true },
          props: (route) => ({
            failedMessage: route.meta.failedMessage || undefined
          })
        }
      ]
    },
    {
      path: '/dashboard',
      component: HomeLayout,
      children: [
        { path: '', component: MainView, meta: { requiresAuth: true } },
        { path: 'skill-practice', component: SkillPracticeHomeView, meta: { requiresAuth: true } }, 
        { path: 'progress-tracking', component: ProgressTrackingView, meta: { requiresAuth: true } },
        { path: 'about', component: AboutView, meta: { requiresAuth: true } },
        { path: 'contact', component: ContactView, meta: { requiresAuth: true } }
      ]
    },
    {
      path: '/skill-builder',
      component: HomeLayout,
      children: [
        { path: '', component: SkillBuilderView, meta: { requiresAuth: true } },
        { path: 'formulario_01', component: Formulario01, meta: { requiresAuth: true } }, 
        { path: 'formulario_02', component: Formulario02, meta: { requiresAuth: true } }, 
        { path: 'formulario_03', component: Formulario03, meta: { requiresAuth: true } }, 
      ]
    },
    {
      path: '/logout',
      component: { template: '<div></div>' },
      beforeEnter: (to, from, next) => {
        const userStore = useUserStore();
        userStore.logout();
        next('/');
      }
    }
  ]
});

// Register an interceptor
router.beforeEach(async (to, from, next) => {
  const { token, clearToken } = useToken();
  if (to.meta.noAuth) {
    if (token.value) {
      next('/dashboard');
      return;
    }
  } else if (to.meta.requiresAuth) {
    const userStore = useUserStore();
    if (!userStore.userData) {
      await userStore.fetchUserData();
    }
    if (!userStore.userData) {
      clearToken();
      next('/');
    } else {
      next();
    }
    return;
  } else if (to.meta.socialAuth) {
    const code = to.query.code || undefined;
    if (typeof code !== 'string') {
      to.meta.failedMessage = 'The authorization code is missing.';
      next();
      return;
    }
    const socialStore = useSocialStore();
    const userStore = useUserStore();
    await socialStore.exchangeAuthorizationCode(DOMPurify.sanitize(code));
    if (socialStore.errorMessage) {
      to.meta.failedMessage = socialStore.errorMessage;
    }
    if (userStore.userData) {
      next('/dashboard');
    } else {
      next();
    }
    return;
  }
  next();
});

export default router;
