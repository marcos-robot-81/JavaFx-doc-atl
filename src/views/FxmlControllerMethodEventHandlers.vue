<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="controller_method_event_handlers">Controller Method Event Handlers</a></h4>
<p>A controller method event handler is a method defined by a document's
 "controller". A controller is an object that is associated with the 
deserialized contents of an FXML document and is responsible for 
coordinating the behaviors of the objects (often user interface 
elements) defined by the document.</p>

<p>A controller method event handler is specified by a leading hash symbol followed by the name of the handler method. For example:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;VBox fx:controller="com.foo.MyController"
    xmlns:fx="http://javafx.com/fxml"&gt;
    &lt;children&gt;
        &lt;Button text="Click Me!" onAction="#handleButtonAction"/&gt;
    &lt;/children&gt;
&lt;/VBox&gt;
</code></pre></div>

<p>Note the use of the <span class="code">fx:controller</span> attribute on the root element. This attribute is used to associate a controller class with the document. If <span class="code">MyController</span> is defined as follows:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>package com.foo;

public class MyController {
    public void handleButtonAction(ActionEvent event) {
        System.out.println("You clicked me!");
    }
}
</code></pre></div>

<p>the <span class="code">handleButtonAction()</span> will be called when the user presses the button, and the text "You clicked me!" will be written to the console.</p>

<p>In general, a handler method should conform to the signature of a 
standard event handler; that is, it should take a single argument of a 
type that extends <span class="code">javafx.event.Event</span> and 
should return void (similar to an event delegate in C#). The event 
argument often carries important and useful information about the nature
 of the event; however, it is optional and may be omitted if desired.
So this is also a valid handler:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>package com.foo;

public class MyController {
    public void handleButtonAction() {
        System.out.println("You clicked me!");
    }
}
</code></pre></div>

<p>Controllers are discussed in more detail in a later section.</p>
<div class="info-alert"><strong>HTML Analogy:</strong> In web development, tying an event to a method in a separate class or script is a core feature of most frontend frameworks (like Vue, React, or Angular). Instead of placing the raw logic in the HTML attribute, you reference a function (the controller method) defined in your JavaScript or TypeScript component.</div>
<div class="code-block"><div class="code-header">Web Equivalent (Vue.js)</div><pre><code>&lt;!-- Template --&gt;
&lt;button @click="handleButtonAction"&gt;Click Me!&lt;/button&gt;

&lt;!-- Script / Controller --&gt;
&lt;script setup&gt;
function handleButtonAction(event) {
    console.log("You clicked me!");
}
&lt;/script&gt;</code></pre></div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/script-event-handlers" class="btn btn-prev">❮ Script Event Handlers</router-link>
      <router-link to="/fxml/event-handlers-from-expressions" class="btn btn-next">Event handlers from expressions ❯</router-link>
    </div>
  </article>
</template>
