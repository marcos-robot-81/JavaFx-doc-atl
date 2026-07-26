<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h3><a id="intronaming">Naming Conventions</a></h3>
      <p>
        Naming conventions have been established for deriving CSS style‑class
        names from JavaFX class names, and for deriving CSS property names from
        JavaFX variable names. Note that this is only a naming convention; there
        is no automatic name conversion. Most JavaFX names use "camel case,"
        that is, mixed case names formed from compound words, where the initial
        letter of each sub-word is capitalized. Most CSS names in the HTML world
        are all lower case, with compound words separated by hyphens. The
        convention is therefore to take JavaFX class names and form their
        corresponding CSS style‑class name by separating the compound words with
        hyphens and converting the letters to all lower case. For example, the
        JavaFX ToggleButton class would have a style‑class of "toggle-button".
        The convention for mapping JavaFX variable names to CSS property names
        is similar, with the addition of the "<code>-fx-</code>" prefix. For
        example, the blendMode variable would have a corresponding CSS property
        name of "<code>-fx-blend-mode</code>".
      </p>
    </section>
    <div class="pagination">
      <router-link
        to="/css/scene-parent-and-subscene-stylesheets"
        class="btn btn-prev"
        >❮ Scene, Parent and SubScene Stylesheets</router-link
      >
      <router-link to="/css/css-public-api" class="btn btn-next"
        >CSS Public API ❯</router-link
      >
    </div>
  </article>
</template>
