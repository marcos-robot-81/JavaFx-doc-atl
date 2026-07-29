<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h3><a id="introparserwarnings">Understanding Parser Warnings</a></h3>
      <p>
        When the JavaFX CSS parser encounters a syntax error, a warning message
        is emitted which conveys as much information as is available to help
        resolve the error. For example
      </p>
      <p class="example">
        WARNING: javafx.css.CssParser declaration Expected '&lt;percent&gt;'
        while parsing '<code>-fx-background-color</code>' at ?[1,49]
      </p>
      <p>
        The cryptic '<span class="p example">?[1,49]</span>' pertains to the
        location of the error. The format of the location string is
      </p>
      <p class="grammar">&lt;url&gt;[line, position]</p>
      <p>
        If the error is found while parsing a file, the file URL will be given.
        If the error is from an inline style (as in the example above), the URL
        is given as a question mark. The line and position give an offset into
        the file or string where the token begins.
        <em
          >Please note that the line and position may not be accurate in
          releases prior to JavaFX 2.2.</em
        ><br />
      </p>
      <p>
        Applications needing to detect errors from the parser can add a listener
        to the errors property of javafx.css.CssParser. <br />
      </p>
    </section>
    <div class="pagination">
      <router-link to="/css/examples" class="btn btn-prev"
        >❮ Examples</router-link
      >
      <router-link to="/css/limitations" class="btn btn-next"
        >Limitations ❯</router-link
      >
    </div>
  </article>
</template>
