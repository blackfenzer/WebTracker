<script setup lang="ts">
import { useAuth } from '~/composables/useAuth';

const username = ref('');
const password = ref('');
const error = ref('');
const loading = ref(false);
const auth = useAuth();

async function handleLogin() {
    try {
        error.value = '';
        loading.value = true;
        await auth.login(username.value, password.value);
        navigateTo('/dashboard'); // Redirect on success
    } catch (err) {
        error.value = (err as Error).message;
    } finally {
        loading.value = false;
    }
}
</script>

<template>
    <v-container class="fill-height d-flex justify-center align-center">
        <v-card class="pa-6" elevation="10" max-width="400">
            <v-card-title class="text-center text-h5 font-weight-bold">
                Login
            </v-card-title>
            <v-card-text>
                <v-form @submit.prevent="handleLogin">
                    <v-text-field v-model="username" label="Username" prepend-inner-icon="mdi-account" outlined dense
                        required></v-text-field>

                    <v-text-field v-model="password" label="Password" type="password" prepend-inner-icon="mdi-lock"
                        outlined dense required></v-text-field>

                    <v-btn type="submit" color="primary" block :loading="loading" class="mt-4">
                        Login
                    </v-btn>

                    <v-alert v-if="error" type="error" dense class="mt-3">
                        {{ error }}
                    </v-alert>
                </v-form>
            </v-card-text>
        </v-card>
    </v-container>
</template>

<style scoped>
/* .v-container {
    min-height: 100vh;
    background: linear-gradient(135deg, #2196F3, #4CAF50);
    width: 100vw;
    margin: 0;
    padding: 0;
} */
.v-card {
    width: 100%;
}
</style>
