<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="button">Button</a></h4>
      <p class="styleclass">Style class: button</p>
      <p>
        The Button control has all the properties of
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
            <th class="propertyname" scope="row">cancel</th>
            <td>
              applies if this Button receives VK_ESC if the event is not
              otherwise consumed
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">default</th>
            <td>
              applies if this Button receives VK_ENTER if the event is not
              otherwise consumed
            </td>
          </tr>
          <tr>
            <td colspan="2" class="parents" scope="row">
              Also has all pseudo‑classes of
              <a href="#buttonbase">ButtonBase</a>
            </td>
          </tr>
        </tbody>
      </table>
    </section>
    <div class="pagination">
      <router-link to="/css/accordion" class="btn btn-prev"
        >❮ Accordion</router-link
      >
      <router-link to="/css/buttonbase" class="btn btn-next"
        >ButtonBase ❯</router-link
      >
    </div>
  </article>
</template>
