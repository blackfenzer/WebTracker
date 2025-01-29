<template>
    <v-app>
        <v-app-bar app color="primary" dark>
            <v-toolbar-title>My Vuetify App</v-toolbar-title>
        </v-app-bar>
        <v-main>
            <slot /> <!-- This is where the page content will be injected -->
        </v-main>
    </v-app>
</template>

<script setup>
// You can add layout-specific logic here
</script>