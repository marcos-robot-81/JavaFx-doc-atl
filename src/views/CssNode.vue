<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="node">Node</a></h4>
      <p class="styleclass">Style class: empty by default<br /></p>
      <table class="table table-dark table-striped table-hover table-bordered">
        <caption>
          Available CSS Properties
        </caption>
        <thead>
          <tr>
            <th class="propertyname" scope="col">CSS Property</th>
            <th class="value" scope="col">Values</th>
            <th class="default" scope="col">Default</th>
            <th class="range" scope="col">Range</th>
            <th scope="col">Comments</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-blend-mode</code>
            </th>
            <td class="value">
              [ add | blue | color-burn | color-dodge | darken | difference |
              exclusion | green | hard-light | lighten | multiply | overlay |
              red | screen | soft-light | src-atop | src-in | src-out | src-over
              ]
            </td>
            <td>null</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-cursor</code></th>
            <td class="value">
              [ null | crosshair | default | hand | move | e-resize | h-resize |
              ne-resize | nw-resize | n-resize | se-resize | sw-resize |
              s-resize | w-resize | v-resize | text | wait ] |
              <a href="#typeurl" class="typelink">&lt;url&gt;</a>
            </td>
            <td class="default">null</td>
            <td class="range">&nbsp;</td>
            <td>inherits</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-effect</code></th>
            <td class="value">
              <a href="#typeeffect" class="typelink">&lt;effect&gt;</a>
            </td>
            <td class="default">null</td>
            <td class="range">&nbsp;</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-focus-traversable</code>
            </th>
            <td class="value">
              <a href="#typeboolean" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td class="default">false</td>
            <td class="range">&nbsp;</td>
            <td>
              The default value for controls is true, although there are some
              exceptions. See <a href="#control">Control</a> for details.
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-view-order</code>
            </th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;number&gt;</a>
            </td>
            <td class="default">0</td>
            <td class="range">&nbsp;</td>
            <td>
              This property is used to alter the rendering and picking order of
              a node within its parent without reordering the parent's children
              list. The parent traverses its children in decreasing viewOrder
              order.
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-opacity</code></th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;number&gt;</a>
            </td>
            <td class="default">1</td>
            <td class="range">[0.0 ... 1.0]</td>
            <td>
              Opacity can be thought of conceptually as a postprocessing
              operation. Conceptually, after the node (including its
              descendants) is rendered into an RGBA offscreen image, the opacity
              setting specifies how to blend the offscreen rendering into the
              current composite rendering.
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-rotate</code></th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;number&gt;</a>
            </td>
            <td class="default">0</td>
            <td class="range">&nbsp;</td>
            <td>
              This is the angle of the rotation in degrees. Zero degrees is at 3
              o'clock (directly to the right). Angle values are positive
              clockwise. Rotation is about the center.
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-scale-x</code></th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;number&gt;</a>
            </td>
            <td class="default">1</td>
            <td class="range">&nbsp;</td>
            <td>scale about the center</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-scale-y</code></th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;number&gt;</a>
            </td>
            <td class="default">1</td>
            <td class="range">&nbsp;</td>
            <td>scale about the center</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-scale-z</code></th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;number&gt;</a>
            </td>
            <td class="default">1</td>
            <td class="range">&nbsp;</td>
            <td>scale about the center</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-translate-x</code>
            </th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;number&gt;</a>
            </td>
            <td class="default">0</td>
            <td class="range">&nbsp;</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-translate-y</code>
            </th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;number&gt;</a>
            </td>
            <td class="default">0</td>
            <td class="range">&nbsp;</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-translate-z</code>
            </th>
            <td class="value">
              <a href="#typenumber" class="typelink">&lt;number&gt;</a>
            </td>
            <td class="default">0</td>
            <td class="range">&nbsp;</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">visibility</th>
            <td class="value">[ visible | hidden | collapse | inherit ]</td>
            <td class="default">true (i.e, visible)</td>
            <td class="range">&nbsp;</td>
            <td>
              See
              <a href="http://www.w3.org/TR/CSS2/visufx.html#visibility"
                >W3C visibility property</a
              >
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-managed</code></th>
            <td class="value">
              <a href="#typeboolean" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td class="default">true</td>
            <td class="range">&nbsp;</td>
            <td>
              Defines whether this node's layout will be managed by its parent
            </td>
          </tr>
        </tbody>
      </table>
      <h4>Pseudo-classes</h4>
      <table class="table table-dark table-striped table-hover table-bordered">
        <caption>
          Available CSS Pseudo-classes
        </caption>
        <tbody>
          <tr>
            <th class="propertyname subheader" scope="col">
              User Action Pseudo-classes
            </th>
            <th class="subheader" scope="col">Comments</th>
          </tr>
          <tr>
            <th class="propertyname" scope="row">focused</th>
            <td>applies when the <strong>focused</strong> variable is true</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">focus-visible</th>
            <td>
              applies when the <strong>focusVisible</strong> variable is true
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">focus-within</th>
            <td>
              applies when the <strong>focusWithin</strong> variable is true
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">hover</th>
            <td>applies when the <strong>hover</strong> variable is true</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">pressed</th>
            <td>applies when the <strong>pressed</strong> variable is true</td>
          </tr>
          <tr>
            <th class="propertyname subheader" scope="col">
              Input Pseudo-classes
            </th>
            <th class="subheader" scope="col">Comments</th>
          </tr>
          <tr>
            <th class="propertyname" scope="row">disabled</th>
            <td>applies when the <strong>disabled</strong> variable is true</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">show-mnemonic</th>
            <td>
              applies when the mnemonic affordance (typically an underscore)
              should be shown
            </td>
          </tr>
          <tr>
            <th class="propertyname subheader" scope="col">
              Tree-Structural Pseudo-classes
            </th>
            <th class="subheader" scope="col">Comments</th>
          </tr>
          <tr>
            <th class="propertyname" scope="row">first-child</th>
            <td>
              applies when the node is the first child in its
              <code>Parent</code> container
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">last-child</th>
            <td>
              applies when the node is the last child in its
              <code>Parent</code> container
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">only-child</th>
            <td>
              applies when the node is the only child in its
              <code>Parent</code> container
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">nth-child(even | odd)</th>
            <td>
              applies when the node is the n-th child in its
              <code>Parent</code> container (the first child at index 0 matches
              "odd", the second child at index 1 matches "even", etc.)
            </td>
          </tr>
        </tbody>
      </table>
    </section>
    <div class="pagination">
      <router-link to="/css/group" class="btn btn-prev">❮ Group</router-link>
      <router-link to="/css/parent" class="btn btn-next">Parent ❯</router-link>
    </div>
  </article>
</template>
