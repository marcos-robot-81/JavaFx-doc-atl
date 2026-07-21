<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h2><a id="controls">Controls</a></h2>
    <h3 class="package">javafx.scene.control</h3>
    <p>Since JavaFX 2.0, the default skins for all controls support styling from
      CSS. This is accomplished by building the skins from layout objects called
      Regions. Most of the style properties for a control are provided by the
      Region objects that comprise the control's skin. Each Region object of the
      skin's substructure has its own style‑class so that it can be styled
      specifically. The control itself will sometimes provide CSS properties in
      addition to those provided by its Regions. Finally, controls may also
      define pseudo‑classes such as "vertical" and "horizontal" in addition to
      those defined by Node.</p>
    <p>With the following exceptions, controls are focus traversable. This means that <a href="#control">Control</a> sets the initial value
        of the focusTraversable property true; whereas in <a href="#node">Node</a>, the initial value of the focusTraversable property
        is false. The following controls are not focus traversable by default: Accordion, Cell, Label, MenuBar,
        ProgressBar, ProgressIndicator, ScrollBar, ScrollPane, Separator, SplitPane, ToolBar.</p>
    </section>
    <div class="pagination">
      <router-link to="/css/webview" class="btn btn-prev">❮ WebView</router-link>
      <router-link to="/css/accordion" class="btn btn-next">Accordion ❯</router-link>
    </div>
  </article>
</template>
