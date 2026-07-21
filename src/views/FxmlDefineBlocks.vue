<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h3><a id="define_elements">Define Blocks</a></h3>
<p>The <span class="code">&lt;fx:define&gt;</span> element is used to create objects that exist outside of the object hierarchy but may need to be referred to elsewhere.</p>

<p>For example, when working with radio buttons, it is common to define a <span class="code">ToggleGroup</span>
 that will manage the buttons' selection state. This group is not part 
of the scene graph itself, so should not be added to the buttons' 
parent. A define block can be used to create the button group without 
interfering with the overall structure of the document:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;VBox&gt;
    &lt;fx:define&gt;
        &lt;ToggleGroup fx:id="myToggleGroup"/&gt;
    &lt;/fx:define&gt;
    &lt;children&gt;
        &lt;RadioButton text="A" toggleGroup="$myToggleGroup"/&gt;
        &lt;RadioButton text="B" toggleGroup="$myToggleGroup"/&gt;
        &lt;RadioButton text="C" toggleGroup="$myToggleGroup"/&gt;
    &lt;/children&gt;
&lt;/VBox&gt;
</code></pre></div>

<p>Elements in define blocks are usually assigned an ID that can be used
 to refer to the element's value later. IDs are discussed in more detail
 in later sections.</p>

      <div class="info-alert"><strong>HTML Analogy:</strong> In HTML, the `&lt;template&gt;` tag or elements hidden in an SVG `&lt;defs&gt;` are used to define objects or structures that aren't rendered immediately but can be referenced or instantiated elsewhere.</div>
      <div class="code-block"><div class="code-header">Example</div><pre><code>&lt;svg&gt;
    &lt;defs&gt;
        &lt;linearGradient id="myGradient"&gt;...&lt;/linearGradient&gt;
    &lt;/defs&gt;
    &lt;rect fill="url(#myGradient)" /&gt;
&lt;/svg&gt;</code></pre></div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/static-properties" class="btn btn-prev">❮ Static Properties</router-link>
      <router-link to="/fxml/attributes" class="btn btn-next">Attributes ❯</router-link>
    </div>
  </article>
</template>
