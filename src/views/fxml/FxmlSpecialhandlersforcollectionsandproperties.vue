<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
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
      <div class="info-alert">
        <strong>Required Import:</strong> To use <code>&lt;VBox&gt;</code>, remember to add <code>&lt;?import javafx.scene.layout.VBox?&gt;</code> at the top of your FXML file.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;VBox fx:controller="com.foo.MyController"
    xmlns:fx="http://javafx.com/fxml"&gt;
    &lt;children onChange="#handleChildrenChange"/&gt;
&lt;/VBox&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <div class="javafx-vbox"></div>
      </JavaFxPreview>

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
      <JavaFxPreview>
        <div style="padding: 10px; border: 1px dashed #ccc; text-align: center;">MyController.java (ListChangeListener)</div>
      </JavaFxPreview>

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
      <JavaFxPreview>
        <div style="padding: 10px; border: 1px dashed #ccc; text-align: center;">MyController.java (ChangeListener)</div>
      </JavaFxPreview>

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

      <div class="info-alert">
        <strong>Required Import:</strong> To use <code>&lt;VBox&gt;</code>, remember to add <code>&lt;?import javafx.scene.layout.VBox?&gt;</code> at the top of your FXML file.
      </div>
      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;VBox fx:controller="com.foo.MyController"
    xmlns:fx="http://javafx.com/fxml" onParentChange="#handleParentChange"/&gt;
</code></pre>
      </div>
      <JavaFxPreview>
        <div class="javafx-vbox"></div>
      </JavaFxPreview>

      <p>
        Note that collections and properties do not currently support scripting
        handlers.
      </p>
      <div class="info-alert">
        <strong>HTML Analogy:</strong> In web development, listening for deep
        changes inside arrays or object properties is typically done using
        reactivity APIs rather than standard DOM events. For example, Vue uses
        the <code>watch</code> function or deeply reactive proxies to track
        mutations in collections or objects, and JavaScript has the native
        <code>Proxy</code> object or <code>MutationObserver</code> to trap and
        respond to property modifications.
      </div>
      <div class="code-block">
        <div class="code-header">Web Equivalent (Vue.js)</div>
        <pre><code>&lt;!-- Vue Reactivity Watcher --&gt;
&lt;script setup&gt;
import { reactive, watch } from 'vue'

const state = reactive({ children: [] })

watch(() =&gt; state.children, (newVal, oldVal) =&gt; {
    console.log("Children changed!");
}, { deep: true })
&lt;/script&gt;</code></pre>
      </div>
      <JavaFxPreview>
        <div style="padding: 10px; border: 1px dashed #ccc; text-align: center;">Vue Reactivity Watcher</div>
      </JavaFxPreview>
    </section>
    <div class="pagination">
      <router-link
        to="/fxml/event-handlers-from-expressions"
        class="btn btn-prev"
        >❮ Event handlers from expressions</router-link
      >
      <router-link to="/fxml/scripting" class="btn btn-next"
        >Scripting ❯</router-link
      >
    </div>
  </article>
</template>
