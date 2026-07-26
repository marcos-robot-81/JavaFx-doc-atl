<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="reference_elements">&lt;fx:reference&gt;</a></h4>
      <p>
        The <span class="code">&lt;fx:reference&gt;</span> element creates a new
        reference to an existing element. Wherever this tag appears, it will
        effectively be replaced by the value of the named element. It is used in
        conjunction with either the <span class="code">fx:id</span> attribute or
        with a script variables, both of which are discussed in more detail in
        later sections. The "source" attribute of the
        <span class="code">&lt;fx:reference&gt;</span> element specifies the
        name of the object to which the new element will refer.
      </p>

      <p>
        For example, the following markup assigns a previously-defined
        <span class="code">Image</span> instance named "myImage" to the "image"
        property of an <span class="code">ImageView</span> control:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;ImageView&gt;
    &lt;image&gt;
        &lt;fx:reference source="myImage"/&gt;
    &lt;/image&gt;
&lt;/ImageView&gt;
</code></pre>
      </div>

      <p>
        Note that, since it is also possible to dereference a variable using the
        attribute variable resolution operator (discussed later in the
        <a href="#attributes">Attributes</a> section),
        <span class="code">fx:reference</span> is generally only used when a
        reference value must be specified as an element, such as when adding the
        reference to a collection:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;ArrayList&gt;
    &lt;fx:reference source="element1"/&gt;
    &lt;fx:reference source="element2"/&gt;
    &lt;fx:reference source="element3"/&gt;
&lt;/ArrayList&gt;
</code></pre>
      </div>

      <p>
        For most other cases, using an attribute is simpler and more concise.
      </p>

      <div class="info-alert">HTML Analogy</div>
      <p>
        In web development, referencing an existing element by its ID is similar
        to how the <code>for</code> attribute in a
        <code>&lt;label&gt;</code> points to an <code>&lt;input&gt;</code>'s ID,
        or how SVG <code>&lt;use&gt;</code> tags reference other graphics using
        their ID.
      </p>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;!-- Referencing an ID in HTML --&gt;
&lt;label for="myInput"&gt;Username&lt;/label&gt;
&lt;input type="text" id="myInput" /&gt;

&lt;!-- Referencing an ID in SVG --&gt;
&lt;svg&gt;
  &lt;defs&gt;
    &lt;circle id="myCircle" cx="50" cy="50" r="40" fill="red" /&gt;
  &lt;/defs&gt;
  &lt;use href="#myCircle" x="10" y="10" /&gt;
&lt;/svg&gt;</code></pre>
      </div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/fx-constant" class="btn btn-prev"
        >❮ &lt;fx:constant&gt;</router-link
      >
      <router-link to="/fxml/fx-copy" class="btn btn-next"
        >&lt;fx:copy&gt; ❯</router-link
      >
    </div>
  </article>
</template>
