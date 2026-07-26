<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="contextmenu">ContextMenu</a></h4>
      <p class="styleclass">Style class: context-menu</p>
      <p>
        The ContextMenu class has all the properties of
        <a href="#popupcontrol">PopupControl</a>.
      </p>
      The selector for a ContextMenu may be made more specific by using the
      selector for the control from which the ContextMenu was shown. For
      example,
      <p class="example">.choice-box &gt; .context-menu { ... }</p>
      <h4>Substructure</h4>
      <ul>
        <li>
          context-menu — a Region
          <ul>
            <li>
              scroll-arrow — a StackPane
              <ul>
                <li>menu-up-arrow — a StackPane</li>
              </ul>
            </li>
            <li>
              scroll-arrow — a StackPane
              <ul>
                <li>menu-down-arrow — a StackPane</li>
              </ul>
            </li>
            <li>
              * — a VBox
              <ul>
                <li>
                  menu-item — a Region
                  <ul>
                    <li>label — a Label</li>
                    <li>
                      left-container — a StackPane (for radio buttons and check
                      boxes)
                    </li>
                    <li>
                      right-container — a StackPane (for pull-right menus)
                      <ul>
                        <li>arrow — a Region</li>
                      </ul>
                    </li>
                    <li>
                      graphic-container — a StackPane (for MenuItem graphic)
                    </li>
                  </ul>
                </li>
              </ul>
            </li>
          </ul>
        </li>
      </ul>
    </section>
    <div class="pagination">
      <router-link to="/css/comboboxbase" class="btn btn-prev"
        >❮ ComboBoxBase</router-link
      >
      <router-link to="/css/control" class="btn btn-next"
        >Control ❯</router-link
      >
    </div>
  </article>
</template>
