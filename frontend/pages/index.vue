<template>
    <v-container class="fill-height d-flex justify-center align-center">
        <v-card class="pa-8 text-center welcome-card" elevation="12" max-width="500">
            <v-card-title class="text-h4 font-weight-bold text-blue-darken-3">
                Welcome 👋
            </v-card-title>
            <v-card-subtitle class="text-subtitle-1 mt-2">
                build with Nuxt 3 et Vuetify.
            </v-card-subtitle>


            <v-btn to="/login" color="blue-darken-2" size="large" elevation="4" class="text-white font-weight-bold">
                Login now →
            </v-btn>
        </v-card>
    </v-container>
</template>

<style scoped>


.welcome-card {
    border-radius: 16px;
    background: white;
    width: 50%;
}
</style>
