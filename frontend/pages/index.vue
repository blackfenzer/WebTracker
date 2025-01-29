<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <h1>Tracked Items</h1>
                <v-btn color="primary" @click="navigateToAdd">Add New Item</v-btn>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12" v-for="item in items" :key="item.id">
                <v-card @click="navigateToItem(item.id)">
                    <v-card-title>{{ item.name }}</v-card-title>
                    <v-card-text>{{ item.description }}</v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
const { data: items } = await useAsyncData('items', () => $fetch.get('/'));

const navigateToAdd = () => {
    navigateTo('/add');
};

const navigateToItem = (itemId) => {
    navigateTo(`/item/${itemId}`);
};
</script>