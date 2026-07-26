<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="constant_elements">&lt;fx:constant&gt;</a></h4>
      <p>
        The <span class="code">&lt;fx:constant&gt;</span> element creates a
        reference to a class constant. For example, the following markup sets
        the value of the "minWidth" property of a<span class="code"
          >Button</span
        >
        instance to the value of the
        <span class="code">NEGATIVE_INFINITY</span> constant defined by the
        <span class="code">java.lang.Double</span> class:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;Button&gt;
    &lt;minHeight&gt;&lt;Double fx:constant="NEGATIVE_INFINITY"/&gt;&lt;/minHeight&gt;
&lt;/Button&gt;</code></pre>
      </div>

      <div class="info-alert">
        <strong>HTML Analogy:</strong> Native HTML doesn't support reading class
        constants directly. The closest web equivalent is binding to JavaScript
        constants or global objects in a framework like Vue or React.
      </div>
      <div class="code-block">
        <div class="code-header">Web Equivalent (Vue)</div>
        <pre><code>&lt;button :style="{ minHeight: Number.NEGATIVE_INFINITY + 'px' }"&gt;
  Content
&lt;/button&gt;</code></pre>
      </div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/fx-include" class="btn btn-prev"
        >❮ &lt;fx:include&gt;</router-link
      >
      <router-link to="/fxml/fx-reference" class="btn btn-next"
        >&lt;fx:reference&gt; ❯</router-link
      >
    </div>
  </article>
</template>
