<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h2>Class Instance Elements</h2>
      <p>
        Class instances can be constructed in FXML in several ways. The most
        common is via <strong>instance declaration elements</strong>, which
        simply create a new instance of a class by name. Other ways of creating
        class instances include referencing existing values, copying existing
        values, and including external FXML files. Each is discussed in more
        detail below.
      </p>

      <h3>Instance Declarations</h3>
      <p>
        An element's tag is considered an instance declaration if the tag begins
        with an uppercase letter (and the class is imported) or, as in Java, it
        denotes a fully-qualified name of a class (including the package name).
        When the FXML loader encounters such an element, it creates an instance
        of that class.
      </p>

      <p>
        Importing a class is done using the "import" processing instruction
        (PI). For example:
      </p>

      <div class="code-block">
        <div class="code-header">Example: Importing a single class</div>
        <pre><code>&lt;?import javafx.scene.control.Label?&gt;</code></pre>
      </div>
      <div class="javafx-preview">
        <!-- just illustrative for import -->
        <div class="javafx-rect" style="width: 100%; height: 20px; background: #eee; border: 1px dashed #ccc; display: flex; align-items: center; justify-content: center; font-size: 12px; color: #666;">Import: javafx.scene.control.Label</div>
      </div>

      <p>
        This PI imports all classes from the
        <code>javafx.scene.control</code> package into the current namespace:
      </p>

      <div class="code-block">
        <div class="code-header">Example: Importing a package</div>
        <pre><code>&lt;?import javafx.scene.control.*?&gt;</code></pre>
      </div>
      <div class="javafx-preview">
        <!-- just illustrative for import -->
        <div class="javafx-rect" style="width: 100%; height: 20px; background: #eee; border: 1px dashed #ccc; display: flex; align-items: center; justify-content: center; font-size: 12px; color: #666;">Import: javafx.scene.control.*</div>
      </div>

      <p>
        Any class that adheres to JavaBean constructor and property naming
        conventions can be readily instantiated and configured using FXML. The
        following is a simple but complete example that creates an instance of
        <code>javafx.scene.control.Label</code> and sets its "text" property to
        "Hello, World!":
      </p>

      <div class="code-block">
        <div class="code-header">Example: Instantiating a Label</div>
        <pre><code>&lt;?import javafx.scene.control.Label?&gt;
&lt;Label text="Hello, World!"/&gt;</code></pre>
      </div>

      <div class="javafx-preview">
        <span class="javafx-label">Hello, World!</span>
      </div>

      <h4>Maps</h4>
      <p>
        If an element represents a type that already implements
        <code>Map</code> (such as <code>java.util.HashMap</code>), it is not
        wrapped and its <code>get()</code> and <code>put()</code> methods are
        invoked directly.
      </p>

      <div class="code-block">
        <div class="code-header">Example: Using HashMap in FXML</div>
        <pre><code>&lt;HashMap foo="123" bar="456"/&gt;</code></pre>
      </div>
      <div class="javafx-preview">
        <div class="javafx-rect" style="padding: 10px; background: #f8f9fa; border: 1px solid #ddd; font-family: monospace;">
          { foo: "123", bar: "456" }
        </div>
      </div>

      <h4>fx:value</h4>
      <p>
        The <code>fx:value</code> attribute can be used to initialize an
        instance of a type that does not have a default constructor but provides
        a static <code>valueOf(String)</code> method (like String, Double,
        Boolean).
      </p>

      <div class="code-block">
        <div class="code-header">Example: Using fx:value</div>
        <pre><code>&lt;String fx:value="Hello, World!"/&gt;
&lt;Double fx:value="1.0"/&gt;
&lt;Boolean fx:value="false"/&gt;</code></pre>
      </div>
      <div class="javafx-preview">
        <div class="javafx-vbox" style="gap: 4px;">
          <div class="javafx-label">String: "Hello, World!"</div>
          <div class="javafx-label">Double: 1.0</div>
          <div class="javafx-label">Boolean: false</div>
        </div>
      </div>

      <h4>fx:factory</h4>
      <p>
        The <code>fx:factory</code> attribute is another means of creating
        objects whose classes do not have a default constructor. The value of
        the attribute is the name of a static, no-arg factory method for
        producing class instances.
      </p>

      <div class="code-block">
        <div class="code-header">Example: Using fx:factory</div>
        <pre><code>&lt;FXCollections fx:factory="observableArrayList"&gt;
    &lt;String fx:value="A"/&gt;
    &lt;String fx:value="B"/&gt;
    &lt;String fx:value="C"/&gt;
&lt;/FXCollections&gt;</code></pre>
      </div>
      <div class="javafx-preview">
        <ul style="margin: 0; padding-left: 20px; font-family: monospace;">
          <li>"A"</li>
          <li>"B"</li>
          <li>"C"</li>
        </ul>
      </div>

      <div class="info-alert">
        <strong>HTML Analogy:</strong> No FXML, a criação de uma instância de
        classe como <code>&lt;VBox&gt;</code> ou <code>&lt;Label&gt;</code> é
        equivalente a criar tags HTML normais no desenvolvimento Web. Veja o
        comparativo abaixo!
      </div>

      <div class="code-block">
        <div class="code-header">HTML Equivalente</div>
        <pre><code>&lt;!-- O equivalente em HTML puro seria a criação de um elemento do DOM e a configuração de seus atributos --&gt;
&lt;div class="vbox-layout"&gt;
    &lt;span class="label"&gt;Hello, World!&lt;/span&gt;
&lt;/div&gt;</code></pre>
      </div>
      <div class="javafx-preview">
        <div class="vbox-layout" style="display: flex; flex-direction: column; padding: 10px; border: 1px solid #ccc;">
            <span class="label" style="font-family: sans-serif;">Hello, World!</span>
        </div>
      </div>
    </section>

    <div class="pagination">
      <router-link to="/fxml/elements" class="btn btn-prev"
        >❮ Elements</router-link
      >
      <router-link to="/fxml/instance-declarations" class="btn btn-next"
        >Instance Declarations ❯</router-link
      >
    </div>
  </article>
</template>
