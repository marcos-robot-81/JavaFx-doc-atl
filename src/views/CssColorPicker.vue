<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="colorpicker">ColorPicker</a></h4>
      <p class="styleclass">Style class: color-picker</p>
      <p>
        The ColorPicker control has all the properties and pseudo‑classes of
        <a href="#comboboxbase">ComboBoxBase</a>
      </p>
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
              <code>-fx-color-label-visible</code>
            </th>
            <td class="value">
              <a href="#typeboolean" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td>true</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th colspan="4" class="parents" scope="row">
              Also has all properties of <a href="#control">Control</a>
            </th>
          </tr>
        </tbody>
      </table>
      <h4>Substructure</h4>
      <ul>
        <li>color display node — Label</li>
        <li>
          arrow-button — StackPane
          <ul>
            <li>arrow — StackPane</li>
          </ul>
        </li>
      </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/choicebox" class="btn btn-prev"
        >❮ ChoiceBox</router-link
      >
      <router-link to="/css/combobox" class="btn btn-next"
        >ComboBox ❯</router-link
      >
    </div>
  </article>
</template>
