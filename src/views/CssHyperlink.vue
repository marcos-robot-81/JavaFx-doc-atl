<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="hyperlink">Hyperlink</a></h4>
    <p class="styleclass">Style class: hyperlink</p>
    <p>The Hyperlink control has all the properties of <a href="#buttonbase">ButtonBase</a>.</p>
    <table class="table table-dark table-striped table-hover table-bordered" >
    <caption>Available CSS Properties</caption>
        <thead>
        <tr>
        <th class="propertyname" scope="col">CSS Property</th>
        <th class="value" scope="col">Values</th>
        <th scope="col">Default</th>
        <th scope="col">Comments</th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <th class="propertyname" scope="row">-fx-cursor</th>
            <td class="value">[ null | crosshair | default | hand | move |
                e-resize | h-resize | ne-resize | nw-resize | n-resize | se-resize |
                sw-resize | s-resize | w-resize | v-resize | text | wait ] | <a href="#typeurl" class="typelink">&lt;url&gt;</a></td>
            <td class="default">hand</td>
            <td>inherits </td>
        </tr>
        </tbody>
    </table>
    <h4>Pseudo-classes</h4>
    <table class="table table-dark table-striped table-hover table-bordered" >
    <caption>Available CSS Pseudo-classes</caption>
      <thead>
        <tr>
        <th class="propertyname" scope="col">CSS Pseudo-class</th>
        <th scope="col">Comments</th>
        </tr>
      </thead>
      <tbody>
        <tr>
        <th class="propertyname" scope="row">visited</th>
          <td>applies when the <strong>visited </strong>variable is true</td>
        </tr>
        <tr>
        <td colspan="2" class="parents" scope="row">Also has all pseudo‑classes of <a href="#buttonbase">ButtonBase</a></td>
        </tr>
      </tbody>
    </table>
    <h4>Substructure</h4>
    <ul>
      <li>label — Label</li>
    </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/htmleditor" class="btn btn-prev">❮ HTMLEditor</router-link>
      <router-link to="/css/indexedcell" class="btn btn-next">IndexedCell ❯</router-link>
    </div>
  </article>
</template>
