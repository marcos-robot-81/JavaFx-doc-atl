<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="menu">Menu</a></h4>
      <p class="styleclass">Style class: menu</p>
      <h4>Pseudo-classes</h4>
      <table class="table table-dark table-striped table-hover table-bordered">
        <caption>
          Available CSS Pseudo-classes
        </caption>
        <thead>
          <tr>
            <th class="propertyname" scope="col">CSS Pseudo-class</th>
            <th scope="col">Comments</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th class="propertyname" scope="row">showing</th>
            <td>applies if this Menu is showing</td>
          </tr>
          <tr>
            <td colspan="2" class="parents" scope="row">
              Also has all pseudo‑classes of <a href="#control">Control</a>
            </td>
          </tr>
        </tbody>
      </table>
    </section>
    <div class="pagination">
      <router-link to="/css/listview" class="btn btn-prev"
        >❮ ListView</router-link
      >
      <router-link to="/css/menubar" class="btn btn-next"
        >MenuBar ❯</router-link
      >
    </div>
  </article>
</template>
