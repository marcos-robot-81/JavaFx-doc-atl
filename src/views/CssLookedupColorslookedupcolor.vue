<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4>Looked-up Colors <span class="grammar" style="font-size: smaller;">&lt;looked-up-color&gt;</span></h4>
    <p>With looked-up colors you can refer to any other color property that is
      set on the current node or any of its parents. This is a very powerful
      feature, as it allows a generic palette of colors to be specified on the
      scene then used throughout the application. If you want to change one of
      those palette colors you can do so at any level in the scene tree and it
      will affect that node and all its decendents. Looked-up colors are not
      looked up until they are applied, so they are live and react to any style
      changes that might occur, such as replacing a palette color at runtime
      with the "style" property on a node.</p>
    <p>In the following example, all background color of all buttons uses the
      looked up color "abc".</p>
    <p class="example">:root { abc: #f00 }<br>
      .button { -fx-background-color: abc }</p>
    </section>
    <div class="pagination">
      <router-link to="/css/named-colors-named-color" class="btn btn-prev">❮ Named Colors &lt;named-color&gt;</router-link>
      <router-link to="/css/rgb-colors-rgb-color" class="btn btn-next">RGB Colors &lt;rgb-color&gt; ❯</router-link>
    </div>
  </article>
</template>
