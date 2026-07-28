<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h3><a id="typeurl">&lt;uri&gt;</a></h3>
      <p class="grammar">url ( [\"\']? &lt;address&gt; [\"\']? )</p>
      <p>
        <span class="grammar">&lt;address&gt;</span> is a hierarchical URI of
        the form [scheme:][//authority][path]
        <a href="#references">(see [2])</a>. For example:
      </p>
      <p class="example">
        url(http://example.com/images/Duke.png)<br />
        url(/com/example/javafx/app/images/Duke.png)<br />
      </p>
      <p>
        If the <span class="grammar">&lt;address&gt;</span> does not have a
        [scheme:] component, the <span class="grammar">&lt;address&gt;</span>
        is considered to be the [path] component only. A leading '/' character
        indicates that the [path] is relative to the root of the classpath. If
        the the style appears in a stylesheet and has no leading '/' character,
        the path is relative to the base URI of the stylesheet. If the style
        appears in an inline style, the path is relative to the root of the
        classpath (regardless of whether or not there is a leading '/').
      </p>
      <table class="table table-dark table-striped table-hover table-bordered">
        <caption>
          Examples of Resolving URLs in Stylesheets
        </caption>
        <thead>
          <tr>
            <th scope="col">Stylesheet URL</th>
            <th scope="col">URL in Style</th>
            <th scope="col">Resolves to</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">
              file:///some/path/build/classes/com/mycompany/myapp/mystyles.css
            </th>
            <td>url(images/Duke.png)</td>
            <td>
              file:///some/path/build/classes/com/mycompany/myapp/images/Duke.png
            </td>
          </tr>
          <tr>
            <th scope="row">
              file:///some/path/build/classes/com/mycompany/myapp/mystyles.css
            </th>
            <td>url(../images/Duke.png)</td>
            <td>
              file:///some/path/build/classes/com/mycompany/images/Duke.png
            </td>
          </tr>
          <tr>
            <th scope="row">
              jar:file:/some/path/build/myapp.jar!/com/mycompany/myapp/mystyles.css
            </th>
            <td>url(images/Duke.png)</td>
            <td>
              jar:file:/some/path/build/myapp.jar!/com/mycompany/myapp/images/Duke.png
            </td>
          </tr>
        </tbody>
      </table>
      <p>&nbsp;</p>
      <table class="table table-dark table-striped table-hover table-bordered">
        <caption>
          Examples of Resolving URLs in Inline Styles
        </caption>
        <thead>
          <tr>
            <th scope="col">Classpath</th>
            <th scope="col">URL in Style</th>
            <th scope="col">Resolved URL</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">file:///some/path/build/classes</th>
            <td>url(/com/mycompany/resources/images/Duke.png)</td>
            <td>
              file:///some/path/build/classes/com/mycompany/resources/images/Duke.png
            </td>
          </tr>
          <tr>
            <th scope="row">file:///some/path/build/myapp.jar</th>
            <td>url(/com/mycompany/resources/images/Duke.png)</td>
            <td>
              jar:file:/some/path/build/myapp.jar!/com/mycompany/resources/images/Duke.png
            </td>
          </tr>
        </tbody>
      </table>
      <p>
        Note that for inline styles, leading dot-segments (e.g. '..' or '.') do
        resolve since the path is always anchored at the root of the classpath.
      </p>
      <p>
        As an example,
        <label for="uri-example-1"
          >the code snippet below creates a scene filled with a fictional
          'Duke.png' image, located in an 'image' directory:</label
        >
      </p>
      <div class="code-block" id="uri-example-1">
        <pre><code>
    @Override public void start(Stage stage) {
        StackPane root = new StackPane();
        root.setStyle("<code>-fx-background-image</code>: url(images/Duke.png);");
        Scene scene = new Scene(root, 300, 250);
        stage.setScene(scene);
        stage.show();
    }
        </code></pre>
      </div>
      <div class="javafx-preview">
        <div class="javafx-rect" style="background-image: url('images/Duke.png'); width: 300px; height: 250px;"></div>
      </div>
      <p>The same style would work equally as well from a stylesheet.</p>
    </section>
    <div class="pagination">
      <router-link to="/css/color-stop" class="btn btn-prev"
        >❮ &lt;color-stop&gt;</router-link
      >
      <router-link to="/css/effect" class="btn btn-next"
        >&lt;effect&gt; ❯</router-link
      >
    </div>
  </article>
</template>
