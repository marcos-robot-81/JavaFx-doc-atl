<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h3><a id="typefont">&lt;font&gt;</a></h3>
    <p>JavaFX CSS supports the ability to specify fonts using separate family,
      size, style, and weight properties, as well as the ability to specify a
      font using a single shorthand property. There are four value types related
      to fonts plus a shorthand property that encompasses all four properties.
      The font-related types are as follows. </p>
    <p><span class="grammar">&lt;font-family&gt;</span>The string name of the
      font family. An actual font family name available on the system can be
      used, or one of the following generic family names can be used:</p>
    <ul>
      <li>'system'</li>
      <li>'serif' (e.g., Times)</li>
      <li>'sans-serif' (e.g., Helvetica)</li>
      <li>'cursive' (e.g., Zapf-Chancery)</li>
      <li>'fantasy' (e.g., Western)</li>
      <li>'monospace' (e.g., Courier)</li>
    </ul>
    <p><span class="grammar">&lt;font-size&gt;</span> The size of the font,
      using the <span class="grammar">&lt;size&gt;</span> syntax.</p>
    <p><span class="grammar">&lt;font-style&gt;</span> The font's style, using
      the following syntax:<br>
      <span class="grammar">[ normal | italic | oblique ]</span></p>
    <p><span class="grammar">&lt;font-weight&gt;</span> The font's weight, using
      the following syntax:<br>
      <span class="grammar">[ normal | bold | bolder | lighter | 100 | 200 | 300
        | 400 | 500 | 600 | 700 | 800 | 900 ]</span></p>
    <p><span class="grammar">&lt;font&gt;</span> This font shorthand property
      can be used in place of the above properties. It uses the following
      syntax:<br>
      <span class="grammar">[[ &lt;font-style&gt; || &lt;font-weight&gt; ]?
        &lt;font-size&gt; &lt;font-family&gt; ]</span></p>
    </section>
    <div class="pagination">
      <router-link to="/css/inner-shadow" class="btn btn-prev">❮ Inner Shadow</router-link>
      <router-link to="/css/font-properties" class="btn btn-next">Font Properties ❯</router-link>
    </div>
  </article>
</template>
