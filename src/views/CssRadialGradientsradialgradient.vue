<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4>Radial Gradients <span class="grammar" style="font-size: smaller;">
            <a id="typeradial-gradient">&lt;radial-gradient&gt;</a>
        </span></h4>
    <p class="grammar">radial-gradient([ focus-angle <a href="#typeangle" class="typelink">&lt;angle&gt;</a>,
      ]? [ focus-distance <a href="#typepercentage" class="typelink">&lt;percentage&gt;</a>,
      ]? [ center <a href="#typepoint" class="typelink">&lt;point&gt;</a>, ]?
      radius [ <a href="#typelength" class="typelink">&lt;length&gt;</a> | <a href="#typepercentage" class="typelink">&lt;percentage&gt;</a>
      ] [ [ repeat | reflect ], ]? <a href="#typecolorstop" class="typelink">&lt;color-stop&gt;</a>[,
      <a href="#typecolorstop" class="typelink">&lt;color-stop&gt;</a>]+) </p>
    <p>Radial gradient creates a gradient going though all the stop colors radiating outward from
        the <a href="#typepoint" class="typelink">center point</a>
        to the <a href="#typelength" class="typelink">radius</a>. If the center point is not given,
        the center defaults to (0,0). Percentage values are relative to the size of the area
        being filled. Percentage and length sizes can not be mixed in a single gradient function.</p>
    <p> If neither repeat nor reflect are given, then the CycleMethod defaults
      "NO_CYCLE".<br>
      Stops are per <a href="http://dev.w3.org/csswg/css3-images/#color-stop-syntax." class="typelink">W3C
        color-stop syntax</a> and are normalized accordingly. </p>
    <p>Following are examples of the use of radial-gradient:</p>
    <p class="example">radial-gradient(radius 100%, red, darkgray, black)</p>
    <p class="example">radial-gradient(focus-angle 45deg, focus-distance 20%,
      center 25% 25%, radius 50%, reflect, gray, darkgray 75%, dimgray)</p>
    <p><span style="color: #af0000; ">The following syntax for radial gradient does not
        conform to the CSS grammar and is deprecated in JavaFX 2.0. The JavaFX
        2.0 CSS parser supports the syntax but this support may be removed in
        later releases.</span></p>
    <p class="grammar"><span style="color: #af0000; ">radial [focus-angle &lt;number&gt;
        | &lt;number&gt; ] ]? [ focus-distance &lt;size&gt; ]? [ center
        &lt;size,size&gt; ]? &lt;size&gt; stops [ ( &lt;number&gt;,
        &lt;color&gt; ) ]+ [ repeat | reflect ]?</span></p>
    </section>
    <div class="pagination">
      <router-link to="/css/linear-gradients-------linear-gradient" class="btn btn-prev">❮ Linear Gradients             &lt;linear-gradient&gt;</router-link>
      <router-link to="/css/image-paint-------image-pattern" class="btn btn-next">Image Paint              &lt;image-pattern&gt; ❯</router-link>
    </div>
  </article>
</template>
