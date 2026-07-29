<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4>Example</h4>
      <p>
        A button that smoothly changes its opacity on mouse-hover can be defined
        in a stylesheet like this:
      </p>
      <p class="example">
        .button {<br />
        &nbsp;&nbsp;&nbsp; <code>-fx-opacity</code>: 0.8;<br />
        &nbsp;&nbsp;&nbsp; transition-property: <code>-fx-opacity</code>;<br />
        &nbsp;&nbsp;&nbsp; transition-duration: 0.5s;<br />
        }<br />
        <br />
        .button:hover {<br />
        &nbsp;&nbsp;&nbsp; <code>-fx-opacity</code>: 1;<br />
        }
      </p>
    </section>
    <div class="pagination">
      <router-link to="/css/transitions" class="btn btn-prev"
        >❮ Transitions</router-link
      >
      <router-link to="/css/-rules" class="btn btn-next">@ Rules ❯</router-link>
    </div>
  </article>
</template>
