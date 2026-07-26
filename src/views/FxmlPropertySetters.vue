<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="property_setter_elements">Property Setters</a></h4>
      <p>
        If an element represents a property setter, the contents of the element
        (which must be either a text node or a nested class instance element)
        are passed as the value to the setter for the property.
      </p>

      <p>
        For example, the following FXML creates an instance of the
        <span class="code">Label</span> class and sets the value of the label's
        "text" property to "Hello, World!":
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;?import javafx.scene.control.Label?&gt;
&lt;Label&gt;
    &lt;text&gt;Hello, World!&lt;/text&gt;
&lt;/Label&gt;
</code></pre>
      </div>

      <p>
        This produces the same result as the earlier example which used an
        attribute to set the "text" property:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;?import javafx.scene.control.Label?&gt;
&lt;Label text="Hello, World!"/&gt;
</code></pre>
      </div>

      <p>
        Property elements are generally used when the property value is a
        complex type that can't be represented using a simple string-based
        attribute value, or when the character length of the value is so long
        that specifying it as an attribute would have a negative impact on
        readability.
      </p>

      <h5>Type Coercion</h5>
      <p>
        FXML uses "type coercion" to convert property values to the appropriate
        type as needed. Type coercion is required because the only data types
        supported by XML are elements, text, and attributes (whose values are
        also text). However, Java supports a number of different data types
        including built-in primitive value types as well as extensible reference
        types.
      </p>

      <p>
        The FXML loader uses the <span class="code">coerce()</span> method of
        <span class="code">BeanAdapter</span> to perform any required type
        conversions. This method is capable of performing basic primitive type
        conversions such as <span class="code">String</span> to
        <span class="code">boolean</span> or <span class="code">int</span> to
        <span class="code">double</span>, and will also convert
        <span class="code">String</span> to <span class="code">Class</span> or
        <span class="code">String</span> to <span class="code">Enum</span>.
        Additional conversions can be implemented by defining a static
        <span class="code">valueOf()</span> method on the target type.
      </p>

      <div class="info-alert">
        <strong>HTML Analogy:</strong> In HTML/Web Components, you might pass
        complex properties via slots or child elements instead of attributes,
        similar to how a `&lt;select&gt;` element takes `&lt;option&gt;`
        elements as its list property.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;select&gt;
    &lt;option&gt;Option 1&lt;/option&gt;
&lt;/select&gt;</code></pre>
      </div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/property-elements" class="btn btn-prev"
        >❮ Property Elements</router-link
      >
      <router-link to="/fxml/read-only-list-properties" class="btn btn-next"
        >Read-Only List Properties ❯</router-link
      >
    </div>
  </article>
</template>
