<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="resource_resolution">Resource Resolution</a></h4>

<p>In FXML, resource substitution can be performed at load time for localization purposes. When provided with an instance of <span class="code">java.util.ResourceBundle</span>,
 the FXML loader will replace instances of resource names with their 
locale-specific values. Resource names are identified by a "%" prefix, 
as shown below:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;Label text="%myText"/&gt;
</code></pre></div>

<p>If the loader is given a resource bundle defined as follows:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>myText = This is the text!
</code></pre></div>


<p>the output of the FXML loader would be a <span class="code">Label</span> instance containing the text "This is the text!".</p>
      <div class="info-alert"><strong>HTML Analogy:</strong> In HTML/Web environments, localization is typically handled by a templating engine or framework (like i18n in Vue, React, or Jinja) injecting variables, often using a specific syntax to look up translations.</div>
      <div class="code-block"><div class="code-header">Example</div><pre><code class="language-html">&lt;!-- Web Analogy for Resource Resolution (using a template engine) --&gt;
&lt;span&gt;{{ $t('myText') }}&lt;/span&gt;
</code></pre></div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/location-resolution" class="btn btn-prev">❮ Location Resolution</router-link>
      <router-link to="/fxml/variable-resolution" class="btn btn-next">Variable Resolution ❯</router-link>
    </div>
  </article>
</template>
