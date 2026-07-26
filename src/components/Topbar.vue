<script setup>
import { defineEmits } from "vue";

const emit = defineEmits(["toggle-sidebar"]);
</script>

<template>
  <header class="topbar">
    <button class="mobile-toggle" @click="emit('toggle-sidebar')">
      <svg
        viewBox="0 0 24 24"
        width="24"
        height="24"
        stroke="currentColor"
        stroke-width="2"
        fill="none"
      >
        <path d="M3 12h18M3 6h18M3 18h18" />
      </svg>
    </button>
    <div class="search-bar">
      <input type="text" placeholder="Search documentation..." />
    </div>
  </header>
</template>

<style scoped>
.topbar {
  height: 70px;
  padding: 0 40px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: rgba(15, 23, 42, 0.8);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--glass-border);
  position: sticky;
  top: 0;
  z-index: 50;
}

.mobile-toggle {
  display: none;
  background: none;
  border: none;
  color: var(--text-main);
  cursor: pointer;
}

.search-bar input {
  background-color: var(--code-bg);
  border: 1px solid var(--glass-border);
  color: var(--text-main);
  padding: 10px 16px;
  border-radius: 20px;
  width: 300px;
  font-size: 0.9rem;
  transition: all 0.3s;
}

.search-bar input:focus {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.2);
}

@media (max-width: 900px) {
  .mobile-toggle {
    display: block;
  }
  .search-bar {
    display: none;
  }
}
</style>
