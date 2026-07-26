<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="tilepane">TilePane</a></h4>
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
            <th class="propertyname" scope="row">
              <code>-fx-orientation</code>
            </th>
            <td class="value">[ horizontal | vertical ]</td>
            <td class="default">horizontal</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-pref-rows</code></th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;integer&gt;</a>
            </td>
            <td class="default">5</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-pref-columns</code>
            </th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;integer&gt;</a>
            </td>
            <td class="default">5</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-pref-tile-width</code>
            </th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;size&gt;</a>
            </td>
            <td class="default">-1</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-pref-tile-height</code>
            </th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;size&gt;</a>
            </td>
            <td class="default">-1</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-hgap</code></th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
            </td>
            <td class="default">0</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-vgap</code></th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
            </td>
            <td class="default">0</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-alignment</code></th>
            <td class="value">
              [ top-left | top-center | top-right | center-left | center |
              center-right bottom-left | bottom-center | bottom-right |
              baseline-left | baseline-center | baseline-right ]
            </td>
            <td class="default">top-left</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-tile-alignment</code>
            </th>
            <td class="value">
              [ top-left | top-center | top-right | center-left | center |
              center-right bottom-left | bottom-center | bottom-right |
              baseline-left | baseline-center | baseline-right ]
            </td>
            <td class="default">center</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th colspan="4" class="parents" scope="row">
              Also has all properties of <a href="#pane">Pane</a>
            </th>
          </tr>
        </tbody>
      </table>
    </section>
    <div class="pagination">
      <router-link to="/css/stackpane" class="btn btn-prev"
        >❮ StackPane</router-link
      >
      <router-link to="/css/vbox" class="btn btn-next">VBox ❯</router-link>
    </div>
  </article>
</template>
