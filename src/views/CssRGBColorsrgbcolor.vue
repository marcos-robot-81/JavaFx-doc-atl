<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4>RGB Colors <span class="grammar" style="font-size: smaller;">&lt;rgb-color&gt;</span></h4>
    <p>The RGB color model is used in numerical color specifications. It has a
      number of different supported forms.</p>
    <p class="grammar">#&lt;digit&gt;&lt;digit&gt;&lt;digit&gt;<br>
      |
      #&lt;digit&gt;&lt;digit&gt;&lt;digit&gt;&lt;digit&gt;&lt;digit&gt;&lt;digit&gt;<br>
      | rgb( <a href="#typenumber" class="typelink">&lt;integer&gt;</a> , <a href="#typenumber" class="typelink">&lt;integer&gt;</a>
      , <a href="#typenumber" class="typelink">&lt;integer&gt;</a> )<br>
      | rgb( <a href="#typenumber" class="typelink">&lt;integer&gt;</a> %, <a href="#typenumber" class="typelink">&lt;integer&gt;</a>%
      , <a href="#typenumber" class="typelink">&lt;integer&gt;</a>% )<br>
      | rgba( <a href="#typenumber" class="typelink">&lt;integer&gt;</a> , <a href="#typenumber" class="typelink">&lt;integer&gt;</a>
      , <a href="#typenumber" class="typelink">&lt;integer&gt;</a> , <a href="#typenumber" class="typelink">&lt;number&gt;</a>
      ) <br>
      | rgba( <a href="#typenumber" class="typelink">&lt;integer&gt;</a>% , <a href="#typenumber" class="typelink">&lt;integer&gt;</a>%
      , <a href="#typenumber" class="typelink">&lt;integer&gt;</a> %, <a href="#typenumber" class="typelink">&lt;number&gt;</a>
      )</p>
    <p>These examples all specify the same color for the text fill of a Label:</p>
    <p class="example">&nbsp;</p>
    <ul style="list-style: none;">
      <li>.label { -fx-text-fill: #f00 } /* #rgb */</li>
      <li>.label { -fx-text-fill: #ff0000 } /* #rrggbb */</li>
      <li>.label { -fx-text-fill: rgb(255,0,0) }</li>
      <li> .label { -fx-text-fill: rgb(100%, 0%, 0%) }</li>
      <li>.label { -fx-text-fill: rgba(255,0,0,1) }</li>
    </ul>
    <p>&nbsp;</p>
    <p><strong>RGB Hex</strong>: The format of an RGB value in hexadecimal
      notation is a ‘#’ immediately followed by either three or six
      hexadecimal characters. The three-digit RGB notation (#rgb) is converted
      into six-digit form (#rrggbb) by replicating digits, not by adding zeros.
      For example, #fb0 expands to #ffbb00. This ensures that white (#ffffff)
      can be specified with the short notation (#fff) and removes any
      dependencies on the color depth of the display.</p>
    <p><strong>RGB Decimal or Percent</strong>: The format of an RGB value in
      the functional notation is ‘rgb(’ followed by a
      comma-separated list of three numerical values (either three decimal
      integer values or three percentage values) followed by ‘)’.
      The integer value 255 corresponds to 100%, and to F or FF in the
      hexadecimal notation: rgb(255,255,255) = rgb(100%,100%,100%) = #FFF. White
      space characters are allowed around the numerical values.</p>
    <p><strong>RGB + Alpha</strong>: This is an extension of the RGB color model
      to include an ‘alpha’ value that specifies the opacity of a
      color. This is accomplished via a functional syntax of the form rgba(...)
      form that takes a fourth parameter which is the alpha value. The alpha
      value must be a number in the range 0.0 (representing completely
      transparent) and 1.0 (completely opaque). As with the rgb() function, the
      red, green, and blue values may be decimal integers or percentages. The
      following examples all specify the same color:</p>
    <p class="example">&nbsp;</p>
    <ul style="list-style: none;">
      <li>.label { -fx-text-fill: rgb(255,0,0) } /* integer range 0 — 255*/</li>
      <li> .label { -fx-text-fill: rgba(255,0,0,1) /* the same, with explicit
        opacity of 1 */</li>
      <li> .label { -fx-text-fill: rgb(100%,0%,0%) } /* float range 0.0% —
        100.0% */</li>
      <li> .label { -fx-text-fill: rgba(100%,0%,0%,1) } /* the same, with
        explicit opacity of 1 */</li>
    </ul>
    <p>&nbsp;</p>
    </section>
    <div class="pagination">
      <router-link to="/css/looked-up-colors-looked-up-color" class="btn btn-prev">❮ Looked-up Colors &lt;looked-up-color&gt;</router-link>
      <router-link to="/css/hsb-colors-hsb-color" class="btn btn-next">HSB Colors &lt;hsb-color&gt; ❯</router-link>
    </div>
  </article>
</template>
