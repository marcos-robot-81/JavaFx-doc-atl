<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="line">Line</a></h4>
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
            <td>null</td>
            <td></td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-stroke</code></th>
            <td class="value">
              <a href="#typepaint" class="typelink">&lt;paint&gt;</a>
            </td>
            <td>black</td>
            <td></td>
          </tr>
          <tr>
            <th colspan="4" class="parents" scope="row">
              Also has all properties of <a href="#shape">Shape</a>
            </th>
          </tr>
        </tbody>
      </table>
    </section>
    <div class="pagination">
      <router-link to="/css/ellipse" class="btn btn-prev"
        >❮ Ellipse</router-link
      >
      <router-link to="/css/path" class="btn btn-next">Path ❯</router-link>
    </div>
  </article>
</template>
