<script setup>
import { ref } from 'vue'
import Sidebar from './components/Sidebar.vue'
import Topbar from './components/Topbar.vue'

const isSidebarOpen = ref(false)

const toggleSidebar = () => {
  isSidebarOpen.value = !isSidebarOpen.value
}

const closeSidebar = () => {
  isSidebarOpen.value = false
}
</script>

<template>
  <div class="app-container">
    <Sidebar :isOpen="isSidebarOpen" @close="closeSidebar" />
    
    <main class="main-content">
      <Topbar @toggle-sidebar="toggleSidebar" />
      <router-view></router-view>
    </main>
  </div>
</template>

<style>
.main-content {
    flex: 1;
    margin-left: 280px;
    display: flex;
    flex-direction: column;
}

@media (max-width: 900px) {
    .main-content {
        margin-left: 0;
    }
}
</style>
