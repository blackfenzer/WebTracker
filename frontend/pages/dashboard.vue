<script setup lang="ts">
import { useAuth } from '~/composables/useAuth';

definePageMeta({ middleware: 'auth' });

const user = ref(null);
const auth = useAuth();
const items = ref<Array<{ id: number, name: string, current_price: number, lowest_price: number }>>([]);
const url = ref('');
const message = ref('');
const fetchTrackedItems = async () => {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/show/');
        const data = await response.json();
        items.value = data.items;
    } catch (error) {
        console.error("Error fetching items:", error);
    }
};

const addTrackedItem = async () => {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/add/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url: url.value }),
        });

        if (!response.ok) throw new Error("Failed to add item");

        message.value = "Item added successfully!";
        url.value = '';
        fetchTrackedItems(); // Refresh list
    } catch (error) {
        console.error("Error fetching items:", error);
    }
};
onMounted(async () => {
    user.value = await auth.getUser() as any;
    fetchTrackedItems();
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

        <h1>Tracked Items</h1>

        <div class="form-container">
            <input v-model="url" placeholder="Enter Lazada product URL" />
            <button @click="addTrackedItem">Track Item</button>
            <p v-if="message">{{ message }}</p>
        </div>

        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Current Price</th>
                    <th>Lowest Price</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in items" :key="item.id">
                    <td>{{ item.name }}</td>
                    <td>฿{{ item.current_price }}</td>
                    <td>฿{{ item.lowest_price }}</td>
                    <td>
                        <NuxtLink :to="`/item/${item.id}`">View</NuxtLink>
                    </td>
                </tr>
            </tbody>
        </table>
        <button @click="handleLogout">Logout</button>
    </div>
</template>
