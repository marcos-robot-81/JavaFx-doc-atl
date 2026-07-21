<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4>Color Functions <span class="grammar" style="font-size: smaller;">&lt;color-function&gt;</span></h4>
    <p>JavaFX supports some color computation functions. These compute new
      colors from input colors at the time the color style is applied. This
      enables a color theme to be specified using a single base color and to
      have variant colors computed from that base color. There are two color
      functions: derive() and ladder().</p>
    <p class="grammar">&lt;derive&gt; | &lt;ladder&gt;</p>
    <p><strong>Derive </strong><span class="grammar" style="font-size: smaller;">&lt;derive&gt;</span></p>
    <p class="grammar">derive( <a href="#typecolor" class="typelink">&lt;color&gt;</a>
      , <a href="#typenumber" class="typelink">&lt;number&gt;</a>% )</p>
    <p>The derive function takes a color and computes a brighter or darker
      version of that color. The second parameter is the brightness offset,
      representing how much brighter or darker the derived color should be. Positive percentages indicate brighter colors
      and negative percentages indicate darker colors. A value of -100% means
      completely black, 0% means no change in brightness, and 100% means
      completely white.</p>
    <p><strong>Ladder</strong><span class="grammar" style="font-size: smaller;">&lt;ladder&gt;</span></p>
    <p class="grammar">ladder(<a href="#typecolor" class="typelink">&lt;color&gt;</a>
      , <a href="#typecolorstop" class="typelink">&lt;color-stop&gt;</a> [, <a href="#typecolorstop" class="typelink">&lt;color-stop&gt;</a>]+)</p>
    <p>The ladder function interpolates between colors. The effect is as if a
      gradient is created using the stops provided, and then the brightness of
      the provided <a href="#typecolor" class="typelink">&lt;color&gt;</a> is
      used to index a color value within that gradient. At 0% brightness, the
      color at the 0.0 end of the gradient is used; at 100% brightness, the
      color at the 1.0 end of the gradient is used; and at 50% brightness, the
      color at 0.5, the midway point of the gradient, is used. Note that no
      gradient is actually rendered. This is merely an interpolation function
      that results in a single color.</p>
    <p>Stops are per <a href="http://dev.w3.org/csswg/css3-images/#color-stop-syntax." class="typelink">W3C
        color-stop syntax</a> and are normalized accordingly.</p>
    <p>For example, you could use the following if you want the text color to be
      black or white depending upon the brightness of the background.</p>
    <p class="example">background: white;<br>
      -fx-text-fill: ladder(background, white 49%, black 50%);</p>
    <p>The resulting -fx-text-fill value will be black, because the background
      (white) has a brightness of 100%, and the color at 1.0 on the gradient is
      black. If we were to change the background color to black or dark grey,
      the brightness would be less than 50%, giving an -fx-text-fill value of
      white.</p>
    <p><span style="color: #af0000; ">The following syntax for ladder does not
        conform to the CSS grammar and is deprecated in JavaFX 2.0. The JavaFX
        2.0 CSS parser supports the syntax but this support may be removed in
        later releases.</span></p>
    <p class="grammar"><span style="color: #af0000; ">ladder(<a href="#typecolor" class="typelink">&lt;color&gt;</a>)
        stops [ ( <a href="#typenumber" class="typelink">&lt;number&gt;</a> , <a href="#typecolor" class="typelink">&lt;color&gt;</a>
        ) ]+ </span></p>
    </section>
    <div class="pagination">
      <router-link to="/css/hsb-colors-hsb-color" class="btn btn-prev">❮ HSB Colors &lt;hsb-color&gt;</router-link>
      <router-link to="/css/easing-function" class="btn btn-next">&lt;easing-function&gt; ❯</router-link>
    </div>
  </article>
</template>
