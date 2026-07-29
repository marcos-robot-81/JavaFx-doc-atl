<template>
  <div class="tutorial-container">
    <header class="hero-section">
      <div class="glow-orb glow-orb-1"></div>
      <div class="glow-orb glow-orb-2"></div>
      <div class="hero-content">
        <div class="badge">Step 1</div>
        <h1 class="title">Directory Structure</h1>
        <p class="subtitle">Learn how to organize the folders in your "Hello World" project so that Maven (and JavaFX) can read everything correctly, avoiding conflicts!</p>
      </div>
    </header>

    <main class="content-wrapper">
      <section class="card info-card">
        <div class="card-header">
          <div class="icon-wrapper">
            📁
          </div>
          <h2>Why does structure matter?</h2>
        </div>
        <p class="card-desc">
          Maven uses a standard directory convention. If you don't put your files in the right places, it simply won't find them during the project build. This is especially important in JavaFX projects, where we have Java code and visual resources (such as FXML and CSS).
        </p>

        <ul class="import-list">
          <li class="import-item">
            <div class="import-name"><code>src/main/java</code></div>
            <div class="import-desc">
              This is the logical heart of your application. All your files with the <code>.java</code> extension must be inside this folder, organized by packages (e.g., <code>com.myapp.Main</code>).<br><br>
              <strong>What to put here:</strong><br>
              - Main Classes<br>
              - JavaFX Controllers<br>
              - Models and Business Logic
            </div>
          </li>
          <li class="import-item">
            <div class="import-name"><code>src/main/resources</code></div>
            <div class="import-desc">
              This folder is intended for all files that <strong>are not</strong> Java source code, but that your application needs to run.<br><br>
              <strong>What to put here:</strong><br>
              - Interface files (<code>.fxml</code>)<br>
              - Stylesheets (<code>.css</code>)<br>
              - Images and Icons<br>
              - Configuration files (properties, json)<br><br>
              <strong>Golden Tip:</strong> The package (folder) structure inside <code>resources</code> should mirror the structure inside <code>java</code> to make loading FXML files easier.
            </div>
          </li>
        </ul>
      </section>

      <section class="card code-card">
        <div class="card-header">
          <div class="icon-wrapper accent-blue">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
          </div>
          <h2>The Standard Maven Structure</h2>
        </div>
        <p class="card-desc">See how your "Hello World" project should be organized:</p>
        
        <div class="code-block-wrapper">
          <div class="code-header">
            <div class="dots">
              <span class="dot mac-red"></span>
              <span class="dot mac-yellow"></span>
              <span class="dot mac-green"></span>
            </div>
            <span class="file-name">my-javafx-project</span>
            <span class="language-tag">folder</span>
          </div>
          <pre><code>my-javafx-project/
├── <span class="keyword">pom.xml</span> <span class="comment">(Maven Configurations)</span>
└── <span class="keyword">src/</span>
    └── <span class="keyword">main/</span>
        ├── <span class="class-name">java/</span>       <span class="comment">(.java source code)</span>
        └── <span class="class-name">resources/</span>  <span class="comment">(Visual files and assets .fxml, .css, images)</span></code></pre>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
</script>

<style scoped>
</style>
