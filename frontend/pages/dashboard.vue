<script setup lang="ts">
import { useAuth } from '~/composables/useAuth';

definePageMeta({ middleware: 'auth' });

const user = ref(null);
const auth = useAuth();

onMounted(async () => {
    user.value = await auth.getUser() as any;
});

async function handleLogout() {
    await auth.logout();
    navigateTo('/login');
}
</script>

<template>
    <div class="container">
        <h1>Dashboard</h1>
        <p v-if="user">Welcome, {{ user || "Anonymous" }}</p>
        <button @click="handleLogout">Logout</button>
    </div>
</template>
