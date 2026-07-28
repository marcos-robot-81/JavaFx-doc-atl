<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h2><a id="fxmlloader">FXMLLoader</a></h2>
      <p>
        The <span class="code">FXMLLoader</span> class is responsible for
        actually loading an FXML source file and returning the resulting object
        graph. For example, the following code loads an FXML file from a
        location on the classpath relative to the loading class and localizes it
        with a resource bundle named "com.foo.example". The type of the root
        element is assumed to be a subclass of
        <span class="code">javafx.scene.layout.Pane</span>, and the document is
        assumed to define a controller of type
        <span class="code">MyController</span>:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>URL location = getClass().getResource("example.fxml");
ResourceBundle resources = ResourceBundle.getBundle("com.foo.example");
FXMLLoader fxmlLoader = new FXMLLoader(location, resources);

Pane root = (Pane)fxmlLoader.load();
MyController controller = (MyController)fxmlLoader.getController();
</code></pre>
      </div>
      <div class="javafx-preview">
        <div class="javafx-rect" style="padding: 10px; background: #282c34; color: #abb2bf; font-family: monospace; font-size: 12px;">Java Code: FXMLLoader instance creation and load</div>
      </div>

      <p>
        Note that the output of an
        <span class="code">FXMLLoader#load()</span> operation is an instance
        hierarchy that reflects the actual named classes in the document, not
        <span class="code">org.w3c.dom</span> nodes representing those classes.
        Internally, <span class="code">FXMLLoader</span> uses the
        <span class="code">javax.xml.stream</span> API (also known as the
        <i>Streaming API for XML</i>, or <i>StAX</i>) to load an FXML document.
        StAX is an extremely efficient event-based XML parsing API that is
        conceptually similar to its W3C predecessor, SAX. It allows an FXML
        document to be processed in a single pass, rather than loaded into an
        intermediate DOM structure and then post-processed.
      </p>

      <h3><a id="custom_components">Custom Components</a></h3>
      <p>
        The <span class="code">setRoot()</span> and
        <span class="code">setController()</span> methods of
        <span class="code">FXMLLoader</span> allow a caller to inject document
        root and controller values, respectively, into the document namespace,
        rather than delegating creation of these values to
        <span class="code">FXMLLoader</span> itself. This allows a developer to
        easily create reusable controls that are internally implemented using
        markup, but (from an API perspective) appear identically to controls
        implemented programmatically.
      </p>

      <p>
        For example, the following markup defines the structure of a simple
        custom control containing a <span class="code">TextField</span> and a
        <span class="code">Button</span> instance. The root container is defined
        as an instance of <span class="code">javafx.scene.layout.VBox</span>:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;?import javafx.scene.*?&gt;
&lt;?import javafx.scene.control.*?&gt;
&lt;?import javafx.scene.layout.*?&gt;

&lt;fx:root type="javafx.scene.layout.VBox" xmlns:fx="http://javafx.com/fxml"&gt;
    &lt;TextField fx:id="textField"/&gt;
    &lt;Button text="Click Me" onAction="#doSomething"/&gt;
&lt;/fx:root&gt;
</code></pre>
      </div>
      <div class="javafx-preview">
        <div class="javafx-vbox">
          <input type="text" class="javafx-textfield" />
          <button class="javafx-btn">Click Me</button>
        </div>
      </div>

      <p>
        As mentioned earlier, the <span class="code">&lt;fx:root&gt;</span> tag
        creates a reference to a previously defined root element. The value of
        this element is obtained by calling the
        <span class="code">getRoot()</span> method of
        <span class="code">FXMLLoader</span>. Prior to calling
        <span class="code">load()</span>, the caller must specify this value via
        a call to <span class="code">setRoot()</span>. The caller may similarly
        provide a value for the document's controller by calling
        <span class="code">setController()</span>, which sets the value that
        will be used as the document's controller when the document is read.
        These two methods are commonly used together when creating custom
        FXML-based components.
      </p>

      <p>
        In the following example, the
        <span class="code">CustomControl</span> class extends
        <span class="code">VBox</span> (the type declared by the
        <span class="code">&lt;fx:root&gt;</span> element), and sets itself as
        both the root and controller of the FXML document in its constructor.
        When the document is loaded, the contents of
        <span class="code">CustomControl</span> will be populated with the
        contents of the previous FXML document:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>package fxml;

import java.io.IOException;

import javafx.beans.property.StringProperty;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;

public class CustomControl extends VBox {
    @FXML private TextField textField;

    public CustomControl() {
        FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("custom_control.fxml"));
        fxmlLoader.setRoot(this);
        fxmlLoader.setController(this);

        try {
            fxmlLoader.load();
        } catch (IOException exception) {
            throw new RuntimeException(exception);
        }
    }

    public String getText() {
        return textProperty().get();
    }

    public void setText(String value) {
        textProperty().set(value);
    }

    public StringProperty textProperty() {
        return textField.textProperty();
    }

    @FXML
    protected void doSomething() {
        System.out.println("The button was clicked!");
    }
}
</code></pre>
      </div>
      <div class="javafx-preview">
        <div class="javafx-rect" style="padding: 10px; background: #282c34; color: #abb2bf; font-family: monospace; font-size: 12px;">Class: CustomControl (FXMLLoader setRoot/setController)</div>
      </div>

      <p>
        Now, callers can use instances of this control in code or in markup,
        just like any other control; e.g.:
      </p>

      <div class="caption">Java</div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>HBox hbox = new HBox();
CustomControl customControl = new CustomControl();
customControl.setText("Hello World!");
hbox.getChildren().add(customControl);
</code></pre>
      </div>
      <div class="javafx-preview">
        <div class="javafx-rect" style="padding: 10px; background: #282c34; color: #abb2bf; font-family: monospace; font-size: 12px;">Java Code: Using CustomControl</div>
      </div>

      <div class="caption">FXML</div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;HBox&gt;
    &lt;CustomControl text="Hello World!"/&gt;
&lt;/HBox&gt;
</code></pre>
      </div>
      <div class="javafx-preview">
        <div class="javafx-hbox">
          <div class="javafx-customcontrol">Hello World!</div>
        </div>
      </div>
      <div class="info-alert">
        <strong>HTML Analogy:</strong> The FXMLLoader acts like the browser's
        HTML parser (or the fetch API combined with DOM parsing) that reads an
        HTML string or file, instantiates the corresponding DOM nodes, and binds
        them to your JavaScript modules or controllers.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>async function loadComponent() {
  const response = await fetch('template.html');
  const html = await response.text();
  const parser = new DOMParser();
  const doc = parser.parseFromString(html, 'text/html');
  document.body.appendChild(doc.body.firstChild);
}
</code></pre>
      </div>
      <div class="javafx-preview">
        <div class="javafx-rect" style="padding: 10px; background: #eee; border: 1px dashed #ccc; font-size: 12px; color: #666;">JavaScript Fetch/DOMParser Example</div>
      </div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/nested-controllers" class="btn btn-prev"
        >❮ Nested Controllers</router-link
      >
      <router-link to="/fxml/custom-components" class="btn btn-next"
        >Custom Components ❯</router-link
      >
    </div>
  </article>
</template>
