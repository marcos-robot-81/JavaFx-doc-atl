<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4><a id="region">Region</a></h4>
<p class="styleclass">Style class: empty by default</p>
    <p>A Region is a Node (extending from Parent) with backgrounds and borders
      that are styleable via CSS. A Region is typically a rounded rectangle,
      though this can be modified through CSS to be an arbitrary shape. Regions
      can contain other Region objects (sub-regions) or they can contain
      sub-controls. All Regions have the same set of CSS properties as described
      below. </p>
    <p>Each Region consists of several layers, painted from bottom to top, in
      this order:</p>
    <ol>
      <li>background fills</li>
      <li>background images</li>
      <li>border strokes</li>
      <li>border images</li>
      <li>contents</li>
    </ol>
    <p>The background and border mechanisms are patterned after the CSS 3 draft
      backgrounds and borders module. See <a href="#references">[4]</a> for a
      detailed description.</p>
    <p>Background fills are specified with the properties <span class="propertyname">-fx-background-color</span>,
      <span class="propertyname">-fx-background-radius</span> and <span class="propertyname">-fx-background-insets</span>.
      The -fx-background-color property is a series of one or more
      comma-separated &lt;paint&gt; values. The number of values in the series
      determines the number of background rectangles that are painted.
      Background rectangles are painted in the order specified using the given
      &lt;paint&gt; value. Each background rectangle can have different radii
      and insets. The -fx-background-radius and -fx-background-insets properties
      are series of comma-separated values (or sets of values). The radius and
      insets values used for a particular background are the found in the
      corresponding position in the -fx-background-radius and
      -fx-background-insets series. For example, suppose a series of three
      values is given for the -fx-background-color property. A series of three
      values should also be specified for the -fx-background-radius and
      -fx-background-insets properties. The first background will be painted
      using the first radius value and first insets value, the second background
      will be painted with the second radius value and second insets value, and
      so forth.</p>
    <p>Note also that properties such as -fx-background-radius and
      -fx-background-insets can contain a series of values or <span style="font-style:italic;">sets</span> of
      four values. A set of values is separated by whitespace, whereas the
      values or sets-of-values in a series are separated by commas. For
      -fx-background-radius, a single value indicates that the value should be
      used for the radius of all four corners of the background rectangle. A set
      of four values indicates that different radius values are to be used for
      the top-left, top-right, bottom-right, and bottom-left corners, in that
      order. Similarly, the -fx-background-insets property can also contain a
      series of values or sets of values. A set of four values for
      -fx-background-insets indicates that different insets are to be used for
      the top, right, bottom, and left edges of the rectangle, in that order.</p>
    <p>Background images are specified with the properties <span class="propertyname">-fx-background-image</span>,
      <span class="propertyname">-fx-background-repeat</span>, <span class="propertyname">-fx-background-position</span>
      and <span class="propertyname">-fx-background-size</span>. The number of
      images in the series of -fx-background-image values determines the number
      of background images that are painted. The -fx-background-repeat,
      -fx-background-position, and -fx-background-size properties each can
      contain a series of values. For each item in the -fx-background-image
      series, the corresponding items in the -fx-background-repeat,
      -fx-background-position, and -fx-background-size properties are applied to
      that background image.</p>
    <p>Stroked borders are specified with the properties <span class="propertyname">-fx-border-color</span>,
      <span class="propertyname">-fx-border-style</span>, <span class="propertyname">-fx-border-width</span>,
      <span class="propertyname">-fx-border-radius</span> and <span class="propertyname">-fx-border-insets</span>.
      Each property contains a series of items. The maximum number of items in the -fx-
      border-color or -fx-border-style property determines the number of border layers that are painted..
      Each border in the series is painted using information from the
      corresponding series item of the -fx-border-color, -fx-border-style, -fx-border-width,
      -fx-border-radius, and -fx-border-insets properties. If there is no -fx-border-color, the default color is black.
    if there is no -fx-border-style, the default style is solid. </p>
    <p>Image borders are specified with the properties <span class="propertyname">-fx-border-image-source</span>,
      <span class="propertyname">-fx-border-image-repeat</span>, <span class="propertyname">-fx-border-image-slice</span>,
      <span class="propertyname">-fx-border-image-width</span> and <span class="propertyname">-fx-border-image-insets</span>.
      Each property contains a series of items. The number of items in the
      -fx-border-image-source property determines the number of images that are
      painted. Each image in the series is painted using information from the
      corresponding series items of the -fx-border-image-repeat,
      -fx-border-image-slice, -fx-border-image-width, and
      -fx-border-image-insets properties.</p>
    <p>The region's contents are a sequence of nodes, like any other container.
      The contents are set programmatically and cannot be set via CSS.</p>
    <table class="table table-dark table-striped table-hover table-bordered" >
    <caption>Available CSS Properties</caption>
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
        <th colspan="4" class="propertyname" scope="row"><em>BACKGROUND FILLS</em> (see <a href="http://www.w3.org/TR/css3-background/#backgrounds" target="_blank">CSS
            Backgrounds and Borders Module Level 3: Backgrounds</a>)</th>
    </tr>
    <tr>
        <th class="propertyname" scope="row">-fx-region-background</th>
            <td class="value">javafx.scene.layout.Background</td>
            <td class="default">null</td>
            <td>This cannot be set directly from CSS but is created from the property values of
                -fx-background-color, -fx-background-image, -fx-background-insets, -fx-background-position,
                -fx-background-radius, -fx-background-repeat, -fx-background-size</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-background-color</th>
          <td class="value"><a href="#typepaint" class="typelink">&lt;paint&gt;</a>
            [ , <a href="#typepaint" class="typelink">&lt;paint&gt;</a> ]*</td>
          <td class="default">transparent</td>
          <td>A series of paint values separated by commas.</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-background-insets</th>
          <td class="value"><a href="#typesize" class="typelink">&lt;size&gt;</a>
            | <a href="#typesize" class="typelink">&lt;size&gt;</a> <a href="#typesize" class="typelink">&lt;size&gt;</a>
            <a href="#typesize" class="typelink">&lt;size&gt;</a> <a href="#typesize" class="typelink">&lt;size&gt;</a>
            [ , [ <a href="#typesize" class="typelink">&lt;size&gt;</a> | <a href="#typesize" class="typelink">&lt;size&gt;</a>
            <a href="#typesize" class="typelink">&lt;size&gt;</a> <a href="#typesize" class="typelink">&lt;size&gt;</a>
            <a href="#typesize" class="typelink">&lt;size&gt;</a>] ]*</td>
          <td class="default">0 0 0 0</td>
          <td>
            <p>A series of size values or sets of four size values, separated by
              commas. A single size value means all insets are the same.
              Otherwise, the four values for each inset are given in the order
              top, right, bottom, left. Each comma-separated value or set of
              values in the series applies to the corresponding background
              color.</p>
          </td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-background-radius</th>
            <td class="value">[<a href="#typesize" class="typelink">&lt;size&gt;</a>]{1,4} [ / [<a href="#typesize" class="typelink">&lt;size&gt;</a>]{1,4} ]?
                [ , [<a href="#typesize" class="typelink">&lt;size&gt;</a>]{1,4} [ / [<a href="#typesize" class="typelink">&lt;size&gt;</a>]{1,4} ]? ]*
            </td><td class="default">0 0 0 0</td>
            <td>
                <p>The same syntax and semantics as CSS Backgrounds and Borders Module Level 3: <a href="http://www.w3.org/TR/css3-background/#the-border-radius">Curve Radii</a>
                applies to -fx-background-radius. Note that JavaFX supports only the short-hand syntax.</p>
                <p>Each comma-separated value or set of values in the series applies to the corresponding background color.</p>
          </td>
        </tr>
        <tr>
        <th colspan="4" class="propertyname" scope="row"><em>BACKGROUND IMAGES</em> (see <a href="http://www.w3.org/TR/css3-background/#the-background-image" target="_blank">CSS
            Backgrounds and Borders Module Level 3: Background Image</a>)</th>
    </tr>
    <tr>
        <th class="propertyname" scope="row">-fx-background-image</th>
          <td class="value"><a href="#typeurl" class="typelink">&lt;uri&gt;</a>
            [ , <a href="#typeurl" class="typelink">&lt;uri&gt;</a> ]*</td>
          <td class="default">null</td>
          <td>A series of image URIs separated by commas.</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-background-position</th>
          <td class="value">
            <p>&lt;bg-position&gt; [ , &lt;bg-position&gt; ]*<br>
              <strong>where</strong> &lt;bg-position&gt; = [<br>
              &nbsp;&nbsp;&nbsp;&nbsp;[ [ <a href="#typesize" class="typelink">&lt;size&gt;</a>
              | left | center | right ] [ <a href="#typesize" class="typelink">&lt;size&gt;</a>
              | top | center | bottom ]? ]<br>
              &nbsp;&nbsp;&nbsp;&nbsp;| [ [ center | [ left | right ] <a href="#typesize" class="typelink">&lt;size&gt;</a>?
              ] || [ center | [ top | bottom ] <a href="#typesize" class="typelink">&lt;size&gt;</a>?
              ]<br>
              ] </p>
          </td>
          <td class="default">0% 0%</td>
          <td>
            <p>A series of &lt;bg-position&gt; values separated by commas. Each
              bg-position item in the series applies to the corresponding image
              in the background-image series.</p>
          </td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-background-repeat</th>
          <td class="value">&lt;repeat-style&gt; [ , &lt;repeat-style&gt; ]*<br>
            <strong>where</strong> &lt;repeat-style&gt; = repeat-x | repeat-y |
            [repeat | space | round | stretch | no-repeat]{1,2}</td>
          <td class="default">repeat repeat</td>
          <td>
            <p>A series of &lt;repeat-style&gt; values separated by commas. Each
              repeat-style item in the series applies to the corresponding image
              in the background-image series.</p>
          </td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-background-size</th>
          <td class="value">&lt;bg-size&gt; [ , &lt;bg-size&gt; ]*<br>
            &lt;bg-size&gt; = [ <a href="#typesize" class="typelink">&lt;size&gt;</a>
            | auto ]{1,2} | cover | contain | stretch</td>
          <td class="default">auto auto</td>
          <td>
            <p>A series of &lt;bg-size&gt; values separated by commas. Each
              bg-size item in the series applies to the corresponding image in
              the background-image series.</p>
          </td>
        </tr>
        <tr>
        <th colspan="4" class="propertyname" scope="row"><em>STROKED BORDERS</em> (see <a href="http://www.w3.org/TR/css3-background/#borders" target="_blank">CSS Backgrounds and Borders Module Level 3: Borders</a>)
            <div><em>BORDER IMAGES</em> (see <a href="http://www.w3.org/TR/css3-background/#border-images" target="_blank">CSS
                Backgrounds and Borders Module Level 3: Border Images</a>)</div>
        </th>
        </tr>

        <tr>
        <th class="propertyname" scope="row">-fx-region-border</th>
            <td class="value">javafx.scene.layout.Border</td>
            <td class="default">null</td>
            <td>This cannot be set directly from CSS but is created from the property values of
                -fx-border-color, -fx-border-insets, -fx-border-radius,  -fx-border-style, -fx-border-width,
                -fx-border-image-insets, -fx-border-image-repeat, -fx-border-image-slice, -fx-border-image-source,
                -fx-border-image-width</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-border-color</th>
          <td class="value"><a href="#typepaint" class="typelink">&lt;paint&gt;</a>
            | <a href="#typepaint" class="typelink">&lt;paint&gt;</a> <a href="#typepaint" class="typelink">&lt;paint&gt;</a>
            <a href="#typepaint" class="typelink">&lt;paint&gt;</a> <a href="#typepaint" class="typelink">&lt;paint&gt;</a>
            [ , [<a href="#typepaint" class="typelink">&lt;paint&gt;</a> | <a href="#typepaint" class="typelink">&lt;paint&gt;</a>
            <a href="#typepaint" class="typelink">&lt;paint&gt;</a> <a href="#typepaint" class="typelink">&lt;paint&gt;</a>
            <a href="#typepaint" class="typelink">&lt;paint&gt;</a>] ]*</td>
          <td class="default">null</td>
          <td>
            <p>A series of paint values or sets of four paint values, separated
              by commas. For each item in the series, if a single paint value is
              specified, then that paint is used as the border for all sides of
              the region; and if a set of four paints is specified, they are
              used for the top, right, bottom, and left borders of the region,
              in that order. If the border is not rectangular, only the first
              paint value in the set is used.</p>
          </td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-border-insets</th>
          <td class="value"><a href="#typesize" class="typelink">&lt;size&gt;</a>
            | <a href="#typesize" class="typelink">&lt;size&gt;</a> <a href="#typesize" class="typelink">&lt;size&gt;</a>
            <a href="#typesize" class="typelink">&lt;size&gt;</a> <a href="#typesize" class="typelink">&lt;size&gt;</a>
            [ , [ <a href="#typesize" class="typelink">&lt;size&gt;</a> | <a href="#typesize" class="typelink">&lt;size&gt;</a>
            <a href="#typesize" class="typelink">&lt;size&gt;</a> <a href="#typesize" class="typelink">&lt;size&gt;</a>
            <a href="#typesize" class="typelink">&lt;size&gt;</a>] ]*</td>
          <td class="default">null</td>
          <td>
            <p>A series of inset or sets of four inset values, separated by
              commas. For each item in the series, a single inset value means
              that all insets are the same; and if a set of four inset values is
              specified, they are used for the top, right, bottom, and left
              edges of the region, in that order. Each item in the series of
              insets applies to the corresponding item in the series of border
              colors.</p>
          </td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-border-radius</th>
          <td class="value">[<a href="#typesize" class="typelink">&lt;size&gt;</a>]{1,4} [ / [<a href="#typesize" class="typelink">&lt;size&gt;</a>]{1,4} ]?
            [ , [<a href="#typesize" class="typelink">&lt;size&gt;</a>]{1,4} [ / [<a href="#typesize" class="typelink">&lt;size&gt;</a>]{1,4} ]? ]*
          </td><td class="default">null</td>
          <td>
            <p>Refer to CSS Backgrounds and Borders Module Level 3: <a href="http://www.w3.org/TR/css3-background/#the-border-radius">Curve Radii</a>.
            JavaFX supports only the short-hand syntax.</p>
            <p>Each comma-separated value or set of values in the series applies to the corresponding border color.</p>
          </td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-border-style</th>
          <td class="value">
            <p>&lt;border-style&gt; [ , &lt;border-style&gt; ]*<br>
              <strong>where</strong> &lt;border-style&gt; = &lt;dash-style&gt;
              [phase &lt;number&gt;]? [centered | inside | outside]? [line-join
              [miter <a href="#typenumber" class="typelink">&lt;number&gt;</a>
              | bevel | round]]? [line-cap [square | butt | round]]?<br>
              <strong>where</strong> &lt;dash-style&gt; = [ none | solid |
              dotted | dashed | segments( &lt;number&gt;, &lt;number&gt; [,
              &lt;number&gt;]*) ]</p>
          </td>
          <td class="default">null</td>
          <td>
            <p>A series of border style values, separated by commas. Each item
              in the series applies to the corresponding item in the series of
              border colors.</p>
            <p>The <span style="font-style:italic;">segments</span> dash-style defines a sequence representing
              the lengths of the dash segments. Alternate entries in the
              sequence represent the lengths of the opaque and transparent
              segments of the dashes. This corresponds to the <span style="font-style:italic;">strokeDashArray</span>
              variable of Shape.</p>
            <p>The optional <span style="font-style:italic;">phase</span> parameter defines the point in the
              dashing pattern that will correspond to the beginning of the
              stroke. This corresponds to the <span style="font-style:italic;">strokeDashOffset</span> variable
              of Shape.</p>
          </td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-border-width</th>
          <td class="value"><a href="#typesize" class="typelink">&lt;size&gt;</a>
            | <a href="#typesize" class="typelink">&lt;size&gt;</a> <a href="#typesize" class="typelink">&lt;size&gt;</a>
            <a href="#typesize" class="typelink">&lt;size&gt;</a> <a href="#typesize" class="typelink">&lt;size&gt;</a>
            [ , [ <a href="#typesize" class="typelink">&lt;size&gt;</a> | <a href="#typesize" class="typelink">&lt;size&gt;</a>
            <a href="#typesize" class="typelink">&lt;size&gt;</a> <a href="#typesize" class="typelink">&lt;size&gt;</a>
            <a href="#typesize" class="typelink">&lt;size&gt;</a>] ]*</td>
          <td class="default">null</td>
          <td>
            <p>A series of width or sets of four width values, separated by
              commas. For each item in the series, a single width value means
              that all border widths are the same; and if a set of four width
              values is specified, they are used for the top, right, bottom, and
              left border widths, in that order. If the border is not
              rectangular, only the first width value is used. Each item in the
              series of widths applies to the corresponding item in the series
              of border colors. </p>
          </td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-border-image-source</th>
          <td class="value"><a href="#typeurl" class="typelink">&lt;uri&gt;</a>
            [ , <a href="#typeurl" class="typelink">&lt;uri&gt;</a> ]*</td>
          <td class="default">null</td>
          <td>
            <p>A series of image URIs, separated by commas.</p>
          </td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-border-image-insets</th>
          <td class="value"><a href="#typesize" class="typelink">&lt;size&gt;</a>
            | <a href="#typesize" class="typelink">&lt;size&gt;</a> <a href="#typesize" class="typelink">&lt;size&gt;</a>
            <a href="#typesize" class="typelink">&lt;size&gt;</a> <a href="#typesize" class="typelink">&lt;size&gt;</a>
            [ , [ <a href="#typesize" class="typelink">&lt;size&gt;</a> | <a href="#typesize" class="typelink">&lt;size&gt;</a>
            <a href="#typesize" class="typelink">&lt;size&gt;</a> <a href="#typesize" class="typelink">&lt;size&gt;</a>
            <a href="#typesize" class="typelink">&lt;size&gt;</a>] ]*</td>
          <td class="default">0 0 0 0</td>
          <td>
            <p>A series of inset or sets of four inset values, separated by
              commas. For each item in the series, a single inset value means
              that all insets are the same; and if a set of four inset values is
              specified, they are used for the top, right, bottom, and left
              edges of the region, in that order. Each item in the series of
              insets applies to the corresponding image in the series of border
              images.</p>
          </td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-border-image-repeat</th>
          <td class="value">&lt;repeat-style&gt; [ , &lt;repeat-style&gt; ]*<br>
            <strong>where</strong> &lt;repeat-style&gt; = repeat-x | repeat-y |
            [repeat | space | round | no-repeat]{1,2}</td>
          <td class="default">repeat repeat</td>
          <td>
            <p>A series of repeat-style values, separated by commas. Each item
              in the series applies to the corresponding image in the series of
              border images.</p>
          </td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-border-image-slice</th>
          <td class="value">
            <p>[<a href="#typesize" class="typelink">&lt;size&gt;</a> | <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a> <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a> ] fill? [ ,
              [ <a href="#typesize" class="typelink">&lt;size&gt;</a> | <a href="#typesize" class="typelink">&lt;size&gt;</a>
                <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a> <a href="#typesize" class="typelink">&lt;size&gt;</a>
              <a href="#typesize" class="typelink">&lt;size&gt;</a> ] fill? ]*</p>
          </td>
          <td class="default">100%</td>
          <td>
            <p>A series of image slice values or sets of four values, separated
              by commas. Each item in the series applies to the corresponding
              image in the series of border images. For each item in the series,
              if four values are given, they specify the size of the top, right,
              bottom, and left slices. This effectively divides the image into
              nine regions: an upper left corner, a top edge, an upper right
              corner, a right edge, a lower right corner, a bottom edge, a lower
              left corner, a left edge and a middle. If one value is specified,
              this value is used for the slice values for all four edges. If
              'fill' is present, the middle slice is preserved, otherwise it is
              discarded. Percentage values may be used here, in which case the
              values are considered proportional to the source image.</p>
          </td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-border-image-width</th>
          <td class="value"><a href="#typesize" class="typelink">&lt;size&gt;</a>
            | <a href="#typesize" class="typelink">&lt;size&gt;</a> <a href="#typesize" class="typelink">&lt;size&gt;</a>
            <a href="#typesize" class="typelink">&lt;size&gt;</a> <a href="#typesize" class="typelink">&lt;size&gt;</a>
            [ , [ <a href="#typesize" class="typelink">&lt;size&gt;</a> | <a href="#typesize" class="typelink">&lt;size&gt;</a>
            <a href="#typesize" class="typelink">&lt;size&gt;</a> <a href="#typesize" class="typelink">&lt;size&gt;</a>
            <a href="#typesize" class="typelink">&lt;size&gt;</a>] ]*</td>
          <td class="default">1 1 1 1</td>
          <td>
            <p>A series of width or sets of four width values, separated by
              commas. For each item in the series, a single width value means
              that all border widths are the same; and if a set of four width
              values is specified, they are used for the top, right, bottom, and
              left border widths, in that order. If the border is not
              rectangular, only the first width value is used. Each item in the
              series of widths applies to the corresponding item in the series
              of border images. Percentage values may be used here, in which
              case the values are considered proportional to the border image
              area.</p>
          </td>
        </tr>
        <tr>
        <th colspan="4" class="propertyname" scope="row"><span style="font-style:italic;">OTHER</span></th>
    </tr>
    <tr>
        <th class="propertyname" scope="row">-fx-padding</th>
          <td class="value"><a href="#typesize" class="typelink">&lt;size&gt;</a>
            | <a href="#typesize" class="typelink">&lt;size&gt;</a> <a href="#typesize" class="typelink">&lt;size&gt;</a>
            <a href="#typesize" class="typelink">&lt;size&gt;</a> <a href="#typesize" class="typelink">&lt;size&gt;</a>
          </td>
          <td class="default">0 0 0 0</td>
          <td>
            <p>A sets of four padding values, separated by commas. For each item
              in the series, a single padding value means that all padding are
              the same; and if a set of four padding values is specified, they
              are used for the top, right, bottom, and left edges of the region,
              in that order.</p>
          </td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-position-shape</th>
          <td class="value"><a href="#typeboolean" class="typelink">&lt;boolean&gt;</a></td>
          <td class="default">true</td>
          <td>If <strong>true</strong> means the shape centered within the
            region's width and height, otherwise the shape is positioned at its
            source position. Has no effect if a shape string is not specified.</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-scale-shape</th>
          <td class="value"><a href="#typeboolean" class="typelink">&lt;boolean&gt;</a></td>
          <td class="default">true</td>
          <td>If <strong>true</strong> means the shape is scaled to fit the
            size of the region, otherwise the shape is at its source size, and
            its position depends on the value of the position-shape property.
            Has no effect if a shape string is not specified.</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-shape</th>
          <td class="value">"<a href="#typestring" class="typelink">&lt;string&gt;</a>"</td>
          <td class="default">null</td>
          <td>An SVG path string. By specifying a shape here the region takes on
            that shape instead of a rectangle or rounded rectangle. The syntax
            of this path string is specified in <a href="#references">[3]</a>.</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-snap-to-pixel</th>
          <td class="value"><a href="#typeboolean" class="typelink">&lt;boolean&gt;</a></td>
          <td class="default">true</td>
          <td>Defines whether this region rounds position/spacing and ceils size
            values to pixel boundaries when laying out its children.</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-region-background</th>
          <td class="value">&nbsp;</td>
          <td class="default">null</td>
          <td>This property is set by specifying -fx-background-color and/or -fx-background-image.
            Optionally, the properties -fx-background-insets, -fx-background-radius,
              -fx-background-position, -fx-background-repeat, and -fx-background-size may also be set.
              In order to set the Region background to null,
            specify the style "-fx-background-color: null; -fx-background-image: null;". There is no
            shorthand notation for -fx-region-background at this time.</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-region-border</th>
          <td class="value">&nbsp;</td>
          <td class="default">null</td>
          <td>This property is set by specifying -fx-border-color and/or -fx-border-image.
            Optionally -fx-border-insets, -fx-border-radius, -fx-border-style,
            -fx-border-width, -fx-border-image-insets, -fx-border-image-repeat,
              -fx-border-image-slice and -fx-border-image-width may be specified.
              In order to set the Region background to null,
              specify the style "-fx-border-color: null; -fx-border-image: null;". There is no
              shorthand notation for -fx-region-border at this time.</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-min-height, -fx-pref-height, -fx-max-height</th>
          <td class="value"><a href="#typesize" class="typelink">&lt;size&gt;</a></td>
          <td class="default">-1</td>
          <td>Percentage values are not useful since the actual value would be
              computed from the width and/or height of the Region's parent before
              the parent is laid out.</td>
        </tr>
        <tr>
        <th class="propertyname" scope="row">-fx-min-width, -fx-pref-width, -fx-max-width</th>
          <td class="value"><a href="#typesize" class="typelink">&lt;size&gt;</a></td>
          <td class="default">-1</td>
          <td>Percentage values are not useful since the actual value would be
              computed from the width and/or height of the Region's parent before
              the parent is laid out.</td>
        </tr>
        <tr>
        <th colspan="4" class="parents" scope="row">Also has all properties of <a href="#parent">Parent</a><br>
        </th>
        </tr>
      </tbody>
    </table>
    <br>
    </section>
    <div class="pagination">
      <router-link to="/css/pane" class="btn btn-prev">❮ Pane</router-link>
      <router-link to="/css/stackpane" class="btn btn-next">StackPane ❯</router-link>
    </div>
  </article>
</template>
