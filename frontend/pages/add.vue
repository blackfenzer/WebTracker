<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <h1>Add Tracked Item</h1>
                <v-form @submit.prevent="addItem">
                    <v-text-field v-model="name" label="Name" required></v-text-field>
                    <v-text-field v-model="description" label="Description" required></v-text-field>
                    <v-btn type="submit" color="primary">Add Item</v-btn>
                </v-form>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
const name = ref('');
const description = ref('');

const addItem = async () => {
    try {
        await $fetch.post('/add/', {
            name: name.value,
            description: description.value,
        });
        navigateTo('/');
    } catch (error) {
        console.error('Error adding item:', error);
    }
};
</script>