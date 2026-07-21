<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="copy_elements">&lt;fx:copy&gt;</a></h4>
<p>The <span class="code">&lt;fx:copy&gt;</span> element creates a copy of an existing element. Like <span class="code">&lt;fx:reference&gt;</span>,
 it is used with the fx:id attribute or a script variable. The element's
 "source" attribute specifies the name of the object that will be 
copied. The source type must define a copy constructor that will be used
 to construct the copy from the source value.</p>

<p>At the moment, no JavaFX platform classes provide such a copy 
constructor, so this element is provided primarily for use by 
application developers. This may change in a future release.</p>
<div class="info-alert"><strong>HTML Analogy:</strong> Copying an element in FXML is analogous to cloning a DOM node in JavaScript using <code>cloneNode(true)</code>, which creates an exact duplicate of the element and its children.</div>
<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;!-- Original Element --&gt;
&lt;div id="template"&gt;Reusable Content&lt;/div&gt;

&lt;!-- JS equivalent of copy --&gt;
&lt;script&gt;
  const clone = document.getElementById('template').cloneNode(true);
  document.body.appendChild(clone);
&lt;/script&gt;</code></pre></div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/fx-reference" class="btn btn-prev">❮ &lt;fx:reference&gt;</router-link>
      <router-link to="/fxml/fx-root" class="btn btn-next">&lt;fx:root&gt; ❯</router-link>
    </div>
  </article>
</template>
