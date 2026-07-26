<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="menubutton">MenuButton</a></h4>
      <p class="styleclass">Style class: menu-button</p>
      <p>
        The MenuButton control has all the properties of
        <a href="#buttonbase">ButtonBase</a>
      </p>
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
            <th class="propertyname" scope="row">openvertically</th>
            <td>
              applies if the <strong>openVertically</strong> variable is true
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">showing</th>
            <td>applies if the <strong>showing</strong> variable is true</td>
          </tr>
          <tr>
            <td colspan="2" class="parents" scope="row">
              Also has all pseudo‑classes of <a href="#node">Node</a>
            </td>
          </tr>
        </tbody>
      </table>
    </section>
    <div class="pagination">
      <router-link to="/css/menubar" class="btn btn-prev"
        >❮ MenuBar</router-link
      >
      <router-link to="/css/menuitem" class="btn btn-next"
        >MenuItem ❯</router-link
      >
    </div>
  </article>
</template>
