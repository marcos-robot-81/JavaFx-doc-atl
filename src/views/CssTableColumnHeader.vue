<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="tablecolumnheader">TableColumnHeader</a></h4>
      <p class="styleclass">Style class: column-header</p>
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
            <th class="propertyname" scope="row"><code>-fx-size</code></th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
            </td>
            <td>20</td>
            <td>The table column header size.</td>
          </tr>
          <tr>
            <th colspan="4" class="parents" scope="row">
              Also has all properties of <a href="#region">Region</a>
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
            <th class="propertyname" scope="row">last-visible</th>
            <td>applies if this is the last visible column in the table.</td>
          </tr>
          <tr>
            <th colspan="2" class="parents" scope="row">
              Also has all pseudo‑classes of <a href="#node">Node</a>
            </th>
          </tr>
        </tbody>
      </table>
      <h4>Substructure</h4>
      <ul>
        <li>column-resize-line — Region</li>
        <li>column-overlay — Region</li>
        <li>placeholder — StackPane</li>
        <li>
          column-header-background — StackPane
          <ul>
            <li>
              nested-column-header
              <ul>
                <li>column-header</li>
              </ul>
            </li>
            <li>filler — Region</li>
            <li>
              show-hide-columns-button — StackPane
              <ul>
                <li>show-hide-column-image — StackPane</li>
              </ul>
            </li>
            <li>
              column-drag-header — StackPane
              <ul>
                <li>label — Label</li>
              </ul>
            </li>
          </ul>
        </li>
      </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/tabpane" class="btn btn-prev"
        >❮ TabPane</router-link
      >
      <router-link to="/css/tableview" class="btn btn-next"
        >TableView ❯</router-link
      >
    </div>
  </article>
</template>
