<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h3><a id="introlimitations">Limitations</a></h3>
    <ol>
    <li> While the JavaFX CSS parser will parse valid CSS syntax, it is not a
        fully compliant CSS parser. One should not expect the parser to handle
        syntax not specified in this document.</li>
    <li>With the exception of @font‑face, @import, and @media, @-keyword statements are ignored.</li>
    <li>The &lt;media-query-list&gt; of the @import statement is not parsed.</li>
    <li>The ":active" and ":focus" dynamic pseudo‑classes are not supported.
        However, <a href="#node">Nodes</a> do support the ":pressed" and
        ":focused" pseudo‑classes, which are similar. </li>
    <li>The ":link" and ":visited" pseudo‑classes are not supported in general.
        However, <a href="#hyperlink">Hyperlink</a> objects can be styled, and
        they support the ":visited" pseudo‑class. </li>
    <li>JavaFX CSS does not support comma-separated series of font family names
        in the -fx-font-family property. The optional line height parameter when
        specifying fonts is not supported. There is no equivalent for the
        font-variant property.</li>
    <li>JavaFX CSS uses the HSB color model instead of the HSL color model. </li>
    <li>If a property of a node is initialized by calling the set method of the
        property, the CSS implementation will see this as a user set value and the
        value will not be overwritten by a style from a user agent style
        sheet.</li>
    <li>When parsing a <a href="http://www.w3.org/TR/CSS2/syndata.html#uri">URI</a>,
        the parser doesn't handle URI escapes nor \&lt;hex-digit&gt;[1,6] code points.</li>
    <li>JavaFX CSS does not combine short-hand and long-hand property notations in a declaration block.
        Using both notations in a single declaration block may lead to unexpected results.</li>
    </ol>
    </section>
    <div class="pagination">
      <router-link to="/css/understanding-----parser-warnings" class="btn btn-prev">❮ Understanding         Parser Warnings</router-link>
      <router-link to="/css/types" class="btn btn-next">Types ❯</router-link>
    </div>
  </article>
</template>
