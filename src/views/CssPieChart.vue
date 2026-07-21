<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="piechart">PieChart</a></h4>
    <table class="table table-dark table-striped table-hover table-bordered" >
    <caption>Available Style Classes</caption>
      <thead>
        <tr>
        <th class="propertyname" scope="col">Style class</th>
        <th scope="col">Comments</th>
        <th scope="col">Properties</th>
        </tr>
      </thead>
      <tbody>
        <tr>
        <th class="propertyname" scope="row">"chart-pie data&lt;i&gt;
            default-color&lt;j&gt;"</th>
          <td>Where &lt;i&gt; is the index of the data and &lt;j&gt; is the
            series’ color index. If the data value is negative, the
            "negative" style‑class is added; e.g., <code>.negative.chart-pie</code>.</td>
          <td><a href="#node" class="typelink">Node</a> </td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">"chart-pie-label-line;"</th>
          <td>&nbsp;</td>
          <td><a href="#path" class="typelink">Path</a> </td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">"chart-pie-label;"</th>
          <td>&nbsp;</td>
          <td><a href="#path" class="typelink">Text</a> </td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">"pie-legend-symbol &lt;<em>i–th</em>
            data item’s style‑class&gt;"</th>
          <td>Each item in the legend has the style‑class "pie-legend-symbol"
            plus the style‑class of the corresponding data item</td>
          <td>LegendItem </td>
        </tr>
      </tbody>
    </table>
    <p>&nbsp;</p>
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
        <th class="propertyname" scope="row">-fx-clockwise</th>
            <td class="value"><a href="#typeboolean" class="typelink">&lt;boolean&gt;</a></td>
            <td>true</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
        <th class="propertyname" scope="row">-fx-pie-label-visible</th>
            <td class="value"><a href="#typeboolean" class="typelink">&lt;boolean&gt;</a></td>
            <td>true</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
        <th class="propertyname" scope="row">-fx-label-line-length</th>
            <td class="value"><a href="#typesize" class="typelink">&lt;size&gt;</a></td>
            <td>20</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
        <th class="propertyname" scope="row">-fx-start-angle</th>
            <td class="value"><a href="#typenumber" class="typelink">&lt;number&gt;</a></td>
            <td>0</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
        <th colspan="4" class="parents" scope="row">Has all properties of <a href="#chart">Chart</a></th>
          </tr>
        </tbody>
      </table>
    </section>
    <div class="pagination">
      <router-link to="/css/numberaxis" class="btn btn-prev">❮ NumberAxis</router-link>
      <router-link to="/css/scatterchart" class="btn btn-next">ScatterChart ❯</router-link>
    </div>
  </article>
</template>
