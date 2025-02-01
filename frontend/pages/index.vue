<template>
    <div class="container">
        <h1>Welcome to Nuxt 3 Auth Demo</h1>
        <nuxt-link to="/login">
            <button>Go to Login</button>
        </nuxt-link>
    </div>
</template>

<style>
.container {
    text-align: center;
    padding: 20px;
}

button {
    padding: 10px;
    background: blue;
    color: white;
    border: none;
    cursor: pointer;
}
</style>