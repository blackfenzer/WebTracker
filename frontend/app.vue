<script setup>
</script>

<template>
  <div class="layout">
    <nav>
      <nuxt-link to="/">Home</nuxt-link> |
      <nuxt-link to="/login">Login</nuxt-link> |
      <nuxt-link to="/dashboard">Dashboard</nuxt-link>
    </nav>

    <!-- This ensures your pages render correctly -->
    <NuxtPage />
  </div>
</template>

<style>
.layout {
  text-align: center;
  padding: 20px;
}

nav {
  margin-bottom: 20px;
}

nav a {
  margin: 0 10px;
  text-decoration: none;
  color: blue;
}
</style>
