<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="indexedcell">IndexedCell</a></h4>
    <p class="styleclass">Style class: indexed-cell</p>
    <p>The IndexedCell control has all the properties of <a href="#cell">Cell</a>.</p>
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
        <th class="propertyname" scope="row">even</th>
          <td>applies if this cell's index is even</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">odd</th>
          <td>applies if this cell's index is odd</td>
        </tr>
        <tr>
        <th colspan="4" class="parents" scope="row">Also has all pseudo‑classes of <a href="#cell">Cell</a></th>
        </tr>
      </tbody>
    </table>
    </section>
    <div class="pagination">
      <router-link to="/css/hyperlink" class="btn btn-prev">❮ Hyperlink</router-link>
      <router-link to="/css/label" class="btn btn-next">Label ❯</router-link>
    </div>
  </article>
</template>
