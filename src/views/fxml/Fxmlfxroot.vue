<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="root_elements">&lt;fx:root&gt;</a></h4>
      <p>
        The <span class="code">&lt;fx:root&gt;</span> element creates a
        reference to a previously defined root element. It is only valid as the
        root node of an FXML document.
        <span class="code">&lt;fx:root&gt;</span> is used primarily when
        creating custom controls that are backed by FXML markup. This is
        discussed in more detail in the
        <a href="#fxmlloader">FXMLLoader</a> section.
      </p>
      <div class="info-alert">
        <strong>HTML Analogy:</strong> The <code>&lt;fx:root&gt;</code> tag
        allows an FXML file to define the inner content of a custom component
        without instantiating the component itself. This is very similar to how
        the Web Components <code>&lt;template&gt;</code> tag and Shadow DOM
        work, where a template defines the internals for a custom HTML element.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;!-- Web Component Template --&gt;
&lt;template id="my-custom-element"&gt;
  &lt;style&gt;p { color: red; }&lt;/style&gt;
  &lt;p&gt;Custom Control Content&lt;/p&gt;
&lt;/template&gt;</code></pre>
      </div>
      <JavaFxPreview>
        <div style="padding: 10px; border: 1px dashed #ccc; text-align: center; color: red;">
          Custom Control Content (Template)
        </div>
      </JavaFxPreview>
    </section>
    <div class="pagination">
      <router-link to="/fxml/fx-copy" class="btn btn-prev"
        >❮ &lt;fx:copy&gt;</router-link
      >
      <router-link to="/fxml/property-elements" class="btn btn-next"
        >Property Elements ❯</router-link
      >
    </div>
  </article>
</template>
