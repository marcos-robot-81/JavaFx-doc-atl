<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="typelength">&lt;length&gt;</a></h4>
      <p class="grammar">
        <a href="#typenumber">&lt;number&gt;</a>[ px | mm | cm | in | pt | pc |
        em | ex ]?
      </p>
      <p>
        No whitespace is allowed between the number and units if provided. Some
        units are relative and others absolute.
      </p>
      <p><strong>Relative</strong></p>
      <ul>
        <li><strong>px</strong>: pixels, relative to the viewing device</li>
        <li><strong>em</strong>: the 'font-size' of the relevant font</li>
        <li><strong>ex</strong>: the 'x-height' of the relevant font</li>
      </ul>
      <p><strong>Absolute</strong></p>
      <ul>
        <li>
          <strong>in</strong>: inches — 1 inch is equal to 2.54 centimeters.
        </li>
        <li><strong>cm</strong>: centimeters</li>
        <li><strong>mm</strong>: millimeters</li>
        <li>
          <strong>pt</strong>: points — the points used by CSS 2.1 are equal to
          1/72nd of an inch.
        </li>
        <li><strong>pc</strong>: picas — 1 pica is equal to 12 points.</li>
      </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/size" class="btn btn-prev"
        >❮ &lt;size&gt;</router-link
      >
      <router-link to="/css/percentage" class="btn btn-next"
        >&lt;percentage&gt; ❯</router-link
      >
    </div>
  </article>
</template>
