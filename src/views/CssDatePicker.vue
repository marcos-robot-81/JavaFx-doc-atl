<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="datepicker">DatePicker</a></h4>
      <p class="styleclass">Style class: date-picker</p>
      <p>
        The DatePicker control has all the properties and pseudo‑classes of
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
              <code>-fx-show-week-numbers</code>
            </th>
            <td class="value">
              <a href="#typeboolean" class="typeboolean">&lt;boolean&gt;</a>
            </td>
            <td>
              true if the resource bundle property "DatePicker.showWeekNumbers"
              contains the country code.
            </td>
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
        <li>date-picker-display-node — TextField</li>
      </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/control" class="btn btn-prev"
        >❮ Control</router-link
      >
      <router-link to="/css/htmleditor" class="btn btn-next"
        >HTMLEditor ❯</router-link
      >
    </div>
  </article>
</template>
