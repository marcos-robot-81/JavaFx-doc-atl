<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h2><a id="overview">Overview</a></h2>
      <p>
        FXML is a scriptable, XML-based markup language for constructing Java
        object graphs. It provides a convenient alternative to constructing such
        graphs in procedural code, and is ideally suited to defining the user
        interface of a JavaFX application, since the hierarchical structure of
        an XML document closely parallels the structure of the JavaFX scene
        graph.
      </p>

      <p>
        This document introduces the FXML markup language and explains how it
        can be used to simplify development of JavaFX applications.
      </p>
      <div class="info-alert">
        <strong>HTML Analogy:</strong> Just as HTML provides a declarative,
        tag-based way to build a web page's DOM tree, FXML provides a
        declarative way to build a JavaFX scene graph. Both separate UI layout
        from application logic.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;!-- HTML UI definition --&gt;
&lt;div id="app"&gt;
  &lt;h1&gt;Hello World&lt;/h1&gt;
  &lt;button&gt;Click Me&lt;/button&gt;
&lt;/div&gt;</code></pre>
      </div>
      <div class="javafx-preview">
        <div>
          <h1>Hello World</h1>
          <button class="javafx-btn">Click Me</button>
        </div>
      </div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/elements" class="btn btn-next"
        >Elements ❯</router-link
      >
    </div>
  </article>
</template>
