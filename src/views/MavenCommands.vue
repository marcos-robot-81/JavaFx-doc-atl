<template>
  <div class="doc-content">
    <h1>Maven Commands (mvn)</h1>
    <p class="description">
      A quick reference guide for running common Maven commands (<code>mvn</code>) when developing JavaFX applications.
    </p>

    <section class="doc-section">
      <h2>Essential Commands</h2>
      <p>Here are the most common commands you will use with the <code>javafx-maven-plugin</code>:</p>

      <h3>1. Clean and Compile</h3>
      <p>Cleans the target directory and compiles your Java code.</p>
      <div class="code-block-wrapper">
        <div class="code-header">Terminal</div>
        <pre><code>mvn clean compile</code></pre>
      </div>

      <h3>2. Run the JavaFX Application</h3>
      <p>Executes the application using the JavaFX Maven plugin. This is the command you'll use most often during development.</p>
      <div class="code-block-wrapper">
        <div class="code-header">Terminal</div>
        <pre><code>mvn javafx:run</code></pre>
      </div>

      <h3>3. Build a Custom JRE (jlink)</h3>
      <p>Creates a custom, stripped-down Java Runtime Environment (JRE) containing only the modules your application needs.</p>
      <div class="code-block-wrapper">
        <div class="code-header">Terminal</div>
        <pre><code>mvn javafx:jlink</code></pre>
      </div>
    </section>

    <div class="alert alert-info">
      <strong>Pro Tip:</strong> You can chain commands together! For example, <code>mvn clean javafx:run</code> will ensure your project is built from scratch before running.
    </div>
  </div>
</template>

<style scoped>
.doc-content {
  padding: 40px;
  max-width: 900px;
  margin: 0 auto;
}
.description {
  font-size: 1.1rem;
  color: var(--text-muted);
  margin-bottom: 30px;
}
.doc-section {
  margin-bottom: 40px;
}
.doc-section h2 {
  border-bottom: 1px solid var(--glass-border);
  padding-bottom: 10px;
  margin-bottom: 20px;
}
.doc-section h3 {
  margin-top: 30px;
  color: var(--accent);
}
.code-block-wrapper {
  background: var(--code-bg);
  border-radius: 8px;
  overflow: hidden;
  margin: 15px 0;
  border: 1px solid var(--glass-border);
}
.code-header {
  background: rgba(0, 0, 0, 0.2);
  padding: 8px 16px;
  font-size: 0.85rem;
  color: var(--text-muted);
  border-bottom: 1px solid var(--glass-border);
}
pre {
  margin: 0;
  padding: 16px;
  overflow-x: auto;
}
code {
  font-family: "Fira Code", monospace;
  color: #e2e8f0;
}
.alert {
  padding: 16px 20px;
  border-radius: 8px;
  margin: 20px 0;
}
.alert-info {
  background-color: rgba(56, 189, 248, 0.1);
  border-left: 4px solid var(--accent);
  color: #e0f2fe;
}
</style>
