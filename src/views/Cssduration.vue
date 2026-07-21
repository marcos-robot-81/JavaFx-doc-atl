<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h3><a id="typeduration">&lt;duration&gt;</a></h3>
    <p>A duration is a <a href="#typenumber" class="typeref">&lt;number&gt;</a>
        with second or millisecond units, or the value <span class="grammar">indefinite</span>.</p>
    <p>&nbsp;</p>
    <p class="grammar">[<a href="#typenumber">&lt;number&gt;</a>[ s | ms ]] | indefinite</p>
    <ul>
        <li><strong>s</strong>: duration in seconds</li>
        <li><strong>ms</strong>: duration in milliseconds. One second is 1000 milliseconds.</li>
        <li><strong>indefinite</strong>: See <a href="https://openjfx.io/javadoc/26/javafx.graphics/javafx/util/Duration.html#INDEFINITE" class="typelink">Duration.INDEFINITE</a></li>
    </ul>
    <p>See also <a href="http://www.w3.org/TR/css3-values/#time" class="typelink">W3C time units</a>.</p>
    </section>
    <div class="pagination">
      <router-link to="/css/angle" class="btn btn-prev">❮ &lt;angle&gt;</router-link>
      <router-link to="/css/point" class="btn btn-next">&lt;point&gt; ❯</router-link>
    </div>
  </article>
</template>
