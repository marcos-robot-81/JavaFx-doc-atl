<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="comboboxbase">ComboBoxBase</a></h4>
      <p class="styleclass">Style class: combo-box-base</p>
      <p>
        The ComboBoxBase control has all the properties of
        <a href="#control">Control</a>
      </p>
      <h4>Substructure</h4>
      <ul>
        <li>
          arrow-button — a StackPane
          <ul>
            <li>arrow — a StackPane</li>
          </ul>
        </li>
      </ul>
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
            <th class="propertyname" scope="row">editable</th>
            <td>applies when the <strong>editable </strong>variable is true</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">showing</th>
            <td>applies when the <strong>showing </strong>variable is true</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">armed</th>
            <td>applies when the <strong>armed </strong>variable is true</td>
          </tr>
        </tbody>
      </table>
    </section>
    <div class="pagination">
      <router-link to="/css/combobox" class="btn btn-prev"
        >❮ ComboBox</router-link
      >
      <router-link to="/css/contextmenu" class="btn btn-next"
        >ContextMenu ❯</router-link
      >
    </div>
  </article>
</template>
