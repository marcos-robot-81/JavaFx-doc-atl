<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="parent">Parent</a></h4>
    <p class="styleclass">Style
      class: empty by default</p>
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
        <th colspan="4" scope="row">Parent extends Node. Parent does not add any additional CSS properties.</th>
    </tr>
    <tr>
        <th colspan="4" class="parents" scope="row">Also has all properties of <a href="#node">Node</a></th>
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
            <th class="propertyname" scope="row">root</th>
            <td>applies when the <code>Parent</code> is the root node of a <code>Scene</code> or <code>SubScene</code></td>
        </tr>
        <tr>
            <td colspan="2" class="parents" scope="row">Also has all pseudo‑classes of <a href="#node">Node</a></td>
        </tr>
        </tbody>
    </table>
    <br>
    </section>
    <div class="pagination">
      <router-link to="/css/node" class="btn btn-prev">❮ Node</router-link>
      <router-link to="/css/scene" class="btn btn-next">Scene ❯</router-link>
    </div>
  </article>
</template>
