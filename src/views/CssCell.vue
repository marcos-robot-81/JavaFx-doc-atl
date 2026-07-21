<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="cell">Cell</a></h4>
    <p class="styleclass">Style class: cell</p>
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
        <th class="propertyname" scope="row">-fx-cell-size</th>
          <td class="value"><a href="#typesize" class="typelink">&lt;size&gt;</a></td>
          <td>24</td>
          <td>The cell size. For vertical ListView or a TreeView or TableView
            this is the height, for a horizontal ListView this is the width.</td>
        </tr>
        <tr>
        <th colspan="4" class="parents" scope="row">The Cell control has all the
            properties of <a href="#labeled">Labeled</a></th>
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
        <th class="propertyname" scope="row">empty</th>
          <td>applies when the <strong>empty </strong>variable is true</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">filled</th>
          <td>applies when the <strong>empty</strong> variable is false</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">selected</th>
          <td>applies when the <strong>selected</strong> variable is true</td>
        </tr>
        <tr>
        <td colspan="2" class="parents" scope="row">Also has all pseudo‑classes of <a href="#labeled">Labeled</a></td>
        </tr>
      </tbody>
    </table>
    <h4>Substructure</h4>
    <ul>
      <li>text — a Labeled</li>
    </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/buttonbase" class="btn btn-prev">❮ ButtonBase</router-link>
      <router-link to="/css/checkbox" class="btn btn-next">CheckBox ❯</router-link>
    </div>
  </article>
</template>
