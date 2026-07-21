<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h3><a id="typecolorstop">&lt;color-stop&gt;</a></h3>
    <p>Stops are per <a href="https://www.w3.org/TR/css3-images/#color-stop-syntax" class="typelink">W3C
        color-stop syntax</a>.</p>
    <p class="grammar">[ <a href="#typecolor" class="typeref">&lt;color&gt;</a>
      [ <a href="#typepercentage" class="typeref">&lt;percentage&gt;</a> | <a href="#typelength" class="typeref">&lt;length&gt;</a>]?
      ]</p>
    <p>In a series of &lt;color-stop&gt;, stop distance values must all be
      &lt;percentage&gt; or &lt;length&gt;. Furthermore, if &lt;length&gt;
      values are used, then the distance value for first and last stop in the
      series must be specified. This restriction may be removed in a future
      release.</p>
    <p>"<span style="color: #050; ">red, white 70%, blue</span>" is valid since the
      distance for red and blue is assumed to be 0% and 100%, respectively.</p>
    <p>"<span style="color: #050; ">red 10, white, blue 90</span>" is valid. Because
      distance for red and blue is 10 and 90, respectively, the distance for
      white can be calculated.</p>
    <p>"<span style="color: #050; ">red, white 70, blue</span>" is <span style="font-style:italic;">not</span> valid
      since distance units do not agree.</p>
    <p>"<span style="color: #050; ">red, white, blue</span>" is valid. The stops are
      distributed evenly between 0% and 100%.</p>
    </section>
    <div class="pagination">
      <router-link to="/css/point" class="btn btn-prev">❮ &lt;point&gt;</router-link>
      <router-link to="/css/uri" class="btn btn-next">&lt;uri&gt; ❯</router-link>
    </div>
  </article>
</template>
