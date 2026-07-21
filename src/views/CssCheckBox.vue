<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="checkbox">CheckBox</a></h4>
    <p class="styleclass">Style class: check-box</p>
    <p>The CheckBox control has all the properties of <a href="#buttonbase">ButtonBase</a></p>
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
        <th class="propertyname" scope="row">selected</th>
          <td>applies when the <strong>selected</strong> variable is true</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">determinate</th>
          <td>applies when the <strong>indeterminate </strong>variable is
            false</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">indeterminate</th>
          <td>applies when the <strong>indeterminate </strong>variable is true</td>
        </tr>
        <tr>
        <td colspan="2" class="parents" scope="row">Also has all pseudo‑classes of <a href="#buttonbase">ButtonBase</a></td>
        </tr>
      </tbody>
    </table>
    <h4>Substructure</h4>
    <ul>
      <li>box — a StackPane
      <ul>
        <li>mark — a StackPane</li>
      </ul>
      </li>
    </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/cell" class="btn btn-prev">❮ Cell</router-link>
      <router-link to="/css/checkmenuitem" class="btn btn-next">CheckMenuItem ❯</router-link>
    </div>
  </article>
</template>
