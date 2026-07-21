<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h3><a id="fxml_annotation">@FXML</a></h3>
<p>Note
that, in the previous examples, the controller member fields and
event handler methods were declared as public so they can be set
or invoked by the loader. In practice, this is not often
an issue, since a controller is generally only visible to the FXML
loader that creates it.
However, for developers who prefer more restricted
visibility for controller fields or handler methods, the <span class="code">javafx.fxml.FXML</span> annotation can be used. This
annotation marks a protected or private class member as accessible
to FXML.
If the class being annotated is in a named module, the
module containing that class must <span class="code">open</span>
the containing package to at least
the <span class="code">javafx.fxml</span> module.</p>

<p>For example, the controllers from the previous examples could be rewritten as follows:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>package com.foo;

public class MyController {
    @FXML
    private void handleButtonAction(ActionEvent event) {
        System.out.println("You clicked me!");
    }
}
</code></pre></div>

<div class="code-block"><div class="code-header">Example</div><pre><code>package com.foo;

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
</code></pre></div>

<p>In the first version, the <span class="code">handleButtonAction()</span> is tagged with <span class="code">@FXML</span>
 to allow markup defined in the controller's document to invoke it. In 
the second example, the button field is annotated to allow the loader to
 set its value. The <span class="code">initialize()</span> method is similarly annotated.</p>
<div class="info-alert"><strong>HTML Analogy:</strong> The @FXML annotation in JavaFX is similar to using the id attribute in HTML and accessing it via document.getElementById() in JavaScript, bridging the UI markup with the controller logic.</div>
<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;button id="myButton"&gt;Click Me&lt;/button&gt;
&lt;script&gt;
  const button = document.getElementById('myButton');
  button.addEventListener('click', () =&gt; console.log('You clicked me!'));
&lt;/script&gt;</code></pre></div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/controllers" class="btn btn-prev">❮ Controllers</router-link>
      <router-link to="/fxml/nested-controllers" class="btn btn-next">Nested Controllers ❯</router-link>
    </div>
  </article>
</template>
