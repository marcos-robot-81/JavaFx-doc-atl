<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="instance_declaration_elements">Instance Declarations</a></h4>
      <p>
        If an element's tag is considered an instance declaration if the tag
        begins with uppercase letter (and the class is imported) or, as in Java,
        it denotes a fully-qualified (including the package name) name of a
        class. When the FXML loader (also introduced later) encounters such an
        element, it creates an instance of that class.
      </p>

      <p>
        Importing a class is done using the "import" processing instruction
        (PI). For example, the following PI imports the
        <span class="code">javafx.scene.control.Label</span> class into the
        current FXML document’s namespace:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;?import javafx.scene.control.Label?&gt;
</code></pre>
      </div>

      <p>
        This PI imports all classes from the javafx.scene.control package into
        the current namespace:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;?import javafx.scene.control.*?&gt;
</code></pre>
      </div>

      <p>
        Any class that adheres to JavaBean constructor and property naming
        conventions can be readily instantiated and configured using FXML. The
        following is a simple but complete example that creates an instance of
        <span class="code">javafx.scene.control.Label</span> and sets its "text"
        property to "Hello, World!":
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;?import javafx.scene.control.Label?&gt;
&lt;Label text="Hello, World!"/&gt;
</code></pre>
      </div>

      <p>
        Note that the <span class="code">Label</span>’s "text" property in this
        example is set using an XML attribute. Properties can also be set using
        nested property elements. Property elements are discussed in more detail
        later in this section. Property attributes are discussed in a later
        section.
      </p>

      <p>
        Classes that don't conform to Bean conventions can also be constructed
        in FXML, using an object called a "builder". Builders are discussed in
        more detail later.
      </p>

      <h5>Maps</h5>
      <p>
        Internally, the FXML loader uses an instance of
        <span class="code">com.sun.javafx.fxml.BeanAdapter</span> to wrap an
        instantiated object and invoke its setter methods. This (currently)
        private class implements the
        <span class="code">java.util.Map</span> interface and allows a caller to
        get and set Bean property values as key/value pairs.
      </p>

      <p>
        If an element represents a type that already implements
        <span class="code">Map</span> (such as
        <span class="code">java.util.HashMap</span>), it is not wrapped and its
        <span class="code">get()</span> and
        <span class="code">put()</span> methods are invoked directly. For
        example, the following FXML creates an instance of
        <span class="code">HashMap</span> and sets its "foo" and "bar" values to
        "123" and "456", respectively:
      </p>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;HashMap foo="123" bar="456"/&gt;
</code></pre>
      </div>

      <h5>fx:value</h5>
      <p>
        The <span class="code">fx:value</span> attribute can be used to
        initialize an instance of a type that does not have a default
        constructor but provides a static
        <span class="code">valueOf(String)</span> method. For example,
        <span class="code">java.lang.String</span> as well as each of the
        primitive wrapper types define a
        <span class="code">valueOf()</span> method and can be constructed in
        FXML as follows:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;String fx:value="Hello, World!"/&gt;
&lt;Double fx:value="1.0"/&gt;
&lt;Boolean fx:value="false"/&gt;
</code></pre>
      </div>

      <p>
        Custom classes that define a static
        <span class="code">valueOf(String)</span> method can also be constructed
        this way.
      </p>

      <h5>fx:factory</h5>
      <p>
        The <span class="code">fx:factory</span> attribute is another means of
        creating objects whose classes do not have a default constructor. The
        value of the attribute is the name of a static, no-arg factory method
        for producing class instances. For example, the following markup creates
        an instance of an observable array list, populated with three string
        values:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;FXCollections fx:factory="observableArrayList"&gt;
    &lt;String fx:value="A"/&gt;
    &lt;String fx:value="B"/&gt;
    &lt;String fx:value="C"/&gt;
&lt;/FXCollections&gt;
</code></pre>
      </div>

      <h5>Builders</h5>
      <p>
        A third means of creating instances of classes that do not conform to
        Bean conventions (such as those representing immutable values) is a
        "builder". The builder design pattern delegates object construction to a
        mutable helper class (called a "builder") that is responsible for
        manufacturing instances of the immutable type.
      </p>

      <p>
        Builder support in FXML is provided by two interfaces. The
        <span class="code">javafx.util.Builder</span> interface defines a single
        method named <span class="code">build()</span> which is responsible for
        constructing the actual object:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>public interface Builder&lt;T&gt; {
    public T build();
}
</code></pre>
      </div>

      <p>
        A <span class="code">javafx.util.BuilderFactory</span> is responsible
        for producing builders that are capable of instantiating a given type:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>public interface BuilderFactory {
    public Builder&lt;?&gt; getBuilder(Class&lt;?&gt; type);
}
</code></pre>
      </div>

      <p>
        A default builder factory,
        <span class="code">JavaFXBuilderFactory</span>, is provided in the
        <span class="code">javafx.fxml</span> package. This factory is capable
        of creating and configuring most immutable JavaFX types. For example,
        the following markup uses the default builder to create an instance of
        the immutable <span class="code">javafx.scene.paint.Color</span> class:
      </p>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;Color red="1.0" green="0.0" blue="0.0"/&gt;
</code></pre>
      </div>

      <p>
        Note that, unlike Bean types, which are constructed when the element's
        start tag is processed, objects constructed by a builder are not
        instantiated until the element's closing tag is reached. This is because
        all of the required arguments may not be available until the element has
        been fully processed. For example, the Color object in the preceding
        example could also be written as:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;Color&gt;
    &lt;red&gt;1.0&lt;/red&gt;
    &lt;green&gt;0.0&lt;/green&gt;
    &lt;blue&gt;0.0&lt;/blue&gt;
&lt;/Color&gt;
</code></pre>
      </div>

      <p>
        The <span class="code">Color</span> instance cannot be fully constructed
        until all three of the color components are known.
      </p>

      <p>
        When processing markup for an object that will be constructed by a
        builder, the <span class="code">Builder</span> instances are treated
        like value objects - if a <span class="code">Builder</span> implements
        the <span class="code">Map</span> interface, the
        <span class="code">put()</span> method is used to set the builder's
        attribute values. Otherwise, the builder is wrapped in a
        <span class="code">BeanAdapter</span> and its properties are assumed to
        be exposed via standard Bean setters.
      </p>
      <div class="info-alert">
        <strong>HTML Analogy:</strong> In HTML, typing
        <code>&lt;button&gt;</code> creates an instance of
        <code>HTMLButtonElement</code>. In FXML, typing
        <code>&lt;Button&gt;</code> creates an instance of the
        <code>javafx.scene.control.Button</code> class. Both rely on a parser to
        convert markup tags into in-memory object instances.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;!-- HTML Instance Declaration --&gt;
&lt;img src="/logo.png" alt="Logo" /&gt;
&lt;!-- This creates an HTMLImageElement in the DOM --&gt;</code></pre>
      </div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/class-instance-elements" class="btn btn-prev"
        >❮ Class Instance Elements</router-link
      >
      <router-link to="/fxml/fx-include" class="btn btn-next"
        >&lt;fx:include&gt; ❯</router-link
      >
    </div>
  </article>
</template>
