<template>
  <article class="content-area">
    <section class="doc-section glass-panel">
      <h4>
        Named Colors
        <span class="grammar" style="font-size: smaller"
          >&lt;named-color&gt;</span
        >
      </h4>
      <p>
        CSS supports a bunch of named constant colors. Named colors can be
        specified with just their unquoted name for example:
      </p>
      <p class="example">
        .button {<br />
        &nbsp;&nbsp;&nbsp; <code>-fx-background-color</code>: red;<br />
        }
      </p>
      <div class="javafx-preview">
        <button class="javafx-btn" style="background-color: red; color: white; padding: 10px 20px; border: none; border-radius: 4px; font-size: 14px;">Botão Exemplo</button>
      </div>
      <p>The named colors that are available in CSS are:</p>

      <div style="margin: 0 3em">
        <div class="colorsquare">
          <span style="background-color: aliceblue">&nbsp;</span>aliceblue =
          #f0f8ff
        </div>
        <div class="colorsquare">
          <span style="background-color: antiquewhite">&nbsp;</span>antiquewhite
          = #faebd7
        </div>
        <div class="colorsquare">
          <span style="background-color: aqua">&nbsp;</span>aqua = #00ffff
        </div>
        <div class="colorsquare">
          <span style="background-color: aquamarine">&nbsp;</span>aquamarine =
          #7fffd4
        </div>
        <div class="colorsquare">
          <span style="background-color: azure">&nbsp;</span>azure = #f0ffff
        </div>
        <div class="colorsquare">
          <span style="background-color: beige">&nbsp;</span>beige = #f5f5dc
        </div>
        <div class="colorsquare">
          <span style="background-color: bisque">&nbsp;</span>bisque = #ffe4c4
        </div>
        <div class="colorsquare">
          <span style="background-color: black">&nbsp;</span>black = #000000
        </div>
        <div class="colorsquare">
          <span style="background-color: blanchedalmond">&nbsp;</span
          >blanchedalmond = #ffebcd
        </div>
        <div class="colorsquare">
          <span style="background-color: blue">&nbsp;</span>blue = #0000ff
        </div>
        <div class="colorsquare">
          <span style="background-color: blueviolet">&nbsp;</span>blueviolet =
          #8a2be2
        </div>
        <div class="colorsquare">
          <span style="background-color: brown">&nbsp;</span>brown = #a52a2a
        </div>
        <div class="colorsquare">
          <span style="background-color: burlywood">&nbsp;</span>burlywood =
          #deb887
        </div>
        <div class="colorsquare">
          <span style="background-color: cadetblue">&nbsp;</span>cadetblue =
          #5f9ea0
        </div>
        <div class="colorsquare">
          <span style="background-color: chartreuse">&nbsp;</span>chartreuse =
          #7fff00
        </div>
        <div class="colorsquare">
          <span style="background-color: chocolate">&nbsp;</span>chocolate =
          #d2691e
        </div>
        <div class="colorsquare">
          <span style="background-color: coral">&nbsp;</span>coral = #ff7f50
        </div>
        <div class="colorsquare">
          <span style="background-color: cornflowerblue">&nbsp;</span
          >cornflowerblue = #6495ed
        </div>
        <div class="colorsquare">
          <span style="background-color: cornsilk">&nbsp;</span>cornsilk =
          #fff8dc
        </div>
        <div class="colorsquare">
          <span style="background-color: crimson">&nbsp;</span>crimson = #dc143c
        </div>
        <div class="colorsquare">
          <span style="background-color: cyan">&nbsp;</span>cyan = #00ffff
        </div>
        <div class="colorsquare">
          <span style="background-color: darkblue">&nbsp;</span>darkblue =
          #00008b
        </div>
        <div class="colorsquare">
          <span style="background-color: darkcyan">&nbsp;</span>darkcyan =
          #008b8b
        </div>
        <div class="colorsquare">
          <span style="background-color: darkgoldenrod">&nbsp;</span
          >darkgoldenrod = #b8860b
        </div>
        <div class="colorsquare">
          <span style="background-color: darkgray">&nbsp;</span>darkgray =
          #a9a9a9
        </div>
        <div class="colorsquare">
          <span style="background-color: darkgreen">&nbsp;</span>darkgreen =
          #006400
        </div>
        <div class="colorsquare">
          <span style="background-color: darkgrey">&nbsp;</span>darkgrey =
          #a9a9a9
        </div>
        <div class="colorsquare">
          <span style="background-color: darkkhaki">&nbsp;</span>darkkhaki =
          #bdb76b
        </div>
        <div class="colorsquare">
          <span style="background-color: darkmagenta">&nbsp;</span>darkmagenta =
          #8b008b
        </div>
        <div class="colorsquare">
          <span style="background-color: darkolivegreen">&nbsp;</span
          >darkolivegreen = #556b2f
        </div>
        <div class="colorsquare">
          <span style="background-color: darkorange">&nbsp;</span>darkorange =
          #ff8c00
        </div>
        <div class="colorsquare">
          <span style="background-color: darkorchid">&nbsp;</span>darkorchid =
          #9932cc
        </div>
        <div class="colorsquare">
          <span style="background-color: darkred">&nbsp;</span>darkred = #8b0000
        </div>
        <div class="colorsquare">
          <span style="background-color: darksalmon">&nbsp;</span>darksalmon =
          #e9967a
        </div>
        <div class="colorsquare">
          <span style="background-color: darkseagreen">&nbsp;</span>darkseagreen
          = #8fbc8f
        </div>
        <div class="colorsquare">
          <span style="background-color: darkslateblue">&nbsp;</span
          >darkslateblue = #483d8b
        </div>
        <div class="colorsquare">
          <span style="background-color: darkslategray">&nbsp;</span
          >darkslategray = #2f4f4f
        </div>
        <div class="colorsquare">
          <span style="background-color: darkslategrey">&nbsp;</span
          >darkslategrey = #2f4f4f
        </div>
        <div class="colorsquare">
          <span style="background-color: darkturquoise">&nbsp;</span
          >darkturquoise = #00ced1
        </div>
        <div class="colorsquare">
          <span style="background-color: darkviolet">&nbsp;</span>darkviolet =
          #9400d3
        </div>
        <div class="colorsquare">
          <span style="background-color: deeppink">&nbsp;</span>deeppink =
          #ff1493
        </div>
        <div class="colorsquare">
          <span style="background-color: deepskyblue">&nbsp;</span>deepskyblue =
          #00bfff
        </div>
        <div class="colorsquare">
          <span style="background-color: dimgray">&nbsp;</span>dimgray = #696969
        </div>
        <div class="colorsquare">
          <span style="background-color: dimgrey">&nbsp;</span>dimgrey = #696969
        </div>
        <div class="colorsquare">
          <span style="background-color: dodgerblue">&nbsp;</span>dodgerblue =
          #1e90ff
        </div>
        <div class="colorsquare">
          <span style="background-color: firebrick">&nbsp;</span>firebrick =
          #b22222
        </div>
        <div class="colorsquare">
          <span style="background-color: floralwhite">&nbsp;</span>floralwhite =
          #fffaf0
        </div>
        <div class="colorsquare">
          <span style="background-color: forestgreen">&nbsp;</span>forestgreen =
          #228b22
        </div>
        <div class="colorsquare">
          <span style="background-color: fuchsia">&nbsp;</span>fuchsia = #ff00ff
        </div>
        <div class="colorsquare">
          <span style="background-color: gainsboro">&nbsp;</span>gainsboro =
          #dcdcdc
        </div>
        <div class="colorsquare">
          <span style="background-color: ghostwhite">&nbsp;</span>ghostwhite =
          #f8f8ff
        </div>
        <div class="colorsquare">
          <span style="background-color: gold">&nbsp;</span>gold = #ffd700
        </div>
        <div class="colorsquare">
          <span style="background-color: goldenrod">&nbsp;</span>goldenrod =
          #daa520
        </div>
        <div class="colorsquare">
          <span style="background-color: gray">&nbsp;</span>gray = #808080
        </div>
        <div class="colorsquare">
          <span style="background-color: green">&nbsp;</span>green = #008000
        </div>
        <div class="colorsquare">
          <span style="background-color: greenyellow">&nbsp;</span>greenyellow =
          #adff2f
        </div>
        <div class="colorsquare">
          <span style="background-color: grey">&nbsp;</span>grey = #808080
        </div>
        <div class="colorsquare">
          <span style="background-color: honeydew">&nbsp;</span>honeydew =
          #f0fff0
        </div>
        <div class="colorsquare">
          <span style="background-color: hotpink">&nbsp;</span>hotpink = #ff69b4
        </div>
        <div class="colorsquare">
          <span style="background-color: indianred">&nbsp;</span>indianred =
          #cd5c5c
        </div>
        <div class="colorsquare">
          <span style="background-color: indigo">&nbsp;</span>indigo = #4b0082
        </div>
        <div class="colorsquare">
          <span style="background-color: ivory">&nbsp;</span>ivory = #fffff0
        </div>
        <div class="colorsquare">
          <span style="background-color: khaki">&nbsp;</span>khaki = #f0e68c
        </div>
        <div class="colorsquare">
          <span style="background-color: lavender">&nbsp;</span>lavender =
          #e6e6fa
        </div>
        <div class="colorsquare">
          <span style="background-color: lavenderblush">&nbsp;</span
          >lavenderblush = #fff0f5
        </div>
        <div class="colorsquare">
          <span style="background-color: lawngreen">&nbsp;</span>lawngreen =
          #7cfc00
        </div>
        <div class="colorsquare">
          <span style="background-color: lemonchiffon">&nbsp;</span>lemonchiffon
          = #fffacd
        </div>
        <div class="colorsquare">
          <span style="background-color: lightblue">&nbsp;</span>lightblue =
          #add8e6
        </div>
        <div class="colorsquare">
          <span style="background-color: lightcoral">&nbsp;</span>lightcoral =
          #f08080
        </div>
        <div class="colorsquare">
          <span style="background-color: lightcyan">&nbsp;</span>lightcyan =
          #e0ffff
        </div>
        <div class="colorsquare">
          <span style="background-color: lightgoldenrodyellow">&nbsp;</span
          >lightgoldenrodyellow = #fafad2
        </div>
        <div class="colorsquare">
          <span style="background-color: lightgray">&nbsp;</span>lightgray =
          #d3d3d3
        </div>
        <div class="colorsquare">
          <span style="background-color: lightgreen">&nbsp;</span>lightgreen =
          #90ee90
        </div>
        <div class="colorsquare">
          <span style="background-color: lightgrey">&nbsp;</span>lightgrey =
          #d3d3d3
        </div>
        <div class="colorsquare">
          <span style="background-color: lightpink">&nbsp;</span>lightpink =
          #ffb6c1
        </div>
        <div class="colorsquare">
          <span style="background-color: lightsalmon">&nbsp;</span>lightsalmon =
          #ffa07a
        </div>
        <div class="colorsquare">
          <span style="background-color: lightseagreen">&nbsp;</span
          >lightseagreen = #20b2aa
        </div>
        <div class="colorsquare">
          <span style="background-color: lightskyblue">&nbsp;</span>lightskyblue
          = #87cefa
        </div>
        <div class="colorsquare">
          <span style="background-color: lightslategray">&nbsp;</span
          >lightslategray = #778899
        </div>
        <div class="colorsquare">
          <span style="background-color: lightslategrey">&nbsp;</span
          >lightslategrey = #778899
        </div>
        <div class="colorsquare">
          <span style="background-color: lightsteelblue">&nbsp;</span
          >lightsteelblue = #b0c4de
        </div>
        <div class="colorsquare">
          <span style="background-color: lightyellow">&nbsp;</span>lightyellow =
          #ffffe0
        </div>
        <div class="colorsquare">
          <span style="background-color: lime">&nbsp;</span>lime = #00ff00
        </div>
        <div class="colorsquare">
          <span style="background-color: limegreen">&nbsp;</span>limegreen =
          #32cd32
        </div>
        <div class="colorsquare">
          <span style="background-color: linen">&nbsp;</span>linen = #faf0e6
        </div>
        <div class="colorsquare">
          <span style="background-color: magenta">&nbsp;</span>magenta = #ff00ff
        </div>
        <div class="colorsquare">
          <span style="background-color: maroon">&nbsp;</span>maroon = #800000
        </div>
        <div class="colorsquare">
          <span style="background-color: mediumaquamarine">&nbsp;</span
          >mediumaquamarine = #66cdaa
        </div>
        <div class="colorsquare">
          <span style="background-color: mediumblue">&nbsp;</span>mediumblue =
          #0000cd
        </div>
        <div class="colorsquare">
          <span style="background-color: mediumorchid">&nbsp;</span>mediumorchid
          = #ba55d3
        </div>
        <div class="colorsquare">
          <span style="background-color: mediumpurple">&nbsp;</span>mediumpurple
          = #9370db
        </div>
        <div class="colorsquare">
          <span style="background-color: mediumseagreen">&nbsp;</span
          >mediumseagreen = #3cb371
        </div>
        <div class="colorsquare">
          <span style="background-color: mediumslateblue">&nbsp;</span
          >mediumslateblue = #7b68ee
        </div>
        <div class="colorsquare">
          <span style="background-color: mediumspringgreen">&nbsp;</span
          >mediumspringgreen = #00fa9a
        </div>
        <div class="colorsquare">
          <span style="background-color: mediumturquoise">&nbsp;</span
          >mediumturquoise = #48d1cc
        </div>
        <div class="colorsquare">
          <span style="background-color: mediumvioletred">&nbsp;</span
          >mediumvioletred = #c71585
        </div>
        <div class="colorsquare">
          <span style="background-color: midnightblue">&nbsp;</span>midnightblue
          = #191970
        </div>
        <div class="colorsquare">
          <span style="background-color: mintcream">&nbsp;</span>mintcream =
          #f5fffa
        </div>
        <div class="colorsquare">
          <span style="background-color: mistyrose">&nbsp;</span>mistyrose =
          #ffe4e1
        </div>
        <div class="colorsquare">
          <span style="background-color: moccasin">&nbsp;</span>moccasin =
          #ffe4b5
        </div>
        <div class="colorsquare">
          <span style="background-color: navajowhite">&nbsp;</span>navajowhite =
          #ffdead
        </div>
        <div class="colorsquare">
          <span style="background-color: navy">&nbsp;</span>navy = #000080
        </div>
        <div class="colorsquare">
          <span style="background-color: oldlace">&nbsp;</span>oldlace = #fdf5e6
        </div>
        <div class="colorsquare">
          <span style="background-color: olive">&nbsp;</span>olive = #808000
        </div>
        <div class="colorsquare">
          <span style="background-color: olivedrab">&nbsp;</span>olivedrab =
          #6b8e23
        </div>
        <div class="colorsquare">
          <span style="background-color: orange">&nbsp;</span>orange = #ffa500
        </div>
        <div class="colorsquare">
          <span style="background-color: orangered">&nbsp;</span>orangered =
          #ff4500
        </div>
        <div class="colorsquare">
          <span style="background-color: orchid">&nbsp;</span>orchid = #da70d6
        </div>
        <div class="colorsquare">
          <span style="background-color: palegoldenrod">&nbsp;</span
          >palegoldenrod = #eee8aa
        </div>
        <div class="colorsquare">
          <span style="background-color: palegreen">&nbsp;</span>palegreen =
          #98fb98
        </div>
        <div class="colorsquare">
          <span style="background-color: paleturquoise">&nbsp;</span
          >paleturquoise = #afeeee
        </div>
        <div class="colorsquare">
          <span style="background-color: palevioletred">&nbsp;</span
          >palevioletred = #db7093
        </div>
        <div class="colorsquare">
          <span style="background-color: papayawhip">&nbsp;</span>papayawhip =
          #ffefd5
        </div>
        <div class="colorsquare">
          <span style="background-color: peachpuff">&nbsp;</span>peachpuff =
          #ffdab9
        </div>
        <div class="colorsquare">
          <span style="background-color: peru">&nbsp;</span>peru = #cd853f
        </div>
        <div class="colorsquare">
          <span style="background-color: pink">&nbsp;</span>pink = #ffc0cb
        </div>
        <div class="colorsquare">
          <span style="background-color: plum">&nbsp;</span>plum = #dda0dd
        </div>
        <div class="colorsquare">
          <span style="background-color: powderblue">&nbsp;</span>powderblue =
          #b0e0e6
        </div>
        <div class="colorsquare">
          <span style="background-color: purple">&nbsp;</span>purple = #800080
        </div>
        <div class="colorsquare">
          <span style="background-color: red">&nbsp;</span>red = #ff0000
        </div>
        <div class="colorsquare">
          <span style="background-color: rosybrown">&nbsp;</span>rosybrown =
          #bc8f8f
        </div>
        <div class="colorsquare">
          <span style="background-color: royalblue">&nbsp;</span>royalblue =
          #4169e1
        </div>
        <div class="colorsquare">
          <span style="background-color: saddlebrown">&nbsp;</span>saddlebrown =
          #8b4513
        </div>
        <div class="colorsquare">
          <span style="background-color: salmon">&nbsp;</span>salmon = #fa8072
        </div>
        <div class="colorsquare">
          <span style="background-color: sandybrown">&nbsp;</span>sandybrown =
          #f4a460
        </div>
        <div class="colorsquare">
          <span style="background-color: seagreen">&nbsp;</span>seagreen =
          #2e8b57
        </div>
        <div class="colorsquare">
          <span style="background-color: seashell">&nbsp;</span>seashell =
          #fff5ee
        </div>
        <div class="colorsquare">
          <span style="background-color: sienna">&nbsp;</span>sienna = #a0522d
        </div>
        <div class="colorsquare">
          <span style="background-color: silver">&nbsp;</span>silver = #c0c0c0
        </div>
        <div class="colorsquare">
          <span style="background-color: skyblue">&nbsp;</span>skyblue = #87ceeb
        </div>
        <div class="colorsquare">
          <span style="background-color: slateblue">&nbsp;</span>slateblue =
          #6a5acd
        </div>
        <div class="colorsquare">
          <span style="background-color: slategray">&nbsp;</span>slategray =
          #708090
        </div>
        <div class="colorsquare">
          <span style="background-color: slategrey">&nbsp;</span>slategrey =
          #708090
        </div>
        <div class="colorsquare">
          <span style="background-color: snow">&nbsp;</span>snow = #fffafa
        </div>
        <div class="colorsquare">
          <span style="background-color: springgreen">&nbsp;</span>springgreen =
          #00ff7f
        </div>
        <div class="colorsquare">
          <span style="background-color: steelblue">&nbsp;</span>steelblue =
          #4682b4
        </div>
        <div class="colorsquare">
          <span style="background-color: tan">&nbsp;</span>tan = #d2b48c
        </div>
        <div class="colorsquare">
          <span style="background-color: teal">&nbsp;</span>teal = #008080
        </div>
        <div class="colorsquare">
          <span style="background-color: thistle">&nbsp;</span>thistle = #d8bfd8
        </div>
        <div class="colorsquare">
          <span style="background-color: tomato">&nbsp;</span>tomato = #ff6347
        </div>
        <div class="colorsquare">
          <span style="background-color: turquoise">&nbsp;</span>turquoise =
          #40e0d0
        </div>
        <div class="colorsquare">
          <span style="background-color: violet">&nbsp;</span>violet = #ee82ee
        </div>
        <div class="colorsquare">
          <span style="background-color: wheat">&nbsp;</span>wheat = #f5deb3
        </div>
        <div class="colorsquare">
          <span style="background-color: white">&nbsp;</span>white = #ffffff
        </div>
        <div class="colorsquare">
          <span style="background-color: whitesmoke">&nbsp;</span>whitesmoke =
          #f5f5f5
        </div>
        <div class="colorsquare">
          <span style="background-color: yellow">&nbsp;</span>yellow = #ffff00
        </div>
        <div class="colorsquare">
          <span style="background-color: yellowgreen">&nbsp;</span>yellowgreen =
          #9acd32
        </div>
        <div class="colorsquare">
          <span style="background-color: transparent">&nbsp;</span>transparent =
          rgba(0,0,0,0)
        </div>
      </div>
    </section>
    <div class="pagination">
      <router-link to="/css/color" class="btn btn-prev"
        >❮ &lt;color&gt;</router-link
      >
      <router-link
        to="/css/looked-up-colors-looked-up-color"
        class="btn btn-next"
        >Looked-up Colors &lt;looked-up-color&gt; ❯</router-link
      >
    </div>
  </article>
</template>
