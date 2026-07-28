<script setup>
import { ref, computed, defineEmits } from "vue";
import { useRouter } from "vue-router";

const emit = defineEmits(["toggle-sidebar"]);
const router = useRouter();
const searchQuery = ref("");
const isFocused = ref(false);

const searchResults = computed(() => {
  if (!searchQuery.value) return [];
  const query = searchQuery.value.toLowerCase();
  
  return router.getRoutes().filter(route => {
    if (route.path === '/' || !route.path) return false;
    
    const title = route.path.split('/').pop().replace(/-/g, ' ');
    return title.toLowerCase().includes(query) || route.path.toLowerCase().includes(query);
  }).slice(0, 8);
});

const formatTitle = (path) => {
  const parts = path.split('/');
  const section = parts[1] ? parts[1].toUpperCase() : '';
  const name = parts.pop().replace(/-/g, ' ');
  const formattedName = name.replace(/\w\S*/g, (txt) => {
    return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
  });
  return section ? `${section} - ${formattedName}` : formattedName;
};

const goToResult = (path) => {
  router.push(path);
  searchQuery.value = "";
  isFocused.value = false;
};

const handleFocus = () => {
  isFocused.value = true;
};

const handleBlur = () => {
  setTimeout(() => {
    isFocused.value = false;
  }, 200);
};
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
      <input 
        type="text" 
        placeholder="Search documentation..." 
        v-model="searchQuery"
        @focus="handleFocus"
        @blur="handleBlur"
      />
      <div class="search-results" v-if="isFocused && searchQuery && searchResults.length > 0">
        <div 
          v-for="result in searchResults" 
          :key="result.path" 
          class="search-result-item"
          @click="goToResult(result.path)"
        >
          <div class="result-title">{{ formatTitle(result.path) }}</div>
          <div class="result-path">{{ result.path }}</div>
        </div>
      </div>
      <div class="search-results no-results" v-else-if="isFocused && searchQuery && searchResults.length === 0">
        No results found.
      </div>
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

.search-bar {
  position: relative;
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

.search-results {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  margin-top: 8px;
  background-color: var(--code-bg, #1e293b);
  border: 1px solid var(--glass-border);
  border-radius: 12px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
  max-height: 400px;
  overflow-y: auto;
  z-index: 100;
  padding: 8px 0;
}

.search-result-item {
  padding: 10px 16px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.search-result-item:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.result-title {
  color: var(--text-main, #f8fafc);
  font-size: 0.9rem;
  font-weight: 500;
  margin-bottom: 4px;
}

.result-path {
  color: var(--text-muted, #94a3b8);
  font-size: 0.75rem;
}

.no-results {
  padding: 16px;
  text-align: center;
  color: var(--text-muted, #94a3b8);
  font-size: 0.9rem;
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
