<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4>
        <a id="read_only_list_property_elements">Read-Only List Properties</a>
      </h4>
      <p>
        A read-only list property is a Bean property whose getter returns an
        instance of <span class="code">java.util.List</span> and has no
        corresponding setter method. The contents of a read-only list element
        are automatically added to the list as they are processed.
      </p>

      <p>
        For example, the "children" property of
        <span class="code">javafx.scene.Group</span> is a read-only list
        property representing the group's child nodes:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;?import javafx.scene.*?&gt;
&lt;?import javafx.scene.shape.*?&gt;
&lt;Group xmlns:fx="http://javafx.com/fxml"&gt;
    &lt;children&gt;
        &lt;Rectangle fx:id="rectangle" x="10" y="10" width="320" height="240"
            fill="#ff0000"/&gt;
        ...
    &lt;/children&gt;
&lt;/Group&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <div class="javafx-group">
          <div class="javafx-rectangle" style="width: 320px; height: 240px; background-color: #ff0000;"></div>
          <span>...</span>
        </div>
      </JavaFxPreview>

      <p>
        As each sub-element of the
        <span class="code">&lt;children&gt;</span> element is read, it is added
        to the list returned by <span class="code">Group#getChildren()</span>.
      </p>

      <div class="info-alert">
        <strong>HTML Analogy:</strong> In HTML, a `&lt;ul&gt;` or `&lt;ol&gt;`
        element acts like a read-only list property for list items
        (`&lt;li&gt;`). The parent provides the collection, and you simply add
        children to populate it.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;ul&gt;
    &lt;li&gt;First item&lt;/li&gt;
    &lt;li&gt;Second item&lt;/li&gt;
&lt;/ul&gt;</code></pre>
      </div>
      <JavaFxPreview>
        <ul>
          <li>First item</li>
          <li>Second item</li>
        </ul>
      </JavaFxPreview>
    </section>
    <div class="pagination">
      <router-link to="/fxml/property-setters" class="btn btn-prev"
        >❮ Property Setters</router-link
      >
      <router-link to="/fxml/read-only-map-properties" class="btn btn-next"
        >Read-Only Map Properties ❯</router-link
      >
    </div>
  </article>
</template>
