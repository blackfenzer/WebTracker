<script setup lang="ts">
import { defineProps, computed } from "vue";
import { LineChart } from "vue-chart-3";
import { Chart, registerables } from "chart.js";

// Register Chart.js components
Chart.register(...registerables);

const props = defineProps<{
    priceHistory: Array<{ current_price: number; created_at: string }>;
}>();

const chartData = computed(() => ({
    labels: props.priceHistory.map(entry => new Date(entry.created_at).toLocaleDateString()),
    datasets: [
        {
            label: "Price Trend",
            data: props.priceHistory.map(entry => entry.current_price),
            fill: true,
            borderColor: "#42A5F5",
            backgroundColor: "rgba(66, 165, 245, 0.2)",
            tension: 0.4,
        },
    ],
}));

const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: { display: true },
    },
    scales: {
        x: { title: { display: true, text: "Date" } },
        y: { title: { display: true, text: "Price (Baht)" } },
    },
};
</script>

<template>
    <div style="height: 300px;">
        <LineChart v-if="priceHistory.length" :chart-data="chartData" :options="chartOptions" />
        <p v-else>No price history available</p>
    </div>
</template>
