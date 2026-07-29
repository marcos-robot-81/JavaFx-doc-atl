<template>
  <div class="javadoc-container">
    <iframe 
      src="https://openjfx.io/javadoc/26/" 
      frameborder="0" 
      class="javadoc-iframe"
      title="JavaFX 26 API Documentation"
    ></iframe>
  </div>
</template>

<style scoped>
.javadoc-container {
  width: 100%;
  height: 100vh; /* Adjust depending on topbar height, maybe calc(100vh - 60px) */
  display: flex;
  flex-direction: column;
}

.javadoc-iframe {
  flex: 1;
  width: 100%;
  height: 100%;
  border: none;
  border-radius: 8px; /* Slightly match premium design */
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  background-color: #fff; /* iFrame background */
}
</style>
