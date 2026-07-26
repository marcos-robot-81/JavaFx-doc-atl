<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h2><a id="controllers">Controllers</a></h2>
      <p>
        While it can be convenient to write simple event handlers in script,
        either inline or defined in external files, it is often preferable to
        define more complex application logic in a compiled, strongly-typed
        language such as Java. As discussed earlier, the
        <span class="code">fx:controller</span> attribute allows a caller to
        associate a "controller" class with an FXML document. A controller is a
        compiled class that implements the "code behind" the object hierarchy
        defined by the document.
      </p>

      <p>
        As shown earlier, controllers are often used to implement event handlers
        for user interface elements defined in markup:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;VBox fx:controller="com.foo.MyController"
    xmlns:fx="http://javafx.com/fxml"&gt;
    &lt;children&gt;
        &lt;Button text="Click Me!" onAction="#handleButtonAction"/&gt;
    &lt;/children&gt;
&lt;/VBox&gt;
</code></pre>
      </div>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>package com.foo;

public class MyController {
    public void handleButtonAction(ActionEvent event) {
        System.out.println("You clicked me!");
    }
}
</code></pre>
      </div>

      <p>
        In many cases, it is sufficient to simply declare event handlers in this
        manner. However, when more control over the behavior of the controller
        and the elements it manages is required, the controller can define an
        <span class="code">initialize()</span> method, which will be called once
        on an implementing controller when the contents of its associated
        document have been completely loaded:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>public void initialize();
</code></pre>
      </div>

      <p>
        This allows the implementing class to perform any necessary
        post-processing on the content. It also provides the controller with
        access to the resources that were used to load the document and the
        location that was used to resolve relative paths within the document
        (commonly equivalent to the location of the document itself).
      </p>

      <p>
        For example, the following code defines an
        <span class="code">initialize()</span> method that attaches an action
        handler to a button in code rather than via an event handler attribute,
        as was done in the previous example. The button instance variable is
        injected by the loader as the document is read. The resulting
        application behavior is identical:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;VBox fx:controller="com.foo.MyController"
    xmlns:fx="http://javafx.com/fxml"&gt;
    &lt;children&gt;
        &lt;Button fx:id="button" text="Click Me!"/&gt;
    &lt;/children&gt;
&lt;/VBox&gt;
</code></pre>
      </div>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>package com.foo;

public class MyController implements Initializable {
    public Button button;

    @Override
    public void initialize(URL location, Resources resources)
        button.setOnAction(new EventHandler&lt;ActionEvent&gt;() {
            @Override
            public void handle(ActionEvent event) {
                System.out.println("You clicked me!");
            }
        });
    }
}
</code></pre>
      </div>

      <h3><a id="fxml_annotation">@FXML</a></h3>
      <p>
        Note that, in the previous examples, the controller member fields and
        event handler methods were declared as public so they can be set or
        invoked by the loader. In practice, this is not often an issue, since a
        controller is generally only visible to the FXML loader that creates it.
        However, for developers who prefer more restricted visibility for
        controller fields or handler methods, the
        <span class="code">javafx.fxml.FXML</span> annotation can be used. This
        annotation marks a protected or private class member as accessible to
        FXML. If the class being annotated is in a named module, the module
        containing that class must <span class="code">open</span> the containing
        package to at least the <span class="code">javafx.fxml</span> module.
      </p>

      <p>
        For example, the controllers from the previous examples could be
        rewritten as follows:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>package com.foo;

public class MyController {
    @FXML
    private void handleButtonAction(ActionEvent event) {
        System.out.println("You clicked me!");
    }
}
</code></pre>
      </div>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>package com.foo;

public class MyController implements Initializable {
    @FXML private Button button;

    @FXML
    protected void initialize()
        button.setOnAction(new EventHandler&lt;ActionEvent&gt;() {
            @Override
            public void handle(ActionEvent event) {
                System.out.println("You clicked me!");
            }
        });
    }
}
</code></pre>
      </div>

      <p>
        In the first version, the
        <span class="code">handleButtonAction()</span> is tagged with
        <span class="code">@FXML</span> to allow markup defined in the
        controller's document to invoke it. In the second example, the button
        field is annotated to allow the loader to set its value. The
        <span class="code">initialize()</span> method is similarly annotated.
      </p>

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

      <div class="info-alert">HTML Analogy</div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;!-- Using a JS file as a controller for HTML --&gt;
&lt;div id="app"&gt;
  &lt;button onclick="handleClick()"&gt;Click Me!&lt;/button&gt;
&lt;/div&gt;
&lt;script src="appController.js"&gt;&lt;/script&gt;
</code></pre>
      </div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/scripting" class="btn btn-prev"
        >❮ Scripting</router-link
      >
      <router-link to="/fxml/fxml" class="btn btn-next">@FXML ❯</router-link>
    </div>
  </article>
</template>
