<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="combobox">ComboBox</a></h4>
      <p class="styleclass">Style class: combo-box</p>
      <p>
        The ComboBox control has all the properties and pseudo‑classes of
        <a href="#comboboxbase">ComboBoxBase</a>
      </p>
      <h4>Substructure</h4>
      <ul>
        <li>
          list-cell — a ListCell instance used to show the selection in the
          button area of a non-editable ComboBox
        </li>
        <li>
          text-input — a TextField instance used to show the selection and allow
          input in the button area of an editable ComboBox
        </li>
        <li>
          combo-box-popup — a PopupControl that is displayed when the button is
          pressed
          <ul>
            <li>
              list-view — a ListView
              <ul>
                <li>list-cell — a ListCell</li>
              </ul>
            </li>
          </ul>
        </li>
      </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/colorpicker" class="btn btn-prev"
        >❮ ColorPicker</router-link
      >
      <router-link to="/css/comboboxbase" class="btn btn-next"
        >ComboBoxBase ❯</router-link
      >
    </div>
  </article>
</template>
