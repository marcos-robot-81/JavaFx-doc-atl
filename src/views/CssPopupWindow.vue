<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="popupwindow">PopupWindow</a></h4>
    <p class="styleclass">Style class: :root.popup</p>
    <p>PopupWindow does not have any properties that can be styled by CSS, but a PopupWindow does have its own Scene.
        Scene's root gets the :root pseudo-class by default. If the Scene is the root scene of a PopupWindow, then the
        .popup style-class is also added. This allows the root scene of a PopupWindow to have distinct styles via
        the CSS rule <code>:root.popup { /* declarations */ }</code>
    </p>
    </section>
    <div class="pagination">
      <router-link to="/css/stage" class="btn btn-prev">❮ Stage</router-link>
      <router-link to="/css/nodes" class="btn btn-next">Nodes ❯</router-link>
    </div>
  </article>
</template>
