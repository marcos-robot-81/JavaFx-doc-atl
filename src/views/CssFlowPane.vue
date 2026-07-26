<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="flowpane">FlowPane</a></h4>
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
              <code>-fx-column-halignment</code>
            </th>
            <td class="value">[ left | center | right ]</td>
            <td class="default">left</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-row-valignment</code>
            </th>
            <td class="value">[ top | center | baseline | bottom ]</td>
            <td class="default">center</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-orientation</code>
            </th>
            <td class="value">[ horizontal | vertical ]</td>
            <td class="default">horizontal</td>
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
      <router-link to="/css/dialogpane" class="btn btn-prev"
        >❮ DialogPane</router-link
      >
      <router-link to="/css/gridpane" class="btn btn-next"
        >GridPane ❯</router-link
      >
    </div>
  </article>
</template>
