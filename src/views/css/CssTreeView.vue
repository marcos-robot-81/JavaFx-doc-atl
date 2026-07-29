<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="treetableview">TreeView</a></h4>
      <p class="styleclass">Style class: tree-table-view</p>
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
            <th class="propertyname" scope="row">
              <code>-fx-fixed-cell-size</code>
            </th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
            </td>
            <td>Region.USE_COMPUTED_SIZE</td>
            <td>
              If both <code>-fx-cell-size</code> and
              <code>-fx-fixed-cell-size</code> properties are specified in CSS,
              <code>-fx-fixed-cell-size</code> takes precedence.
            </td>
          </tr>
          <tr>
            <th colspan="4" class="parents" scope="row">
              Also has all properties and pseudo‑class state of
              <a href="#control">Control</a>
            </th>
          </tr>
        </tbody>
      </table>
    </section>
    <div class="pagination">
      <router-link to="/css/treetablecell" class="btn btn-prev"
        >❮ TreeTableCell</router-link
      >
      <router-link to="/css/treeview-1" class="btn btn-next"
        >TreeView 1 ❯</router-link
      >
    </div>
  </article>
</template>
