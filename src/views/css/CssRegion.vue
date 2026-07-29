<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="region">Region</a></h4>
      <p class="styleclass">Style class: empty by default</p>
      <p>
        A Region is a Node (extending from Parent) with backgrounds and borders
        that are styleable via CSS. A Region is typically a rounded rectangle,
        though this can be modified through CSS to be an arbitrary shape.
        Regions can contain other Region objects (sub-regions) or they can
        contain sub-controls. All Regions have the same set of CSS properties as
        described below.
      </p>
      <p>
        Each Region consists of several layers, painted from bottom to top, in
        this order:
      </p>
      <ol>
        <li>background fills</li>
        <li>background images</li>
        <li>border strokes</li>
        <li>border images</li>
        <li>contents</li>
      </ol>
      <p>
        The background and border mechanisms are patterned after the CSS 3 draft
        backgrounds and borders module. See <a href="#references">[4]</a> for a
        detailed description.
      </p>
      <p>
        Background fills are specified with the properties
        <span class="propertyname"><code>-fx-background-color</code></span
        >,
        <span class="propertyname"><code>-fx-background-radius</code></span> and
        <span class="propertyname"><code>-fx-background-insets</code></span
        >. The <code>-fx-background-color</code> property is a series of one or
        more comma-separated &lt;paint&gt; values. The number of values in the
        series determines the number of background rectangles that are painted.
        Background rectangles are painted in the order specified using the given
        &lt;paint&gt; value. Each background rectangle can have different radii
        and insets. The <code>-fx-background-radius</code> and
        <code>-fx-background-insets</code> properties are series of
        comma-separated values (or sets of values). The radius and insets values
        used for a particular background are the found in the corresponding
        position in the <code>-fx-background-radius</code> and
        <code>-fx-background-insets</code> series. For example, suppose a series
        of three values is given for the
        <code>-fx-background-color</code> property. A series of three values
        should also be specified for the <code>-fx-background-radius</code> and
        <code>-fx-background-insets</code>
        properties. The first background will be painted using the first radius
        value and first insets value, the second background will be painted with
        the second radius value and second insets value, and so forth.
      </p>
      <p>
        Note also that properties such as <code>-fx-background-radius</code> and
        <code>-fx-background-insets</code> can contain a series of values or
        <span style="font-style: italic">sets</span> of four values. A set of
        values is separated by whitespace, whereas the values or sets-of-values
        in a series are separated by commas. For
        <code>-fx-background-radius</code>, a single value indicates that the
        value should be used for the radius of all four corners of the
        background rectangle. A set of four values indicates that different
        radius values are to be used for the top-left, top-right, bottom-right,
        and bottom-left corners, in that order. Similarly, the
        <code>-fx-background-insets</code> property can also contain a series of
        values or sets of values. A set of four values for
        <code>-fx-background-insets</code> indicates that different insets are
        to be used for the top, right, bottom, and left edges of the rectangle,
        in that order.
      </p>
      <p>
        Background images are specified with the properties
        <span class="propertyname"><code>-fx-background-image</code></span
        >, <span class="propertyname"><code>-fx-background-repeat</code></span
        >,
        <span class="propertyname"><code>-fx-background-position</code></span>
        and <span class="propertyname"><code>-fx-background-size</code></span
        >. The number of images in the series of
        <code>-fx-background-image</code> values determines the number of
        background images that are painted. The
        <code>-fx-background-repeat</code>,
        <code>-fx-background-position</code>, and
        <code>-fx-background-size</code> properties each can contain a series of
        values. For each item in the <code>-fx-background-image</code> series,
        the corresponding items in the <code>-fx-background-repeat</code>,
        <code>-fx-background-position</code>, and
        <code>-fx-background-size</code> properties are applied to that
        background image.
      </p>
      <p>
        Stroked borders are specified with the properties
        <span class="propertyname"><code>-fx-border-color</code></span
        >, <span class="propertyname"><code>-fx-border-style</code></span
        >, <span class="propertyname"><code>-fx-border-width</code></span
        >, <span class="propertyname"><code>-fx-border-radius</code></span> and
        <span class="propertyname"><code>-fx-border-insets</code></span
        >. Each property contains a series of items. The maximum number of items
        in the <code>-fx-</code> border-color or
        <code>-fx-border-style</code> property determines the number of border
        layers that are painted.. Each border in the series is painted using
        information from the corresponding series item of the
        <code>-fx-border-color</code>, <code>-fx-border-style</code>,
        <code>-fx-border-width</code>, <code>-fx-border-radius</code>, and
        <code>-fx-border-insets</code> properties. If there is no
        <code>-fx-border-color</code>, the default color is black. if there is
        no <code>-fx-border-style</code>, the default style is solid.
      </p>
      <p>
        Image borders are specified with the properties
        <span class="propertyname"><code>-fx-border-image-source</code></span
        >, <span class="propertyname"><code>-fx-border-image-repeat</code></span
        >, <span class="propertyname"><code>-fx-border-image-slice</code></span
        >,
        <span class="propertyname"><code>-fx-border-image-width</code></span>
        and
        <span class="propertyname"><code>-fx-border-image-insets</code></span
        >. Each property contains a series of items. The number of items in the
        <code>-fx-border-image-source</code> property determines the number of
        images that are painted. Each image in the series is painted using
        information from the corresponding series items of the
        <code>-fx-border-image-repeat</code>,
        <code>-fx-border-image-slice</code>,
        <code>-fx-border-image-width</code>, and
        <code>-fx-border-image-insets</code> properties.
      </p>
      <p>
        The region's contents are a sequence of nodes, like any other container.
        The contents are set programmatically and cannot be set via CSS.
      </p>
      <table class="table table-dark table-striped table-hover table-bordered">
        <caption>
          Available CSS Properties
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
            <th colspan="4" class="propertyname" scope="row">
              <em>BACKGROUND FILLS</em> (see
              <a
                href="http://www.w3.org/TR/css3-background/#backgrounds"
                target="_blank"
                >CSS Backgrounds and Borders Module Level 3: Backgrounds</a
              >)
            </th>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-region-background</code>
            </th>
            <td class="value">javafx.scene.layout.Background</td>
            <td class="default">null</td>
            <td>
              This cannot be set directly from CSS but is created from the
              property values of <code>-fx-background-color</code>,
              <code>-fx-background-image</code>,
              <code>-fx-background-insets</code>,
              <code>-fx-background-position</code>,
              <code>-fx-background-radius</code>,
              <code>-fx-background-repeat</code>,
              <code>-fx-background-size</code>
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-background-color</code>
            </th>
            <td class="value">
              <a href="#typepaint" class="typelink">&lt;paint&gt;</a> [ ,
              <a href="#typepaint" class="typelink">&lt;paint&gt;</a> ]*
            </td>
            <td class="default">transparent</td>
            <td>A series of paint values separated by commas.</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-background-insets</code>
            </th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;size&gt;</a> |
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a> [ , [
              <a href="#typesize" class="typelink">&lt;size&gt;</a> |
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>] ]*
            </td>
            <td class="default">0 0 0 0</td>
            <td>
              <p>
                A series of size values or sets of four size values, separated
                by commas. A single size value means all insets are the same.
                Otherwise, the four values for each inset are given in the order
                top, right, bottom, left. Each comma-separated value or set of
                values in the series applies to the corresponding background
                color.
              </p>
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-background-radius</code>
            </th>
            <td class="value">
              [<a href="#typesize" class="typelink">&lt;size&gt;</a>]{1,4} [ /
              [<a href="#typesize" class="typelink">&lt;size&gt;</a>]{1,4} ]? [
              , [<a href="#typesize" class="typelink">&lt;size&gt;</a>]{1,4} [ /
              [<a href="#typesize" class="typelink">&lt;size&gt;</a>]{1,4} ]? ]*
            </td>
            <td class="default">0 0 0 0</td>
            <td>
              <p>
                The same syntax and semantics as CSS Backgrounds and Borders
                Module Level 3:
                <a
                  href="http://www.w3.org/TR/css3-background/#the-border-radius"
                  >Curve Radii</a
                >
                applies to <code>-fx-background-radius</code>. Note that JavaFX
                supports only the short-hand syntax.
              </p>
              <p>
                Each comma-separated value or set of values in the series
                applies to the corresponding background color.
              </p>
            </td>
          </tr>
          <tr>
            <th colspan="4" class="propertyname" scope="row">
              <em>BACKGROUND IMAGES</em> (see
              <a
                href="http://www.w3.org/TR/css3-background/#the-background-image"
                target="_blank"
                >CSS Backgrounds and Borders Module Level 3: Background Image</a
              >)
            </th>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-background-image</code>
            </th>
            <td class="value">
              <a href="#typeurl" class="typelink">&lt;uri&gt;</a> [ ,
              <a href="#typeurl" class="typelink">&lt;uri&gt;</a> ]*
            </td>
            <td class="default">null</td>
            <td>A series of image URIs separated by commas.</td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-background-position</code>
            </th>
            <td class="value">
              <p>
                &lt;bg-position&gt; [ , &lt;bg-position&gt; ]*<br />
                <strong>where</strong> &lt;bg-position&gt; = [<br />
                &nbsp;&nbsp;&nbsp;&nbsp;[ [
                <a href="#typesize" class="typelink">&lt;size&gt;</a> | left |
                center | right ] [
                <a href="#typesize" class="typelink">&lt;size&gt;</a> | top |
                center | bottom ]? ]<br />
                &nbsp;&nbsp;&nbsp;&nbsp;| [ [ center | [ left | right ]
                <a href="#typesize" class="typelink">&lt;size&gt;</a>? ] || [
                center | [ top | bottom ]
                <a href="#typesize" class="typelink">&lt;size&gt;</a>? ]<br />
                ]
              </p>
            </td>
            <td class="default">0% 0%</td>
            <td>
              <p>
                A series of &lt;bg-position&gt; values separated by commas. Each
                bg-position item in the series applies to the corresponding
                image in the background-image series.
              </p>
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-background-repeat</code>
            </th>
            <td class="value">
              &lt;repeat-style&gt; [ , &lt;repeat-style&gt; ]*<br />
              <strong>where</strong> &lt;repeat-style&gt; = repeat-x | repeat-y
              | [repeat | space | round | stretch | no-repeat]{1,2}
            </td>
            <td class="default">repeat repeat</td>
            <td>
              <p>
                A series of &lt;repeat-style&gt; values separated by commas.
                Each repeat-style item in the series applies to the
                corresponding image in the background-image series.
              </p>
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-background-size</code>
            </th>
            <td class="value">
              &lt;bg-size&gt; [ , &lt;bg-size&gt; ]*<br />
              &lt;bg-size&gt; = [
              <a href="#typesize" class="typelink">&lt;size&gt;</a> | auto
              ]{1,2} | cover | contain | stretch
            </td>
            <td class="default">auto auto</td>
            <td>
              <p>
                A series of &lt;bg-size&gt; values separated by commas. Each
                bg-size item in the series applies to the corresponding image in
                the background-image series.
              </p>
            </td>
          </tr>
          <tr>
            <th colspan="4" class="propertyname" scope="row">
              <em>STROKED BORDERS</em> (see
              <a
                href="http://www.w3.org/TR/css3-background/#borders"
                target="_blank"
                >CSS Backgrounds and Borders Module Level 3: Borders</a
              >)
              <div>
                <em>BORDER IMAGES</em> (see
                <a
                  href="http://www.w3.org/TR/css3-background/#border-images"
                  target="_blank"
                  >CSS Backgrounds and Borders Module Level 3: Border Images</a
                >)
              </div>
            </th>
          </tr>

          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-region-border</code>
            </th>
            <td class="value">javafx.scene.layout.Border</td>
            <td class="default">null</td>
            <td>
              This cannot be set directly from CSS but is created from the
              property values of <code>-fx-border-color</code>,
              <code>-fx-border-insets</code>, <code>-fx-border-radius</code>,
              <code>-fx-border-style</code>, <code>-fx-border-width</code>,
              <code>-fx-border-image-insets</code>,
              <code>-fx-border-image-repeat</code>,
              <code>-fx-border-image-slice</code>,
              <code>-fx-border-image-source</code>,
              <code>-fx-border-image-width</code>
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-border-color</code>
            </th>
            <td class="value">
              <a href="#typepaint" class="typelink">&lt;paint&gt;</a> |
              <a href="#typepaint" class="typelink">&lt;paint&gt;</a>
              <a href="#typepaint" class="typelink">&lt;paint&gt;</a>
              <a href="#typepaint" class="typelink">&lt;paint&gt;</a>
              <a href="#typepaint" class="typelink">&lt;paint&gt;</a> [ , [<a
                href="#typepaint"
                class="typelink"
                >&lt;paint&gt;</a
              >
              | <a href="#typepaint" class="typelink">&lt;paint&gt;</a>
              <a href="#typepaint" class="typelink">&lt;paint&gt;</a>
              <a href="#typepaint" class="typelink">&lt;paint&gt;</a>
              <a href="#typepaint" class="typelink">&lt;paint&gt;</a>] ]*
            </td>
            <td class="default">null</td>
            <td>
              <p>
                A series of paint values or sets of four paint values, separated
                by commas. For each item in the series, if a single paint value
                is specified, then that paint is used as the border for all
                sides of the region; and if a set of four paints is specified,
                they are used for the top, right, bottom, and left borders of
                the region, in that order. If the border is not rectangular,
                only the first paint value in the set is used.
              </p>
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-border-insets</code>
            </th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;size&gt;</a> |
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a> [ , [
              <a href="#typesize" class="typelink">&lt;size&gt;</a> |
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>] ]*
            </td>
            <td class="default">null</td>
            <td>
              <p>
                A series of inset or sets of four inset values, separated by
                commas. For each item in the series, a single inset value means
                that all insets are the same; and if a set of four inset values
                is specified, they are used for the top, right, bottom, and left
                edges of the region, in that order. Each item in the series of
                insets applies to the corresponding item in the series of border
                colors.
              </p>
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-border-radius</code>
            </th>
            <td class="value">
              [<a href="#typesize" class="typelink">&lt;size&gt;</a>]{1,4} [ /
              [<a href="#typesize" class="typelink">&lt;size&gt;</a>]{1,4} ]? [
              , [<a href="#typesize" class="typelink">&lt;size&gt;</a>]{1,4} [ /
              [<a href="#typesize" class="typelink">&lt;size&gt;</a>]{1,4} ]? ]*
            </td>
            <td class="default">null</td>
            <td>
              <p>
                Refer to CSS Backgrounds and Borders Module Level 3:
                <a
                  href="http://www.w3.org/TR/css3-background/#the-border-radius"
                  >Curve Radii</a
                >. JavaFX supports only the short-hand syntax.
              </p>
              <p>
                Each comma-separated value or set of values in the series
                applies to the corresponding border color.
              </p>
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-border-style</code>
            </th>
            <td class="value">
              <p>
                &lt;border-style&gt; [ , &lt;border-style&gt; ]*<br />
                <strong>where</strong> &lt;border-style&gt; = &lt;dash-style&gt;
                [phase &lt;number&gt;]? [centered | inside | outside]?
                [line-join [miter
                <a href="#typenumber" class="typelink">&lt;number&gt;</a> |
                bevel | round]]? [line-cap [square | butt | round]]?<br />
                <strong>where</strong> &lt;dash-style&gt; = [ none | solid |
                dotted | dashed | segments( &lt;number&gt;, &lt;number&gt; [,
                &lt;number&gt;]*) ]
              </p>
            </td>
            <td class="default">null</td>
            <td>
              <p>
                A series of border style values, separated by commas. Each item
                in the series applies to the corresponding item in the series of
                border colors.
              </p>
              <p>
                The <span style="font-style: italic">segments</span> dash-style
                defines a sequence representing the lengths of the dash
                segments. Alternate entries in the sequence represent the
                lengths of the opaque and transparent segments of the dashes.
                This corresponds to the
                <span style="font-style: italic">strokeDashArray</span> variable
                of Shape.
              </p>
              <p>
                The optional
                <span style="font-style: italic">phase</span> parameter defines
                the point in the dashing pattern that will correspond to the
                beginning of the stroke. This corresponds to the
                <span style="font-style: italic">strokeDashOffset</span>
                variable of Shape.
              </p>
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-border-width</code>
            </th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;size&gt;</a> |
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a> [ , [
              <a href="#typesize" class="typelink">&lt;size&gt;</a> |
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>] ]*
            </td>
            <td class="default">null</td>
            <td>
              <p>
                A series of width or sets of four width values, separated by
                commas. For each item in the series, a single width value means
                that all border widths are the same; and if a set of four width
                values is specified, they are used for the top, right, bottom,
                and left border widths, in that order. If the border is not
                rectangular, only the first width value is used. Each item in
                the series of widths applies to the corresponding item in the
                series of border colors.
              </p>
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-border-image-source</code>
            </th>
            <td class="value">
              <a href="#typeurl" class="typelink">&lt;uri&gt;</a> [ ,
              <a href="#typeurl" class="typelink">&lt;uri&gt;</a> ]*
            </td>
            <td class="default">null</td>
            <td>
              <p>A series of image URIs, separated by commas.</p>
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-border-image-insets</code>
            </th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;size&gt;</a> |
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a> [ , [
              <a href="#typesize" class="typelink">&lt;size&gt;</a> |
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>] ]*
            </td>
            <td class="default">0 0 0 0</td>
            <td>
              <p>
                A series of inset or sets of four inset values, separated by
                commas. For each item in the series, a single inset value means
                that all insets are the same; and if a set of four inset values
                is specified, they are used for the top, right, bottom, and left
                edges of the region, in that order. Each item in the series of
                insets applies to the corresponding image in the series of
                border images.
              </p>
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-border-image-repeat</code>
            </th>
            <td class="value">
              &lt;repeat-style&gt; [ , &lt;repeat-style&gt; ]*<br />
              <strong>where</strong> &lt;repeat-style&gt; = repeat-x | repeat-y
              | [repeat | space | round | no-repeat]{1,2}
            </td>
            <td class="default">repeat repeat</td>
            <td>
              <p>
                A series of repeat-style values, separated by commas. Each item
                in the series applies to the corresponding image in the series
                of border images.
              </p>
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-border-image-slice</code>
            </th>
            <td class="value">
              <p>
                [<a href="#typesize" class="typelink">&lt;size&gt;</a> |
                <a href="#typesize" class="typelink">&lt;size&gt;</a>
                <a href="#typesize" class="typelink">&lt;size&gt;</a>
                <a href="#typesize" class="typelink">&lt;size&gt;</a>
                <a href="#typesize" class="typelink">&lt;size&gt;</a> ] fill? [
                , [ <a href="#typesize" class="typelink">&lt;size&gt;</a> |
                <a href="#typesize" class="typelink">&lt;size&gt;</a>
                <a href="#typesize" class="typelink">&lt;size&gt;</a>
                <a href="#typesize" class="typelink">&lt;size&gt;</a>
                <a href="#typesize" class="typelink">&lt;size&gt;</a>
                <a href="#typesize" class="typelink">&lt;size&gt;</a> ] fill? ]*
              </p>
            </td>
            <td class="default">100%</td>
            <td>
              <p>
                A series of image slice values or sets of four values, separated
                by commas. Each item in the series applies to the corresponding
                image in the series of border images. For each item in the
                series, if four values are given, they specify the size of the
                top, right, bottom, and left slices. This effectively divides
                the image into nine regions: an upper left corner, a top edge,
                an upper right corner, a right edge, a lower right corner, a
                bottom edge, a lower left corner, a left edge and a middle. If
                one value is specified, this value is used for the slice values
                for all four edges. If 'fill' is present, the middle slice is
                preserved, otherwise it is discarded. Percentage values may be
                used here, in which case the values are considered proportional
                to the source image.
              </p>
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-border-image-width</code>
            </th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;size&gt;</a> |
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a> [ , [
              <a href="#typesize" class="typelink">&lt;size&gt;</a> |
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>] ]*
            </td>
            <td class="default">1 1 1 1</td>
            <td>
              <p>
                A series of width or sets of four width values, separated by
                commas. For each item in the series, a single width value means
                that all border widths are the same; and if a set of four width
                values is specified, they are used for the top, right, bottom,
                and left border widths, in that order. If the border is not
                rectangular, only the first width value is used. Each item in
                the series of widths applies to the corresponding item in the
                series of border images. Percentage values may be used here, in
                which case the values are considered proportional to the border
                image area.
              </p>
            </td>
          </tr>
          <tr>
            <th colspan="4" class="propertyname" scope="row">
              <span style="font-style: italic">OTHER</span>
            </th>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-padding</code></th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;size&gt;</a> |
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
            </td>
            <td class="default">0 0 0 0</td>
            <td>
              <p>
                A sets of four padding values, separated by commas. For each
                item in the series, a single padding value means that all
                padding are the same; and if a set of four padding values is
                specified, they are used for the top, right, bottom, and left
                edges of the region, in that order.
              </p>
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-position-shape</code>
            </th>
            <td class="value">
              <a href="#typeboolean" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td class="default">true</td>
            <td>
              If <strong>true</strong> means the shape centered within the
              region's width and height, otherwise the shape is positioned at
              its source position. Has no effect if a shape string is not
              specified.
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-scale-shape</code>
            </th>
            <td class="value">
              <a href="#typeboolean" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td class="default">true</td>
            <td>
              If <strong>true</strong> means the shape is scaled to fit the size
              of the region, otherwise the shape is at its source size, and its
              position depends on the value of the position-shape property. Has
              no effect if a shape string is not specified.
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row"><code>-fx-shape</code></th>
            <td class="value">
              "<a href="#typestring" class="typelink">&lt;string&gt;</a>"
            </td>
            <td class="default">null</td>
            <td>
              An SVG path string. By specifying a shape here the region takes on
              that shape instead of a rectangle or rounded rectangle. The syntax
              of this path string is specified in <a href="#references">[3]</a>.
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-snap-to-pixel</code>
            </th>
            <td class="value">
              <a href="#typeboolean" class="typelink">&lt;boolean&gt;</a>
            </td>
            <td class="default">true</td>
            <td>
              Defines whether this region rounds position/spacing and ceils size
              values to pixel boundaries when laying out its children.
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-region-background</code>
            </th>
            <td class="value">&nbsp;</td>
            <td class="default">null</td>
            <td>
              This property is set by specifying
              <code>-fx-background-color</code> and/or
              <code>-fx-background-image</code>. Optionally, the properties
              <code>-fx-background-insets</code>,
              <code>-fx-background-radius</code>,
              <code>-fx-background-position</code>,
              <code>-fx-background-repeat</code>, and
              <code>-fx-background-size</code> may also be set. In order to set
              the Region background to null, specify the style
              "<code>-fx-background-color</code>: null;
              <code>-fx-background-image</code>: null;". There is no shorthand
              notation for <code>-fx-region-background</code> at this time.
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-region-border</code>
            </th>
            <td class="value">&nbsp;</td>
            <td class="default">null</td>
            <td>
              This property is set by specifying
              <code>-fx-border-color</code> and/or
              <code>-fx-border-image</code>. Optionally
              <code>-fx-border-insets</code>, <code>-fx-border-radius</code>,
              <code>-fx-border-style</code>, <code>-fx-border-width</code>,
              <code>-fx-border-image-insets</code>,
              <code>-fx-border-image-repeat</code>,
              <code>-fx-border-image-slice</code> and
              <code>-fx-border-image-width</code> may be specified. In order to
              set the Region background to null, specify the style
              "<code>-fx-border-color</code>: null;
              <code>-fx-border-image</code>: null;". There is no shorthand
              notation for <code>-fx-region-border</code> at this time.
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-min-height</code>, <code>-fx-pref-height</code>,
              <code>-fx-max-height</code>
            </th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
            </td>
            <td class="default">-1</td>
            <td>
              Percentage values are not useful since the actual value would be
              computed from the width and/or height of the Region's parent
              before the parent is laid out.
            </td>
          </tr>
          <tr>
            <th class="propertyname" scope="row">
              <code>-fx-min-width</code>, <code>-fx-pref-width</code>,
              <code>-fx-max-width</code>
            </th>
            <td class="value">
              <a href="#typesize" class="typelink">&lt;size&gt;</a>
            </td>
            <td class="default">-1</td>
            <td>
              Percentage values are not useful since the actual value would be
              computed from the width and/or height of the Region's parent
              before the parent is laid out.
            </td>
          </tr>
          <tr>
            <th colspan="4" class="parents" scope="row">
              Also has all properties of <a href="#parent">Parent</a><br />
            </th>
          </tr>
        </tbody>
      </table>
      <br />
    </section>
    <div class="pagination">
      <router-link to="/css/pane" class="btn btn-prev">❮ Pane</router-link>
      <router-link to="/css/stackpane" class="btn btn-next"
        >StackPane ❯</router-link
      >
    </div>
  </article>
</template>
