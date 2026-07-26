<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h3><a id="introtransitions">Transitions</a></h3>
      <p>
        JavaFX supports <em>implicit transitions</em> for properties that are
        styled by CSS. When a property value is changed by CSS, it transitions
        to its new value over a period of time. Implicit transitions are
        supported for all primitive types, as well as for types that implement
        <code>javafx.animation.Interpolatable</code>.
      </p>
      <p>
        Transitions can be defined for any node in the JavaFX scene graph with
        the following properties:
      </p>
      <table class="table table-dark table-striped table-hover table-bordered">
        <caption>
          Transition Properties
        </caption>
        <thead>
          <tr>
            <th class="propertyname" scope="col">CSS Property</th>
            <th class="value" scope="col">Values</th>
            <th scope="col">Default</th>
            <th scope="col">Comments</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th class="propertyname" scope="row">transition‑property</th>
            <td class="value">[ none | all | &lt;custom‑ident&gt;# ]</td>
            <td class="default">all</td>
            <td>
              The name of the CSS property to which the transition is applied.
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">transition‑duration</th>
            <td class="value">
              <a href="#typeduration" class="typelink">&lt;duration&gt;#</a>
            </td>
            <td class="default">0s</td>
            <td>
              The duration of the transition, not including an optional delay
              before the transition starts.
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">transition‑timing‑function</th>
            <td class="value">
              <a href="#typeeasingfunction" class="typelink"
                >&lt;easing‑function&gt;#</a
              >
            </td>
            <td class="default">ease</td>
            <td>
              The easing function that is used to calculate the intermediate
              values.
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">transition‑delay</th>
            <td class="value">
              <a href="#typeduration" class="typelink">&lt;duration&gt;#</a>
            </td>
            <td class="default">0s</td>
            <td>
              The delay after which the transition starts. If a negative delay
              is specified, the transition starts as if it had already been
              running for the specified time.
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">transition</th>
            <td class="value">
              &lt;single-transition&gt;#
              <br /><br />
              <strong>where</strong> &lt;single‑transition&gt; = [ none | all |
              &lt;custom‑ident&gt; ] ||
              <a href="#typeduration" class="typelink">&lt;duration&gt;</a> ||
              <a href="#typeeasingfunction" class="typelink"
                >&lt;easing‑function&gt;</a
              >
              ||
              <a href="#typeduration" class="typelink">&lt;duration&gt;</a>
            </td>
            <td class="default"></td>
            <td>
              Short-hand notation for the individual properties. Note that while
              the order of the values generally doesn't matter, the first
              duration is always assigned to the
              <strong>transition-duration</strong> property, while the second
              duration is always assigned to the
              <strong>transition-delay</strong> property.
            </td>
          </tr>
        </tbody>
      </table>
      <p>
        A transition is not started (or cancelled if already running) in any of
        these scenarios:
      </p>
      <ol>
        <li>The property value is set programmatically</li>
        <li>The property is bound</li>
        <li>
          The node (or any of its parents) is invisible, as indicated by the
          <a
            href="https://openjfx.io/javadoc/26/javafx.graphics/javafx/scene/Node.html#visibleProperty()"
            >Node.visible</a
          >
          property
        </li>
        <li>The node is removed from the scene graph</li>
      </ol>
      <p></p>
      Nodes fire
      <a
        href="https://openjfx.io/javadoc/26/javafx.graphics/javafx/css/TransitionEvent.html"
        >TransitionEvent</a
      >
      to signal the creation, beginning, completion and cancellation of
      transitions.
    </section>
    <div class="pagination">
      <router-link to="/css/inheritance" class="btn btn-prev"
        >❮ Inheritance</router-link
      >
      <router-link to="/css/example" class="btn btn-next"
        >Example ❯</router-link
      >
    </div>
  </article>
</template>
