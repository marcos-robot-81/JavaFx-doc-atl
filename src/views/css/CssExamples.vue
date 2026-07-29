<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h3><a id="introexamples">Examples</a></h3>
      <p>Consider the following simple JavaFX application:</p>
      <p class="example">
        Scene scene = new Scene(new Group()); <br />
        scene.getStylesheets().add(“test.css”); <br />
        Rectangle rect = new Rectangle(100,100); <br />
        rect.setLayoutX(50); <br />
        rect.setLayoutY(50); <br />
        rect.getStyleClass().add("my-rect"); <br />
        ((Group)scene.getRoot()).getChildren().add(rect);
      </p>
      <p>
        Without any styles, this will display a plain black rectangle. If
        test.css contains the following:
      </p>
      <p class="example">.my-rect { <code>-fx-fill</code>: red; }</p>
      <p>the rectangle will be red instead of black:</p>
      <p>
        <img src="/img/cssexample1_Sj7H.png" alt="A rectangle with red fill" />
      </p>
      <p>If test.css contains the following:</p>
      <p class="example">
        .my-rect {<br />
        &nbsp;&nbsp;&nbsp; <code>-fx-fill</code>: yellow;<br />
        &nbsp;&nbsp;&nbsp; <code>-fx-stroke</code>: green;<br />
        &nbsp;&nbsp;&nbsp; <code>-fx-stroke-width</code>: 5;<br />
        &nbsp;&nbsp;&nbsp; <code>-fx-stroke-dash-array</code>: 12 2 4 2;<br />
        &nbsp;&nbsp;&nbsp; <code>-fx-stroke-dash-offset</code>: 6;<br />
        &nbsp;&nbsp;&nbsp; <code>-fx-stroke-line-cap</code>: butt;<br />
        }<br />
      </p>
      <p>
        the result will be a yellow rectangle with a nicely dashed green border:
      </p>
      <p>
        <img
          src="/img/cssexample2_Sj7H.png"
          alt="A rectangle with yellow fill and a green, dashed border"
        />
      </p>
    </section>
    <div class="pagination">
      <router-link to="/css/media" class="btn btn-prev">❮ @media</router-link>
      <router-link
        to="/css/understanding-----parser-warnings"
        class="btn btn-next"
        >Understanding Parser Warnings ❯</router-link
      >
    </div>
  </article>
</template>
