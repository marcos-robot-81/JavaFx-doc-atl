<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h3><a id="typeangle">&lt;angle&gt;</a></h3>
    <p>An angle is a <a href="#typenumber" class="typeref">&lt;number&gt;</a>
      with one of the following units.</p>
    <p>&nbsp;</p>
    <p class="grammar"><a href="#typenumber">&lt;number&gt;</a>[ deg | rad |
      grad | turn ]</p>
    <ul>
      <li><strong>deg</strong>: angle in degrees — all other angle units are
        converted to degrees.</li>
      <li><strong>rad</strong>: angle in radians</li>
      <li><strong>grad</strong>: angle in gradians</li>
      <li><strong>turn</strong>: angle in turns</li>
    </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/percentage" class="btn btn-prev">❮ &lt;percentage&gt;</router-link>
      <router-link to="/css/duration" class="btn btn-next">&lt;duration&gt; ❯</router-link>
    </div>
  </article>
</template>
