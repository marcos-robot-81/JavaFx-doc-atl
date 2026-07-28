<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="escape_sequences">Escape Sequences</a></h4>

      <p>
        If the value of an attribute begins with one of the resource resolution
        prefixes, the character can be escaped by prepending it with a leading
        backslash ("\") character. For example, the following markup creates a
        <span class="code">Label</span> instance whose text reads "$10.00":
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;Label text="\$10.00"/&gt;
</code></pre>
      </div>
      <div class="javafx-preview">
        <span class="javafx-label">$10.00</span>
      </div>
      <div class="info-alert">
        <strong>HTML Analogy:</strong> In HTML, special characters (like &lt; or
        &amp;) are escaped using HTML entities to render them literally instead
        of being interpreted as markup.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code class="language-html">&lt;!-- HTML Analogy for Escape Sequences --&gt;
&lt;span&gt;&amp;lt;10.00&amp;gt;&lt;/span&gt;
</code></pre>
      </div>
      <div class="javafx-preview">
        <span style="font-family: sans-serif;">&lt;10.00&gt;</span>
      </div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/variable-resolution" class="btn btn-prev"
        >❮ Variable Resolution</router-link
      >
      <router-link to="/fxml/expression-binding" class="btn btn-next"
        >Expression Binding ❯</router-link
      >
    </div>
  </article>
</template>
