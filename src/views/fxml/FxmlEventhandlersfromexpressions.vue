<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="expression_handlers">Event handlers from expressions</a></h4>
      <p>
        Any expression that point to a
        <a href="#variable_resolution">variable</a> of javafx.event.EventHandler
        type can be used as an expression handler.
      </p>
      <p>Previous example using an expression handler:</p>
      <div class="info-alert">
        <strong>Required Import:</strong> To use <code>&lt;VBox&gt;</code> and <code>&lt;Button&gt;</code>, remember to add <code>&lt;?import javafx.scene.layout.VBox?&gt;</code> and <code>&lt;?import javafx.scene.control.Button?&gt;</code> at the top of your FXML file.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;VBox fx:controller="com.foo.MyController"
    xmlns:fx="http://javafx.com/fxml"&gt;
    &lt;children&gt;
        &lt;Button text="Click Me!" onAction="$controller.onActionHandler"/&gt;
    &lt;/children&gt;
&lt;/VBox&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <div class="javafx-vbox">
          <button class="javafx-btn">Click Me!</button>
        </div>
      </JavaFxPreview>

      <p>With the controller that contains a field like this</p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>public class MyController {

    @FXML
    public EventHandler&lt;ActionEvent&gt; onActionHandler = new EventHandler&lt;&gt;() { ... }

    ...
}
</code></pre>
      </div>
      <JavaFxPreview>
        <div class="javafx-rect" style="padding: 10px; background: #282c34; color: #abb2bf; font-family: monospace; font-size: 12px;">Class: MyController (onActionHandler field)</div>
      </JavaFxPreview>

      <p>
        Note that other kinds of expressions, like
        <a href="#expression_binding">binding expressions</a> are not supported
        in this context.
      </p>
      <div class="info-alert">
        <strong>HTML Analogy:</strong> Binding an event handler using an
        expression is equivalent to passing a function reference to an event
        listener. In modern web frameworks like React or Vue, you frequently
        pass references to functions (or expressions that evaluate to a
        function) directly into the component's event attribute.
      </div>
      <div class="code-block">
        <div class="code-header">Web Equivalent (React)</div>
        <pre><code>&lt;!-- React JSX --&gt;
&lt;button onClick={this.onActionHandler}&gt;Click Me!&lt;/button&gt;</code></pre>
      </div>
      <JavaFxPreview>
        <div style="padding: 10px; border: 1px dashed #ccc;">
            <button class="javafx-btn">Click Me!</button>
        </div>
      </JavaFxPreview>
    </section>
    <div class="pagination">
      <router-link
        to="/fxml/controller-method-event-handlers"
        class="btn btn-prev"
        >❮ Controller Method Event Handlers</router-link
      >
      <router-link
        to="/fxml/special-handlers-for-collections-and-properties"
        class="btn btn-next"
        >Special handlers for collections and properties ❯</router-link
      >
    </div>
  </article>
</template>
