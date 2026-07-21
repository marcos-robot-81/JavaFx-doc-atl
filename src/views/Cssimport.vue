<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4>@import</h4>
    <p>
        Beginning with JavaFX 8u20, the CSS
        <a href="http://www.w3.org/TR/CSS21/cascade.html#at-import">@import</a> is partially supported.
        Only unconditional import is supported. In other words, the media‑type qualifier is not supported.
        Also, the JavaFX CSS parser is non-compliant with regard to where an @import may appear within a stylesheet
        (see <a href="http://www.w3.org/TR/CSS21/syndata.html#at-rules">At‑rules</a>).
        Users are cautioned that this will be fixed in a future release. Adherence to the W3C standard is strongly advised.
    </p>
    </section>
    <div class="pagination">
      <router-link to="/css/-rules" class="btn btn-prev">❮ @ Rules</router-link>
      <router-link to="/css/font-face" class="btn btn-next">@font-face ❯</router-link>
    </div>
  </article>
</template>
