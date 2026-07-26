<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="script_event_handlers">Script Event Handlers</a></h4>
      <p>
        A script event handler is an event handler that executes script code
        when the event is fired, similar to event handlers in HTML. For example,
        the following script-based handler for the button's "onAction" event
        uses JavaScript to write the text "You clicked me!" to the console when
        the user presses the button:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;?language javascript?&gt;
...

&lt;VBox&gt;
    &lt;children&gt;
        &lt;Button text="Click Me!"
            onAction="java.lang.System.out.println('You clicked me!');"/&gt;
    &lt;/children&gt;
&lt;/VBox&gt;
</code></pre>
      </div>

      <p>
        Note the use of the language processing instruction at the beginning of
        the code snippet. This PI tells the FXML loader which scripting language
        should be used to execute the event handler. A page language must be
        specified whenever inline script is used in an FXML document, and can
        only be specified once per document. However, this does not apply to
        external scripts, which may be implemented using any number of supported
        scripting languages. Scripting is discussed in more detail in the next
        section.
      </p>

      <p>
        Note: to turn off automatic compilation of script code place the
        processing instruction
        <span class="code">&lt;?compile false?&gt;</span> before the element
        that contains the script. To turn on compilation of script code again
        use the processing instruction
        <span class="code">&lt;?compile true?&gt;</span> (or short:
        <span class="code">&lt;?compile?&gt;</span>). The compile processing
        instruction can be used repeatedly to turn compilation of script code
        off and on.
      </p>

      <p>
        <strong>Note:</strong> The JavaScript script engine is disabled by
        default. If the JDK has a JavaScript script engine, it can be enabled
        using a system property <span class="code">javafx.allowjs=true.</span>
      </p>
      <div class="info-alert">
        <strong>HTML Analogy:</strong> Script event handlers in FXML are
        directly analogous to inline JavaScript event handlers in HTML. Both
        allow you to embed executable script logic directly within the markup
        attribute.
      </div>
      <div class="code-block">
        <div class="code-header">Web Equivalent</div>
        <pre><code>&lt;button onclick="console.log('You clicked me!');"&gt;Click Me!&lt;/button&gt;</code></pre>
      </div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/event-handlers" class="btn btn-prev"
        >❮ Event Handlers</router-link
      >
      <router-link
        to="/fxml/controller-method-event-handlers"
        class="btn btn-next"
        >Controller Method Event Handlers ❯</router-link
      >
    </div>
  </article>
</template>
