<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h2><a id="deploy_as_module">Deploying an Application as a Module</a></h2>
<p>If <span class="code">FXMLLoader</span> is used to load types in a named
module, the application must ensure that all types that are referenced in the
FXML files, including the controller class and any custom <span class="code">Node</span>
classes, are reflectively accessible to the <span class="code">javafx.fxml</span>
module. A type is reflectively accessible if the module
<span class="code">opens</span> the containing package to at least the
<span class="code">javafx.fxml</span> module.
</p>

<p>For example, if <span class="code">com.foo.MyController</span> is in the
<span class="code">foo.app</span> module, the
<span class="code">module-info.java</span> might look like this:
</p>
<div class="code-block"><div class="code-header">Example</div><pre><code>module foo.app {
    opens com.foo to javafx.fxml;
}</code></pre></div>

<p>Alternatively, a type is reflectively accessible if the module
<span class="code">exports</span> the containing package unconditionally.
</p>
<hr>
<p>
<small><a href="http://bugreport.java.com/bugreport/">Report a bug or suggest an enhancement</a><br> Copyright © 2008, 2026, Oracle and/or its affiliates. All rights reserved.</small>
</p>
<div class="info-alert"><strong>HTML Analogy:</strong> Module access rules in Java modules are similar to CORS (Cross-Origin Resource Sharing) policies in web applications, restricting which parts of an application can interact with resources from different domains or contexts.</div>
<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;!-- Cross-Origin Policy Example --&gt;
&lt;script type="module" crossorigin="use-credentials" src="https://example.com/app.js"&gt;&lt;/script&gt;
</code></pre></div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/custom-components" class="btn btn-prev">❮ Custom Components</router-link>
    </div>
  </article>
</template>
