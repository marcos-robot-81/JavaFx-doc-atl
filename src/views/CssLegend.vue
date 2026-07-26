<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="legend">Legend</a></h4>
      <p class="styleclass">Style class: chart-legend</p>
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
            <th colspan="4" class="parents" scope="row">
              Has all properties of <a href="#region">Region</a>
            </th>
          </tr>
        </tbody>
      </table>
      <h4>Substructure</h4>
      <ul>
        <li>chart-legend-item — Label</li>
        <li>chart-legend-item-symbol — Node (the Label's graphic)</li>
      </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/chart" class="btn btn-prev">❮ Chart</router-link>
      <router-link to="/css/linechart" class="btn btn-next"
        >LineChart ❯</router-link
      >
    </div>
  </article>
</template>
