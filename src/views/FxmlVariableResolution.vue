<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="variable_resolution">Variable Resolution</a></h4>
      <p>
        An FXML document defines a variable namespace in which named elements
        and script variables may be uniquely identified. The variable resolution
        operator allows a caller to replace an attribute value with an instance
        of a named object before the corresponding setter method is invoked.
        Variable references are identified by a "$" prefix, as shown below:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;fx:define&gt;
    &lt;ToggleGroup fx:id="myToggleGroup"/&gt;
&lt;/fx:define&gt;
...
&lt;RadioButton text="A" toggleGroup="$myToggleGroup"/&gt;
&lt;RadioButton text="B" toggleGroup="$myToggleGroup"/&gt;
&lt;RadioButton text="C" toggleGroup="$myToggleGroup"/&gt;
</code></pre>
      </div>

      <p>
        Assigning an <span class="code">fx:id</span> value to an element creates
        a variable in the document's namespace that can later be referred to by
        variable dereference attributes, such as the "toggleGroup" attribute
        shown above, or in script code, discussed in a later section.
        Additionally, if the object's type defines an "id" property, this value
        will also be passed to the objects
        <span class="code">setId()</span> method.
      </p>
      <div class="info-alert">
        <strong>HTML Analogy:</strong> In HTML, elements can be referenced by
        their <code>id</code> attribute, often used in forms with the
        <code>for</code> attribute, or accessed via JavaScript.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code class="language-html">&lt;!-- HTML Analogy for Variable Resolution --&gt;
&lt;input type="radio" id="myToggleGroup" name="group1" /&gt;
&lt;label for="myToggleGroup"&gt;Option A&lt;/label&gt;
</code></pre>
      </div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/resource-resolution" class="btn btn-prev"
        >❮ Resource Resolution</router-link
      >
      <router-link to="/fxml/escape-sequences" class="btn btn-next"
        >Escape Sequences ❯</router-link
      >
    </div>
  </article>
</template>
