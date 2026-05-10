<template>
  <div class="os-monitor">
    <h2>OS 상태 모니터링</h2>
    <ul>
      <li v-for="(proc, idx) in processes" :key="proc.pid">
        PID: {{ proc.pid }}, State: {{ proc.state }}, CPU: {{ proc.cpu }}%
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const processes = ref([])

const fetchProcesses = async () => {
  try {
    const res = await axios.get('/api/processes')
    processes.value = res.data
  } catch (e) {
    console.error('Failed to fetch processes', e)
  }
}

onMounted(() => {
  fetchProcesses()
  setInterval(fetchProcesses, 5000)
})
</script>

<style scoped>
.os-monitor {
  padding: 1rem;
}
</style>
