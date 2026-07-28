import os
import re

files_to_process = [
    "CssCSSPublicAPI.vue", "CssCSSandtheJavaFXSceneGraph.vue", "CssCharts.vue", "CssColorFunctionscolorfunction.vue", "CssControls.vue", "CssExample.vue", "CssExamples.vue", "CssFontProperties.vue", "CssHSBColorshsbcolor.vue", "CssImagePaintimagepattern.vue", "CssIncubatorModules.vue", "CssInheritance.vue", "CssIntroduction.vue", "CssLimitations.vue", "CssLinearGradientslineargradient.vue", "CssLookedupColorslookedupcolor.vue", "CssNamedColorsnamedcolor.vue", "CssNamingConventions.vue", "CssNodes.vue", "CssRGBColorsrgbcolor.vue", "CssRadialGradientsradialgradient.vue", "CssRules.vue", "CssSceneParentandSubSceneStylesheets.vue", "CssStage.vue", "CssTransitions.vue", "CssTypes.vue", "CssUnderstandingParserWarnings.vue", "Cssangle.vue", "Cssboolean.vue", "Csscolor.vue", "Csscolorstop.vue", "Cssduration.vue", "Csseasingfunction.vue", "Csseffect.vue", "Cssfont.vue", "Cssfontface.vue", "Cssimport.vue", "Cssinherit.vue", "Csslength.vue", "Cssmedia.vue", "Cssnumberinteger.vue", "Csspaint.vue", "Csspercentage.vue", "Csspoint.vue", "Csssize.vue", "Cssstring.vue", "Csstextbounds.vue", "Cssuri.vue"
]

base_dir = "/home/her/Documentos/java fx reference/v2/vue-docs/src/views/"

found = False
for file in files_to_process:
    path = os.path.join(base_dir, file)
    if not os.path.exists(path):
        continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # find <div class="code-block">...</div>
    matches = re.finditer(r'<div class="code-block".*?>(.*?)</div>', content, re.DOTALL)
    for m in matches:
        print(f"--- FILE: {file} ---")
        print(m.group(1).strip()[:200] + "...")
        found = True

if not found:
    print("No code-block div found in any of the files.")
