<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h3><a id="typetextbounds">&lt;text-bounds&gt;</a></h3>
      <p>
        The geometry of text can be measured either in terms of the bounds of
        the particular text to be rendered - visual bounds, or as properties of
        the font and the characters to be rendered - logical bounds. Visual
        bounds are more useful for positioning text as graphics, and for
        obtaining tight enclosing bounds around the text.
      </p>
      <p>
        Logical bounds are important for laying out text relative to other text
        and other components, particularly those which also contain text. The
        bounds aren't specific to the text being rendered, and so will report
        heights which account for the potential ascent and descent of text using
        the font at its specified size. Also leading and trailing spaces are
        part of the logical advance width of the text.
      </p>
      <p>&nbsp;</p>
      <p class="grammar">[ logical | visual | logical-vertical-center ]</p>
      <ul>
        <li>
          <strong>logical</strong>: The logical bounds are based on font metrics
          information. The width is based on the glyph advances and the height
          of the ascent, descent, and line gap, except for the last line which
          does not include the line gap. This is usually the fastest option.
        </li>
        <li>
          <strong>visual</strong>: Use visual bounds as the basis for
          calculating the bounds. This is likely to be slower than using logical
          bounds.
        </li>
        <li>
          <strong>logical-vertical-center</strong>: Use logical vertical
          centered bounds as the basis for calculating the bounds. This bounds
          type is typically used to center Text nodes vertically within the
          bounds of its parent.
        </li>
      </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/easing-function" class="btn btn-prev"
        >❮ &lt;easing-function&gt;</router-link
      >
      <router-link to="/css/stage" class="btn btn-next">Stage ❯</router-link>
    </div>
  </article>
</template>
