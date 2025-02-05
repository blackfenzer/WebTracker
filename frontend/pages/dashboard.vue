<script setup lang="ts">
import { useAuth } from '~/composables/useAuth';
import { createVuetify } from 'vuetify';

definePageMeta({ middleware: 'auth' });

const user = ref(null);
const auth = useAuth();
const items = ref<Array<{
    url: string,
    name: string,
    current_price: number,
    last_checked: string,
    price_history: Array<{ price: number, timestamp: string }>
}>>([]);

const url = ref('');
const message = ref('');

const headers = [
    { title: 'Name', key: 'name' },
    { title: 'Current Price', key: 'current_price' },
    { title: 'Last Checked', key: 'created_at' },
    { title: "Url", key: "url" },
    // { title: 'Actions', key: 'actions', sortable: false }
];
const history = ref<Array<{
    tracked_id: number;
    name: string;
    url: string;
    price_history: Array<{
        current_price: number;
        created_at: string;
        name: string;
    }>;
}>>([]);

const fetchTrackedItems = async () => {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/show/');
        const data = await response.json();

        // Fetch price history separately
        const historyResponse = await fetch('http://127.0.0.1:8000/api/history/');
        const historyData = await historyResponse.json();

        items.value = data.items.map(item => ({
            ...item,
            price_history: historyData[item.id] || []  // Match item price history
        }));
        history.value = historyData.items;
        console.log(items.value);
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
        console.error("Error adding item:", error);
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
    <v-container>
        <v-row>
            <v-col cols="12">
                <v-card>
                    <v-card-title class="headline">Dashboard</v-card-title>
                    <v-card-text>
                        <p v-if="user">Welcome</p>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>

        <v-row>
            <v-col cols="12">
                <v-card>
                    <v-card-title class="headline">Track New Item</v-card-title>
                    <v-card-text>
                        <v-form @submit.prevent="addTrackedItem">
                            <v-text-field v-model="url" label="Enter Lazada product URL" outlined dense></v-text-field>
                            <v-btn type="submit" color="primary">Track Item</v-btn>
                            <p v-if="message" class="mt-2">{{ message }}</p>
                        </v-form>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>

        <v-row>
            <v-col cols="12">
                <v-card>
                    <v-card-title class="headline">Tracked Items List</v-card-title>
                    <v-card-text>
                        <v-data-table :headers="headers" :items="items" :items-per-page="5" class="elevation-1">
                            <template v-slot:item.url="{ item }">
                                <NuxtLink :href="`${item.url}`" target="_blank">
                                    <v-btn color="primary" small>View</v-btn>
                                </NuxtLink>
                            </template>
                        </v-data-table>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>

        <v-row>
            <v-col cols="12">
                <v-card>
                    <v-card-title class="headline">Price History</v-card-title>
                    <v-card-text>
                        <v-expansion-panels>
                            <v-expansion-panel v-for="item in history" :key="item.tracked_id">
                                <v-expansion-panel-title>
                                    {{ item.name }}
                                </v-expansion-panel-title>
                                <v-expansion-panel-text>
                                    <v-list>
                                        <v-list-item v-for="history in item.price_history" :key="history.created_at">
                                            <v-list-item-title>
                                                {{ history.current_price }} baht -- at ({{ new
                                                Date(history.created_at).toLocaleString()
                                                }})
                                            </v-list-item-title>
                                        </v-list-item>
                                    </v-list>
                                </v-expansion-panel-text>
                            </v-expansion-panel>
                        </v-expansion-panels>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>

        <v-row>
            <v-col cols="12" class="text-center">
                <v-btn color="error" @click="handleLogout">Logout</v-btn>
            </v-col>
        </v-row>
    </v-container>
</template>

<style scoped>
.v-card {
    margin-bottom: 20px;
}
</style>
