<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="bubblechart">BubbleChart</a></h4>
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
        <th class="propertyname" scope="row">"chart-bubble series&lt;i&gt; data&lt;j&gt;
            default-color&lt;k&gt;"</th>
          <td>Where &lt;i&gt; is the index of the series, &lt;j&gt; is the index
            of the data within the series, and &lt;k&gt; is the series’
            color index</td>
          <td><a href="#node" class="typelink">Node</a> </td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">"chart-bubble series&lt;i&gt;
            bubble-legend-symbol default-color&lt;j&gt;"</th>
          <td>Where &lt;i&gt; is the index of the series and &lt;j&gt; is the
            series’ color index</td>
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
        <th colspan="4" class="parents" scope="row">Has all properties of <a href="#xychart">XYChart</a></th>
          </tr>
        </tbody>
      </table>
    </section>
    <div class="pagination">
      <router-link to="/css/barchart" class="btn btn-prev">❮ BarChart</router-link>
      <router-link to="/css/categoryaxis" class="btn btn-next">CategoryAxis ❯</router-link>
    </div>
  </article>
</template>
