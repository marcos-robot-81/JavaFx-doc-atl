<template>
  <div class="javafx-preview">
    <div class="javafx-preview-header" v-if="showHeader">
      <span class="javafx-preview-badge">👁 JavaFX Preview</span>
      <span class="javafx-preview-subtitle">{{ subtitle }}</span>
    </div>
    <div class="javafx-window">
      <div class="javafx-titlebar">
        <div class="javafx-titlebar-left">
          <img class="javafx-app-icon" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Crect width='16' height='16' rx='3' fill='%234b6cb7'/%3E%3Ctext x='8' y='12' text-anchor='middle' fill='white' font-size='10' font-family='sans-serif' font-weight='bold'%3EFX%3C/text%3E%3C/svg%3E" alt="FX" />
          <span class="javafx-titlebar-title">{{ title }}</span>
        </div>
        <div class="javafx-window-controls">
          <span class="javafx-ctrl javafx-ctrl-min">─</span>
          <span class="javafx-ctrl javafx-ctrl-max">□</span>
          <span class="javafx-ctrl javafx-ctrl-close">✕</span>
        </div>
      </div>
      <div class="javafx-content">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    default: 'JavaFX Application'
  },
  subtitle: {
    type: String,
    default: 'Result on screen'
  },
  showHeader: {
    type: Boolean,
    default: true
  }
})
</script>

<style scoped>
.javafx-content {
  color: #1a1a1a !important; /* Força o texto interno a ser escuro, pois o fundo da janela é cinza claro */
}
</style>
