<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h3><a id="static_property_elements">Static Properties</a></h3>
      <p>
        An element may also represent a "static" property (sometimes called an
        "attached property"). Static properties are properties that only make
        sense in a particular context. They are not intrinsic to the class to
        which they are applied, but are defined by another class (often, the
        parent container of a control).
      </p>

      <p>
        Static properties are prefixed with the name of class that defines them.
        For example, The following FXML invokes the static setter for
        <span class="code">GridPane</span>'s "rowIndex" and "columnIndex"
        properties:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;GridPane&gt;
    &lt;children&gt;
        &lt;Label text="My Label"&gt;
            &lt;GridPane.rowIndex&gt;0&lt;/GridPane.rowIndex&gt;
       &lt;GridPane.columnIndex&gt;0&lt;/GridPane.columnIndex&gt;
        &lt;/Label&gt;
    &lt;/children&gt;
&lt;/GridPane&gt;
</code></pre>
      </div>
      <div class="javafx-preview">
        <div class="javafx-gridpane" style="display: grid;">
          <span class="javafx-label" style="grid-row: 1; grid-column: 1;">My Label</span>
        </div>
      </div>

      <p>This translates roughly to the following in Java:</p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>GridPane gridPane = new GridPane();

Label label = new Label();
label.setText("My Label");

GridPane.setRowIndex(label, 0);
GridPane.setColumnIndex(label, 0);

gridPane.getChildren().add(label);
</code></pre>
      </div>
      <div class="javafx-preview">
        <div class="javafx-gridpane" style="display: grid;">
          <span class="javafx-label" style="grid-row: 1; grid-column: 1;">My Label</span>
        </div>
      </div>

      <p>
        The calls to <span class="code">GridPane#setRowIndex()</span> and
        <span class="code">GridPane#setColumnIndex()</span> "attach" the index
        data to the <span class="code">Label</span> instance.
        <span class="code">GridPane</span> then uses these during layout to
        arrange its children appropriately. Other containers, including
        <span class="code">AnchorPane</span>,
        <span class="code">BorderPane</span>, and
        <span class="code">StackPane</span>, define similar properties.
      </p>

      <p>
        As with instance properties, static property elements are generally used
        when the property value cannot be efficiently represented by an
        attribute value. Otherwise, static property attributes (discussed in a
        later section) will generally produce more concise and readable markup.
      </p>

      <div class="info-alert">
        <strong>HTML Analogy:</strong> In HTML/CSS, CSS Grid or Flexbox allows
        children to define properties that only make sense in the context of
        their parent container (like `grid-row`, `grid-column`, or `align-self`
        via style attributes or classes).
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;div style="display: grid;"&gt;
    &lt;label style="grid-row: 1; grid-column: 1;"&gt;My Label&lt;/label&gt;
&lt;/div&gt;</code></pre>
      </div>
      <div class="javafx-preview">
        <div style="display: grid;">
          <label style="grid-row: 1; grid-column: 1;">My Label</label>
        </div>
      </div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/default-properties" class="btn btn-prev"
        >❮ Default Properties</router-link
      >
      <router-link to="/fxml/define-blocks" class="btn btn-next"
        >Define Blocks ❯</router-link
      >
    </div>
  </article>
</template>
