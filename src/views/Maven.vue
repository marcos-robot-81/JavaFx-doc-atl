<script setup>
</script>

<template>
  <div class="doc-page">
    <header class="doc-header">
      <h1>JavaFX with Maven</h1>
      <p class="doc-subtitle">Learn how to configure your JavaFX projects using Apache Maven.</p>
    </header>

    <div class="doc-content">
      <section class="doc-section">
        <h2>Introduction</h2>
        <p>
          Apache Maven is a powerful project management and comprehension tool. Using Maven with JavaFX makes managing dependencies and building your application straightforward and reproducible.
        </p>

        <div class="alert alert-info">
          <strong>Tip:</strong> Modern JavaFX (version 11 and later) is no longer bundled with the JDK, so using a build tool like Maven is highly recommended to fetch the necessary modules.
        </div>
      </section>

      <section class="doc-section">
        <h2>Setting up your pom.xml</h2>
        <p>
          To use JavaFX, you need to add the required JavaFX modules to your dependencies list. You will typically need at least <code>javafx-controls</code>. If you are using FXML, you will also need <code>javafx-fxml</code>.
        </p>
        <p>
          Additionally, you must configure the <code>javafx-maven-plugin</code> to easily run and package your application.
        </p>

        <div class="code-block-wrapper">
          <div class="code-block-header">
            <span class="code-block-lang">xml</span>
            <span class="code-block-filename">pom.xml</span>
          </div>
          <pre><code class="language-xml">&lt;project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd"&gt;
    &lt;modelVersion&gt;4.0.0&lt;/modelVersion&gt;

    &lt;groupId&gt;com.example&lt;/groupId&gt;
    &lt;artifactId&gt;javafx-maven-app&lt;/artifactId&gt;
    &lt;version&gt;1.0-SNAPSHOT&lt;/version&gt;

    &lt;properties&gt;
        &lt;project.build.sourceEncoding&gt;UTF-8&lt;/project.build.sourceEncoding&gt;
        &lt;maven.compiler.source&gt;17&lt;/maven.compiler.source&gt;
        &lt;maven.compiler.target&gt;17&lt;/maven.compiler.target&gt;
        &lt;javafx.version&gt;17.0.6&lt;/javafx.version&gt;
    &lt;/properties&gt;

    &lt;dependencies&gt;
        &lt;!-- JavaFX Controls --&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.openjfx&lt;/groupId&gt;
            &lt;artifactId&gt;javafx-controls&lt;/artifactId&gt;
            &lt;version&gt;${javafx.version}&lt;/version&gt;
        &lt;/dependency&gt;
        
        &lt;!-- JavaFX FXML --&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.openjfx&lt;/groupId&gt;
            &lt;artifactId&gt;javafx-fxml&lt;/artifactId&gt;
            &lt;version&gt;${javafx.version}&lt;/version&gt;
        &lt;/dependency&gt;
    &lt;/dependencies&gt;

    &lt;build&gt;
        &lt;plugins&gt;
            &lt;!-- Compiler Plugin --&gt;
            &lt;plugin&gt;
                &lt;groupId&gt;org.apache.maven.plugins&lt;/groupId&gt;
                &lt;artifactId&gt;maven-compiler-plugin&lt;/artifactId&gt;
                &lt;version&gt;3.11.0&lt;/version&gt;
            &lt;/plugin&gt;

            &lt;!-- JavaFX Maven Plugin --&gt;
            &lt;plugin&gt;
                &lt;groupId&gt;org.openjfx&lt;/groupId&gt;
                &lt;artifactId&gt;javafx-maven-plugin&lt;/artifactId&gt;
                &lt;version&gt;0.0.8&lt;/version&gt;
                &lt;configuration&gt;
                    &lt;mainClass&gt;com.example.Main&lt;/mainClass&gt;
                &lt;/configuration&gt;
            &lt;/plugin&gt;
        &lt;/plugins&gt;
    &lt;/build&gt;
&lt;/project&gt;</code></pre>
        </div>
      </section>
      
      <section class="doc-section">
        <h2>Running the Application</h2>
        <p>
          Once your <code>pom.xml</code> is configured and your main class is set in the <code>javafx-maven-plugin</code> configuration, you can run your application simply by using the following Maven command:
        </p>

        <div class="code-block-wrapper">
          <pre><code class="language-bash">mvn clean javafx:run</code></pre>
        </div>
        
        <div class="alert alert-success">
          <strong>Success:</strong> If everything is set up correctly, your JavaFX window will appear!
        </div>
      </section>
    </div>
  </div>
</template>

<style scoped>
.doc-page {
  max-width: 900px;
  margin: 0 auto;
  padding: 2rem;
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  color: #e0e0e0;
}

.doc-header {
  margin-bottom: 3rem;
  border-bottom: 1px solid #333;
  padding-bottom: 1.5rem;
}

.doc-header h1 {
  font-size: 3rem;
  font-weight: 800;
  margin: 0 0 0.5rem 0;
  background: linear-gradient(135deg, #42d392 0%, #647eff 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  letter-spacing: -1px;
}

.doc-subtitle {
  font-size: 1.2rem;
  color: #a0a0a0;
  margin: 0;
}

.doc-section {
  margin-bottom: 3rem;
}

.doc-section h2 {
  font-size: 1.8rem;
  font-weight: 600;
  color: #fff;
  margin-top: 0;
  margin-bottom: 1rem;
}

.doc-section p {
  line-height: 1.6;
  font-size: 1.1rem;
  color: #c0c0c0;
  margin-bottom: 1.5rem;
}

.alert {
  padding: 1rem 1.5rem;
  border-radius: 8px;
  margin-bottom: 1.5rem;
  border-left: 4px solid;
}

.alert-info {
  background-color: rgba(66, 211, 146, 0.1);
  border-left-color: #42d392;
  color: #42d392;
}

.alert-success {
  background-color: rgba(100, 126, 255, 0.1);
  border-left-color: #647eff;
  color: #8fa1ff;
}

.alert strong {
  font-weight: 600;
}

.code-block-wrapper {
  background-color: #1a1a1a;
  border-radius: 8px;
  overflow: hidden;
  margin-bottom: 1.5rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
  border: 1px solid #333;
}

.code-block-header {
  display: flex;
  justify-content: space-between;
  padding: 0.5rem 1rem;
  background-color: #2a2a2a;
  border-bottom: 1px solid #333;
  font-size: 0.85rem;
  color: #888;
}

.code-block-lang {
  text-transform: uppercase;
  font-weight: bold;
}

.code-block-wrapper pre {
  margin: 0;
  padding: 1.5rem;
  overflow-x: auto;
}

.code-block-wrapper code {
  font-family: 'Fira Code', 'JetBrains Mono', Consolas, monospace;
  font-size: 0.95rem;
  line-height: 1.5;
  color: #e6e6e6;
}

code {
  background-color: #2a2a2a;
  padding: 0.2em 0.4em;
  border-radius: 4px;
  font-family: 'Fira Code', Consolas, monospace;
  font-size: 0.9em;
  color: #ff8a65;
}

@media (max-width: 768px) {
  .doc-page {
    padding: 1rem;
  }
  .doc-header h1 {
    font-size: 2.5rem;
  }
}
</style>
