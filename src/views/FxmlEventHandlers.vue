<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h3><a id="event_handler_attributes">Event Handlers</a></h3>
      <p>
        Event handler attributes are a convenient means of attaching behaviors
        to document elements. Any class that defines a
        <span class="code">setOn<span class="variable">Event</span>()</span>
        method can be assigned an event handler in markup.
      </p>

      <p>
        FXML supports three types of event handler attributes: script event
        handlers, controller method event handlers and expressions. Each are
        discussed below.
      </p>

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

      <h4>
        <a id="controller_method_event_handlers"
          >Controller Method Event Handlers</a
        >
      </h4>
      <p>
        A controller method event handler is a method defined by a document's
        "controller". A controller is an object that is associated with the
        deserialized contents of an FXML document and is responsible for
        coordinating the behaviors of the objects (often user interface
        elements) defined by the document.
      </p>

      <p>
        A controller method event handler is specified by a leading hash symbol
        followed by the name of the handler method. For example:
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

      <p>
        Note the use of the <span class="code">fx:controller</span> attribute on
        the root element. This attribute is used to associate a controller class
        with the document. If <span class="code">MyController</span> is defined
        as follows:
      </p>

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
        the <span class="code">handleButtonAction()</span> will be called when
        the user presses the button, and the text "You clicked me!" will be
        written to the console.
      </p>

      <p>
        In general, a handler method should conform to the signature of a
        standard event handler; that is, it should take a single argument of a
        type that extends <span class="code">javafx.event.Event</span> and
        should return void (similar to an event delegate in C#). The event
        argument often carries important and useful information about the nature
        of the event; however, it is optional and may be omitted if desired. So
        this is also a valid handler:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>package com.foo;

public class MyController {
    public void handleButtonAction() {
        System.out.println("You clicked me!");
    }
}
</code></pre>
      </div>

      <p>Controllers are discussed in more detail in a later section.</p>

      <h4><a id="expression_handlers">Event handlers from expressions</a></h4>
      <p>
        Any expression that point to a
        <a href="#variable_resolution">variable</a> of javafx.event.EventHandler
        type can be used as an expression handler.
      </p>
      <p>Previous example using an expression handler:</p>
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

      <p>
        Note that other kinds of expressions, like
        <a href="#expression_binding">binding expressions</a> are not supported
        in this context.
      </p>

      <h4>
        <a id="collections_and_property_handlers"
          >Special handlers for collections and properties</a
        >
      </h4>
      <p>
        Collections and object properties cannot be listen to using
        <span class="code">setOn<span class="variable">Event</span>()</span>
        methods. For these reason, special handler methods need to be used.
        <span class="code">ObservableList</span>,
        <span class="code">ObservableMap</span> or
        <span class="code">ObservableSet</span> uses a special
        <span class="code">onChange</span> attribute that points to a handler
        method with a <span class="code">ListChangeListener.Change</span>,
        <span class="code">MapChangeListener.Change</span> or
        <span class="code">SetChangeListener.Change</span> parameter,
        respectively.
      </p>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;VBox fx:controller="com.foo.MyController"
    xmlns:fx="http://javafx.com/fxml"&gt;
    &lt;children onChange="#handleChildrenChange"/&gt;
&lt;/VBox&gt;
</code></pre>
      </div>

      where the handler method looks like this:

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>package com.foo;

import javafx.collections.ListChangeListener.Change;

public class MyController {
    public void handleChildrenChange(ListChangeListener.Change c) {
        System.out.println("Children changed!");
    }
}
</code></pre>
      </div>

      <p>
        Similarly, the property handlers are methods that have the same
        parameters as changed method of ChangeListener :
      </p>
      <p>
        <span class="code"
          >changed(ObservableValue&lt;? extends T&gt; observable, T oldValue, T
          newValue)</span
        >
      </p>

      <p>A handler for parent property would look like this</p>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>public class MyController {
    public void handleParentChange(ObservableValue value, Parent oldValue, Parent newValue) {
        System.out.println("Parent changed!");
    }
}
</code></pre>
      </div>

      <p>
        For convenience, the first parameter can be a subclass of
        <span class="code">ObservableValue</span>, e.g.
        <span class="code">Property</span>
      </p>

      <p>
        For registering to a property, a special
        <span class="code">on&lt;propertyName&gt;Change</span> attribute must be
        used.
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;VBox fx:controller="com.foo.MyController"
    xmlns:fx="http://javafx.com/fxml" onParentChange="#handleParentChange"/&gt;
</code></pre>
      </div>

      <p>
        Note that collections and properties do not currently support scripting
        handlers.
      </p>
      <div class="info-alert">
        <strong>HTML Analogy:</strong> In HTML and Web development, attaching
        event handlers to elements is a fundamental concept for interactivity.
        You can do this inline (like <code>onclick</code>), which is akin to
        FXML script or expression handlers, or you can attach them via
        JavaScript using <code>addEventListener</code>. Similarly, modern
        frameworks like Vue or React use a declarative syntax to bind events to
        controller/component methods.
      </div>
      <div class="code-block">
        <div class="code-header">Web Equivalent</div>
        <pre><code>&lt;!-- Inline event handler --&gt;
&lt;button onclick="console.log('You clicked me!')"&gt;Click Me!&lt;/button&gt;

&lt;!-- Framework declarative handler (Vue.js) --&gt;
&lt;button @click="handleButtonAction"&gt;Click Me!&lt;/button&gt;</code></pre>
      </div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/expression-binding" class="btn btn-prev"
        >❮ Expression Binding</router-link
      >
      <router-link to="/fxml/script-event-handlers" class="btn btn-next"
        >Script Event Handlers ❯</router-link
      >
    </div>
  </article>
</template>
