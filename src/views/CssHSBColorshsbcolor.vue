<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4>HSB Colors <span class="grammar" style="font-size: smaller;">&lt;hsb-color&gt;</span></h4>
    <p>Colors can be specified using the HSB (sometimes called HSV) color model,
      as follows:</p>
    <p class="grammar">hsb( <a href="#typenumber" class="typelink">&lt;number&gt;</a>
      , <a href="#typenumber" class="typelink">&lt;number&gt;</a>% , <a href="#typenumber" class="typelink">&lt;number&gt;</a>%
      ) | hsba( <a href="#typenumber" class="typelink">&lt;number&gt;</a> , <a href="#typenumber" class="typelink">&lt;number&gt;</a>%
      , <a href="#typenumber" class="typelink">&lt;number&gt;</a>% , <a href="#typenumber" class="typelink">&lt;number&gt;</a>
      )</p>
    <p>The first number is <span style="font-style:italic;">hue</span>, a number in the range 0 to 360
      degrees. The second number is <em>saturation,</em> a percentage in the
      range 0% to 100%. The third number is <span style="font-style:italic;">brightness</span>, also a
      percentage in the range 0% to 100%. The hsba(...) form takes a fourth
      parameter at the end which is a alpha value in the range 0.0 to 1.0,
      specifying completely transparent and completely opaque, respectively.</p>
    </section>
    <div class="pagination">
      <router-link to="/css/rgb-colors-rgb-color" class="btn btn-prev">❮ RGB Colors &lt;rgb-color&gt;</router-link>
      <router-link to="/css/color-functions-color-function" class="btn btn-next">Color Functions &lt;color-function&gt; ❯</router-link>
    </div>
  </article>
</template>
