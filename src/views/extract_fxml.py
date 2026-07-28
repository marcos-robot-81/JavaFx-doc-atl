import os
import re

files = [
    "FxmlEventHandlers.vue", "FxmlScriptEventHandlers.vue", "FxmlExpressionBinding.vue",
    "FxmlFXMLLoader.vue", "FxmlInstanceProperties.vue", "FxmlScripting.vue",
    "FxmlReadOnlyListProperties.vue", "FxmlReadOnlyMapProperties.vue", "FxmlStaticProperties.vue",
    "Fxmlfxinclude.vue", "Fxmlfxreference.vue", "Fxmlfxconstant.vue",
    "Fxmlfxcopy.vue", "Fxmlfxroot.vue", "FxmlOverview.vue",
    "FxmlEscapeSequences.vue", "FxmlLocationResolution.vue", "FxmlResourceResolution.vue",
    "FxmlVariableResolution.vue", "FxmlNestedControllers.vue", "FxmlDeployinganApplicationasaModule.vue",
    "FxmlEventhandlersfromexpressions.vue", "FxmlSpecialhandlersforcollectionsandproperties.vue"
]

base_path = "/home/her/Documentos/java fx reference/v2/vue-docs/src/views/"

for fname in files:
    path = os.path.join(base_path, fname)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all code-blocks using a better regex or logic
    blocks = re.findall(r'<div class="code-block">.*?</div>\s*</section>', content, re.DOTALL) # wait, no
    blocks = content.split('<div class="code-block">')[1:]
    for i, b in enumerate(blocks):
        b = b.split('</pre>')[0] if '</pre>' in b else b
        if '&lt;' in b and 'class="code-header">Example' in b:
            if 'package ' in b or 'public class' in b or 'import ' in b:
                continue # Java code
            if '&lt;!-- HTML' in b or 'Web Equivalent' in b:
                continue # HTML code
            print(f"--- {fname} block {i} ---")
            code_match = re.search(r'<code>(.*?)</code>', b, re.DOTALL)
            if code_match:
                print(code_match.group(1).strip())
