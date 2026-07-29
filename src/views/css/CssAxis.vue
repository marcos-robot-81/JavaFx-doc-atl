<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="axis">Axis</a></h4>
      <p class="styleclass">Style class: axis</p>
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
            <th class="propertyname" scope="row"><code>-fx-side</code></th>
            <td class="value">Side</td>
            <td>null</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-tick-length</code>
            </th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
            </td>
            <td>8</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-tick-label-font</code>
            </th>
            <td class="value">
              <a href="#typefont" class="typelink">&lt;font&gt;</a>
            </td>
            <td>8 system</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-tick-label-fill</code>
            </th>
            <td class="value">
              <a href="#typepaint" class="typelink">&lt;paint&gt;</a>
            </td>
            <td>black</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-tick-label-gap</code>
            </th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
            </td>
            <td>3</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-tick-mark-visible</code>
            </th>
            <td class="value">
              <a href="#typeboolean" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td>true</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-tick-labels-visible</code>
            </th>
            <td class="value">
              <a href="#typeboolean" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td>true</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th colspan="4" class="parents" scope="row">
              Has all properties of <a href="#region">Region</a>
            </th>
          </tr>
        </tbody>
      </table>
      <h4>Substructure</h4>
      <ul>
        <li>axis-label — Text</li>
        <li>axis-tick-mark — Path</li>
      </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/areachart" class="btn btn-prev"
        >❮ AreaChart</router-link
      >
      <router-link to="/css/barchart" class="btn btn-next"
        >BarChart ❯</router-link
      >
    </div>
  </article>
</template>
