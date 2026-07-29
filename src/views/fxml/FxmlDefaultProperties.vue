<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="default_properties">Default Properties</a></h4>
      <p>
        A class may define a "default property" using the
        <span class="code">@DefaultProperty</span> annotation defined in the
        <span class="code">javafx.beans</span> package. If present, the
        sub-element representing the default property can be omitted from the
        markup.
      </p>

      <p>
        For example, since
        <span class="code">javafx.scene.layout.Pane</span> (the superclass of
        <span class="code">javafx.scene.layout.VBox</span>) defines a default
        property of "children", a
        <span class="code">&lt;children&gt;</span> element is not required; the
        loader will automatically add the sub-elements of the
        <span class="code">VBox</span> to the container's "children" collection:
      </p>

      <div class="info-alert">
        <strong>Required Import:</strong> To use <code>&lt;VBox&gt;</code> and <code>&lt;Button&gt;</code>, remember to add <code>&lt;?import javafx.scene.layout.VBox?&gt;</code> and <code>&lt;?import javafx.scene.control.Button?&gt;</code> at the top of your FXML file.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;?import javafx.scene.*?&gt;
&lt;?import javafx.scene.shape.*?&gt;
&lt;VBox xmlns:fx="http://javafx.com/fxml"&gt;
    &lt;Button text="Click Me!"/&gt;
    ...
&lt;/VBox&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <div class="javafx-vbox">
          <button class="javafx-btn">Click Me!</button>
          <span>...</span>
        </div>
      </JavaFxPreview>

      <p>
        Note that default properties are not limited to collections. If an
        element's default property refers to a scalar value, any sub-element of
        that element will be set as the value of the property.
      </p>

      <p>
        For example, since
        <span class="code">javafx.scene.control.ScrollPane</span> defines a
        default property of "content", a scroll pane containing a
        <span class="code">TextArea</span> as its content can be specified as
        follows:
      </p>
      <div class="info-alert">
        <strong>Required Import:</strong> To use <code>&lt;ScrollPane&gt;</code> and <code>&lt;TextArea&gt;</code>, remember to add <code>&lt;?import javafx.scene.control.ScrollPane?&gt;</code> and <code>&lt;?import javafx.scene.control.TextArea?&gt;</code> at the top of your FXML file.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;ScrollPane&gt;
    &lt;TextArea text="Once upon a time..."/&gt;
&lt;/ScrollPane&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <div class="javafx-scrollpane">
          <textarea class="javafx-textarea">Once upon a time...</textarea>
        </div>
      </JavaFxPreview>

      <p>
        Taking advantage of default properties can significantly reduce the
        verbosity of FXML markup.
      </p>

      <div class="info-alert">
        <strong>HTML Analogy:</strong> In HTML, child elements are naturally
        added to a default "children" collection of their parent node without
        needing to specify a `&lt;children&gt;` wrapper tag.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;div&gt;
    &lt;!-- Automatically added as children of the div --&gt;
    &lt;button&gt;Click Me!&lt;/button&gt;
&lt;/div&gt;</code></pre>
      </div>
      <JavaFxPreview>
        <div style="padding: 10px; border: 1px dashed #ccc;">
            <button class="javafx-btn">Click Me!</button>
        </div>
      </JavaFxPreview>
    </section>
    <div class="pagination">
      <router-link to="/fxml/read-only-map-properties" class="btn btn-prev"
        >❮ Read-Only Map Properties</router-link
      >
      <router-link to="/fxml/static-properties" class="btn btn-next"
        >Static Properties ❯</router-link
      >
    </div>
  </article>
</template>
