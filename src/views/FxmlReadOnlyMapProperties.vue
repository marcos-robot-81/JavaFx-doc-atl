<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4>
        <a id="read_only_map_property_elements">Read-Only Map Properties</a>
      </h4>
      <p>
        A read-only map property is a bean property whose getter returns an
        instance of <span class="code">java.util.Map</span> and has no
        corresponding setter method. The attributes of a read-only map element
        are applied to the map when the closing tag is processed.
      </p>

      <p>
        The "properties" property of
        <span class="code">javafx.scene.Node</span> is an example of a read-only
        map property. The following markup sets the "foo" and "bar" properties
        of a <span class="code">Label</span> instance to "123" and "456",
        respectively:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;?import javafx.scene.control.*?&gt;
&lt;Button&gt;
    &lt;properties foo="123" bar="456"/&gt;
&lt;/Button&gt;
</code></pre>
      </div>

      <p>
        Note that a read-only property whose type is neither a
        <span class="code">List</span> nor a <span class="code">Map</span> will
        be treated as if it were a read-only map. The return value of the getter
        method will be wrapped in a <span class="code">BeanAdapter</span> and
        can be used in the same way as any other read-only map.
      </p>

      <div class="info-alert">
        <strong>HTML Analogy:</strong> In HTML, this is similar to using the
        `dataset` attribute (e.g., `data-*` attributes) to apply a map of custom
        properties to an element.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;button data-foo="123" data-bar="456"&gt;
    Click me
&lt;/button&gt;</code></pre>
      </div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/read-only-list-properties" class="btn btn-prev"
        >❮ Read-Only List Properties</router-link
      >
      <router-link to="/fxml/default-properties" class="btn btn-next"
        >Default Properties ❯</router-link
      >
    </div>
  </article>
</template>
