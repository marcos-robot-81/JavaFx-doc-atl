<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h3><a id="custom_components">Custom Components</a></h3>
<p>The <span class="code">setRoot()</span> and <span class="code">setController()</span> methods of <span class="code">FXMLLoader</span>
 allow a caller to inject document root and controller values, 
respectively, into the document namespace, rather than delegating 
creation of these values to <span class="code">FXMLLoader</span> itself.
 This allows a developer to easily create reusable controls that are 
internally implemented using markup, but (from an API perspective) 
appear identically to controls implemented programmatically.</p>

<p>For example, the following markup defines the structure of a simple custom control containing a <span class="code">TextField</span> and a <span class="code">Button</span> instance. The root container is defined as an instance of <span class="code">javafx.scene.layout.VBox</span>:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;?import javafx.scene.*?&gt;
&lt;?import javafx.scene.control.*?&gt;
&lt;?import javafx.scene.layout.*?&gt;

&lt;fx:root type="javafx.scene.layout.VBox" xmlns:fx="http://javafx.com/fxml"&gt;
    &lt;TextField fx:id="textField"/&gt;
    &lt;Button text="Click Me" onAction="#doSomething"/&gt;
&lt;/fx:root&gt;
</code></pre></div>

<p>As mentioned earlier, the <span class="code">&lt;fx:root&gt;</span> tag creates a reference to a previously defined root element. The value of this element is obtained by calling the <span class="code">getRoot()</span> method of <span class="code">FXMLLoader</span>. Prior to calling <span class="code">load()</span>, the caller must specify this value via a call to <span class="code">setRoot()</span>. The caller may similarly provide a value for the document's controller by calling <span class="code">setController()</span>,
 which sets the value that will be used as the document's controller 
when the document is read. These two methods are commonly used together 
when creating custom FXML-based components.</p>

<p>In the following example, the <span class="code">CustomControl</span> class extends <span class="code">VBox</span> (the type declared by the <span class="code">&lt;fx:root&gt;</span>
 element), and sets itself as both the root and controller of the FXML 
document in its constructor. When the document is loaded, the contents 
of <span class="code">CustomControl</span> will be populated with the contents of the previous FXML document:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>package fxml;

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
</code></pre></div>

<p>Now, callers can use instances of this control in code or in markup, just like any other control; e.g.:</p>

<div class="caption">Java</div>
<div class="code-block"><div class="code-header">Example</div><pre><code>HBox hbox = new HBox();
CustomControl customControl = new CustomControl();
customControl.setText("Hello World!");
hbox.getChildren().add(customControl);
</code></pre></div>

<div class="caption">FXML</div>
<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;HBox&gt;
    &lt;CustomControl text="Hello World!"/&gt;
&lt;/HBox&gt;
</code></pre></div>
<div class="info-alert"><strong>HTML Analogy:</strong> Custom components in FXML are conceptually identical to Web Components (Custom Elements) in HTML, where you define a reusable tag with its own encapsulated structure and behavior.</div>
<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;!-- Using a Custom Element in HTML --&gt;
&lt;custom-control text="Hello World!"&gt;&lt;/custom-control&gt;
&lt;script&gt;
  class CustomControl extends HTMLElement {
    connectedCallback() {
      this.innerHTML = `&lt;input type="text"&gt;&lt;button&gt;Click Me&lt;/button&gt;`;
    }
  }
  customElements.define('custom-control', CustomControl);
&lt;/script&gt;</code></pre></div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/fxmlloader" class="btn btn-prev">❮ FXMLLoader</router-link>
      <router-link to="/fxml/deploying-an-application-as-a-module" class="btn btn-next">Deploying an Application as a Module ❯</router-link>
    </div>
  </article>
</template>
