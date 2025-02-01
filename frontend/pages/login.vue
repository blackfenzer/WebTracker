<script setup lang="ts">
import { useAuth } from '~/composables/useAuth';

const username = ref('');
const password = ref('');
const error = ref('');
const auth = useAuth();

async function handleLogin() {
    try {
        error.value = '';
        await auth.login(username.value, password.value);
        navigateTo('/dashboard'); // Redirect on success
    } catch (err) {
        error.value = (err as Error).message;
    }
}
</script>

<template>
    <div class="container">
        <h1>Login</h1>
        <form @submit.prevent="handleLogin">
            <input v-model="username" placeholder="Username" required />
            <input v-model="password" type="password" placeholder="Password" required />
            <button type="submit">Login</button>
        </form>
        <p v-if="error" class="error">{{ error }}</p>
    </div>
</template>

<style>
.container {
    max-width: 400px;
    margin: auto;
    padding: 20px;
}

input {
    display: block;
    margin-bottom: 10px;
    width: 100%;
    padding: 8px;
}

button {
    width: 100%;
    padding: 10px;
    background: blue;
    color: white;
    border: none;
}

.error {
    color: red;
}
</style>
