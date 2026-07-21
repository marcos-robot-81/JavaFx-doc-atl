<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="include_elements">&lt;fx:include&gt;</a></h4>
<p>The <span class="code">&lt;fx:include&gt;</span> tag creates an object from FXML markup defined in another file. It is used as follows:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;fx:include source="<span class="variable">filename</span>"/&gt;</code></pre></div>

<p>where <span class="variable">filename</span> is the name of the FXML 
file to include. Values that begin with a leading slash character are 
treated as relative to the classpath. Values with no leading slash are 
considered relative to the path of the current document.</p>

<p>For example, given the following markup:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;?import javafx.scene.control.*?&gt;
&lt;?import javafx.scene.layout.*?&gt;
&lt;VBox xmlns:fx="http://javafx.com/fxml"&gt;
    &lt;children&gt;
        &lt;fx:include source="my_button.fxml"/&gt;
    &lt;/children&gt;
&lt;/VBox&gt;</code></pre></div>

<p>If <span class="filename">my_button.fxml</span> contains the following:

</p><div class="code-block"><div class="code-header">Example</div><pre><code>&lt;?import javafx.scene.control.*?&gt;
&lt;Button text="My Button"/&gt;</code></pre></div>

<p>the resulting scene graph would contain a <span class="code">VBox</span> as a root object with a single <span class="code">Button</span> as a child node.</p>

<p>Note the use of the "fx" namespace prefix. This is a reserved prefix 
that defines a number of elements and attributes that are used for 
internal processing of an FXML source file. It is generally declared on 
the root element of a FXML document. Other features provided by the "fx"
 namespace are described in the following sections.</p>

<p><span class="code">&lt;fx:include&gt;</span> also supports attributes
 for specifying the name of the resource bundle that should be used to 
localize the included content, as well as the character set used to 
encode the source file. Resource resolution is discussed in a later 
section.</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;fx:include source="<span class="variable">filename</span>" resources="<span class="variable">resource_file</span>" charset="utf-8"/&gt;</code></pre></div>
      <div class="info-alert">HTML Analogy</div>
      <p>In HTML, including an external markup file into another can be achieved using an <code>&lt;iframe&gt;</code> or an <code>&lt;object&gt;</code> tag to embed the document.</p>
      <div class="code-block"><div class="code-header">Example</div><pre><code>&lt;!-- Using an iframe --&gt;
&lt;iframe src="my_button.html"&gt;&lt;/iframe&gt;

&lt;!-- Using an object --&gt;
&lt;object type="text/html" data="my_button.html"&gt;&lt;/object&gt;</code></pre></div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/instance-declarations" class="btn btn-prev">❮ Instance Declarations</router-link>
      <router-link to="/fxml/fx-constant" class="btn btn-next">&lt;fx:constant&gt; ❯</router-link>
    </div>
  </article>
</template>
