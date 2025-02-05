<script setup>
import { NuxtLayout } from '#components';
</script>

<template>
  <NuxtLayout>
    <v-app>
      <!-- App Bar (Header) -->
      <v-app-bar color="primary" prominent>
        <v-toolbar-title>My App</v-toolbar-title>
        <v-spacer></v-spacer>
        <nav>
          <v-btn to="/" variant="text" color="white">Home</v-btn>
          <v-btn to="/login" variant="text" color="white">Login</v-btn>
          <v-btn to="/dashboard" variant="text" color="white">Dashboard</v-btn>
        </nav>
      </v-app-bar>

      <!-- Main Content -->
      <v-main>
        <v-container>
          <NuxtPage />
        </v-container>
      </v-main>

      <!-- Footer -->
      <v-footer color="primary" class="mt-auto">
        <v-row justify="center" no-gutters>
          <v-col class="text-center mt-4" cols="12">
            <strong>© {{ new Date().getFullYear() }} My App</strong> — Built with
            <v-icon small color="white">mdi-heart</v-icon> and
            <strong>Vuetify</strong>
          </v-col>
        </v-row>
      </v-footer>
    </v-app>
  </NuxtLayout>
</template>

<style>
.v-main {
  min-height: 80vh;

}

.v-footer {
  color: white;

}

.v-app-bar {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.v-btn {
  text-transform: none;
  font-weight: bold;
}
</style>