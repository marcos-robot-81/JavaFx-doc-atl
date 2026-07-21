<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4>Image Paint <span class="grammar" style="font-size: smaller;">
            <a id="typeimage-pattern">&lt;image-pattern&gt;</a>
        </span></h4>
    <p class="grammar">image-pattern(<a href="#typestring" class="typelink">&lt;string&gt;</a>,
      [<a href="#typesize" class="typelink">&lt;size&gt;</a>,
      <a href="#typesize" class="typelink">&lt;size&gt;</a>,
      <a href="#typesize" class="typelink">&lt;size&gt;</a>,
      <a href="#typesize" class="typelink">&lt;size&gt;</a>[,
      <a href="#typeboolean" class="typelink">&lt;boolean&gt;</a>]?]?)</p>
    <p>The parameters, in order, are:<br>
    </p><p style="margin-left: 40px;">
    <span class="grammar"><a href="#typestring" class="typelink">&lt;string&gt;</a></span>
      The URL of the image.<br>
      <span class="grammar"><a href="#typesize" class="typelink">&lt;size&gt;</a></span>
      The <span style="font-style:italic;">x</span> origin of the anchor rectangle.<br>
      <span class="grammar"><a href="#typesize" class="typelink">&lt;size&gt;</a></span>
      The <span style="font-style: italic;">y</span> origin of the anchor rectangle.<br>
      <span class="grammar"><a href="#typesize" class="typelink">&lt;size&gt;</a></span>
      The width of the anchor rectangle.<br>
      <span class="grammar"><a href="#typesize" class="typelink">&lt;size&gt;</a></span>
      The height of the anchor rectangle.<br>
      <span class="grammar"><a href="#typeboolean" class="typelink">&lt;boolean&gt;</a></span>
      The proportional flag which indicates whether start and end locations are proportional or absolute<br>
    </p>
    <p>For a full explanation of the parameters, refer to the
        <a href="https://openjfx.io/javadoc/26/javafx.graphics/javafx/scene/paint/ImagePattern.html" class="typelink">ImagePattern</a> javadoc.</p>
    <p>Following are examples of the use of image-pattern:</p>
    <p class="example">image-pattern("images/Duke.png")</p>
    <p class="example">image-pattern("images/Duke.png", 20%, 20%, 80%, 80%)</p>
    <p class="example">image-pattern("images/Duke.png", 20%, 20%, 80%, 80%, true)</p>
    <p class="example">image-pattern("images/Duke.png", 20, 20, 80, 80, false)</p>

    <p>Related, there is the <code>repeating-image-pattern</code> function which is a shorthand
    for producing tiled image based fills. It is equivalent to
    </p><p class="example">image-pattern("images/Duke.png", 0, 0, imageWidth, imageHeight, false)</p>

    <p class="grammar">repeating-image-pattern(<a href="#typestring" class="typelink">&lt;string&gt;</a>)</p>
    <p>The only parameter is the uri of the image. Following is an example of the use of image-pattern:</p>
    <p class="example">repeating-image-pattern("com/mycompany/myapp/images/Duke.png")</p>
    </section>
    <div class="pagination">
      <router-link to="/css/radial-gradients-------radial-gradient" class="btn btn-prev">❮ Radial Gradients              &lt;radial-gradient&gt;</router-link>
      <router-link to="/css/color" class="btn btn-next">&lt;color&gt; ❯</router-link>
    </div>
  </article>
</template>
