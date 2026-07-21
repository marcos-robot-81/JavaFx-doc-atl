<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="tableview">TableView</a></h4>
    <p class="styleclass">Style class: table-view</p>
    <table class="table table-dark table-striped table-hover table-bordered" >
    <caption>Available CSS Properties</caption>
      <thead>
        <tr>
        <th class="propertyname" scope="col">CSS Property</th>
        <th class="value" scope="col">Values</th>
        <th scope="col">Default</th>
        <th scope="col">Comments</th>
      </tr></thead>
      <tbody>
        <tr>
        <th class="propertyname" scope="row">-fx-fixed-cell-size</th>
          <td class="value"><a href="#typesize" class="typelink">&lt;size&gt;</a></td>
          <td>-1</td>
          <td>A value greater than zero sets the fixed cell size of the table.
              A value of zero or less disables fixed cell size.</td>
        </tr>
        <tr>
        <th colspan="4" class="parents" scope="row">Also has all properties of <a href="#control">Control</a></th>
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
        <th class="propertyname" scope="row">cell-selection</th>
          <td>applies if this TableView's selection model is cell selection</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">row-selection</th>
          <td>applies if this TableView's selection model is row selection</td>
        </tr>
        <tr>
        <th colspan="2" class="parents" scope="row">Also has all pseudo‑classes of <a href="#node">Node</a></th>
        </tr>
      </tbody>
    </table>
    <h4>Substructure</h4>
    <ul>
      <li>column-resize-line — Region</li>
      <li>column-overlay — Region</li>
      <li>placeholder — StackPane</li>
      <li>column-header-background — StackPane
      <ul>
        <li>nested-column-header
        <ul>
          <li>column-header</li>
        </ul>
        </li>
        <li>filler — Region</li>
        <li>show-hide-columns-button — StackPane
        <ul>
          <li>show-hide-column-image — StackPane</li>
        </ul>
        </li>
        <li>column-drag-header — StackPane
        <ul>
          <li>label — Label</li>
        </ul>
        </li>
      </ul>
      </li>
        <li>table-column — TableColumn</li>
    </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/tablecolumnheader" class="btn btn-prev">❮ TableColumnHeader</router-link>
      <router-link to="/css/textarea" class="btn btn-next">TextArea ❯</router-link>
    </div>
  </article>
</template>
