<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4>
        Linear Gradients<span class="grammar" style="font-size: smaller">
          <a id="typelinear-gradient">&lt;linear-gradient&gt;</a>
        </span>
      </h4>
      <p class="grammar">
        linear-gradient( [ [from
        <a href="#typepoint" class="typelink">&lt;point&gt;</a> to
        <a href="#typepoint" class="typelink">&lt;point&gt;</a>] | [ to
        &lt;side-or-corner&gt;], ]? [ [ repeat | reflect ], ]?
        <a href="#typecolorstop" class="typelink">&lt;color-stop&gt;</a>[,
        <a href="#typecolorstop" class="typelink">&lt;color-stop&gt;</a>]+)
        <br />
        <br />
        where &lt;side-or-corner&gt; = [left | right] || [top | bottom]
      </p>
      <p>&nbsp;</p>
      <p>
        Linear gradient creates a gradient going though all the stop colors
        along the line between the "from"
        <a href="#typepoint" class="typelink">&lt;point&gt;</a> and the "to"
        <a href="#typepoint" class="typelink">&lt;point&gt;</a>. If the points
        are percentages, then they are relative to the size of the area being
        filled. Percentage and length sizes can not be mixed in a single
        gradient function.
      </p>
      <p>
        If neither repeat nor reflect are given, then the CycleMethod defaults
        "NO_CYCLE".<br />
        If neither [from &lt;point&gt; to &lt;point&gt;] nor [ to
        &lt;side-or-corner&gt; ] are given, then the gradient direction defaults
        to 'to bottom'.<br />
        Stops are per
        <a
          href="http://dev.w3.org/csswg/css3-images/#color-stop-syntax."
          class="typelink"
          >W3C color-stop syntax</a
        >
        and are normalized accordingly.
      </p>
      <p>
        This example will create a gradient from top left to bottom right of the
        filled area with red at the top left corner and black at the bottom
        right.
      </p>
      <p class="example">linear-gradient(to bottom right, red, black)</p>
      <JavaFxPreview>
        <div class="javafx-rect" style="background: linear-gradient(to bottom right, red, black); width: 200px; height: 100px; border: 1px solid #ccc;"></div>
      </JavaFxPreview>
      <p>This is equivalent to:</p>
      <p class="example">
        linear-gradient(from 0% 0% to 100% 100%, red 0%, black 100%)
      </p>
      <JavaFxPreview>
        <div class="javafx-rect" style="background: linear-gradient(to bottom right, red 0%, black 100%); width: 200px; height: 100px; border: 1px solid #ccc;"></div>
      </JavaFxPreview>
      <p>
        This more complex example will create a 50px high bar at the top with a
        3 color gradient with white underneath for the rest of the filled area.
      </p>
      <p class="example">
        linear-gradient(from 0px 0px to 0px 50px, gray, darkgray 50%, dimgray
        99%, white)
      </p>
      <JavaFxPreview>
        <div class="javafx-rect" style="background: linear-gradient(to bottom, gray, darkgray 50%, dimgray 99%, white); width: 200px; height: 100px; border: 1px solid #ccc;"></div>
      </JavaFxPreview>
      <p>
        <span style="color: #af0000"
          >The following syntax for linear gradient does not conform to the CSS
          grammar and is deprecated in JavaFX 2.0. The JavaFX 2.0 CSS parser
          supports the syntax but this support may be removed in later
          releases.</span
        >
      </p>
      <p class="grammar">
        <span style="color: #af0000"
          >linear (&lt;size&gt;, &lt;size&gt;) to (&lt;size&gt;, &lt;size&gt;)
          stops [ (&lt;number&gt;,&lt;color&gt;) ]+ [ repeat | reflect ]?</span
        >
      </p>
    </section>
    <div class="pagination">
      <router-link to="/css/paint" class="btn btn-prev"
        >❮ &lt;paint&gt;</router-link
      >
      <router-link
        to="/css/radial-gradients-------radial-gradient"
        class="btn btn-next"
        >Radial Gradients &lt;radial-gradient&gt; ❯</router-link
      >
    </div>
  </article>
</template>
