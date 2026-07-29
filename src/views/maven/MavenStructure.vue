<template>
  <div class="doc-content">
    <h1>Maven Directory Structure</h1>
    <p class="description">
      Maven relies on a standard directory layout. If your files aren't in the exact right folders, Maven will not be able to find your code or resources, and your project will fail to build.
    </p>

    <div class="alert alert-warning">
      <strong>Important:</strong> Unlike some IDEs where you can put files anywhere, Maven strictly enforces this "Convention over Configuration" approach. Do not change these folder names!
    </div>

    <section class="doc-section">
      <h2>The Standard Layout</h2>
      <p>Here is the exact folder structure your JavaFX project must follow:</p>
      
      <div class="code-block-wrapper">
        <div class="code-header">Project Root</div>
        <pre><code>my-javafx-app/
├── pom.xml                 # The Maven configuration file (MUST be at the root)
└── src/
    ├── main/
    │   ├── java/           # All your Java source code (.java files) goes here
    │   │   └── com/
    │   │       └── myapp/
    │   │           └── Main.java
    │   └── resources/      # Non-Java files (FXML, CSS, Images, properties) go here
    │       └── com/
    │           └── myapp/
    │               ├── main.fxml
    │               └── style.css
    └── test/
        ├── java/           # Your unit tests (JUnit, etc.)
        └── resources/      # Resources specifically used for testing
</code></pre>
      </div>
    </section>

    <section class="doc-section">
      <h2>Understanding the Folders</h2>

      <h3><span class="highlight">src/main/java/</span></h3>
      <p>
        This is where your actual Java code lives. The packages you create (e.g., <code>com.myapp</code>) must exist as folders inside this directory. If you place a <code>.java</code> file outside of this folder, Maven simply won't compile it.
      </p>

      <h3><span class="highlight">src/main/resources/</span></h3>
      <p>
        <strong>Crucial for JavaFX!</strong> Any file that is NOT Java code must go here. When you use <code>FXMLLoader.load(getClass().getResource("main.fxml"))</code>, Java looks inside this resources folder. 
        <br><br>
        <em>Tip:</em> It's highly recommended to mirror your Java package structure inside the resources folder so that your FXML files live right next to your controller classes in the final compiled output.
      </p>

      <h3><span class="highlight">pom.xml</span></h3>
      <p>
        The Project Object Model. This is the heart of Maven. It defines your dependencies (like JavaFX), plugins, and project version. It must be directly inside the root folder of your project.
      </p>
    </section>

    <div class="alert alert-success">
      <strong>Pro Tip:</strong> When you run <code>mvn compile</code>, Maven takes everything in <code>src/main/java</code> and <code>src/main/resources</code> and merges them together into the <code>target/classes</code> folder. This is why mirroring the package structure in both folders works so perfectly!
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
  margin-bottom: 20px;
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
  color: var(--text-main);
}
.highlight {
  background: rgba(56, 189, 248, 0.1);
  color: var(--accent);
  padding: 4px 8px;
  border-radius: 4px;
  font-family: monospace;
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
.alert-warning {
  background-color: rgba(245, 158, 11, 0.1);
  border-left: 4px solid #f59e0b;
  color: #fef3c7;
}
.alert-success {
  background-color: rgba(16, 185, 129, 0.1);
  border-left: 4px solid #10b981;
  color: #d1fae5;
}
</style>
