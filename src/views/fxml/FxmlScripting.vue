<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h2><a id="scripting">Scripting</a></h2>
      <p>
        The <span class="code">&lt;fx:script&gt;</span> tag allows a caller to
        import scripting code into or embed script within a FXML file. Any JVM
        scripting language can be used, including JavaScript, Groovy, and
        Clojure, among others. Script code is often used to define event
        handlers directly in markup or in an associated source file, since event
        handlers can often be written more concisely in more loosely-typed
        scripting languages than they can in a statically-typed language such as
        Java.
      </p>

      <p>
        <strong>Note:</strong> The JavaScript script engine is disabled by
        default. If the JDK has a JavaScript script engine, it can be enabled
        using a system property <span class="code">javafx.allowjs=true.</span>
      </p>

      <p>
        Scripts are compiled by default, when they are first loaded, if the
        <span class="code">ScriptEngine</span> implements the
        <span class="code">javax.script.Compilable</span> interface. If
        compilation fails, the <span class="code">FXMLLoader</span> will fall
        back to interpreted mode.
      </p>

      <p>
        Note: to turn off automatic compilation of script code place the
        processing instruction
        <span class="code">&lt;?compile false?&gt;</span> before the script
        element. To turn on compilation of script code again use the processing
        instruction <span class="code">&lt;?compile true?&gt;</span> (or short:
        <span class="code">&lt;?compile?&gt;</span>). The compile processing
        instruction can be used repeatedly to turn compilation of script code
        off and on.
      </p>

      <p>
        The following example markup defines a function called
        <span class="code">handleButtonAction()</span> that is called by the
        action handler attached to the <span class="code">Button</span> element:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;?language javascript?&gt;

&lt;?import javafx.scene.control.*?&gt;
&lt;?import javafx.scene.layout.*?&gt;

&lt;VBox xmlns:fx="http://javafx.com/fxml"&gt;
    &lt;fx:script&gt;

    function handleButtonAction(event) {
       java.lang.System.out.println('You clicked me!');
    }
    &lt;/fx:script&gt;

    &lt;children&gt;
        &lt;Button text="Click Me!" onAction="handleButtonAction(event);"/&gt;
    &lt;/children&gt;
&lt;/VBox&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <div class="javafx-vbox">
          <button class="javafx-btn">Click Me!</button>
        </div>
      </JavaFxPreview>

      <p>
        Clicking the button triggers the event handler, which invokes the
        function, producing output identical to the previous examples.
      </p>

      <p>
        Script code may also be defined in external files. The previous example
        could be split into an FXML file and a JavaScript source file with no
        difference in functionality:
      </p>

      <div class="caption">example.fxml</div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;?language javascript?&gt;

&lt;?import javafx.scene.control.*?&gt;
&lt;?import javafx.scene.layout.*?&gt;

&lt;VBox xmlns:fx="http://javafx.com/fxml"&gt;
    &lt;fx:script source="example.js" charset="cp1252"/&gt;

    &lt;children&gt;
        &lt;Button text="Click Me!" onAction="handleButtonAction(event);"/&gt;
    &lt;/children&gt;
&lt;/VBox&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <div class="javafx-vbox">
          <button class="javafx-btn">Click Me!</button>
        </div>
      </JavaFxPreview>

      <div class="caption">example.js</div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>
function handleButtonAction(event) {
   java.lang.System.out.println('You clicked me!');
}
</code></pre>
      </div>
      <JavaFxPreview>
        <div style="padding: 10px; border: 1px dashed #ccc; text-align: center;">example.js (Script)</div>
      </JavaFxPreview>

      <p>
        It is often preferable to separate code from markup in this way, since
        many text editors support syntax highlighting for the various scripting
        languages supported by the JVM. It can also help improve readability of
        the source code and markup.
      </p>

      <p>
        Note that script blocks are not limited to defining event handler
        functions. Script code is executed as it is processed, so it can also be
        used to dynamically configure the structure of the resulting output. As
        a simple example, the following FXML includes a script block that
        defines a variable named "labelText". The value of this variable is used
        to populate the text property of a
        <span class="code">Label</span> instance:
      </p>

      <div class="info-alert">
        <strong>Required Import:</strong> To use <code>&lt;Label&gt;</code>, remember to add <code>&lt;?import javafx.scene.control.Label?&gt;</code> at the top of your FXML file.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;fx:script&gt;
var myText = "This is the text of my label.";
&lt;/fx:script&gt;

...

&lt;Label text="$myText"/&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <span class="javafx-label">$myText</span>
      </JavaFxPreview>

      <p>
        <strong>Warning:</strong> As of JavaFX 8,
        <span class="code">importClass()</span> javascript function is no longer
        supported. You have to use fully qualified names as in the example above
        or load a nashorn compatibility script.
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>load("nashorn:mozilla_compat.js");
importClass(java.lang.System);

function handleButtonAction(event) {
   System.out.println('You clicked me!');
}
</code></pre>
      </div>
      <JavaFxPreview>
        <div style="padding: 10px; border: 1px dashed #ccc; text-align: center;">Nashorn compatibility script</div>
      </JavaFxPreview>

      <div class="info-alert">HTML Analogy</div>
      <p>
        In HTML/Web development, FXML's <code>&lt;fx:script&gt;</code> tag
        behaves just like the standard <code>&lt;script&gt;</code> tag. Inline
        scripts and external scripts using the <code>source</code> attribute map
        directly to <code>&lt;script&gt;...&lt;/script&gt;</code> and
        <code>&lt;script src="..."&gt;&lt;/script&gt;</code>. Binding an event
        handler using <code>onAction</code> works similarly to an inline
        <code>onclick</code> attribute.
      </p>
      <div class="code-block">
        <div class="code-header">Web Equivalent</div>
        <pre><code>&lt;!-- Inline Script --&gt;
&lt;script&gt;
  function handleButtonAction(event) {
    console.log('You clicked me!');
  }
&lt;/script&gt;

&lt;!-- External Script --&gt;
&lt;script src="example.js"&gt;&lt;/script&gt;

&lt;!-- Event Binding --&gt;
&lt;button onclick="handleButtonAction(event)"&gt;Click Me!&lt;/button&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <button class="javafx-btn">Click Me!</button>
      </JavaFxPreview>
    </section>
    <div class="pagination">
      <router-link
        to="/fxml/special-handlers-for-collections-and-properties"
        class="btn btn-prev"
        >❮ Special handlers for collections and properties</router-link
      >
      <router-link to="/fxml/controllers" class="btn btn-next"
        >Controllers ❯</router-link
      >
    </div>
  </article>
</template>
