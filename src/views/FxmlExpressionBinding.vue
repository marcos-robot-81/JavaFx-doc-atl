<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="expression_binding">Expression Binding</a></h4>
      <p>
        Attribute variables as shown above are resolved once at load time. Later
        updates to the variables value are not automatically reflected in any
        properties to which the value was assigned. In many cases, this is
        sufficient; however, it is often convenient to "bind" a property value
        to a variable or expression such that changes to the variable are
        automatically propagated to the target property. Expression bindings can
        be used for this purpose.
      </p>

      <p>
        An expression binding also begins with the variable resolution operator,
        but is followed by a set of curly braces which wrap the expression
        value. For example, the following markup binds the value of a text
        input's "text" property to the "text" property of a
        <span class="code">Label</span> instance:
      </p>

      <div class="code-block">
        <div class="code-header">Example</div>
        <pre><code>&lt;TextField fx:id="textField"/&gt;
&lt;Label text="${textField.text}"/&gt;
</code></pre>
      </div>

      <p>
        As the user types in the text input, the label's text content will be
        automatically updated.
      </p>

      <p>
        More complex expression are also supported. A list of supported
        constants and operators follows:
      </p>

      <table>
        <caption>
          Constants and Operators Table
        </caption>
        <tbody>
          <tr>
            <th scope="col">Constant / Operator</th>
            <th scope="col">Description</th>
          </tr>
          <tr>
            <th scope="row">"string"<br />'string'</th>
            <td>A string constant</td>
          </tr>
          <tr>
            <th scope="row">true<br />false</th>
            <td>A boolean constant</td>
          </tr>
          <tr>
            <th scope="row">null</th>
            <td>A constant representing the null value</td>
          </tr>
          <tr>
            <th scope="row">50.0<br />3e5<br />42</th>
            <td>A numerical constant</td>
          </tr>
          <tr>
            <th scope="row">- <br />(unary operator)</th>
            <td>Unary minus operator, applied on a number</td>
          </tr>
          <tr>
            <th scope="row">! <br />(unary operator)</th>
            <td>Unary negation of a boolean</td>
          </tr>
          <tr>
            <th scope="row">
              + - <br />
              * / %
            </th>
            <td>Numerical binary operators</td>
          </tr>
          <tr>
            <th scope="row">&amp;&amp; ||</th>
            <td>Boolean binary operators</td>
          </tr>
          <tr>
            <th scope="row">
              &gt; &gt;= <br />
              &lt; &lt;= <br />
              == !=
            </th>
            <td>
              Binary operators of comparison.<br />
              Both arguments must be of type Comparable
            </td>
          </tr>
        </tbody>
      </table>
      <div class="info-alert">
        <strong>HTML Analogy:</strong> In pure HTML, there is no built-in
        expression binding, so you would need to use JavaScript event listeners
        (e.g. <code>input</code> event) to manually update a DOM element when an
        input changes. However, in modern web frameworks like Vue.js, you
        achieve this using declarative bindings like <code>v-model</code> and
        text interpolation <code>{{}}</code>.
      </div>
      <div class="code-block">
        <div class="code-header">Web Equivalent (Vue.js)</div>
        <pre><code>&lt;input v-model="text" /&gt;
&lt;span&gt;{{ text }}&lt;/span&gt;</code></pre>
      </div>
    </section>
    <div class="pagination">
      <router-link to="/fxml/escape-sequences" class="btn btn-prev"
        >❮ Escape Sequences</router-link
      >
      <router-link to="/fxml/event-handlers" class="btn btn-next"
        >Event Handlers ❯</router-link
      >
    </div>
  </article>
</template>
