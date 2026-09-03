# Scripture Text Formatter

---

This program is used in conjunction with Anki and the Lyris/Poetry Cloze Generator add-on to facilitate bulk creation of Bible verse flash cards.

## Instructions

1. Paste text with the following format into the app: {verse number} {verse} {verse number} {verse} ...
2. Open `Tools > Import Lyrics/Poetry`
3. Paste the formatted text under `Poem` and enter the book and chapter under `Title`.
4. Click `Add notes`.
5. Only once per deck go to `Browse > Cards... > Front Template` and change the formatting to
```
<div class="title">{{Title}}:<span id="num"></span></div>
{{#Author}}<div class="author">{{Author}}</div>{{/Author}}

<br>

<div class="lines">
    {{Context}}
    <div class="cloze">
        {{#Prompt}}{{Prompt}}{{/Prompt}}
        {{^Prompt}}[...]{{/Prompt}}
    </div>
</div>

<script>
  var match = `{{text:Line}}`.match(/\d+/);
  if (match) document.getElementById('num').textContent = match[0];
</script>
```
6. Similarly, card backside, go to `Back Template` and change the formatting to
```
<div class="title">{{Title}}:<span id="num"></span></div>
{{#Author}}<div class="author">{{Author}}</div>{{/Author}}

<br>

<div class="lines">
    {{Context}}
    <div class="cloze">{{Line}}</div>
</div>

<script>
  var match = `{{text:Line}}`.match(/\d+/);
  if (match) document.getElementById('num').textContent = match[0];
</script>
```