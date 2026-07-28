<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h3><a id="nested_controllers">Nested Controllers</a></h3>
      <p>
        Controller instances for nested FXML documents loaded via the
        <span class="code">&lt;fx:include&gt;</span>
        element are mapped directly to member fields of the including
        controller. This allows a developer to easily access functionality
        defined by an include (such as a dialog window presented by an
        application's main window controller). For example, given the following
        code:
      </p>
      <div class="caption">main_window_content.fxml</div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;VBox fx:controller="com.foo.MainController"&gt;
   &lt;fx:define&gt;
      &lt;fx:include fx:id="dialog" source="dialog.fxml"/&gt;
   &lt;/fx:define&gt;
   ...
&lt;/VBox&gt;
</code></pre>
      </div>
      <div class="javafx-preview">
        <div class="javafx-vbox">...</div>
      </div>

      <div class="caption">MainController.java</div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>public class MainController extends Controller {
    @FXML private Window dialog;
    @FXML private DialogController dialogController;

    ...
}
</code></pre>
      </div>
      <div class="javafx-preview">
        <div class="javafx-vbox" style="padding: 10px; border: 1px dashed #ccc; text-align: center;">
          MainController (Java)
        </div>
      </div>

      <p>
        when the controller's <span class="code">initialize()</span> method is
        called, the <span class="code">dialog</span> field will contain the root
        element loaded from the "dialog.fxml" include, and the
        <span class="code">dialogController</span> field will contain the
        include's controller. The main controller can then invoke methods on the
        included controller, to populate and show the dialog, for example. Note
        that as the content of the file referenced by fx:include otherwise would
        become part of the scene graph spanned from main_window_content.fxml, it
        is necessary to wrap fx:include by fx:define to separate the scene
        graphs of both windows.
      </p>
      <div class="info-alert">
        <strong>HTML Analogy:</strong> Nested controllers in JavaFX act much
        like Web Components or iframe imports in HTML, where a parent page can
        reference and interact with a distinct, encapsulated sub-component or
        child document.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;!-- Parent HTML --&gt;
&lt;div id="mainApp"&gt;
  &lt;my-dialog id="dialogComponent"&gt;&lt;/my-dialog&gt;
&lt;/div&gt;
&lt;script&gt;
  const dialog = document.getElementById('dialogComponent');
  dialog.showModal();
&lt;/script&gt;</code></pre>
      </div>
      <div class="javafx-preview">
        <div style="border: 1px solid #ccc; padding: 10px;">
          <strong>mainApp</strong>
          <div style="border: 1px dashed #007bff; padding: 10px; margin-top: 10px;">
            my-dialog (dialogComponent)
          </div>
        </div>
      </div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/fxml" class="btn btn-prev">❮ @FXML</router-link>
      <router-link to="/fxml/fxmlloader" class="btn btn-next"
        >FXMLLoader ❯</router-link
      >
    </div>
  </article>
</template>
