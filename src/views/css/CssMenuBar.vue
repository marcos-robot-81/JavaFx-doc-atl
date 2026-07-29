<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="menubar">MenuBar</a></h4>
      <p class="styleclass">Style class: menu-bar</p>
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
            <th class="propertyname" scope="row">
              <code>-fx-use-system-menu-bar</code>
            </th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td>false</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th colspan="4" class="parents" scope="row">
              Also has all properties of <a href="#control">Control</a>
            </th>
          </tr>
        </tbody>
      </table>
      <p>
        MenuBar has all the pseudo‑class states of
        <a href="#control">Control</a>
      </p>
      <h4>Substructure</h4>
      <ul>
        <li>menu</li>
      </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/menu" class="btn btn-prev">❮ Menu</router-link>
      <router-link to="/css/menubutton" class="btn btn-next"
        >MenuButton ❯</router-link
      >
    </div>
  </article>
</template>
