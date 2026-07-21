<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="location_resolution">Location Resolution</a></h4>
<p>As strings, XML attributes cannot natively represent typed location 
information such as a URL. However, it is often necessary to specify 
such locations in markup; for example, the source of an image resource. 
The location resolution operator (represented by an "@" prefix to the 
attribute value) is used to specify that an attribute value should be 
treated as a location relative to the current file rather than a simple 
string.</p>

<p>For example, the following markup creates an ImageView and populates it with image data from <span class="filename">my_image.png</span>, which is assumed to be located at a path relative to the current FXML file:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;ImageView&gt;
    &lt;image&gt;
        &lt;Image url="@my_image.png"/&gt;
    &lt;/image&gt;
&lt;/ImageView&gt;
</code></pre></div>

<p>Since <span class="code">Image</span> is an immutable object, a builder is required to construct it. Alternatively, if <span class="code">Image</span> were to define a <span class="code">valueOf(URL)</span> factory method, the image view could be populated as follows:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;ImageView image="@my_image.png"/&gt;
</code></pre></div>

<p>The value of the "image" attribute would be converted to a URL by the FXML loader, then coerced to an <span class="code">Image</span> using the <span class="code">valueOf()</span> method.</p>

<p>Note that whitespace values in the URL must be encoded; for example, 
to refer to a file named "My Image.png", the FXML document should 
contain the following:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;Image url="@My%20Image.png"/&gt;
</code></pre></div>

<p>rather than:</p>

<div class="code-block"><div class="code-header">Example</div><pre><code>&lt;Image url="@My Image.png"/&gt;
</code></pre></div>
      <div class="info-alert"><strong>HTML Analogy:</strong> In HTML, using relative paths for assets like images, scripts, or stylesheets resolves to the location of the HTML file.</div>
      <div class="code-block"><div class="code-header">Example</div><pre><code class="language-html">&lt;!-- HTML Analogy for Location Resolution --&gt;
&lt;img src="/my_image.png" alt="Relative image" /&gt;
</code></pre></div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/instance-properties" class="btn btn-prev">❮ Instance Properties</router-link>
      <router-link to="/fxml/resource-resolution" class="btn btn-next">Resource Resolution ❯</router-link>
    </div>
  </article>
</template>
