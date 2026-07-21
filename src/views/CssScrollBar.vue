<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="scrollbar">ScrollBar</a></h4>
    <p class="styleclass">Style class: scroll-bar</p>
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
        <th class="propertyname" scope="row">-fx-block-increment</th>
          <td class="value"><a href="#typenumber" class="typelink">&lt;number&gt;</a></td>
          <td>10</td>
          <td>&nbsp;</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-unit-increment</th>
          <td class="value"><a href="#typenumber" class="typelink">&lt;number&gt;</a></td>
          <td>1</td>
          <td>&nbsp;</td>
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
        <th class="propertyname" scope="row">vertical</th>
          <td>applies if this ScrollBar is vertical</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">horizontal</th>
          <td>applies if this ScrollBar is horizontal</td>
        </tr>
        <tr>
        <td colspan="2" class="parents" scope="row">Also has all pseudo‑classes of <a href="#control">Control</a></td>
        </tr>
      </tbody>
    </table>
    <h4>Substructure</h4>
    <ul>
      <li>decrement-button — StackPane
        <ul>
          <li>decrement-arrow — StackPane </li>
        </ul>
      </li>
      <li>track — StackPane</li>
      <li>thumb — StackPane</li>
      <li>increment-button — StackPane
        <ul>
          <li>increment-arrow — StackPane</li>
        </ul>
      </li>
    </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/radiomenuitem" class="btn btn-prev">❮ RadioMenuItem</router-link>
      <router-link to="/css/scrollpane" class="btn btn-next">ScrollPane ❯</router-link>
    </div>
  </article>
</template>
