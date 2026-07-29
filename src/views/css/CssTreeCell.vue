<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="treecell">TreeCell</a></h4>
      <p class="styleclass">Style class: tree-cell</p>
      <table class="table table-dark table-striped table-hover table-bordered">
        <caption>
          Available CSS Properties
        </caption>
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
            <th class="propertyname" scope="row"><code>-fx-indent</code></th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
            </td>
            <td>10</td>
            <td>
              The amount of space to multiply by the treeItem.level to get the
              left margin
            </td>
          </tr>
          <tr>
            <th colspan="4" class="parents" scope="row">
              Also has all properties of <a href="#indexedcell">IndexedCell</a>
            </th>
          </tr>
        </tbody>
      </table>
      <h4>Pseudo-classes</h4>
      <table class="table table-dark table-striped table-hover table-bordered">
        <caption>
          Available CSS Pseudo-classes
        </caption>
        <thead>
          <tr>
            <th class="propertyname" scope="col">CSS Pseudo-class</th>
            <th scope="col">Comments</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th class="propertyname" scope="row">expanded</th>
            <td>applies if this cell is expanded</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">collapsed</th>
            <td>applies if this cell is not expanded</td>
          </tr>
          <tr>
            <td colspan="2" class="parents" scope="row">
              Also has all pseudo‑classes of
              <a href="#indexedcell">IndexedCell</a>
            </td>
          </tr>
        </tbody>
      </table>
    </section>
    <div class="pagination">
      <router-link to="/css/tooltip" class="btn btn-prev"
        >❮ Tooltip</router-link
      >
      <router-link to="/css/treetablecell" class="btn btn-next"
        >TreeTableCell ❯</router-link
      >
    </div>
  </article>
</template>
