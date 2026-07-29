<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4>@font-face</h4>
      <p>
        Since JavaFX 8, the implementation partially supports the
        <label for="font-face-example-1"
          >CSS3 syntax to load a font from a URL</label
        >
        using the
        <a href="http://www.w3.org/TR/css3-fonts/#the-font-face-rule"
          >@font‑face</a
        >
        rule:
      </p>
      <div class="code-block" id="font-face-example-1">
        <pre><code>
     @font-face {
        font-family: 'sample';
        font-style: normal;
        font-weight: normal;
        src: local('sample'), url('http://font.samples/resources/sample.ttf';) format('truetype');
    }
        </code></pre>
      </div>
      <JavaFxPreview>
        <div class="javafx-rect" style="font-family: 'sample';">Sample Text with Custom Font</div>
      </JavaFxPreview>
      <p>
        This allows public resources for fonts to be used in a JavaFX
        application. For example, assume the URL
        "http://font.samples/web?family=samples" returns the @font‑face rule
        given above. Then the following code shows
        <label for="font-face-example-2"
          >how the sample font could be used in a JavaFX application.</label
        >
      </p>
      <div class="code-block" id="font-face-example-2">
        <pre><code>
    import javafx.application.Application;
    import javafx.scene.Scene;
    import javafx.scene.control.Label;
    import javafx.stage.Stage;

    public class HelloFontFace extends Application {
        @Override public void start(Stage primaryStage) {
            Label label = new Label("Hello @FontFace");
            label.setStyle("<code>-fx-font-family</code>: sample; <code>-fx-font-size</code>: 80;");
            Scene scene = new Scene(label);
            scene.getStylesheets().add("http://font.samples/web?family=samples");
            primaryStage.setTitle("Hello @FontFace");
            primaryStage.setScene(scene);
            primaryStage.show();
        }

        public static void main(String[] args) { launch(args); }
    }
        </code></pre>
      </div>
      <JavaFxPreview>
        <div style="font-family: 'sample'; font-size: 80px;">Hello @FontFace</div>
      </JavaFxPreview>
      <p>
        Or, the URL could be imported into a stylesheet with the @import rule.
      </p>
      <p>
        Although the parser will parse the syntax, all @font‑face descriptors
        are ignored except for the <code>src</code> descriptor. The
        <code>src</code> descriptor is expected to be a
        <a href="#typeurl" class="typelink">&lt;url&gt;</a>. The
        <code>format</code> hint is ignored.
      </p>
    </section>
    <div class="pagination">
      <router-link to="/css/import" class="btn btn-prev">❮ @import</router-link>
      <router-link to="/css/media" class="btn btn-next">@media ❯</router-link>
    </div>
  </article>
</template>
