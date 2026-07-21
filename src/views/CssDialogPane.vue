<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="dialogpane">DialogPane</a></h4>
    <p class="styleclass">Style class: dialog-pane</p>
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
        <th class="propertyname" scope="row">-fx-graphic</th>
            <td class="value"><a href="#typeurl" class="typelink">&lt;uri&gt;</a></td>
            <td>null</td>
            <td>&nbsp;</td>
        </tr>
        <tr>
        <th colspan="4" class="parents" scope="row">Also has all properties of <a href="#pane">Pane</a></th>
        </tr>
        </tbody>
    </table>
    <h4>Substructure</h4>
    <ul>
        <li>header-panel  — BorderPane
        <ul><li>graphic-container — StackPane</li></ul>
        </li>
        <li>content — Label</li>
        <li>button-bar — ButtonBar</li>
    </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/borderpane" class="btn btn-prev">❮ BorderPane</router-link>
      <router-link to="/css/flowpane" class="btn btn-next">FlowPane ❯</router-link>
    </div>
  </article>
</template>
