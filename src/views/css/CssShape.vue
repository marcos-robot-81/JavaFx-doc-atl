<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="shape">Shape</a></h4>
      <p class="styleclass">Style class: empty by default</p>
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
            <th class="propertyname" scope="row"><code>-fx-fill</code></th>
            <td class="value">
              <a href="#typepaint" class="typelink">&lt;paint&gt;</a>
            </td>
            <td>BLACK</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-smooth</code></th>
            <td class="value">
              <a href="#typeboolean" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td>true</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-stroke</code></th>
            <td class="value">
              <a href="#typepaint" class="typelink">&lt;paint&gt;</a>
            </td>
            <td>null</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-stroke-type</code>
            </th>
            <td class="value">[ inside | outside | centered ]</td>
            <td>centered</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-stroke-dash-array</code>
            </th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;size&gt;</a>[
              <a href="#typesize" class="typelink">&lt;size&gt;</a>]+
            </td>
            <td>see comment</td>
            <td>
              The initial value is that of an empty array, effectively a solid
              line.
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-stroke-dash-offset</code>
            </th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;number&gt;</a>
            </td>
            <td>0</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-stroke-line-cap</code>
            </th>
            <td class="value">[ square | butt | round ]</td>
            <td>square</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-stroke-line-join</code>
            </th>
            <td class="value">[ miter | bevel | round ]</td>
            <td>miter</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-stroke-miter-limit</code>
            </th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;number&gt;</a>
            </td>
            <td>10</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-stroke-width</code>
            </th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
            </td>
            <td>1</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th colspan="4" class="parents" scope="row">
              Also has all properties of <a href="#node">Node</a>
            </th>
          </tr>
        </tbody>
      </table>
    </section>
    <div class="pagination">
      <router-link to="/css/mediaview" class="btn btn-prev"
        >❮ MediaView</router-link
      >
      <router-link to="/css/arc" class="btn btn-next">Arc ❯</router-link>
    </div>
  </article>
</template>
