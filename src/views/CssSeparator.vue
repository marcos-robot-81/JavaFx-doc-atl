<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="separator">Separator</a></h4>
    <p class="styleclass">Style class: separator</p>
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
        <th class="propertyname" scope="row">-fx-orientation</th>
          <td class="value">[ horizontal | vertical ]</td>
          <td class="default">horizontal</td>
          <td>&nbsp;</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-halignment</th>
          <td class="value">[ left | center | right ]</td>
          <td>center</td>
          <td>&nbsp;</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-valignment</th>
          <td class="value">[ top | center | baseline | bottom ]</td>
          <td>center</td>
          <td>&nbsp;</td>
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
        <th class="propertyname" scope="row">horizontal</th>
          <td>applies if this Separator is horizontal</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">vertical</th>
          <td>applies if this Separator is vertical</td>
        </tr>
        <tr>
        <td colspan="2" class="parents" scope="row">Also has all pseudo‑classes of <a href="#control">Control</a></td>
        </tr>
      </tbody>
    </table>
    <h4>Substructure</h4>
    <ul>
      <li>line — Region</li>
    </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/scrollpane" class="btn btn-prev">❮ ScrollPane</router-link>
      <router-link to="/css/spinner" class="btn btn-next">Spinner ❯</router-link>
    </div>
  </article>
</template>
