import sys
import os

def diff(article, avant, apres):
    avant = avant.strip()
    apres = apres.strip()
    open('a.txt', 'w').write(avant)
    open('b.txt', 'w').write(apres)
    os.system('php -dextension=/home/damien/repos/mediawiki-php-wikidiff2/modules/wikidiff2.so dodiff.php a.txt b.txt > c.txt')
    diff = open('c.txt').read()
    print('<h2>' + article + '</h2>')
    print("""<table class="diff">
            <colgroup><col class="diff-marker">
                <col class="diff-content">
                <col class="diff-marker">
                <col class="diff-content">
            </colgroup>""" + diff + "</table>")

article = ""
avant = ""
apres = ""

for line in open(sys.argv[1]):
    if line.startswith('# '):
        if article:
            diff(article, avant, apres)
        article = line.replace('#', '').strip()
        avant = None
        apres = None
        continue
    elif line.startswith("## Avant"):
        avant = ""
        continue
    elif line.startswith('## Aprés'):
        apres = ""
        continue
    if apres is not None:
        apres += line
    elif avant is not None:
        avant += line
diff(article, avant, apres)


print("""
<style>
/* diff */

table.diff { 
  background-color:white;
  border:none;
  border-spacing:4px;
  margin:0;
  width:100%;
  table-layout:fixed;
}
table.diff td{
  padding:0.33em 0.5em;
}
table.diff td.diff-marker {
  padding:0.25em;
}
table.diff col.diff-marker {
  width:2%;
}
table.diff col.diff-content {
  width:48%;
}
table.diff td div {
  word-wrap:break-word
}
td.diff-otitle,td.diff-ntitle {
  text-align:center;
}
td.diff-lineno {
  font-weight:bold;
}
td.diff-marker {
  text-align:right;
  font-weight:bold;
  font-size:1.25em
}
td.diff-addedline, td.diff-deletedline, td.diff-context {
  font-size:88%;
  vertical-align:top;
  white-space:-moz-pre-wrap;
  white-space:pre-wrap;
  border-style:solid;
  border-width:1px 1px 1px 4px;
  border-radius:0.33em;
}
td.diff-addedline {
  border-color:#a3d3ff;
}
td.diff-deletedline {
  border-color:#ffe49c;
}
td.diff-context {
  background:#f9f9f9;
  border-color:#e6e6e6;
  color:#333333;
}
.diffchange {
  font-weight:bold;
  text-decoration:none
}
td.diff-addedline .diffchange, td.diff-deletedline .diffchange {
  border-radius:0.33em;
  padding:0.25em 0;
}
td.diff-addedline .diffchange {
  background:#d8ecff;
}
td.diff-deletedline .diffchange {
  background:#feeec8;
}















@media print {
 .mw-revslider-container {
  display:none
 }
}
.mw-revslider-container {
 direction:ltr;
 position:relative;
 border:1px solid #c8ccd1
}
.mw-revslider-container .mw-revslider-toggle-button.oo-ui-buttonElement-frameless.oo-ui-labelElement {
 width:100%;
 text-align:center;
 margin-left:0 !important;
 margin-right:0
}
.mw-revslider-toggle-button .oo-ui-buttonElement-button {
 width:100%
}
.mw-revslider-toggle-button .oo-ui-iconElement-icon {
 left:auto !important;
 right:0.28571429em;
 position:absolute
}
.mw-revslider-slider-wrapper {
 min-height:142px;
 border-top:1px solid #c8ccd1;
 padding:20px 10px
}
.mw-revslider-spinner {
 white-space:nowrap;
 display:block;
 max-width:56px;
 margin:60px auto
}
.mw-revslider-spinner .mw-revslider-bounce,
.mw-revslider-spinner:before,
.mw-revslider-spinner:after {
 content:'';
 background-color:#72777d;
 display:block;
 float:left;
 width:16px;
 height:16px;
 border-radius:100%;
 -webkit-animation:bouncedelay 1600ms infinite ease-in-out both;
 animation:bouncedelay 1600ms infinite ease-in-out both;
 -webkit-animation-delay:-160ms;
 animation-delay:-160ms
}
.mw-revslider-spinner:before {
 margin-right:4px;
 -webkit-animation-delay:-330ms;
 animation-delay:-330ms
}
.mw-revslider-spinner:after {
 margin-left:4px;
 -webkit-animation-delay:0s;
 animation-delay:0s
}
@-webkit-keyframes bouncedelay {
 0%,
 50%,
 100% {
  -webkit-transform:scale(0.625)
 }
 20% {
  opacity:0.87;
  -webkit-transform:scale(1)
 }
}
@-moz-keyframes bouncedelay {
 0%,
 50%,
 100% {
  -moz-transform:scale(0.625)
 }
 20% {
  opacity:0.87;
  -moz-transform:scale(1)
 }
}
@keyframes bouncedelay {
 0%,
 50%,
 100% {
  -ms-transform:scale(0.625);
  transform:scale(0.625)
 }
 20% {
  opacity:0.87;
  -ms-transform:scale(1);
  transform:scale(1)
 }
}
.client-nojs .mw-revslider-container {
 display:none
}
#pt-notifications-alert .mw-echo-notifications-badge,
#pt-notifications-notice .mw-echo-notifications-badge {
 position:relative;
 display:block;
 width:20px;
 height:20px;
 margin:0 2px;
 top:-5px;
 text-indent:-9999px;
 border-radius:2px;
 cursor:pointer;
 text-decoration:none;
 line-height:normal;
 -webkit-box-sizing:border-box;
 -moz-box-sizing:border-box;
 box-sizing:border-box;
 opacity:0.87;
 color:transparent
}
#pt-notifications-alert .mw-echo-notifications-badge:hover,
#pt-notifications-notice .mw-echo-notifications-badge:hover,
#pt-notifications-alert .mw-echo-notifications-badge:active,
#pt-notifications-notice .mw-echo-notifications-badge:active,
#pt-notifications-alert .mw-echo-notifications-badge:focus,
#pt-notifications-notice .mw-echo-notifications-badge:focus {
 outline:0
}
#pt-notifications-alert .mw-echo-notifications-badge:focus,
#pt-notifications-notice .mw-echo-notifications-badge:focus {
 -webkit-box-shadow:0 0 0 1px #fff,0 0 0 3px #36c;
 box-shadow:0 0 0 1px #fff,0 0 0 3px #36c;
 opacity:1
}
#pt-notifications-alert .mw-echo-notifications-badge:focus:after,
#pt-notifications-notice .mw-echo-notifications-badge:focus:after {
 border-color:#36c
}
#pt-notifications-alert .mw-echo-notifications-badge:after,
#pt-notifications-notice .mw-echo-notifications-badge:after {
 position:absolute;
 display:inline-block;
 cursor:pointer;
 top:9px;
 text-indent:0;
 left:55%;
 font-size:0.9em;
 font-weight:bold;
 padding:0 0.3em;
 border:1px solid #fff;
 border-radius:2px;
 background-color:#72777d;
 content:attr(data-counter-text);
 color:#fff
}
#pt-notifications-alert .mw-echo-notifications-badge-dimmed,
#pt-notifications-notice .mw-echo-notifications-badge-dimmed {
 opacity:0.4
}
#pt-notifications-alert .mw-echo-notifications-badge.mw-echo-notifications-badge-long-label,
#pt-notifications-notice .mw-echo-notifications-badge.mw-echo-notifications-badge-long-label {
 margin-right:0.5em
}
#pt-notifications-alert .mw-echo-notifications-badge.mw-echo-notifications-badge-long-label:after,
#pt-notifications-notice .mw-echo-notifications-badge.mw-echo-notifications-badge-long-label:after {
 left:35%
}
#pt-notifications-alert .mw-echo-notifications-badge.mw-echo-notifications-badge-all-read,
#pt-notifications-notice .mw-echo-notifications-badge.mw-echo-notifications-badge-all-read {
 opacity:0.51
}
#pt-notifications-alert .mw-echo-notifications-badge.mw-echo-notifications-badge-all-read:after,
#pt-notifications-notice .mw-echo-notifications-badge.mw-echo-notifications-badge-all-read:after {
 visibility:hidden
}
#pt-notifications-alert .mw-echo-notifications-badge.oo-ui-flaggedElement-unseen:after,
#pt-notifications-alert .mw-echo-notifications-badge.mw-echo-unseen-notifications:after {
 background-color:#dd3333
}
#pt-notifications-notice .mw-echo-notifications-badge.oo-ui-flaggedElement-unseen:after,
#pt-notifications-notice .mw-echo-notifications-badge.mw-echo-unseen-notifications:after {
 background-color:#3366cc
}
#p-personal #pt-notifications-alert,
#p-personal #pt-notifications-notice {
 margin-right:0.4em
}
#p-lang .uls-settings-trigger {
 background:transparent url(/w/extensions/UniversalLanguageSelector/resources/images/cog-sprite.svg?c3fa1) no-repeat center top;
 border:0;
 min-height:16px;
 min-width:16px;
 float:right;
 cursor:pointer
}
#p-lang .uls-settings-trigger::-moz-focus-inner {
 border:0
}
#p-lang .uls-settings-trigger:focus {
 outline:1px solid #36c
}
.skin-vector #p-lang .uls-settings-trigger {
 margin-top:8px
}
#p-lang .uls-settings-trigger:hover {
 background-position:center -16px
}
.client-nojs #ca-ve-edit,
.client-nojs .mw-editsection-divider,
.client-nojs .mw-editsection-visualeditor,
.ve-not-available #ca-ve-edit,
.ve-not-available .mw-editsection-divider,
.ve-not-available .mw-editsection-visualeditor {
 display:none
}
.client-js .mw-content-ltr .mw-editsection-bracket:first-of-type,
.client-js .mw-content-rtl .mw-editsection-bracket:not(:first-of-type) {
 margin-right:0.25em;
 color:#54595d
}
.client-js .mw-content-rtl .mw-editsection-bracket:first-of-type,
.client-js .mw-content-ltr .mw-editsection-bracket:not(:first-of-type) {
 margin-left:0.25em;
 color:#54595d
}
.ve-init-mw-diffPage-diff:after {
 content:'';
 clear:both;
 display:block
}
.ve-init-mw-diffPage-diffMode {
 text-align:right;
 margin:1em 0
}
.client-nojs .ve-init-mw-diffPage-diffMode {
 display:none
}
.ve-init-mw-diffPage-loading {
 clear:both;
 margin:2em auto
}
.ve-init-mw-diffPage-revSlider-visual .mw-revslider-pointer-line .mw-revslider-upper-color {
 border-color:#39b79c
}
.ve-init-mw-diffPage-revSlider-visual .mw-revslider-pointer-line .mw-revslider-lower-color {
 border-color:#d73c34
}
.ve-init-mw-diffPage-revSlider-visual .mw-revslider-revision-new .mw-revslider-revision-border-box {
 border-bottom-color:#39b79c
}
.ve-init-mw-diffPage-revSlider-visual .mw-revslider-revision-old .mw-revslider-revision-border-box {
 border-bottom-color:#d73c34
}
.ve-init-mw-diffPage-revSlider-visual .mw-revslider-revision-hovered.mw-revslider-revision-wrapper-up .mw-revslider-pointer-ghost {
 background-color:#a6e3d6;
 border-color:#39b79c
}
.ve-init-mw-diffPage-revSlider-visual .mw-revslider-revision-hovered.mw-revslider-revision-wrapper-down .mw-revslider-pointer-ghost {
 background-color:#f0b7b4;
 border-color:#d73c34
}
.ve-init-mw-diffPage-revSlider-visual .mw-revslider-revision-wrapper-hovered .mw-revslider-revision-hovered.mw-revslider-revision-wrapper-up {
 background-color:rgba(57,183,156,0.3)
}
.ve-init-mw-diffPage-revSlider-visual .mw-revslider-revision-wrapper-hovered .mw-revslider-revision-hovered.mw-revslider-revision-wrapper-down {
 background-color:rgba(215,60,52,0.3)
}
.ve-init-mw-diffPage-revSlider-visual .mw-revslider-pointer.mw-revslider-pointer-newer {
 border-color:#39b79c;
 background-color:#6fcdb9;
 background-image:-webkit-gradient(linear,right top,right bottom,color-stop(0,#a6e3d6),color-stop(100%,#39b79c));
 background-image:-webkit-linear-gradient(top,#a6e3d6 0,#39b79c 100%);
 background-image:-moz-linear-gradient(top,#a6e3d6 0,#39b79c 100%);
 background-image:linear-gradient(to bottom,#a6e3d6 0,#39b79c 100%)
}
.ve-init-mw-diffPage-revSlider-visual .mw-revslider-pointer.mw-revslider-pointer-newer:hover {
 background-color:#83d3c2;
 background-image:-webkit-gradient(linear,right top,right bottom,color-stop(0,#cdefe8),color-stop(100%,#39b79c));
 background-image:-webkit-linear-gradient(top,#cdefe8 0,#39b79c 100%);
 background-image:-moz-linear-gradient(top,#cdefe8 0,#39b79c 100%);
 background-image:linear-gradient(to bottom,#cdefe8 0,#39b79c 100%)
}
.ve-init-mw-diffPage-revSlider-visual .mw-revslider-pointer.mw-revslider-pointer-older {
 border-color:#d73c34;
 background-color:#e47974;
 background-image:-webkit-gradient(linear,right top,right bottom,color-stop(0,#f0b7b4),color-stop(100%,#d73c34));
 background-image:-webkit-linear-gradient(top,#f0b7b4 0,#d73c34 100%);
 background-image:-moz-linear-gradient(top,#f0b7b4 0,#d73c34 100%);
 background-image:linear-gradient(to bottom,#f0b7b4 0,#d73c34 100%)
}
.ve-init-mw-diffPage-revSlider-visual .mw-revslider-pointer.mw-revslider-pointer-older:hover {
 background-color:#e88e89;
 background-image:-webkit-gradient(linear,right top,right bottom,color-stop(0,#f9e0de),color-stop(100%,#d73c34));
 background-image:-webkit-linear-gradient(top,#f9e0de 0,#d73c34 100%);
 background-image:-moz-linear-gradient(top,#f9e0de 0,#d73c34 100%);
 background-image:linear-gradient(to bottom,#f9e0de 0,#d73c34 100%)
}
.ve-init-mw-diffPage-revSlider-visual .mw-revslider-pointer-container-newer .mw-revslider-slider-line {
 border-bottom-color:rgba(57,183,156,0.5)
}
.ve-init-mw-diffPage-revSlider-visual .mw-revslider-pointer-container-newer:hover .mw-revslider-slider-line {
 border-bottom-color:rgba(57,183,156,0.8)
}
.ve-init-mw-diffPage-revSlider-visual .mw-revslider-pointer-container-older .mw-revslider-slider-line {
 border-top-color:rgba(215,60,52,0.5)
}
.ve-init-mw-diffPage-revSlider-visual .mw-revslider-pointer-container-older:hover .mw-revslider-slider-line {
 border-top-color:rgba(215,60,52,0.8)
}
.badge-goodarticle,
.badge-goodlist,
.badge-recommendedarticle {
 list-style-image:url(/w/extensions/WikimediaBadges/resources/images/badge-silver-star.png?70a8c)
}
.badge-featuredarticle,
.badge-featuredportal,
.badge-featuredlist {
 list-style-image:url(/w/extensions/WikimediaBadges/resources/images/badge-golden-star.png?ed948)
}
.badge-problematic {
 list-style-image:url(/w/extensions/WikimediaBadges/resources/images/badge-problematic.png?f3177)
}
.badge-proofread {
 list-style-image:url(/w/extensions/WikimediaBadges/resources/images/badge-proofread.png?e81f9)
}
.badge-validated {
 list-style-image:url(/w/extensions/WikimediaBadges/resources/images/badge-validated.png?6232c)
}
.badge-digitaldocument {
 list-style-image:url(/w/extensions/WikimediaBadges/resources/images/badge-digitaldocument.png?d1c50)
}
.client-js .sortable:not(.jquery-tablesorter) > * > tr:first-child > th:not(.unsortable),
.jquery-tablesorter th.headerSort {
 background-image:url(/w/resources/src/jquery.tablesorter.styles/images/sort_both.svg?6b5ca);
 cursor:pointer;
 background-repeat:no-repeat;
 background-position:center right;
 padding-right:21px
}
.jquery-tablesorter th.headerSortUp {
 background-image:url(/w/resources/src/jquery.tablesorter.styles/images/sort_up.svg?dd026)
}
.jquery-tablesorter th.headerSortDown {
 background-image:url(/w/resources/src/jquery.tablesorter.styles/images/sort_down.svg?fb375)
}
.diff {
 border:0;
 border-spacing:4px;
 margin:0;
 width:100%;
 table-layout:fixed
}
.diff td {
 padding:0.33em 0.5em
}
.diff td.diff-marker {
 padding:0.25em;
 text-align:right;
 font-weight:bold;
 font-size:1.25em;
 line-height:1.2
}
.diff td div {
 word-wrap:break-word
}
.diff col.diff-marker {
 width:2%
}
.diff .diff-content {
 width:48%
}
.diff-title {
 vertical-align:top
}
.diff-notice,
.diff-multi,
.diff-otitle,
.diff-ntitle {
 text-align:center
}
.diff-lineno {
 font-weight:bold
}
.mw-diff-inline-added ins,
.mw-diff-inline-changed ins,
.mw-diff-inline-deleted ins,
.mw-diff-inline-added del,
.mw-diff-inline-changed del,
.mw-diff-inline-deleted del {
 display:inline-block;
 text-decoration:none
}
.mw-diff-inline-added ins,
.mw-diff-inline-changed ins {
 background:#a3d3ff
}
.mw-diff-inline-deleted del,
.mw-diff-inline-changed del {
 background:#ffe49c
}
.diff-addedline,
.diff-deletedline,
.diff-context {
 font-size:13px;
 line-height:1.6;
 vertical-align:top;
 white-space:pre-wrap;
 border-style:solid;
 border-width:1px 1px 1px 4px;
 border-radius:0.33em
}
.diff-editfont-monospace .diff-addedline,
.diff-editfont-monospace .diff-deletedline,
.diff-editfont-monospace .diff-context {
 font-family:monospace,monospace
}
.diff-editfont-sans-serif .diff-addedline,
.diff-editfont-sans-serif .diff-deletedline,
.diff-editfont-sans-serif .diff-context {
 font-family:sans-serif
}
.diff-editfont-serif .diff-addedline,
.diff-editfont-serif .diff-deletedline,
.diff-editfont-serif .diff-context {
 font-family:serif
}
.diff-context {
 background:#f8f9fa;
 border-color:#eaecf0;
 color:#202122
}
.diff-addedline {
 border-color:#a3d3ff
}
.diff-deletedline {
 border-color:#ffe49c
}
.diffchange {
 font-weight:bold;
 text-decoration:none
}
.diff-addedline .diffchange,
.diff-deletedline .diffchange {
 border-radius:0.33em;
 padding:0.25em 0
}
.diff-addedline .diffchange {
 background:#d8ecff
}
.diff-deletedline .diffchange {
 background:#feeec8
}
.diff-currentversion-title,
.diff {
 direction:ltr;
 unicode-bidi:embed
}
.diff-contentalign-right td {
 direction:rtl;
 unicode-bidi:embed
}
.diff-contentalign-left td {
 direction:ltr;
 unicode-bidi:embed
}
.diff-multi,
.diff-otitle,
.diff-ntitle,
.diff-lineno {
 direction:ltr !important;
 unicode-bidi:embed
}
.mw-diff-slot-header {
 text-align:center
}
.mw-diff-movedpara-left,
.mw-diff-movedpara-right,
.mw-diff-movedpara-left:visited,
.mw-diff-movedpara-right:visited,
.mw-diff-movedpara-left:active,
.mw-diff-movedpara-right:active {
 display:block;
 color:transparent
}
.mw-diff-movedpara-left:hover,
.mw-diff-movedpara-right:hover {
 text-decoration:none;
 color:transparent
}
.mw-diff-movedpara-left:after,
.mw-diff-movedpara-right:after {
 display:block;
 color:#202122;
 margin-top:-1.25em
}
.mw-diff-movedpara-left:after,
.rtl .mw-diff-movedpara-right:after {
 content:'↪'
}
.mw-diff-movedpara-right:after,
.rtl .mw-diff-movedpara-left:after {
 content:'↩'
}
#mw-inlinediff-header #mw-diff-otitle1,
#mw-inlinediff-header #mw-diff-otitle2,
#mw-inlinediff-header #mw-diff-otitle3,
#mw-inlinediff-header #mw-diff-otitle5 {
 display:none
}
@media print {
 td.diff-context,
 td.diff-addedline .diffchange,
 td.diff-deletedline .diffchange {
  background-color:transparent
 }
 td.diff-addedline .diffchange {
  text-decoration:underline
 }
 td.diff-deletedline .diffchange {
  text-decoration:line-through
 }
}
.mw-changeslist-separator:empty:before {
 content:'. .'
}
.mw-changeslist-separator--semicolon:before {
 content:' ;'
}
.mw-rollback-link:before {
 content:'['
}
.mw-rollback-link:after {
 content:']'
}
.comment--without-parentheses:before,
.mw-changeslist-links:before,
.mw-diff-bytes:before,
.mw-tag-markers:before,
.mw-uctop:before {
 content:'('
}
.comment--without-parentheses:after,
.mw-changeslist-links:after,
.mw-diff-bytes:after,
.mw-tag-markers:after,
.mw-uctop:after {
 content:')'
}
.mw-changeslist-links {
 display:inline-block
}
.mw-changeslist-links > span:not(:first-child):before {
 content:' | '
}
.mw-changeslist-links .mw-rollback-link:before,
.mw-changeslist-links .mw-rollback-link:after {
 content:''
}
.mw-tag-marker:after {
 content:','
}
.mw-tag-marker:last-child:after {
 content:''
}
.toctogglecheckbox:checked ~ ul {
 display:none
}
@media screen {
 :not(:checked) > .toctogglecheckbox {
  display:inline !important;
  position:absolute;
  opacity:0;
  z-index:-1
 }
 .toctogglespan {
  font-size:94%
 }
 :not(:checked) > .toctogglespan:before {
  content:' ['
 }
 :not(:checked) > .toctogglespan:after {
  content:']'
 }
 .toctogglelabel {
  cursor:pointer;
  color:#0645ad
 }
 .toctogglelabel:hover {
  text-decoration:underline
 }
 .toctogglecheckbox:focus + .toctitle .toctogglelabel {
  text-decoration:underline;
  outline:dotted 1px;
  outline:auto -webkit-focus-ring-color
 }
 .toctogglecheckbox:checked + .toctitle .toctogglelabel:after {
  content:'afficher'
 }
 .toctogglecheckbox:not(:checked) + .toctitle .toctogglelabel:after {
  content:'masquer'
 }
}
@media print {
 .toctogglecheckbox:checked + .toctitle {
  display:none
 }
}
.mw-ui-icon {
 position:relative;
 line-height:1.5em;
 min-height:1.5em;
 min-width:1.5em
}
span.mw-ui-icon {
 display:inline-block
}
.mw-ui-icon.mw-ui-icon-element {
 text-indent:-999px;
 overflow:hidden;
 width:3.5em;
 min-width:3.5em;
 max-width:3.5em
}
.mw-ui-icon.mw-ui-icon-element:before {
 left:0;
 right:0;
 position:absolute;
 margin:0 1em
}
.mw-ui-icon.mw-ui-icon-element.mw-ui-icon-large {
 width:4.625em;
 min-width:4.625em;
 max-width:4.625em;
 line-height:4.625em;
 min-height:4.625em
}
.mw-ui-icon.mw-ui-icon-element.mw-ui-icon-large:before {
 min-height:4.625em
}
.mw-ui-icon.mw-ui-icon-before:before,
.mw-ui-icon.mw-ui-icon-element:before {
 background-position:50% 50%;
 background-repeat:no-repeat;
 background-size:100% auto;
 float:left;
 display:block;
 min-height:1.5em;
 content:''
}
.mw-ui-icon.mw-ui-icon-before:before {
 position:relative;
 width:1.5em;
 margin-right:1em
}
.mw-ui-icon.mw-ui-icon-small:before {
 background-size:66.67% auto
}
.mw-widget-complexNamespaceInputWidget .mw-widget-namespaceInputWidget,
.mw-widget-complexNamespaceInputWidget .oo-ui-fieldLayout {
 display:inline-block;
 margin-right:1em
}
.mw-widget-complexNamespaceInputWidget .oo-ui-fieldLayout {
 vertical-align:middle;
 margin-bottom:0
}
.mw-widget-complexNamespaceInputWidget .oo-ui-fieldLayout.oo-ui-fieldLayout-align-inline.oo-ui-labelElement > .oo-ui-fieldLayout-body > .oo-ui-labelElement-label {
 padding-left:0.5em
}
.mw-widget-complexNamespaceInputWidget .mw-widget-namespaceInputWidget {
 max-width:20em
}
.mw-widget-complexTitleInputWidget .mw-widget-namespaceInputWidget,
.mw-widget-complexTitleInputWidget .mw-widget-titleInputWidget {
 display:inline-block
}
.mw-widget-complexTitleInputWidget .mw-widget-namespaceInputWidget {
 max-width:20em;
 margin-right:0.5em
}
.mw-widget-complexTitleInputWidget .mw-widget-titleInputWidget {
 max-width:29.5em
}
.oo-ui-icon-alert,
.mw-ui-icon-alert:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=alert&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ealert%3C/title%3E%3Cpath d=%22M11.53 2.3A1.85 1.85 0 0010 1.21 1.85 1.85 0 008.48 2.3L.36 16.36C-.48 17.81.21 19 1.88 19h16.24c1.67 0 2.36-1.19 1.52-2.64zM11 16H9v-2h2zm0-4H9V6h2z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-alert,
.mw-ui-icon-alert-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=alert&variant=invert&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ealert%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M11.53 2.3A1.85 1.85 0 0010 1.21 1.85 1.85 0 008.48 2.3L.36 16.36C-.48 17.81.21 19 1.88 19h16.24c1.67 0 2.36-1.19 1.52-2.64zM11 16H9v-2h2zm0-4H9V6h2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-alert,
.mw-ui-icon-alert-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=alert&variant=progressive&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ealert%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M11.53 2.3A1.85 1.85 0 0010 1.21 1.85 1.85 0 008.48 2.3L.36 16.36C-.48 17.81.21 19 1.88 19h16.24c1.67 0 2.36-1.19 1.52-2.64zM11 16H9v-2h2zm0-4H9V6h2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-warning.oo-ui-icon-alert,
.mw-ui-icon-alert-warning:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=alert&variant=warning&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ealert%3C/title%3E%3Cg fill=%22%23fc3%22%3E%3Cpath d=%22M11.53 2.3A1.85 1.85 0 0010 1.21 1.85 1.85 0 008.48 2.3L.36 16.36C-.48 17.81.21 19 1.88 19h16.24c1.67 0 2.36-1.19 1.52-2.64zM11 16H9v-2h2zm0-4H9V6h2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-error,
.mw-ui-icon-error:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=error&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eerror%3C/title%3E%3Cpath d=%22M13.728 1H6.272L1 6.272v7.456L6.272 19h7.456L19 13.728V6.272zM11 15H9v-2h2zm0-4H9V5h2z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-error,
.mw-ui-icon-error-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=error&variant=invert&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eerror%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M13.728 1H6.272L1 6.272v7.456L6.272 19h7.456L19 13.728V6.272zM11 15H9v-2h2zm0-4H9V5h2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-error,
.mw-ui-icon-error-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=error&variant=progressive&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eerror%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M13.728 1H6.272L1 6.272v7.456L6.272 19h7.456L19 13.728V6.272zM11 15H9v-2h2zm0-4H9V5h2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-error.oo-ui-icon-error,
.mw-ui-icon-error-error:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=error&variant=error&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eerror%3C/title%3E%3Cg fill=%22%23d33%22%3E%3Cpath d=%22M13.728 1H6.272L1 6.272v7.456L6.272 19h7.456L19 13.728V6.272zM11 15H9v-2h2zm0-4H9V5h2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-info,
.mw-ui-icon-info:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=info&format=rasterized&lang=fr&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Einfo%3C/title%3E%3Cpath d=%22M9.5 16A6.61 6.61 0 013 9.5 6.61 6.61 0 019.5 3 6.61 6.61 0 0116 9.5 6.63 6.63 0 019.5 16zm0-14A7.5 7.5 0 1017 9.5 7.5 7.5 0 009.5 2zm.5 6v4.08h1V13H8.07v-.92H9V9H8V8zM9 6h1v1H9z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-info,
.mw-ui-icon-info-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=info&variant=invert&format=rasterized&lang=fr&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Einfo%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M9.5 16A6.61 6.61 0 013 9.5 6.61 6.61 0 019.5 3 6.61 6.61 0 0116 9.5 6.63 6.63 0 019.5 16zm0-14A7.5 7.5 0 1017 9.5 7.5 7.5 0 009.5 2zm.5 6v4.08h1V13H8.07v-.92H9V9H8V8zM9 6h1v1H9z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-info,
.mw-ui-icon-info-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=info&variant=progressive&format=rasterized&lang=fr&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Einfo%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M9.5 16A6.61 6.61 0 013 9.5 6.61 6.61 0 019.5 3 6.61 6.61 0 0116 9.5 6.63 6.63 0 019.5 16zm0-14A7.5 7.5 0 1017 9.5 7.5 7.5 0 009.5 2zm.5 6v4.08h1V13H8.07v-.92H9V9H8V8zM9 6h1v1H9z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-infoFilled,
.mw-ui-icon-infoFilled:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=infoFilled&format=rasterized&lang=fr&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Einfo%3C/title%3E%3Cpath d=%22M10 0C4.477 0 0 4.477 0 10s4.477 10 10 10 10-4.477 10-10S15.523 0 10 0zM9 5h2v2H9zm0 4h2v6H9z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-infoFilled,
.mw-ui-icon-infoFilled-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=infoFilled&variant=invert&format=rasterized&lang=fr&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Einfo%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M10 0C4.477 0 0 4.477 0 10s4.477 10 10 10 10-4.477 10-10S15.523 0 10 0zM9 5h2v2H9zm0 4h2v6H9z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-infoFilled,
.mw-ui-icon-infoFilled-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=infoFilled&variant=progressive&format=rasterized&lang=fr&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Einfo%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M10 0C4.477 0 0 4.477 0 10s4.477 10 10 10 10-4.477 10-10S15.523 0 10 0zM9 5h2v2H9zm0 4h2v6H9z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-add,
.mw-ui-icon-add:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=add&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eadd%3C/title%3E%3Cpath d=%22M11 9V4H9v5H4v2h5v5h2v-5h5V9z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-add,
.mw-ui-icon-add-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=add&variant=invert&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eadd%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M11 9V4H9v5H4v2h5v5h2v-5h5V9z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-add,
.mw-ui-icon-add-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=add&variant=progressive&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eadd%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M11 9V4H9v5H4v2h5v5h2v-5h5V9z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-check,
.mw-ui-icon-check:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=check&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Echeck%3C/title%3E%3Cpath d=%22M7 14.17L2.83 10l-1.41 1.41L7 17 19 5l-1.41-1.42z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-check,
.mw-ui-icon-check-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=check&variant=invert&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Echeck%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M7 14.17L2.83 10l-1.41 1.41L7 17 19 5l-1.41-1.42z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-check,
.mw-ui-icon-check-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=check&variant=progressive&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Echeck%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M7 14.17L2.83 10l-1.41 1.41L7 17 19 5l-1.41-1.42z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-destructive.oo-ui-icon-check,
.mw-ui-icon-check-destructive:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=check&variant=destructive&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Echeck%3C/title%3E%3Cg fill=%22%23d33%22%3E%3Cpath d=%22M7 14.17L2.83 10l-1.41 1.41L7 17 19 5l-1.41-1.42z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-success.oo-ui-icon-check,
.mw-ui-icon-check-success:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=check&variant=success&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Echeck%3C/title%3E%3Cg fill=%22%2314866d%22%3E%3Cpath d=%22M7 14.17L2.83 10l-1.41 1.41L7 17 19 5l-1.41-1.42z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-close,
.mw-ui-icon-close:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=close&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eclose%3C/title%3E%3Cpath d=%22M4.34 2.93l12.73 12.73-1.41 1.41L2.93 4.35z%22/%3E%3Cpath d=%22M17.07 4.34L4.34 17.07l-1.41-1.41L15.66 2.93z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-close,
.mw-ui-icon-close-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=close&variant=invert&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eclose%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M4.34 2.93l12.73 12.73-1.41 1.41L2.93 4.35z%22/%3E%3Cpath d=%22M17.07 4.34L4.34 17.07l-1.41-1.41L15.66 2.93z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-close,
.mw-ui-icon-close-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=close&variant=progressive&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eclose%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M4.34 2.93l12.73 12.73-1.41 1.41L2.93 4.35z%22/%3E%3Cpath d=%22M17.07 4.34L4.34 17.07l-1.41-1.41L15.66 2.93z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-search,
.mw-ui-icon-search:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=search&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Esearch%3C/title%3E%3Cpath d=%22M7.5 13c3.04 0 5.5-2.46 5.5-5.5S10.54 2 7.5 2 2 4.46 2 7.5 4.46 13 7.5 13zm4.55.46A7.432 7.432 0 017.5 15C3.36 15 0 11.64 0 7.5S3.36 0 7.5 0C11.64 0 15 3.36 15 7.5c0 1.71-.57 3.29-1.54 4.55l6.49 6.49-1.41 1.41-6.49-6.49z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-search,
.mw-ui-icon-search-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=search&variant=invert&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Esearch%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M7.5 13c3.04 0 5.5-2.46 5.5-5.5S10.54 2 7.5 2 2 4.46 2 7.5 4.46 13 7.5 13zm4.55.46A7.432 7.432 0 017.5 15C3.36 15 0 11.64 0 7.5S3.36 0 7.5 0C11.64 0 15 3.36 15 7.5c0 1.71-.57 3.29-1.54 4.55l6.49 6.49-1.41 1.41-6.49-6.49z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-search,
.mw-ui-icon-search-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=search&variant=progressive&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Esearch%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M7.5 13c3.04 0 5.5-2.46 5.5-5.5S10.54 2 7.5 2 2 4.46 2 7.5 4.46 13 7.5 13zm4.55.46A7.432 7.432 0 017.5 15C3.36 15 0 11.64 0 7.5S3.36 0 7.5 0C11.64 0 15 3.36 15 7.5c0 1.71-.57 3.29-1.54 4.55l6.49 6.49-1.41 1.41-6.49-6.49z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-subtract,
.mw-ui-icon-subtract:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=subtract&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Esubtract%3C/title%3E%3Cpath d=%22M4 9h12v2H4z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-subtract,
.mw-ui-icon-subtract-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=subtract&variant=invert&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Esubtract%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M4 9h12v2H4z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-subtract,
.mw-ui-icon-subtract-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=subtract&variant=progressive&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Esubtract%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M4 9h12v2H4z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-destructive.oo-ui-icon-subtract,
.mw-ui-icon-subtract-destructive:before {
 background-image:url(/w/load.php?modules=oojs-ui-core.icons&image=subtract&variant=destructive&format=rasterized&skin=vector&version=1tnx5);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Esubtract%3C/title%3E%3Cg fill=%22%23d33%22%3E%3Cpath d=%22M4 9h12v2H4z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-element-hidden {
 display:none !important
}
.oo-ui-buttonElement {
 display:inline-block;
 line-height:normal;
 vertical-align:middle
}
.oo-ui-buttonElement > .oo-ui-buttonElement-button {
 cursor:pointer;
 display:inline-block;
 -webkit-box-sizing:border-box;
 -moz-box-sizing:border-box;
 box-sizing:border-box;
 vertical-align:middle;
 font-family:inherit;
 font-size:inherit;
 white-space:nowrap;
 -webkit-touch-callout:none;
 -webkit-user-select:none;
 -moz-user-select:none;
 -ms-user-select:none;
 user-select:none
}
.oo-ui-buttonElement > .oo-ui-buttonElement-button::-moz-focus-inner {
 border-color:transparent;
 padding:0
}
.oo-ui-buttonElement.oo-ui-widget-disabled > .oo-ui-buttonElement-button {
 cursor:default
}
.oo-ui-buttonElement-frameless {
 position:relative
}
.oo-ui-buttonElement-framed > .oo-ui-buttonElement-button {
 vertical-align:top;
 text-align:center
}
.oo-ui-buttonElement > .oo-ui-buttonElement-button {
 position:relative;
 min-height:2.28571429em;
 border-radius:2px;
 padding-top:2.14285714em;
 font-weight:bold;
 text-decoration:none
}
.oo-ui-buttonElement > .oo-ui-buttonElement-button:focus {
 outline:0
}
.oo-ui-buttonElement > input.oo-ui-buttonElement-button {
 -webkit-appearance:none
}
.oo-ui-buttonElement.oo-ui-labelElement > .oo-ui-buttonElement-button {
 line-height:1
}
.oo-ui-buttonElement.oo-ui-labelElement > input.oo-ui-buttonElement-button,
.oo-ui-buttonElement.oo-ui-labelElement > .oo-ui-buttonElement-button > .oo-ui-labelElement-label {
 line-height:1.42857143em
}
.oo-ui-buttonElement.oo-ui-labelElement.oo-ui-indicatorElement > .oo-ui-buttonElement-button {
 padding-right:2.14285714em
}
.oo-ui-buttonElement.oo-ui-iconElement .oo-ui-iconElement-icon,
.oo-ui-buttonElement.oo-ui-indicatorElement .oo-ui-indicatorElement-indicator {
 -webkit-transform:translateZ(0);
 transform:translateZ(0)
}
.oo-ui-buttonElement.oo-ui-indicatorElement.oo-ui-labelElement > .oo-ui-buttonElement-button > .oo-ui-indicatorElement-indicator,
.oo-ui-buttonElement.oo-ui-indicatorElement.oo-ui-iconElement > .oo-ui-buttonElement-button > .oo-ui-indicatorElement-indicator {
 right:0.71428571em
}
.oo-ui-buttonElement.oo-ui-widget-enabled > .oo-ui-buttonElement-button {
 -webkit-transition:background-color 100ms,color 100ms,border-color 100ms,box-shadow 100ms;
 -moz-transition:background-color 100ms,color 100ms,border-color 100ms,box-shadow 100ms;
 transition:background-color 100ms,color 100ms,border-color 100ms,box-shadow 100ms
}
.oo-ui-buttonElement.oo-ui-widget-enabled > .oo-ui-buttonElement-button > .oo-ui-iconElement-icon,
.oo-ui-buttonElement.oo-ui-widget-enabled > .oo-ui-buttonElement-button > .oo-ui-indicatorElement-indicator {
 -webkit-transition:opacity 100ms;
 -moz-transition:opacity 100ms;
 transition:opacity 100ms
}
.oo-ui-buttonElement.oo-ui-widget-enabled > .oo-ui-buttonElement-button > .oo-ui-iconElement-icon:not(.oo-ui-image-invert),
.oo-ui-buttonElement.oo-ui-widget-enabled > .oo-ui-buttonElement-button > .oo-ui-indicatorElement-indicator:not(.oo-ui-image-invert) {
 opacity:0.87
}
.oo-ui-buttonElement.oo-ui-widget-enabled.oo-ui-buttonElement-pressed > .oo-ui-buttonElement-button > .oo-ui-iconElement-icon,
.oo-ui-buttonElement.oo-ui-widget-enabled.oo-ui-buttonElement-pressed > .oo-ui-buttonElement-button > .oo-ui-indicatorElement-indicator {
 opacity:1
}
.oo-ui-buttonElement-frameless.oo-ui-iconElement:first-child {
 margin-left:-0.42857143em
}
.oo-ui-buttonElement-frameless.oo-ui-iconElement > .oo-ui-buttonElement-button {
 min-width:1.42857143em;
 min-height:1.42857143em;
 border-color:transparent;
 border-style:solid;
 border-width:1px;
 padding-top:2.14285714em;
 padding-left:2.14285714em
}
.oo-ui-buttonElement-frameless.oo-ui-iconElement > .oo-ui-buttonElement-button > .oo-ui-iconElement-icon {
 left:0.35714286em
}
.oo-ui-buttonElement-frameless.oo-ui-labelElement:first-child {
 margin-left:-6px
}
.oo-ui-buttonElement-frameless.oo-ui-labelElement.oo-ui-iconElement:first-child {
 margin-left:-0.42857143em
}
.oo-ui-buttonElement-frameless.oo-ui-labelElement > .oo-ui-buttonElement-button {
 border-color:transparent;
 border-style:solid;
 border-width:1px;
 padding:5px 6px
}
.oo-ui-buttonElement-frameless.oo-ui-labelElement.oo-ui-iconElement > .oo-ui-buttonElement-button {
 padding-left:2.14285714em
}
.oo-ui-buttonElement-frameless.oo-ui-indicatorElement > .oo-ui-buttonElement-button {
 min-width:12px;
 min-height:12px
}
.oo-ui-buttonElement-frameless.oo-ui-indicatorElement.oo-ui-iconElement > .oo-ui-buttonElement-button {
 padding-left:3.85714286em
}
.oo-ui-buttonElement-frameless.oo-ui-indicatorElement.oo-ui-labelElement > .oo-ui-buttonElement-button {
 padding-left:6px;
 padding-top:5px
}
.oo-ui-buttonElement-frameless.oo-ui-indicatorElement.oo-ui-iconElement.oo-ui-labelElement > .oo-ui-buttonElement-button {
 padding-left:2.14285714em
}
.oo-ui-buttonElement-frameless.oo-ui-widget-enabled > .oo-ui-buttonElement-button {
 color:#202122
}
.oo-ui-buttonElement-frameless.oo-ui-widget-enabled > .oo-ui-buttonElement-button:hover {
 background-color:rgba(0,24,73,0.02745098);
 color:#000
}
.oo-ui-buttonElement-frameless.oo-ui-widget-enabled > .oo-ui-buttonElement-button:active {
 background-color:rgba(0,36,73,0.08235294);
 color:#404244
}
.oo-ui-buttonElement-frameless.oo-ui-widget-enabled.oo-ui-iconElement > .oo-ui-buttonElement-button:focus,
.oo-ui-buttonElement-frameless.oo-ui-widget-enabled.oo-ui-labelElement > .oo-ui-buttonElement-button:focus {
 border-color:#36c;
 box-shadow:inset 0 0 0 1px #36c;
 outline:1px solid transparent
}
.oo-ui-buttonElement-frameless.oo-ui-widget-enabled.oo-ui-iconElement > .oo-ui-buttonElement-button:focus:active,
.oo-ui-buttonElement-frameless.oo-ui-widget-enabled.oo-ui-labelElement > .oo-ui-buttonElement-button:focus:active {
 border-color:transparent;
 box-shadow:none
}
.oo-ui-buttonElement-frameless.oo-ui-widget-enabled.oo-ui-indicatorElement:not(.oo-ui-iconElement):not(.oo-ui-labelElement) > .oo-ui-buttonElement-button {
 border-radius:1px
}
.oo-ui-buttonElement-frameless.oo-ui-widget-enabled.oo-ui-indicatorElement:not(.oo-ui-iconElement):not(.oo-ui-labelElement) > .oo-ui-buttonElement-button:focus {
 box-shadow:0 0 0 2px #36c;
 outline:1px solid transparent
}
.oo-ui-buttonElement-frameless.oo-ui-widget-enabled.oo-ui-indicatorElement:not(.oo-ui-iconElement):not(.oo-ui-labelElement) > .oo-ui-buttonElement-button:focus:active {
 box-shadow:none
}
.oo-ui-buttonElement-frameless.oo-ui-widget-enabled.oo-ui-buttonElement-pressed > input.oo-ui-buttonElement-button,
.oo-ui-buttonElement-frameless.oo-ui-widget-enabled > .oo-ui-buttonElement-button:active {
 color:#000;
 border-color:transparent;
 box-shadow:none
}
.oo-ui-buttonElement-frameless.oo-ui-widget-enabled.oo-ui-flaggedElement-progressive > .oo-ui-buttonElement-button {
 color:#36c
}
.oo-ui-buttonElement-frameless.oo-ui-widget-enabled.oo-ui-flaggedElement-progressive > .oo-ui-buttonElement-button:hover {
 color:#447ff5
}
.oo-ui-buttonElement-frameless.oo-ui-widget-enabled.oo-ui-flaggedElement-progressive > .oo-ui-buttonElement-button:active,
.oo-ui-buttonElement-frameless.oo-ui-widget-enabled.oo-ui-flaggedElement-progressive > .oo-ui-buttonElement-button:active:focus,
.oo-ui-buttonElement-frameless.oo-ui-widget-enabled.oo-ui-flaggedElement-progressive.oo-ui-buttonElement-pressed > .oo-ui-buttonElement-button {
 color:#2a4b8d;
 box-shadow:none
}
.oo-ui-buttonElement-frameless.oo-ui-widget-enabled.oo-ui-flaggedElement-destructive > .oo-ui-buttonElement-button {
 color:#d33
}
.oo-ui-buttonElement-frameless.oo-ui-widget-enabled.oo-ui-flaggedElement-destructive > .oo-ui-buttonElement-button:hover {
 color:#ff4242
}
.oo-ui-buttonElement-frameless.oo-ui-widget-enabled.oo-ui-flaggedElement-destructive > .oo-ui-buttonElement-button:active,
.oo-ui-buttonElement-frameless.oo-ui-widget-enabled.oo-ui-flaggedElement-destructive > .oo-ui-buttonElement-button:active:focus,
.oo-ui-buttonElement-frameless.oo-ui-widget-enabled.oo-ui-flaggedElement-destructive.oo-ui-buttonElement-pressed > .oo-ui-buttonElement-button {
 color:#b32424;
 box-shadow:none
}
.oo-ui-buttonElement-frameless.oo-ui-widget-enabled[class*='oo-ui-flaggedElement'] > .oo-ui-buttonElement-button > .oo-ui-iconElement-icon,
.oo-ui-buttonElement-frameless.oo-ui-widget-enabled[class*='oo-ui-flaggedElement'] > .oo-ui-buttonElement-button > .oo-ui-indicatorElement-indicator {
 opacity:1
}
.oo-ui-buttonElement-frameless.oo-ui-widget-disabled > .oo-ui-buttonElement-button {
 color:#72777d
}
.oo-ui-buttonElement-frameless.oo-ui-widget-disabled > .oo-ui-buttonElement-button > .oo-ui-iconElement-icon,
.oo-ui-buttonElement-frameless.oo-ui-widget-disabled > .oo-ui-buttonElement-button > .oo-ui-indicatorElement-indicator {
 opacity:0.51
}
.oo-ui-buttonElement-framed > .oo-ui-buttonElement-button {
 border-style:solid;
 border-width:1px;
 border-radius:2px;
 padding-left:12px;
 padding-right:12px
}
.oo-ui-buttonElement-framed.oo-ui-iconElement > .oo-ui-buttonElement-button {
 padding-top:2.14285714em;
 padding-bottom:0;
 padding-left:2.14285714em
}
.oo-ui-buttonElement-framed.oo-ui-iconElement > .oo-ui-buttonElement-button > .oo-ui-iconElement-icon {
 left:50%;
 margin-left:-0.71428571em
}
.oo-ui-buttonElement-framed.oo-ui-iconElement.oo-ui-labelElement > .oo-ui-buttonElement-button,
.oo-ui-buttonElement-framed.oo-ui-iconElement.oo-ui-indicatorElement > .oo-ui-buttonElement-button {
 padding-left:2.71428571em
}
.oo-ui-buttonElement-framed.oo-ui-iconElement.oo-ui-labelElement > .oo-ui-buttonElement-button > .oo-ui-iconElement-icon,
.oo-ui-buttonElement-framed.oo-ui-iconElement.oo-ui-indicatorElement > .oo-ui-buttonElement-button > .oo-ui-iconElement-icon {
 left:0.78571429em;
 margin-left:0
}
.oo-ui-buttonElement-framed.oo-ui-indicatorElement > .oo-ui-buttonElement-button {
 padding-top:2.14285714em;
 padding-right:1.71428571em;
 padding-bottom:0
}
.oo-ui-buttonElement-framed.oo-ui-labelElement > .oo-ui-buttonElement-button {
 padding-top:5px;
 padding-bottom:5px
}
.oo-ui-buttonElement-framed.oo-ui-widget-disabled > .oo-ui-buttonElement-button {
 background-color:#c8ccd1;
 color:#fff;
 border-color:#c8ccd1
}
.oo-ui-buttonElement-framed.oo-ui-widget-disabled.oo-ui-buttonElement-active > .oo-ui-buttonElement-button {
 background-color:#919fb9
}
.oo-ui-buttonElement-framed.oo-ui-widget-enabled > .oo-ui-buttonElement-button {
 background-color:#f8f9fa;
 color:#202122;
 border-color:#a2a9b1
}
.oo-ui-buttonElement-framed.oo-ui-widget-enabled > .oo-ui-buttonElement-button:hover {
 background-color:#fff;
 color:#404244;
 border-color:#a2a9b1
}
.oo-ui-buttonElement-framed.oo-ui-widget-enabled > .oo-ui-buttonElement-button:hover > .oo-ui-iconElement-icon:not(.oo-ui-image-invert),
.oo-ui-buttonElement-framed.oo-ui-widget-enabled > .oo-ui-buttonElement-button:hover > .oo-ui-indicatorElement-indicator:not(.oo-ui-image-invert) {
 opacity:0.74
}
.oo-ui-buttonElement-framed.oo-ui-widget-enabled > .oo-ui-buttonElement-button:focus {
 border-color:#36c;
 box-shadow:inset 0 0 0 1px #36c;
 outline:1px solid transparent
}
.oo-ui-buttonElement-framed.oo-ui-widget-enabled > .oo-ui-buttonElement-button:active,
.oo-ui-buttonElement-framed.oo-ui-widget-enabled > .oo-ui-buttonElement-button:active:focus,
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-buttonElement-pressed > .oo-ui-buttonElement-button {
 background-color:#c8ccd1;
 color:#000;
 border-color:#72777d;
 box-shadow:none
}
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-buttonElement-active > .oo-ui-buttonElement-button {
 background-color:#2a4b8d;
 color:#fff;
 border-color:#2a4b8d
}
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-buttonElement-active > .oo-ui-buttonElement-button:focus {
 border-color:#36c;
 box-shadow:inset 0 0 0 1px #36c,inset 0 0 0 2px #fff
}
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-progressive > .oo-ui-buttonElement-button {
 color:#36c
}
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-progressive > .oo-ui-buttonElement-button:hover {
 background-color:#fff;
 border-color:#447ff5
}
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-progressive > .oo-ui-buttonElement-button:active,
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-progressive > .oo-ui-buttonElement-button:active:focus,
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-progressive.oo-ui-buttonElement-pressed > .oo-ui-buttonElement-button,
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-progressive.oo-ui-buttonElement-active > .oo-ui-buttonElement-button,
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-progressive.oo-ui-popupToolGroup-active > .oo-ui-buttonElement-button {
 background-color:#eff3fa;
 color:#2a4b8d;
 border-color:#2a4b8d;
 box-shadow:none
}
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-progressive > .oo-ui-buttonElement-button:focus {
 border-color:#36c;
 box-shadow:inset 0 0 0 1px #36c;
 outline:1px solid transparent
}
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-destructive > .oo-ui-buttonElement-button {
 color:#d73333
}
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-destructive > .oo-ui-buttonElement-button:hover {
 background-color:#fff;
 border-color:#ff4242
}
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-destructive > .oo-ui-buttonElement-button:active,
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-destructive > .oo-ui-buttonElement-button:active:focus,
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-destructive.oo-ui-buttonElement-pressed > .oo-ui-buttonElement-button,
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-destructive.oo-ui-buttonElement-active > .oo-ui-buttonElement-button,
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-destructive.oo-ui-popupToolGroup-active > .oo-ui-buttonElement-button {
 background-color:#ffffff;
 color:#b32424;
 border-color:#b32424;
 box-shadow:none
}
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-destructive > .oo-ui-buttonElement-button:focus {
 border-color:#d33;
 box-shadow:inset 0 0 0 1px #d33;
 outline:1px solid transparent
}
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-primary.oo-ui-flaggedElement-progressive > .oo-ui-buttonElement-button {
 color:#fff;
 background-color:#36c;
 border-color:#36c
}
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-primary.oo-ui-flaggedElement-progressive > .oo-ui-buttonElement-button:hover {
 background-color:#447ff5;
 border-color:#447ff5
}
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-primary.oo-ui-flaggedElement-progressive > .oo-ui-buttonElement-button:active,
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-primary.oo-ui-flaggedElement-progressive > .oo-ui-buttonElement-button:active:focus,
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-primary.oo-ui-flaggedElement-progressive.oo-ui-buttonElement-pressed > .oo-ui-buttonElement-button,
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-primary.oo-ui-flaggedElement-progressive.oo-ui-buttonElement-active > .oo-ui-buttonElement-button,
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-primary.oo-ui-flaggedElement-progressive.oo-ui-popupToolGroup-active > .oo-ui-buttonElement-button {
 color:#fff;
 background-color:#2a4b8d;
 border-color:#2a4b8d;
 box-shadow:none
}
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-primary.oo-ui-flaggedElement-progressive > .oo-ui-buttonElement-button:focus {
 border-color:#36c;
 box-shadow:inset 0 0 0 1px #36c,inset 0 0 0 2px #fff;
 outline:1px solid transparent
}
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-primary.oo-ui-flaggedElement-destructive > .oo-ui-buttonElement-button {
 color:#fff;
 background-color:#d33;
 border-color:#d33
}
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-primary.oo-ui-flaggedElement-destructive > .oo-ui-buttonElement-button:hover {
 background-color:#ff4242;
 border-color:#ff4242
}
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-primary.oo-ui-flaggedElement-destructive > .oo-ui-buttonElement-button:active,
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-primary.oo-ui-flaggedElement-destructive > .oo-ui-buttonElement-button:active:focus,
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-primary.oo-ui-flaggedElement-destructive.oo-ui-buttonElement-pressed > .oo-ui-buttonElement-button,
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-primary.oo-ui-flaggedElement-destructive.oo-ui-buttonElement-active > .oo-ui-buttonElement-button,
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-primary.oo-ui-flaggedElement-destructive.oo-ui-popupToolGroup-active > .oo-ui-buttonElement-button {
 color:#fff;
 background-color:#b32424;
 border-color:#b32424;
 box-shadow:none
}
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-primary.oo-ui-flaggedElement-destructive > .oo-ui-buttonElement-button:focus {
 border-color:#d33;
 box-shadow:inset 0 0 0 1px #d33,inset 0 0 0 2px #fff;
 outline:1px solid transparent
}
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-primary > .oo-ui-buttonElement-button > .oo-ui-iconElement-icon,
.oo-ui-buttonElement-framed.oo-ui-widget-enabled.oo-ui-flaggedElement-primary > .oo-ui-buttonElement-button > .oo-ui-indicatorElement-indicator {
 opacity:1
}
.oo-ui-clippableElement-clippable {
 -webkit-box-sizing:border-box;
 -moz-box-sizing:border-box;
 box-sizing:border-box;
 min-height:40px;
 -webkit-overflow-scrolling:touch
}
.oo-ui-floatableElement {
 position:absolute
}
.oo-ui-labelElement .oo-ui-labelElement-label,
.oo-ui-labelElement.oo-ui-labelElement-label {
 -webkit-box-sizing:border-box;
 -moz-box-sizing:border-box;
 box-sizing:border-box
}
.oo-ui-labelElement-invisible {
 display:block;
 position:absolute;
 clip:rect(1px,1px,1px,1px);
 width:1px;
 height:1px;
 margin:-1px;
 border:0;
 padding:0;
 overflow:hidden
}
.oo-ui-labelElement .oo-ui-labelElement-label {
 line-height:1.42857143em
}
.oo-ui-labelElement .oo-ui-labelElement-label-highlight {
 font-weight:bold
}
.oo-ui-iconElement-icon {
 background-size:contain;
 background-position:center center;
 background-repeat:no-repeat;
 position:absolute;
 top:0;
 min-width:20px;
 width:1.42857143em;
 min-height:20px;
 height:100%
}
.oo-ui-iconElement-noIcon {
 display:none
}
.oo-ui-indicatorElement-indicator {
 background-size:contain;
 background-position:center center;
 background-repeat:no-repeat;
 position:absolute;
 top:0;
 min-width:12px;
 width:0.85714286em;
 min-height:12px;
 height:100%
}
.oo-ui-indicatorElement-noIndicator {
 display:none
}
.oo-ui-pendingElement-pending {
 background-color:#eaecf0;
 background-image:-webkit-linear-gradient(135deg,#fff 25%,transparent 25%,transparent 50%,#fff 50%,#fff 75%,transparent 75%,transparent);
 background-image:-moz-linear-gradient(135deg,#fff 25%,transparent 25%,transparent 50%,#fff 50%,#fff 75%,transparent 75%,transparent);
 background-image:linear-gradient(135deg,#fff 25%,transparent 25%,transparent 50%,#fff 50%,#fff 75%,transparent 75%,transparent);
 background-size:1.42857143em 1.42857143em;
 -webkit-animation:oo-ui-pendingElement-stripes 650ms linear infinite;
 -moz-animation:oo-ui-pendingElement-stripes 650ms linear infinite;
 animation:oo-ui-pendingElement-stripes 650ms linear infinite
}
@-webkit-keyframes oo-ui-pendingElement-stripes {
 0% {
  background-position:-1.42857143em 0
 }
 100% {
  background-position:0 0
 }
}
@-moz-keyframes oo-ui-pendingElement-stripes {
 0% {
  background-position:-1.42857143em 0
 }
 100% {
  background-position:0 0
 }
}
@keyframes oo-ui-pendingElement-stripes {
 0% {
  background-position:-1.42857143em 0
 }
 100% {
  background-position:0 0
 }
}
.oo-ui-fieldLayout {
 display:block;
 margin-top:16px
}
.oo-ui-fieldLayout:before,
.oo-ui-fieldLayout:after {
 content:' ';
 display:table
}
.oo-ui-fieldLayout:after {
 clear:both
}
.oo-ui-fieldLayout.oo-ui-fieldLayout-align-left > .oo-ui-fieldLayout-body:after,
.oo-ui-fieldLayout.oo-ui-fieldLayout-align-right > .oo-ui-fieldLayout-body:after {
 content:' ';
 display:block;
 clear:both
}
.oo-ui-fieldLayout.oo-ui-fieldLayout-align-left > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-header,
.oo-ui-fieldLayout.oo-ui-fieldLayout-align-right > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-header {
 word-wrap:break-word;
 -webkit-hyphens:auto;
 -moz-hyphens:auto;
 -ms-hyphens:auto;
 hyphens:auto
}
.oo-ui-fieldLayout.oo-ui-fieldLayout-align-left > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-header,
.oo-ui-fieldLayout.oo-ui-fieldLayout-align-right > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-header,
.oo-ui-fieldLayout.oo-ui-fieldLayout-align-left > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-help,
.oo-ui-fieldLayout.oo-ui-fieldLayout-align-right > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-help,
.oo-ui-fieldLayout.oo-ui-fieldLayout-align-left > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-field,
.oo-ui-fieldLayout.oo-ui-fieldLayout-align-right > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-field {
 display:block;
 float:left
}
.oo-ui-fieldLayout.oo-ui-fieldLayout-align-right > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-header {
 text-align:right
}
.oo-ui-fieldLayout.oo-ui-fieldLayout-align-inline {
 word-wrap:break-word;
 -webkit-hyphens:auto;
 -moz-hyphens:auto;
 -ms-hyphens:auto;
 hyphens:auto
}
.oo-ui-fieldLayout.oo-ui-fieldLayout-align-inline > .oo-ui-fieldLayout-body {
 display:table;
 width:100%
}
.oo-ui-fieldLayout.oo-ui-fieldLayout-align-inline > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-header,
.oo-ui-fieldLayout.oo-ui-fieldLayout-align-inline > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-field {
 display:table-cell
}
.oo-ui-fieldLayout.oo-ui-fieldLayout-align-inline > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-header {
 vertical-align:middle
}
.oo-ui-fieldLayout.oo-ui-fieldLayout-align-inline > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-field {
 width:1px;
 vertical-align:top
}
.oo-ui-fieldLayout.oo-ui-fieldLayout-align-top > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-header,
.oo-ui-fieldLayout.oo-ui-fieldLayout-align-top > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-field {
 display:block
}
.oo-ui-fieldLayout .oo-ui-fieldLayout-help {
 float:right
}
.oo-ui-fieldLayout .oo-ui-fieldLayout-help:not(.oo-ui-popupButtonWidget) > .oo-ui-buttonElement-button {
 cursor:help
}
.oo-ui-fieldLayout.oo-ui-labelElement,
.oo-ui-fieldLayout.oo-ui-fieldLayout-align-inline {
 margin-top:12px
}
.oo-ui-fieldLayout:first-child,
.oo-ui-fieldLayout.oo-ui-labelElement:first-child,
.oo-ui-fieldLayout.oo-ui-fieldLayout-align-inline:first-child {
 margin-top:0
}
.oo-ui-fieldLayout.oo-ui-labelElement > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-header {
 padding-bottom:4px
}
.oo-ui-fieldLayout.oo-ui-labelElement.oo-ui-fieldLayout-align-top > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-header,
.oo-ui-fieldLayout.oo-ui-labelElement.oo-ui-fieldLayout-align-inline > .oo-ui-fieldLayout-body {
 max-width:50em
}
.oo-ui-fieldLayout.oo-ui-labelElement.oo-ui-fieldLayout-align-left > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-header,
.oo-ui-fieldLayout.oo-ui-labelElement.oo-ui-fieldLayout-align-right > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-header {
 -webkit-box-sizing:border-box;
 -moz-box-sizing:border-box;
 box-sizing:border-box;
 width:40%;
 padding-right:2.64285714em
}
.oo-ui-fieldLayout.oo-ui-labelElement.oo-ui-fieldLayout-align-left > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-header > .oo-ui-labelElement-label,
.oo-ui-fieldLayout.oo-ui-labelElement.oo-ui-fieldLayout-align-right > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-header > .oo-ui-labelElement-label {
 display:block;
 padding-top:4px
}
.oo-ui-fieldLayout.oo-ui-labelElement.oo-ui-fieldLayout-align-left > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-help,
.oo-ui-fieldLayout.oo-ui-labelElement.oo-ui-fieldLayout-align-right > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-help {
 margin-right:0;
 margin-left:-2.35714286em
}
.oo-ui-fieldLayout.oo-ui-labelElement.oo-ui-fieldLayout-align-left > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-field,
.oo-ui-fieldLayout.oo-ui-labelElement.oo-ui-fieldLayout-align-right > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-field {
 width:60%
}
.oo-ui-fieldLayout.oo-ui-labelElement.oo-ui-fieldLayout-align-inline > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-header {
 padding-top:0;
 padding-bottom:0;
 padding-left:6px
}
.oo-ui-fieldLayout .oo-ui-fieldLayout-help {
 margin-right:0
}
.oo-ui-fieldLayout .oo-ui-fieldLayout-help .oo-ui-buttonElement-button {
 padding-top:1.42857143em;
 padding-right:0
}
.oo-ui-fieldLayout .oo-ui-fieldLayout-help .oo-ui-buttonElement-button:hover,
.oo-ui-fieldLayout .oo-ui-fieldLayout-help .oo-ui-buttonElement-button:active {
 background-color:transparent
}
.oo-ui-fieldLayout.oo-ui-fieldLayout-align-top > .oo-ui-fieldLayout-body > .oo-ui-inline-help {
 margin-top:4px
}
.oo-ui-fieldLayout.oo-ui-fieldLayout-align-top .oo-ui-fieldLayout-help,
.oo-ui-fieldLayout.oo-ui-fieldLayout-align-inline .oo-ui-fieldLayout-help {
 margin-top:-6px;
 margin-right:-8px;
 margin-left:0
}
.oo-ui-fieldLayout-messages {
 -webkit-box-sizing:border-box;
 -moz-box-sizing:border-box;
 box-sizing:border-box;
 max-width:50em;
 padding:4px 0
}
.oo-ui-fieldLayout-messages > .oo-ui-messageWidget {
 margin-left:12px;
 margin-right:12px
}
.oo-ui-fieldLayout-messages > .oo-ui-messageWidget:first-child {
 margin-top:4px
}
.oo-ui-fieldLayout-disabled > .oo-ui-fieldLayout-body > .oo-ui-fieldLayout-header > .oo-ui-labelElement-label {
 color:#72777d
}
.oo-ui-actionFieldLayout-input,
.oo-ui-actionFieldLayout-button {
 display:table-cell;
 vertical-align:middle
}
.oo-ui-actionFieldLayout-button {
 width:1%;
 white-space:nowrap
}
.oo-ui-actionFieldLayout.oo-ui-fieldLayout-align-top {
 max-width:50em
}
.oo-ui-actionFieldLayout .oo-ui-actionFieldLayout-input > .oo-ui-widget {
 margin-right:8px
}
.oo-ui-actionFieldLayout .oo-ui-actionFieldLayout-input > .oo-ui-widget.oo-ui-textInputWidget > .oo-ui-inputWidget-input,
.oo-ui-actionFieldLayout .oo-ui-actionFieldLayout-input > .oo-ui-widget .oo-ui-dropdownWidget-handle,
.oo-ui-actionFieldLayout .oo-ui-actionFieldLayout-input > .oo-ui-widget .oo-ui-tagMultiselectWidget-handle {
 border-radius:2px 0 0 2px;
 position:relative
}
.oo-ui-actionFieldLayout .oo-ui-actionFieldLayout-button .oo-ui-buttonElement-framed > .oo-ui-buttonElement-button {
 border-radius:0 2px 2px 0;
 margin-left:-1px
}
.oo-ui-actionFieldLayout .oo-ui-actionFieldLayout-button .oo-ui-buttonElement-frameless {
 margin-left:6px
}
.oo-ui-actionFieldLayout .oo-ui-actionFieldLayout-input > .oo-ui-textInputWidget > .oo-ui-inputWidget-input:hover,
.oo-ui-actionFieldLayout .oo-ui-actionFieldLayout-input > .oo-ui-textInputWidget > .oo-ui-inputWidget-input:focus,
.oo-ui-actionFieldLayout .oo-ui-actionFieldLayout-input > .oo-ui-textInputWidget.oo-ui-flaggedElement-invalid > .oo-ui-inputWidget-input,
.oo-ui-actionFieldLayout .oo-ui-actionFieldLayout-input > .oo-ui-textInputWidget > .oo-ui-inputWidget-input:hover ~ *,
.oo-ui-actionFieldLayout .oo-ui-actionFieldLayout-input > .oo-ui-textInputWidget > .oo-ui-inputWidget-input:focus ~ *,
.oo-ui-actionFieldLayout .oo-ui-actionFieldLayout-input > .oo-ui-textInputWidget.oo-ui-flaggedElement-invalid > .oo-ui-inputWidget-input ~ * {
 z-index:1
}
.oo-ui-actionFieldLayout .oo-ui-actionFieldLayout-button > .oo-ui-buttonElement > .oo-ui-buttonElement-button:hover,
.oo-ui-actionFieldLayout .oo-ui-actionFieldLayout-button > .oo-ui-buttonElement > .oo-ui-buttonElement-button:focus {
 z-index:1
}
.oo-ui-fieldsetLayout {
 position:relative;
 min-width:0;
 margin:0;
 border:0;
 padding:0.01px 0 0 0
}
body:not(:-moz-handler-blocked) .oo-ui-fieldsetLayout {
 display:table-cell
}
.oo-ui-fieldsetLayout > .oo-ui-fieldsetLayout-header {
 display:none
}
.oo-ui-fieldsetLayout.oo-ui-iconElement > .oo-ui-fieldsetLayout-header,
.oo-ui-fieldsetLayout.oo-ui-labelElement > .oo-ui-fieldsetLayout-header {
 color:inherit;
 display:inline-table;
 box-sizing:border-box;
 padding:0;
 white-space:normal;
 float:left;
 width:100%
}
.oo-ui-fieldsetLayout > .oo-ui-inline-help {
 clear:left
}
.oo-ui-fieldsetLayout-group {
 clear:both
}
.oo-ui-fieldsetLayout .oo-ui-fieldsetLayout-help {
 float:right
}
.oo-ui-fieldsetLayout .oo-ui-fieldsetLayout-help:not(.oo-ui-popupButtonWidget) > .oo-ui-buttonElement-button {
 cursor:help
}
.oo-ui-fieldsetLayout .oo-ui-fieldsetLayout-header {
 max-width:50em
}
.oo-ui-fieldsetLayout .oo-ui-fieldsetLayout-header .oo-ui-iconElement-icon {
 height:1.42857143em
}
.oo-ui-fieldsetLayout.oo-ui-iconElement > .oo-ui-fieldsetLayout-header .oo-ui-iconElement-icon {
 display:block
}
.oo-ui-fieldsetLayout + .oo-ui-fieldsetLayout,
.oo-ui-fieldsetLayout + .oo-ui-formLayout {
 margin-top:24px
}
.oo-ui-fieldsetLayout.oo-ui-labelElement > .oo-ui-fieldsetLayout-header > .oo-ui-labelElement-label {
 display:inline-block;
 margin-bottom:8px;
 font-size:1.14285714em;
 font-weight:bold
}
.oo-ui-fieldsetLayout.oo-ui-iconElement > .oo-ui-fieldsetLayout-header > .oo-ui-labelElement-label {
 padding-left:1.625em
}
.oo-ui-fieldsetLayout > .oo-ui-inline-help {
 margin-bottom:8px
}
.oo-ui-fieldsetLayout .oo-ui-fieldsetLayout-help,
.oo-ui-fieldsetLayout .oo-ui-fieldsetLayout-help:last-child {
 margin-right:-8px
}
.oo-ui-fieldsetLayout .oo-ui-fieldsetLayout-help .oo-ui-buttonElement-button {
 padding-top:1.42857143em;
 padding-right:0
}
.oo-ui-fieldsetLayout .oo-ui-fieldsetLayout-help .oo-ui-buttonElement-button:hover,
.oo-ui-fieldsetLayout .oo-ui-fieldsetLayout-help .oo-ui-buttonElement-button:active {
 background-color:transparent
}
.oo-ui-formLayout + .oo-ui-fieldsetLayout,
.oo-ui-formLayout + .oo-ui-formLayout {
 margin-top:24px
}
.oo-ui-panelLayout {
 position:relative
}
.oo-ui-panelLayout-scrollable {
 overflow:auto;
 -webkit-overflow-scrolling:touch
}
.oo-ui-panelLayout-expanded {
 position:absolute;
 top:0;
 left:0;
 right:0;
 bottom:0
}
.oo-ui-panelLayout-padded {
 padding:12px 16px 16px
}
.oo-ui-panelLayout-padded.oo-ui-formLayout > .oo-ui-fieldsetLayout .oo-ui-labelElement-label,
.oo-ui-panelLayout-padded.oo-ui-formLayout > .oo-ui-fieldsetLayout .oo-ui-iconElement-icon {
 margin-top:-6px
}
.oo-ui-panelLayout-framed {
 border:1px solid #a2a9b1;
 border-radius:2px
}
.oo-ui-panelLayout-padded.oo-ui-panelLayout-framed {
 margin:12px 0
}
.oo-ui-horizontalLayout > .oo-ui-widget {
 display:inline-block;
 vertical-align:middle
}
.oo-ui-horizontalLayout > .oo-ui-layout {
 display:inline-block
}
.oo-ui-horizontalLayout > .oo-ui-layout,
.oo-ui-horizontalLayout > .oo-ui-widget {
 margin-right:8px
}
.oo-ui-horizontalLayout > .oo-ui-layout:last-child,
.oo-ui-horizontalLayout > .oo-ui-widget:last-child {
 margin-right:0
}
.oo-ui-horizontalLayout > .oo-ui-layout {
 margin-top:0
}
.oo-ui-horizontalLayout > .oo-ui-widget {
 margin-bottom:8px
}
.oo-ui-optionWidget {
 position:relative;
 display:block
}
.oo-ui-optionWidget.oo-ui-widget-enabled {
 cursor:pointer
}
.oo-ui-optionWidget.oo-ui-widget-disabled {
 cursor:default
}
.oo-ui-optionWidget.oo-ui-labelElement > .oo-ui-labelElement-label {
 display:block;
 white-space:nowrap;
 text-overflow:ellipsis;
 overflow:hidden
}
.oo-ui-optionWidget-selected .oo-ui-buttonElement-button > .oo-ui-iconElement-icon {
 opacity:1
}
.oo-ui-optionWidget.oo-ui-widget-disabled {
 color:#72777d
}
.oo-ui-decoratedOptionWidget {
 padding:6px 12px;
 line-height:1
}
.oo-ui-decoratedOptionWidget.oo-ui-iconElement {
 padding-left:2.64285714em
}
.oo-ui-decoratedOptionWidget .oo-ui-iconElement-icon {
 left:0.78571429em
}
.oo-ui-decoratedOptionWidget .oo-ui-labelElement-label {
 line-height:1.42857143em
}
.oo-ui-decoratedOptionWidget.oo-ui-indicatorElement {
 padding-right:2.14285714em
}
.oo-ui-decoratedOptionWidget .oo-ui-indicatorElement-indicator {
 right:12px
}
.oo-ui-decoratedOptionWidget.oo-ui-widget-enabled:hover .oo-ui-iconElement-icon,
.oo-ui-decoratedOptionWidget.oo-ui-widget-enabled:hover .oo-ui-indicatorElement-indicator {
 opacity:0.74
}
.oo-ui-decoratedOptionWidget.oo-ui-widget-enabled .oo-ui-iconElement-icon,
.oo-ui-decoratedOptionWidget.oo-ui-widget-enabled .oo-ui-indicatorElement-indicator {
 opacity:0.87;
 -webkit-transition:opacity 100ms;
 -moz-transition:opacity 100ms;
 transition:opacity 100ms
}
.oo-ui-decoratedOptionWidget.oo-ui-widget-disabled .oo-ui-iconElement-icon,
.oo-ui-decoratedOptionWidget.oo-ui-widget-disabled .oo-ui-indicatorElement-indicator {
 opacity:0.51
}
.oo-ui-radioSelectWidget:focus {
 outline:0
}
.oo-ui-radioSelectWidget:focus [type='radio']:checked + span:before {
 border-color:#fff
}
.oo-ui-radioOptionWidget {
 display:table;
 padding:4px 0
}
.oo-ui-radioOptionWidget .oo-ui-radioInputWidget,
.oo-ui-radioOptionWidget.oo-ui-labelElement > .oo-ui-labelElement-label {
 display:table-cell;
 vertical-align:top
}
.oo-ui-radioOptionWidget .oo-ui-radioInputWidget {
 width:1px
}
.oo-ui-radioOptionWidget.oo-ui-labelElement > .oo-ui-labelElement-label {
 white-space:normal
}
.oo-ui-radioOptionWidget:first-child {
 padding-top:0
}
.oo-ui-radioOptionWidget.oo-ui-labelElement > .oo-ui-labelElement-label {
 padding-left:6px
}
.oo-ui-radioOptionWidget .oo-ui-radioInputWidget {
 margin-right:0
}
.oo-ui-labelWidget {
 display:inline-block
}
.oo-ui-labelWidget.oo-ui-inline-help {
 display:block;
 color:#54595d;
 font-size:0.92857143em
}
.oo-ui-messageWidget {
 position:relative;
 -webkit-box-sizing:border-box;
 -moz-box-sizing:border-box;
 box-sizing:border-box;
 font-weight:bold
}
.oo-ui-messageWidget > .oo-ui-labelElement-label {
 display:block
}
.oo-ui-messageWidget > .oo-ui-iconElement-icon {
 background-position:0 0
}
.oo-ui-messageWidget > .oo-ui-labelElement-label {
 margin-left:2em
}
.oo-ui-messageWidget.oo-ui-messageWidget-block {
 border:1px solid;
 padding:16px 24px;
 font-weight:normal
}
.oo-ui-messageWidget.oo-ui-messageWidget-block > .oo-ui-iconElement-icon {
 background-position:0 16px
}
.oo-ui-messageWidget.oo-ui-messageWidget-block.oo-ui-flaggedElement-error {
 background-color:#fee7e6;
 border-color:#d33
}
.oo-ui-messageWidget.oo-ui-messageWidget-block.oo-ui-flaggedElement-warning {
 background-color:#fef6e7;
 border-color:#fc3
}
.oo-ui-messageWidget.oo-ui-messageWidget-block.oo-ui-flaggedElement-success {
 background-color:#d5fdf4;
 border-color:#14866d
}
.oo-ui-messageWidget.oo-ui-messageWidget-block.oo-ui-flaggedElement-notice {
 background-color:#eaecf0;
 border-color:#a2a9b1
}
.oo-ui-messageWidget.oo-ui-flaggedElement-error:not(.oo-ui-messageWidget-block) {
 color:#d33
}
.oo-ui-messageWidget.oo-ui-flaggedElement-success:not(.oo-ui-messageWidget-block) {
 color:#14866d
}
.oo-ui-messageWidget + .oo-ui-messageWidget {
 margin-top:8px
}
.oo-ui-iconWidget {
 vertical-align:middle;
 -webkit-touch-callout:none;
 -webkit-user-select:none;
 -moz-user-select:none;
 -ms-user-select:none;
 user-select:none;
 clip:auto;
 margin:0;
 text-indent:-9999px;
 line-height:2.5;
 display:inline-block;
 position:static;
 top:auto;
 height:1.42857143em
}
.oo-ui-iconWidget.oo-ui-widget-disabled {
 opacity:0.51
}
.oo-ui-indicatorWidget {
 vertical-align:middle;
 -webkit-touch-callout:none;
 -webkit-user-select:none;
 -moz-user-select:none;
 -ms-user-select:none;
 user-select:none;
 clip:auto;
 margin:0;
 text-indent:-9999px;
 line-height:2.5;
 margin:0.42857143em;
 display:inline-block;
 position:static;
 top:auto;
 height:0.85714286em
}
.oo-ui-indicatorWidget.oo-ui-widget-disabled {
 opacity:0.51
}
.oo-ui-buttonWidget {
 margin-right:8px
}
.oo-ui-buttonWidget:last-child {
 margin-right:0
}
.oo-ui-buttonGroupWidget {
 display:inline-block;
 border-radius:2px;
 margin-right:8px;
 z-index:0;
 position:relative;
 padding-bottom:1px
}
.oo-ui-buttonGroupWidget .oo-ui-buttonWidget.oo-ui-buttonElement-active .oo-ui-buttonElement-button {
 cursor:default
}
.oo-ui-buttonGroupWidget:last-child {
 margin-right:0
}
.oo-ui-buttonGroupWidget .oo-ui-buttonElement {
 margin-right:0;
 z-index:0
}
.oo-ui-buttonGroupWidget .oo-ui-buttonElement-framed .oo-ui-buttonElement-button {
 margin-right:-1px;
 margin-bottom:-1px;
 border-radius:0
}
.oo-ui-buttonGroupWidget .oo-ui-buttonElement-framed:first-child .oo-ui-buttonElement-button {
 border-bottom-left-radius:2px;
 border-top-left-radius:2px
}
.oo-ui-buttonGroupWidget .oo-ui-buttonElement-framed:last-child .oo-ui-buttonElement-button {
 margin-right:0;
 border-bottom-right-radius:2px;
 border-top-right-radius:2px
}
.oo-ui-buttonGroupWidget .oo-ui-buttonElement-framed.oo-ui-widget-disabled + .oo-ui-widget-disabled > .oo-ui-buttonElement-button {
 border-left-color:#fff
}
.oo-ui-buttonGroupWidget.oo-ui-widget-enabled .oo-ui-buttonElement.oo-ui-widget-enabled > .oo-ui-buttonElement-button:active {
 z-index:1
}
.oo-ui-buttonGroupWidget.oo-ui-widget-enabled .oo-ui-buttonElement.oo-ui-widget-enabled > .oo-ui-buttonElement-button:focus {
 z-index:2
}
.oo-ui-buttonGroupWidget.oo-ui-widget-enabled .oo-ui-buttonElement.oo-ui-buttonElement-active > .oo-ui-buttonElement-button {
 z-index:3
}
.oo-ui-buttonGroupWidget.oo-ui-widget-enabled .oo-ui-buttonElement.oo-ui-widget-disabled > .oo-ui-buttonElement-button {
 z-index:-1
}
.oo-ui-buttonGroupWidget.oo-ui-widget-enabled .oo-ui-buttonElement.oo-ui-toggleWidget-on + .oo-ui-toggleWidget-on > .oo-ui-buttonElement-button,
.oo-ui-buttonGroupWidget.oo-ui-widget-enabled .oo-ui-buttonElement.oo-ui-toggleWidget-on + .oo-ui-toggleWidget-on > .oo-ui-buttonElement-button:active {
 border-left-color:#a2a9b1;
 z-index:3
}
.oo-ui-popupWidget {
 position:absolute;
 z-index:1
}
.oo-ui-popupWidget-popup {
 position:relative;
 overflow:hidden;
 word-wrap:break-word;
 overflow-wrap:break-word
}
.oo-ui-popupWidget-anchor {
 display:none
}
.oo-ui-popupWidget-anchored .oo-ui-popupWidget-anchor {
 display:block;
 position:absolute;
 background-repeat:no-repeat
}
.oo-ui-popupWidget-anchored .oo-ui-popupWidget-anchor:before,
.oo-ui-popupWidget-anchored .oo-ui-popupWidget-anchor:after {
 content:'';
 position:absolute;
 width:0;
 height:0;
 border-style:solid;
 border-color:transparent
}
.oo-ui-popupWidget-anchored-top .oo-ui-popupWidget-anchor {
 left:0
}
.oo-ui-popupWidget-anchored-top .oo-ui-popupWidget-anchor:before,
.oo-ui-popupWidget-anchored-top .oo-ui-popupWidget-anchor:after {
 border-top:0
}
.oo-ui-popupWidget-anchored-bottom .oo-ui-popupWidget-anchor {
 left:0
}
.oo-ui-popupWidget-anchored-bottom .oo-ui-popupWidget-anchor:before,
.oo-ui-popupWidget-anchored-bottom .oo-ui-popupWidget-anchor:after {
 border-bottom:0
}
.oo-ui-popupWidget-anchored-start .oo-ui-popupWidget-anchor {
 top:0
}
.oo-ui-popupWidget-anchored-start .oo-ui-popupWidget-anchor:before,
.oo-ui-popupWidget-anchored-start .oo-ui-popupWidget-anchor:after {
 border-left:0
}
.oo-ui-popupWidget-anchored-end .oo-ui-popupWidget-anchor {
 top:0
}
.oo-ui-popupWidget-anchored-end .oo-ui-popupWidget-anchor:before,
.oo-ui-popupWidget-anchored-end .oo-ui-popupWidget-anchor:after {
 border-right:0
}
.oo-ui-popupWidget-head {
 -webkit-touch-callout:none;
 -webkit-user-select:none;
 -moz-user-select:none;
 -ms-user-select:none;
 user-select:none
}
.oo-ui-popupWidget-head > .oo-ui-buttonWidget {
 position:absolute
}
.oo-ui-popupWidget-head > .oo-ui-iconElement-icon {
 float:left
}
.oo-ui-popupWidget-head > .oo-ui-labelElement-label {
 float:left;
 cursor:default
}
.oo-ui-popupWidget-body {
 clear:both
}
.oo-ui-popupWidget-body.oo-ui-clippableElement-clippable {
 min-height:1em
}
.oo-ui-popupWidget-popup {
 background-color:#fff;
 border:1px solid #a2a9b1;
 border-radius:2px;
 box-shadow:0 2px 2px 0 rgba(0,0,0,0.25)
}
@supports (filter:drop-shadow(0 0 0)) {
 .oo-ui-popupWidget {
  filter:drop-shadow(0 2px 1px rgba(0,0,0,0.3));
  -webkit-transform:translateZ(0);
  transform:translateZ(0)
 }
 .oo-ui-popupWidget-popup {
  box-shadow:none
 }
}
.oo-ui-popupWidget-anchored-top {
 margin-top:9px
}
.oo-ui-popupWidget-anchored-top .oo-ui-popupWidget-anchor {
 top:-9px
}
.oo-ui-popupWidget-anchored-top .oo-ui-popupWidget-anchor:before {
 bottom:-10px;
 left:-9px;
 border-bottom-color:#7b8590;
 border-width:10px
}
.oo-ui-popupWidget-anchored-top .oo-ui-popupWidget-anchor:after {
 bottom:-10px;
 left:-8px;
 border-bottom-color:#fff;
 border-width:9px
}
.oo-ui-popupWidget-anchored-bottom {
 margin-bottom:9px
}
.oo-ui-popupWidget-anchored-bottom .oo-ui-popupWidget-anchor {
 bottom:-9px
}
.oo-ui-popupWidget-anchored-bottom .oo-ui-popupWidget-anchor:before {
 top:-10px;
 left:-9px;
 border-top-color:#a2a9b1;
 border-width:10px
}
.oo-ui-popupWidget-anchored-bottom .oo-ui-popupWidget-anchor:after {
 top:-10px;
 left:-8px;
 border-top-color:#fff;
 border-width:9px
}
.oo-ui-popupWidget-anchored-start {
 margin-left:9px
}
.oo-ui-popupWidget-anchored-start .oo-ui-popupWidget-anchor {
 left:-9px
}
.oo-ui-popupWidget-anchored-start .oo-ui-popupWidget-anchor:before {
 right:-10px;
 top:-9px;
 border-right-color:#a2a9b1;
 border-width:10px
}
.oo-ui-popupWidget-anchored-start .oo-ui-popupWidget-anchor:after {
 right:-10px;
 top:-8px;
 border-right-color:#fff;
 border-width:9px
}
.oo-ui-popupWidget-anchored-end {
 margin-right:9px
}
.oo-ui-popupWidget-anchored-end .oo-ui-popupWidget-anchor {
 right:-9px
}
.oo-ui-popupWidget-anchored-end .oo-ui-popupWidget-anchor:before {
 left:-10px;
 top:-9px;
 border-left-color:#a2a9b1;
 border-width:10px
}
.oo-ui-popupWidget-anchored-end .oo-ui-popupWidget-anchor:after {
 left:-10px;
 top:-8px;
 border-left-color:#fff;
 border-width:9px
}
.oo-ui-popupWidget-transitioning .oo-ui-popupWidget-popup {
 -webkit-transition:width 100ms,height 100ms,left 100ms;
 -moz-transition:width 100ms,height 100ms,left 100ms;
 transition:width 100ms,height 100ms,left 100ms
}
.oo-ui-popupWidget-head > .oo-ui-iconElement-icon {
 left:0.78571429em;
 height:2.02857143em
}
.oo-ui-popupWidget-head > .oo-ui-iconElement-noIcon + .oo-ui-labelElement-label {
 margin-left:12px
}
.oo-ui-popupWidget-head > .oo-ui-labelElement-label {
 margin:9px 12px 9px 2.64285714em;
 line-height:1.42857143em
}
.oo-ui-popupWidget-head > .oo-ui-buttonWidget {
 right:0
}
.oo-ui-popupWidget-head > .oo-ui-buttonWidget .oo-ui-icon-close {
 background-size:1.14285714em 1.14285714em
}
.oo-ui-popupWidget-body {
 line-height:1.42857143em
}
.oo-ui-popupWidget-body-padded {
 margin:0 12px 5px
}
.oo-ui-popupWidget-body-padded > :first-child {
 margin-top:0
}
.oo-ui-popupWidget-footer {
 margin:9px 12px
}
.oo-ui-popupButtonWidget {
 position:relative
}
.oo-ui-popupButtonWidget .oo-ui-popupWidget {
 cursor:auto
}
.oo-ui-inputWidget {
 margin-right:8px
}
.oo-ui-inputWidget:last-child {
 margin-right:0
}
.oo-ui-buttonInputWidget > button,
.oo-ui-buttonInputWidget > input {
 background-color:transparent;
 margin:0;
 border:0;
 padding:0
}
.oo-ui-checkboxInputWidget {
 display:inline-block;
 z-index:0;
 position:relative;
 line-height:1.42857143em;
 white-space:nowrap
}
.oo-ui-checkboxInputWidget * {
 font:inherit;
 vertical-align:middle
}
.oo-ui-checkboxInputWidget [type='checkbox'] {
 position:relative;
 max-width:none;
 width:1.42857143em;
 height:1.42857143em;
 margin:0;
 opacity:0;
 z-index:1
}
.oo-ui-checkboxInputWidget [type='checkbox'] + span {
 background-color:#fff;
 background-size:0 0;
 -webkit-box-sizing:border-box;
 -moz-box-sizing:border-box;
 box-sizing:border-box;
 position:absolute;
 left:0;
 width:1.42857143em;
 height:1.42857143em;
 border-color:#72777d;
 border-style:solid;
 border-radius:2px;
 border-width:1px
}
.oo-ui-checkboxInputWidget [type='checkbox']:checked:not(:indeterminate) + span {
 background-size:1em 1em
}
.oo-ui-checkboxInputWidget [type='checkbox']:indeterminate + span:before {
 content:' ';
 background-color:#fff;
 position:absolute;
 top:50%;
 left:0.21428571em;
 right:0.21428571em;
 height:2px;
 margin-top:-1px
}
.oo-ui-checkboxInputWidget [type='checkbox']:disabled + span {
 background-color:#c8ccd1;
 border-color:#c8ccd1
}
.oo-ui-checkboxInputWidget.oo-ui-widget-enabled [type='checkbox'] {
 cursor:pointer
}
.oo-ui-checkboxInputWidget.oo-ui-widget-enabled [type='checkbox'] + span {
 cursor:pointer;
 -webkit-transition:background-color 100ms,border-color 100ms,box-shadow 100ms;
 -moz-transition:background-color 100ms,border-color 100ms,box-shadow 100ms;
 transition:background-color 100ms,border-color 100ms,box-shadow 100ms
}
.oo-ui-checkboxInputWidget.oo-ui-widget-enabled [type='checkbox']:focus + span {
 border-color:#36c;
 box-shadow:inset 0 0 0 1px #36c;
 outline:1px solid transparent
}
.oo-ui-checkboxInputWidget.oo-ui-widget-enabled [type='checkbox']:hover + span {
 border-color:#447ff5
}
.oo-ui-checkboxInputWidget.oo-ui-widget-enabled [type='checkbox']:active + span {
 background-color:#2a4b8d;
 border-color:#2a4b8d;
 box-shadow:inset 0 0 0 1px #2a4b8d
}
.oo-ui-checkboxInputWidget.oo-ui-widget-enabled [type='checkbox']:checked + span,
.oo-ui-checkboxInputWidget.oo-ui-widget-enabled [type='checkbox']:indeterminate + span {
 background-color:#36c;
 border-color:#36c
}
.oo-ui-checkboxInputWidget.oo-ui-widget-enabled [type='checkbox']:checked:focus + span,
.oo-ui-checkboxInputWidget.oo-ui-widget-enabled [type='checkbox']:indeterminate:focus + span {
 background-color:#36c;
 border-color:#36c;
 box-shadow:inset 0 0 0 1px #36c,inset 0 0 0 2px #fff
}
.oo-ui-checkboxInputWidget.oo-ui-widget-enabled [type='checkbox']:checked:hover + span,
.oo-ui-checkboxInputWidget.oo-ui-widget-enabled [type='checkbox']:indeterminate:hover + span {
 background-color:#447ff5;
 border-color:#447ff5
}
.oo-ui-checkboxInputWidget.oo-ui-widget-enabled [type='checkbox']:checked:active + span,
.oo-ui-checkboxInputWidget.oo-ui-widget-enabled [type='checkbox']:indeterminate:active + span {
 background-color:#2a4b8d;
 border-color:#2a4b8d;
 box-shadow:inset 0 0 0 1px #2a4b8d
}
.oo-ui-checkboxMultiselectInputWidget .oo-ui-fieldLayout {
 margin-top:0;
 padding:4px 0
}
.oo-ui-checkboxMultiselectInputWidget .oo-ui-fieldLayout:first-child {
 padding-top:0
}
.oo-ui-dropdownInputWidget {
 position:relative;
 vertical-align:middle;
 -webkit-box-sizing:border-box;
 -moz-box-sizing:border-box;
 box-sizing:border-box;
 width:100%;
 max-width:50em
}
.oo-ui-dropdownInputWidget .oo-ui-dropdownWidget,
.oo-ui-dropdownInputWidget.oo-ui-dropdownInputWidget-php select,
.oo-ui-dropdownInputWidget.oo-ui-isMobile select {
 display:block
}
.oo-ui-dropdownInputWidget.oo-ui-isMobile .oo-ui-dropdownWidget {
 display:none
}
.oo-ui-dropdownInputWidget select {
 display:none;
 background-position:-9999em 0;
 background-repeat:no-repeat;
 width:100%;
 -webkit-box-sizing:border-box;
 -moz-box-sizing:border-box;
 box-sizing:border-box
}
.oo-ui-dropdownInputWidget.oo-ui-widget-enabled select {
 cursor:pointer
}
.oo-ui-dropdownInputWidget select {
 -webkit-appearance:none;
 -moz-appearance:none;
 background-color:transparent;
 background-position:right 12px center;
 -webkit-box-sizing:border-box;
 -moz-box-sizing:border-box;
 box-sizing:border-box;
 height:2.28571429em;
 border:1px solid #a2a9b1;
 border-radius:2px;
 padding-left:12px;
 padding-right:2.14285714em;
 font-size:inherit;
 font-family:inherit;
 vertical-align:middle;
 background-position:-9999em 0\9;
 padding:0\9
}
@media screen and (-ms-high-contrast:active),(-ms-high-contrast:none) {
 .oo-ui-dropdownInputWidget select {
  background-position:right 12px center;
  padding-left:12px;
  padding-right:2.14285714em
 }
}
.oo-ui-dropdownInputWidget select::-ms-expand {
 display:none
}
.oo-ui-dropdownInputWidget option {
 background-color:transparent;
 font-size:inherit;
 font-family:inherit;
 height:1.5em;
 padding:5px 12px
}
.oo-ui-dropdownInputWidget.oo-ui-widget-enabled {
 background-color:#f8f9fa;
 -webkit-transition:background-color 100ms;
 -moz-transition:background-color 100ms;
 transition:background-color 100ms
}
.oo-ui-dropdownInputWidget.oo-ui-widget-enabled:hover {
 background-color:#fff
}
.oo-ui-dropdownInputWidget.oo-ui-widget-enabled select {
 color:#202122;
 -webkit-transition:border-color 100ms,box-shadow 100ms;
 -moz-transition:border-color 100ms,box-shadow 100ms;
 transition:border-color 100ms,box-shadow 100ms
}
.oo-ui-dropdownInputWidget.oo-ui-widget-enabled select:hover {
 color:#404244;
 border-color:#a2a9b1
}
.oo-ui-dropdownInputWidget.oo-ui-widget-enabled select:active {
 color:#000;
 border-color:#72777d
}
.oo-ui-dropdownInputWidget.oo-ui-widget-enabled select:focus {
 border-color:#36c;
 outline:0;
 box-shadow:inset 0 0 0 1px #36c
}
.oo-ui-dropdownInputWidget.oo-ui-widget-disabled {
 background-color:#eaecf0
}
.oo-ui-dropdownInputWidget.oo-ui-widget-disabled select {
 color:#72777d;
 border-color:#c8ccd1
}
.oo-ui-radioInputWidget {
 display:inline-block;
 z-index:0;
 position:relative;
 line-height:1.42857143em;
 white-space:nowrap
}
.oo-ui-radioInputWidget * {
 font:inherit;
 vertical-align:middle
}
.oo-ui-radioInputWidget [type='radio'] {
 position:relative;
 max-width:none;
 width:1.42857143em;
 height:1.42857143em;
 margin:0;
 opacity:0;
 z-index:1
}
.oo-ui-radioInputWidget [type='radio'] + span {
 background-color:#fff;
 position:absolute;
 left:0;
 -webkit-box-sizing:border-box;
 -moz-box-sizing:border-box;
 box-sizing:border-box;
 width:1.42857143em;
 height:1.42857143em;
 border-color:#72777d;
 border-style:solid;
 border-radius:100%;
 border-width:0;
 border-width:1px
}
.oo-ui-radioInputWidget [type='radio'] + span:before {
 content:' ';
 position:absolute;
 top:-4px;
 left:-4px;
 right:-4px;
 bottom:-4px;
 border:1px solid transparent;
 border-radius:100%
}
.oo-ui-radioInputWidget [type='radio']:checked + span,
.oo-ui-radioInputWidget [type='radio']:checked:hover + span,
.oo-ui-radioInputWidget [type='radio']:checked:focus:hover + span {
 border-width:6px
}
.oo-ui-radioInputWidget [type='radio']:disabled + span {
 background-color:#c8ccd1;
 border-color:#c8ccd1
}
.oo-ui-radioInputWidget [type='radio']:disabled:checked + span {
 background-color:#fff
}
.oo-ui-radioInputWidget.oo-ui-widget-enabled [type='radio'] {
 cursor:pointer
}
.oo-ui-radioInputWidget.oo-ui-widget-enabled [type='radio'] + span {
 cursor:pointer;
 -webkit-transition:background-color 100ms,border-color 100ms,border-width 100ms;
 -moz-transition:background-color 100ms,border-color 100ms,border-width 100ms;
 transition:background-color 100ms,border-color 100ms,border-width 100ms
}
.oo-ui-radioInputWidget.oo-ui-widget-enabled [type='radio']:hover + span {
 border-color:#447ff5
}
.oo-ui-radioInputWidget.oo-ui-widget-enabled [type='radio']:active + span {
 background-color:#2a4b8d;
 border-color:#2a4b8d
}
.oo-ui-radioInputWidget.oo-ui-widget-enabled [type='radio']:checked + span {
 border-color:#36c
}
.oo-ui-radioInputWidget.oo-ui-widget-enabled [type='radio']:checked:focus + span:before {
 border-color:#fff
}
.oo-ui-radioInputWidget.oo-ui-widget-enabled [type='radio']:checked:hover + span {
 border-color:#447ff5
}
.oo-ui-radioInputWidget.oo-ui-widget-enabled [type='radio']:checked:active + span {
 border-color:#2a4b8d;
 box-shadow:inset 0 0 0 1px #2a4b8d
}
.oo-ui-radioInputWidget.oo-ui-widget-enabled [type='radio']:checked:active + span:before {
 border-color:#2a4b8d
}
.oo-ui-radioSelectInputWidget .oo-ui-fieldLayout {
 margin-top:0;
 padding:4px 0
}
.oo-ui-radioSelectInputWidget .oo-ui-fieldLayout:first-child {
 padding-top:0
}
.oo-ui-textInputWidget {
 position:relative;
 vertical-align:middle;
 -webkit-box-sizing:border-box;
 -moz-box-sizing:border-box;
 box-sizing:border-box;
 width:100%;
 max-width:50em
}
.oo-ui-textInputWidget .oo-ui-inputWidget-input {
 -webkit-appearance:none;
 -moz-appearance:textfield;
 display:block;
 width:100%;
 -webkit-box-sizing:border-box;
 -moz-box-sizing:border-box;
 box-sizing:border-box
}
.oo-ui-textInputWidget input::-ms-clear {
 display:none
}
.oo-ui-textInputWidget textarea {
 overflow:auto
}
.oo-ui-textInputWidget textarea.oo-ui-textInputWidget-autosized {
 resize:none
}
.oo-ui-textInputWidget [type='number']::-webkit-outer-spin-button,
.oo-ui-textInputWidget [type='number']::-webkit-inner-spin-button {
 -webkit-appearance:none;
 margin:0
}
.oo-ui-textInputWidget [type='search']::-webkit-search-decoration,
.oo-ui-textInputWidget [type='search']::-webkit-search-cancel-button {
 display:none
}
.oo-ui-textInputWidget > .oo-ui-iconElement-icon,
.oo-ui-textInputWidget-labelPosition-before > .oo-ui-labelElement-label {
 left:0
}
.oo-ui-textInputWidget > .oo-ui-indicatorElement-indicator,
.oo-ui-textInputWidget-labelPosition-after > .oo-ui-labelElement-label {
 right:0
}
.oo-ui-textInputWidget > .oo-ui-labelElement-label {
 position:absolute;
 top:0
}
.oo-ui-textInputWidget.oo-ui-labelElement > .oo-ui-labelElement-label {
 display:block
}
.oo-ui-textInputWidget-labelPosition-after.oo-ui-labelElement ::-ms-clear {
 display:none
}
.oo-ui-textInputWidget-php > .oo-ui-iconElement-icon,
.oo-ui-textInputWidget-php > .oo-ui-indicatorElement-indicator,
.oo-ui-textInputWidget-php > .oo-ui-labelElement-label {
 pointer-events:none
}
.oo-ui-textInputWidget.oo-ui-widget-enabled > .oo-ui-iconElement-icon,
.oo-ui-textInputWidget.oo-ui-widget-enabled > .oo-ui-indicatorElement-indicator {
 cursor:text
}
.oo-ui-textInputWidget.oo-ui-widget-enabled.oo-ui-textInputWidget-type-search > .oo-ui-indicatorElement-indicator {
 cursor:pointer
}
.oo-ui-textInputWidget.oo-ui-widget-disabled > * {
 -webkit-touch-callout:none;
 -webkit-user-select:none;
 -moz-user-select:none;
 -ms-user-select:none;
 user-select:none
}
.oo-ui-textInputWidget .oo-ui-inputWidget-input {
 background-color:#fff;
 color:#000;
 margin:0;
 border:1px solid #a2a9b1;
 border-radius:2px;
 padding:5px 8px;
 font-size:inherit;
 font-family:inherit;
 line-height:1.42857143em
}
.oo-ui-textInputWidget input {
 height:2.28571429em
}
.oo-ui-textInputWidget .oo-ui-pendingElement-pending {
 background-color:#eaecf0
}
.oo-ui-textInputWidget.oo-ui-iconElement .oo-ui-inputWidget-input {
 padding-left:2.42857143em
}
.oo-ui-textInputWidget.oo-ui-iconElement > .oo-ui-iconElement-icon {
 left:9px
}
.oo-ui-textInputWidget.oo-ui-iconElement textarea + .oo-ui-iconElement-icon {
 max-height:2.28571429em
}
.oo-ui-textInputWidget > .oo-ui-labelElement-label {
 color:#72777d;
 padding:0 12px 0 8px;
 line-height:2.28571429em
}
.oo-ui-textInputWidget.oo-ui-indicatorElement .oo-ui-inputWidget-input {
 padding-right:28px
}
.oo-ui-textInputWidget.oo-ui-indicatorElement.oo-ui-textInputWidget-labelPosition-after > .oo-ui-labelElement-label {
 padding-right:0
}
.oo-ui-textInputWidget.oo-ui-indicatorElement > .oo-ui-indicatorElement-indicator {
 max-height:2.28571429em;
 margin-right:0.71428571em
}
.oo-ui-textInputWidget-labelPosition-after.oo-ui-indicatorElement > .oo-ui-labelElement-label {
 margin-right:2.28571429em
}
.oo-ui-textInputWidget-labelPosition-before.oo-ui-iconElement > .oo-ui-labelElement-label {
 padding-left:2.42857143em
}
.oo-ui-textInputWidget.oo-ui-widget-enabled .oo-ui-inputWidget-input {
 box-shadow:inset 0 0 0 1px transparent;
 -webkit-transition:border-color 250ms,box-shadow 250ms;
 -moz-transition:border-color 250ms,box-shadow 250ms;
 transition:border-color 250ms,box-shadow 250ms
}
.oo-ui-textInputWidget.oo-ui-widget-enabled .oo-ui-inputWidget-input::-webkit-input-placeholder {
 color:#72777d;
 opacity:1
}
.oo-ui-textInputWidget.oo-ui-widget-enabled .oo-ui-inputWidget-input:-ms-input-placeholder {
 color:#72777d;
 opacity:1
}
.oo-ui-textInputWidget.oo-ui-widget-enabled .oo-ui-inputWidget-input::-moz-placeholder {
 color:#72777d;
 opacity:1
}
.oo-ui-textInputWidget.oo-ui-widget-enabled .oo-ui-inputWidget-input:-moz-placeholder {
 color:#72777d;
 opacity:1
}
.oo-ui-textInputWidget.oo-ui-widget-enabled .oo-ui-inputWidget-input::placeholder {
 color:#72777d;
 opacity:1
}
.oo-ui-textInputWidget.oo-ui-widget-enabled .oo-ui-inputWidget-input:focus {
 outline:0;
 border-color:#36c;
 box-shadow:inset 0 0 0 1px #36c
}
.oo-ui-textInputWidget.oo-ui-widget-enabled .oo-ui-inputWidget-input:focus ~ .oo-ui-iconElement-icon,
.oo-ui-textInputWidget.oo-ui-widget-enabled .oo-ui-inputWidget-input:focus ~ .oo-ui-indicatorElement-indicator {
 opacity:1
}
.oo-ui-textInputWidget.oo-ui-widget-enabled .oo-ui-inputWidget-input[readonly]:not(.oo-ui-pendingElement-pending) {
 background-color:#f8f9fa
}
.oo-ui-textInputWidget.oo-ui-widget-enabled:hover .oo-ui-inputWidget-input {
 border-color:#72777d
}
.oo-ui-textInputWidget.oo-ui-widget-enabled:hover .oo-ui-inputWidget-input:focus {
 border-color:#36c
}
@media screen and (min-width:0) {
 .oo-ui-textInputWidget.oo-ui-widget-enabled textarea.oo-ui-inputWidget-input:focus {
  outline:1px solid #36c;
  outline-offset:-2px
 }
 .oo-ui-textInputWidget.oo-ui-widget-enabled.oo-ui-flaggedElement-invalid textarea.oo-ui-inputWidget-input:focus {
  outline-color:#d33
 }
}
.oo-ui-textInputWidget.oo-ui-widget-enabled > .oo-ui-iconElement-icon {
 opacity:0.67
}
.oo-ui-textInputWidget.oo-ui-widget-enabled > .oo-ui-indicatorElement-indicator {
 opacity:0.87
}
.oo-ui-textInputWidget.oo-ui-widget-enabled.oo-ui-flaggedElement-invalid .oo-ui-inputWidget-input {
 border-color:#d33
}
.oo-ui-textInputWidget.oo-ui-widget-enabled.oo-ui-flaggedElement-invalid .oo-ui-inputWidget-input:hover {
 border-color:#d33
}
.oo-ui-textInputWidget.oo-ui-widget-enabled.oo-ui-flaggedElement-invalid .oo-ui-inputWidget-input:focus {
 border-color:#d33;
 box-shadow:inset 0 0 0 1px #d33
}
.oo-ui-textInputWidget.oo-ui-widget-disabled .oo-ui-inputWidget-input {
 background-color:#eaecf0;
 -webkit-text-fill-color:#72777d;
 color:#72777d;
 text-shadow:0 1px 1px #fff;
 border-color:#c8ccd1
}
.oo-ui-textInputWidget.oo-ui-widget-disabled > .oo-ui-iconElement-icon,
.oo-ui-textInputWidget.oo-ui-widget-disabled > .oo-ui-indicatorElement-indicator {
 opacity:0.51
}
.oo-ui-textInputWidget.oo-ui-widget-disabled > .oo-ui-labelElement-label {
 color:#72777d;
 text-shadow:0 1px 1px #fff
}
.oo-ui-menuSelectWidget {
 position:absolute;
 width:100%;
 z-index:4;
 background-color:#fff;
 margin-top:-1px;
 margin-bottom:-1px;
 border:1px solid #a2a9b1;
 border-radius:0 0 2px 2px;
 box-shadow:0 2px 2px 0 rgba(0,0,0,0.25)
}
.oo-ui-menuSelectWidget.oo-ui-clippableElement-clippable {
 min-height:32px
}
.oo-ui-menuSelectWidget-invisible {
 display:none
}
.oo-ui-menuOptionWidget {
 -webkit-transition:background-color 100ms,color 100ms;
 -moz-transition:background-color 100ms,color 100ms;
 transition:background-color 100ms,color 100ms
}
.oo-ui-menuOptionWidget-checkIcon {
 display:none
}
.oo-ui-menuOptionWidget.oo-ui-optionWidget-highlighted {
 background-color:#eaecf0;
 color:#000
}
.oo-ui-menuOptionWidget.oo-ui-optionWidget-selected {
 background-color:#eaf3ff;
 color:#36c
}
.oo-ui-menuOptionWidget.oo-ui-optionWidget-selected.oo-ui-menuOptionWidget.oo-ui-optionWidget-highlighted,
.oo-ui-menuOptionWidget.oo-ui-optionWidget-pressed.oo-ui-menuOptionWidget.oo-ui-optionWidget-highlighted {
 background-color:rgba(41,98,204,0.1);
 color:#36c
}
.oo-ui-menuOptionWidget.oo-ui-widget-enabled.oo-ui-optionWidget {
 color:#202122
}
.oo-ui-menuSectionOptionWidget {
 color:#72777d;
 padding:5px 12px 4px;
 font-weight:bold
}
.oo-ui-menuSectionOptionWidget.oo-ui-widget-enabled {
 cursor:default
}
.oo-ui-menuSectionOptionWidget ~ .oo-ui-menuOptionWidget {
 padding-left:24px
}
.oo-ui-menuSectionOptionWidget ~ .oo-ui-menuOptionWidget.oo-ui-iconElement {
 padding-left:3.5em
}
.oo-ui-menuSectionOptionWidget ~ .oo-ui-menuOptionWidget.oo-ui-iconElement .oo-ui-iconElement-icon {
 left:1.71428571em
}
.oo-ui-dropdownWidget {
 display:inline-block;
 position:relative;
 vertical-align:middle;
 width:100%;
 max-width:50em;
 margin-right:8px
}
.oo-ui-dropdownWidget-handle {
 position:relative;
 width:100%;
 display:block;
 white-space:nowrap;
 overflow:hidden;
 text-overflow:ellipsis;
 cursor:default;
 -webkit-touch-callout:none;
 -webkit-user-select:none;
 -moz-user-select:none;
 -ms-user-select:none;
 user-select:none;
 -webkit-box-sizing:border-box;
 -moz-box-sizing:border-box;
 box-sizing:border-box
}
.oo-ui-dropdownWidget-handle .oo-ui-labelElement-label {
 display:inline-block
}
.oo-ui-dropdownWidget.oo-ui-widget-enabled .oo-ui-dropdownWidget-handle {
 cursor:pointer
}
.oo-ui-dropdownWidget:last-child {
 margin-right:0
}
.oo-ui-dropdownWidget-handle {
 min-height:2.28571429em;
 border:1px solid #a2a9b1;
 border-radius:2px;
 padding:5px 2.14285714em 5px 12px;
 line-height:1
}
.oo-ui-dropdownWidget-handle .oo-ui-iconElement-icon {
 left:12px
}
.oo-ui-dropdownWidget-handle .oo-ui-indicatorElement-indicator {
 right:11px
}
.oo-ui-dropdownWidget-handle .oo-ui-labelElement-label {
 line-height:1.42857143em
}
.oo-ui-dropdownWidget.oo-ui-iconElement .oo-ui-dropdownWidget-handle {
 padding-left:2.71428571em
}
.oo-ui-dropdownWidget.oo-ui-indicatorElement .oo-ui-dropdownWidget-handle {
 padding-right:2.57142857em
}
.oo-ui-dropdownWidget.oo-ui-widget-enabled .oo-ui-dropdownWidget-handle {
 background-color:#f8f9fa;
 color:#202122;
 -webkit-transition:background-color 100ms,border-color 100ms,box-shadow 100ms;
 -moz-transition:background-color 100ms,border-color 100ms,box-shadow 100ms;
 transition:background-color 100ms,border-color 100ms,box-shadow 100ms
}
.oo-ui-dropdownWidget.oo-ui-widget-enabled .oo-ui-dropdownWidget-handle:hover {
 background-color:#fff;
 color:#404244;
 border-color:#a2a9b1
}
.oo-ui-dropdownWidget.oo-ui-widget-enabled .oo-ui-dropdownWidget-handle:hover .oo-ui-iconElement-icon,
.oo-ui-dropdownWidget.oo-ui-widget-enabled .oo-ui-dropdownWidget-handle:hover .oo-ui-indicatorElement-indicator {
 opacity:0.74
}
.oo-ui-dropdownWidget.oo-ui-widget-enabled .oo-ui-dropdownWidget-handle:active {
 color:#000;
 border-color:#72777d
}
.oo-ui-dropdownWidget.oo-ui-widget-enabled .oo-ui-dropdownWidget-handle:focus {
 border-color:#36c;
 outline:0;
 box-shadow:inset 0 0 0 1px #36c
}
.oo-ui-dropdownWidget.oo-ui-widget-enabled .oo-ui-dropdownWidget-handle .oo-ui-iconElement-icon,
.oo-ui-dropdownWidget.oo-ui-widget-enabled .oo-ui-dropdownWidget-handle .oo-ui-indicatorElement-indicator {
 opacity:0.87;
 -webkit-transition:opacity 100ms;
 -moz-transition:opacity 100ms;
 transition:opacity 100ms
}
.oo-ui-dropdownWidget.oo-ui-widget-enabled.oo-ui-dropdownWidget-open .oo-ui-dropdownWidget-handle {
 background-color:#fff
}
.oo-ui-dropdownWidget.oo-ui-widget-enabled.oo-ui-dropdownWidget-open .oo-ui-dropdownWidget-handle .oo-ui-iconElement-icon,
.oo-ui-dropdownWidget.oo-ui-widget-enabled.oo-ui-dropdownWidget-open .oo-ui-dropdownWidget-handle .oo-ui-indicatorElement-indicator {
 opacity:1
}
.oo-ui-dropdownWidget.oo-ui-widget-disabled .oo-ui-dropdownWidget-handle {
 color:#72777d;
 text-shadow:0 1px 1px #fff;
 border-color:#c8ccd1;
 background-color:#eaecf0
}
.oo-ui-dropdownWidget.oo-ui-widget-disabled .oo-ui-dropdownWidget-handle:focus {
 outline:0
}
.oo-ui-dropdownWidget.oo-ui-widget-disabled .oo-ui-dropdownWidget-handle .oo-ui-indicatorElement-indicator {
 opacity:0.15
}
.oo-ui-comboBoxInputWidget {
 display:inline-block;
 position:relative
}
.oo-ui-comboBoxInputWidget-field {
 display:table;
 width:100%;
 table-layout:fixed
}
.oo-ui-comboBoxInputWidget .oo-ui-inputWidget-input {
 display:table-cell;
 vertical-align:middle;
 position:relative;
 overflow:hidden
}
.oo-ui-comboBoxInputWidget-dropdownButton {
 display:table-cell
}
.oo-ui-comboBoxInputWidget-dropdownButton > .oo-ui-buttonElement-button {
 display:block;
 overflow:hidden
}
.oo-ui-comboBoxInputWidget.oo-ui-comboBoxInputWidget-empty .oo-ui-comboBoxInputWidget-dropdownButton {
 display:none
}
.oo-ui-comboBoxInputWidget-php ::-webkit-calendar-picker-indicator {
 opacity:0;
 position:absolute;
 right:0;
 top:0;
 width:2.5em;
 height:2.5em;
 padding:0
}
.oo-ui-comboBoxInputWidget-php > .oo-ui-indicatorWidget {
 display:block;
 position:absolute;
 top:0;
 height:100%;
 pointer-events:none
}
.oo-ui-comboBoxInputWidget .oo-ui-inputWidget-input {
 height:2.28571429em;
 border-top-right-radius:0;
 border-bottom-right-radius:0;
 border-right-width:0
}
.oo-ui-comboBoxInputWidget.oo-ui-comboBoxInputWidget-empty .oo-ui-inputWidget-input,
.oo-ui-comboBoxInputWidget-php .oo-ui-inputWidget-input {
 border-top-right-radius:2px;
 border-bottom-right-radius:2px;
 border-right-width:1px
}
.oo-ui-comboBoxInputWidget-dropdownButton.oo-ui-indicatorElement {
 width:2.64285714em
}
.oo-ui-comboBoxInputWidget-dropdownButton.oo-ui-indicatorElement .oo-ui-buttonElement-button {
 min-width:37px;
 padding-left:0
}
.oo-ui-comboBoxInputWidget-dropdownButton.oo-ui-indicatorElement .oo-ui-buttonElement-button > .oo-ui-indicatorElement-indicator {
 right:0.85714286em
}
.oo-ui-comboBoxInputWidget-dropdownButton.oo-ui-indicatorElement .oo-ui-buttonElement-button,
.oo-ui-comboBoxInputWidget-dropdownButton.oo-ui-indicatorElement .oo-ui-buttonElement-button:focus {
 border-top-left-radius:0;
 border-bottom-left-radius:0
}
.oo-ui-comboBoxInputWidget-php .oo-ui-indicatorWidget {
 right:12px;
 margin:0
}
.oo-ui-comboBoxInputWidget-open .oo-ui-comboBoxInputWidget-dropdownButton > .oo-ui-buttonElement-button {
 background-color:#fff
}
.oo-ui-comboBoxInputWidget-open .oo-ui-comboBoxInputWidget-dropdownButton > .oo-ui-buttonElement-button .oo-ui-indicatorElement-indicator {
 opacity:1
}
.oo-ui-comboBoxInputWidget.oo-ui-widget-disabled .oo-ui-indicatorElement-indicator {
 opacity:1
}
.oo-ui-multioptionWidget {
 position:relative;
 display:block
}
.oo-ui-multioptionWidget.oo-ui-widget-enabled {
 cursor:pointer
}
.oo-ui-multioptionWidget.oo-ui-widget-disabled {
 cursor:default
}
.oo-ui-multioptionWidget.oo-ui-labelElement .oo-ui-labelElement-label {
 display:block;
 white-space:nowrap;
 text-overflow:ellipsis;
 overflow:hidden
}
.oo-ui-multioptionWidget.oo-ui-widget-disabled {
 color:#72777d
}
.oo-ui-checkboxMultioptionWidget {
 display:table;
 padding:4px 0
}
.oo-ui-checkboxMultioptionWidget .oo-ui-checkboxInputWidget,
.oo-ui-checkboxMultioptionWidget.oo-ui-labelElement > .oo-ui-labelElement-label {
 display:table-cell;
 vertical-align:top
}
.oo-ui-checkboxMultioptionWidget .oo-ui-checkboxInputWidget {
 width:1px
}
.oo-ui-checkboxMultioptionWidget.oo-ui-labelElement > .oo-ui-labelElement-label {
 white-space:normal
}
.oo-ui-checkboxMultioptionWidget:first-child {
 padding-top:0
}
.oo-ui-checkboxMultioptionWidget.oo-ui-labelElement > .oo-ui-labelElement-label {
 padding-left:6px
}
.oo-ui-checkboxMultioptionWidget .oo-ui-checkboxInputWidget {
 margin-right:0
}
.oo-ui-progressBarWidget {
 -webkit-box-sizing:border-box;
 -moz-box-sizing:border-box;
 box-sizing:border-box;
 max-width:50em;
 background-color:#fff;
 border:1px solid #a2a9b1;
 border-radius:1em;
 box-shadow:0 1px 1px rgba(0,0,0,0.15);
 overflow:hidden
}
.oo-ui-progressBarWidget-bar {
 height:1em;
 -webkit-transition:width 100ms;
 -moz-transition:width 100ms;
 transition:width 100ms
}
.oo-ui-progressBarWidget-indeterminate .oo-ui-progressBarWidget-bar {
 -webkit-animation:oo-ui-progressBarWidget-slide 2s infinite linear;
 -moz-animation:oo-ui-progressBarWidget-slide 2s infinite linear;
 animation:oo-ui-progressBarWidget-slide 2s infinite linear;
 width:40%;
 -webkit-transform:translate(-25%);
 -moz-transform:translate(-25%);
 -ms-transform:translate(-25%);
 transform:translate(-25%)
}
.oo-ui-progressBarWidget.oo-ui-widget-enabled .oo-ui-progressBarWidget-bar {
 background-color:#36c
}
.oo-ui-progressBarWidget.oo-ui-widget-disabled .oo-ui-progressBarWidget-bar {
 background-color:#c8ccd1
}
@-webkit-keyframes oo-ui-progressBarWidget-slide {
 from {
  -webkit-transform:translate(-100%);
  -moz-transform:translate(-100%);
  -ms-transform:translate(-100%);
  transform:translate(-100%)
 }
 to {
  -webkit-transform:translate(350%);
  -moz-transform:translate(350%);
  -ms-transform:translate(350%);
  transform:translate(350%)
 }
}
@-moz-keyframes oo-ui-progressBarWidget-slide {
 from {
  -webkit-transform:translate(-100%);
  -moz-transform:translate(-100%);
  -ms-transform:translate(-100%);
  transform:translate(-100%)
 }
 to {
  -webkit-transform:translate(350%);
  -moz-transform:translate(350%);
  -ms-transform:translate(350%);
  transform:translate(350%)
 }
}
@keyframes oo-ui-progressBarWidget-slide {
 from {
  -webkit-transform:translate(-100%);
  -moz-transform:translate(-100%);
  -ms-transform:translate(-100%);
  transform:translate(-100%)
 }
 to {
  -webkit-transform:translate(350%);
  -moz-transform:translate(350%);
  -ms-transform:translate(350%);
  transform:translate(350%)
 }
}
.oo-ui-numberInputWidget {
 display:inline-block;
 position:relative;
 max-width:50em
}
.oo-ui-numberInputWidget-buttoned .oo-ui-buttonWidget,
.oo-ui-numberInputWidget-buttoned .oo-ui-inputWidget-input {
 display:table-cell;
 height:100%
}
.oo-ui-numberInputWidget-field {
 display:table;
 table-layout:fixed;
 width:100%
}
.oo-ui-numberInputWidget-buttoned .oo-ui-buttonWidget {
 width:2.64285714em
}
.oo-ui-numberInputWidget-buttoned .oo-ui-buttonWidget .oo-ui-buttonElement-button {
 display:block;
 min-width:37px;
 min-height:2.28571429em;
 padding-left:0;
 padding-right:0
}
.oo-ui-numberInputWidget-buttoned .oo-ui-inputWidget-input {
 border-radius:0;
 height:2.28571429em
}
.oo-ui-numberInputWidget-minusButton > .oo-ui-buttonElement-button {
 border-top-right-radius:0;
 border-bottom-right-radius:0;
 border-right-width:0
}
.oo-ui-numberInputWidget-plusButton > .oo-ui-buttonElement-button {
 border-top-left-radius:0;
 border-bottom-left-radius:0;
 border-left-width:0
}
.oo-ui-numberInputWidget.oo-ui-widget-disabled.oo-ui-numberInputWidget-buttoned .oo-ui-iconElement-icon {
 opacity:1
}
.oo-ui-selectFileInputWidget {
 width:100%;
 max-width:50em
}
.oo-ui-selectFileInputWidget-selectButton > .oo-ui-buttonElement-button {
 position:relative;
 overflow:hidden
}
.oo-ui-selectFileInputWidget-selectButton > .oo-ui-buttonElement-button > [type='file'] {
 position:absolute;
 top:0;
 bottom:0;
 left:0;
 right:0;
 width:100%;
 height:100%;
 opacity:0;
 z-index:1;
 cursor:pointer;
 padding-top:100px
}
.oo-ui-selectFileInputWidget-selectButton.oo-ui-widget-disabled > .oo-ui-buttonElement-button > [type='file'] {
 display:none
}
.oo-ui-selectFileInputWidget-info > .oo-ui-inputWidget-input {
 pointer-events:none
}
.oo-ui-selectFileInputWidget-empty.oo-ui-widget-enabled .oo-ui-selectFileInputWidget-label {
 cursor:default
}
.oo-ui-selectFileInputWidget-info > .oo-ui-inputWidget-input {
 height:2.28571429em
}
.oo-ui-defaultOverlay {
 position:absolute;
 top:0;
 left:0
}
.oo-ui-defaultOverlay,
.skin-vector .oo-ui-windowManager-modal > .oo-ui-dialog,
.skin-vector .ve-ui-overlay-global {
 z-index:101
}
body > .oo-ui-windowManager,
.oo-ui-defaultOverlay {
 font-size:0.875em
}
.oo-ui-icon-bright,
.mw-ui-icon-bright:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=bright&format=rasterized&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ebright%3C/title%3E%3Cpath d=%22M17.07 7.07V2.93h-4.14L10 0 7.07 2.93H2.93v4.14L0 10l2.93 2.93v4.14h4.14L10 20l2.93-2.93h4.14v-4.14L20 10zM10 16a6 6 0 116-6 6 6 0 01-6 6z%22/%3E%3Ccircle cx=%2210%22 cy=%2210%22 r=%224.5%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-bright,
.mw-ui-icon-bright-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=bright&variant=invert&format=rasterized&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ebright%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M17.07 7.07V2.93h-4.14L10 0 7.07 2.93H2.93v4.14L0 10l2.93 2.93v4.14h4.14L10 20l2.93-2.93h4.14v-4.14L20 10zM10 16a6 6 0 116-6 6 6 0 01-6 6z%22/%3E%3Ccircle cx=%2210%22 cy=%2210%22 r=%224.5%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-bright,
.mw-ui-icon-bright-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=bright&variant=progressive&format=rasterized&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ebright%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M17.07 7.07V2.93h-4.14L10 0 7.07 2.93H2.93v4.14L0 10l2.93 2.93v4.14h4.14L10 20l2.93-2.93h4.14v-4.14L20 10zM10 16a6 6 0 116-6 6 6 0 01-6 6z%22/%3E%3Ccircle cx=%2210%22 cy=%2210%22 r=%224.5%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-halfBright,
.mw-ui-icon-halfBright:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=halfBright&format=rasterized&lang=fr&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ehalf bright%3C/title%3E%3Cpath d=%22M17 6.67V3h-4.2L9.87.07 6.94 3H3v3.67L.07 9.6 3 12.53V17h3.94l2.93 2.93L12.8 17H17v-4.47l2.93-2.93zm-7 8.93v-12a6.21 6.21 0 016 6 6.21 6.21 0 01-6 6z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-halfBright,
.mw-ui-icon-halfBright-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=halfBright&variant=invert&format=rasterized&lang=fr&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ehalf bright%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M17 6.67V3h-4.2L9.87.07 6.94 3H3v3.67L.07 9.6 3 12.53V17h3.94l2.93 2.93L12.8 17H17v-4.47l2.93-2.93zm-7 8.93v-12a6.21 6.21 0 016 6 6.21 6.21 0 01-6 6z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-halfBright,
.mw-ui-icon-halfBright-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=halfBright&variant=progressive&format=rasterized&lang=fr&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ehalf bright%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M17 6.67V3h-4.2L9.87.07 6.94 3H3v3.67L.07 9.6 3 12.53V17h3.94l2.93 2.93L12.8 17H17v-4.47l2.93-2.93zm-7 8.93v-12a6.21 6.21 0 016 6 6.21 6.21 0 01-6 6z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-notBright,
.mw-ui-icon-notBright:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=notBright&format=rasterized&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Enot bright%3C/title%3E%3Ccircle cx=%229.85%22 cy=%2210%22 r=%229%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-notBright,
.mw-ui-icon-notBright-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=notBright&variant=invert&format=rasterized&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Enot bright%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Ccircle cx=%229.85%22 cy=%2210%22 r=%229%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-notBright,
.mw-ui-icon-notBright-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=notBright&variant=progressive&format=rasterized&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Enot bright%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Ccircle cx=%229.85%22 cy=%2210%22 r=%229%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-eye,
.mw-ui-icon-eye:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=eye&format=rasterized&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eeye%3C/title%3E%3Cpath d=%22M10 14.5a4.5 4.5 0 114.5-4.5 4.5 4.5 0 01-4.5 4.5zM10 3C3 3 0 10 0 10s3 7 10 7 10-7 10-7-3-7-10-7z%22/%3E%3Ccircle cx=%2210%22 cy=%2210%22 r=%222.5%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-eye,
.mw-ui-icon-eye-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=eye&variant=invert&format=rasterized&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eeye%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M10 14.5a4.5 4.5 0 114.5-4.5 4.5 4.5 0 01-4.5 4.5zM10 3C3 3 0 10 0 10s3 7 10 7 10-7 10-7-3-7-10-7z%22/%3E%3Ccircle cx=%2210%22 cy=%2210%22 r=%222.5%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-eye,
.mw-ui-icon-eye-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=eye&variant=progressive&format=rasterized&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eeye%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M10 14.5a4.5 4.5 0 114.5-4.5 4.5 4.5 0 01-4.5 4.5zM10 3C3 3 0 10 0 10s3 7 10 7 10-7 10-7-3-7-10-7z%22/%3E%3Ccircle cx=%2210%22 cy=%2210%22 r=%222.5%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-eyeClosed,
.mw-ui-icon-eyeClosed:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=eyeClosed&format=rasterized&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eeye closed%3C/title%3E%3Cpath d=%22M12.49 9.94A2.5 2.5 0 0010 7.5z%22/%3E%3Cpath d=%22M8.2 5.9a4.38 4.38 0 011.8-.4 4.5 4.5 0 014.5 4.5 4.34 4.34 0 01-.29 1.55L17 14.14A14 14 0 0020 10s-3-7-10-7a9.63 9.63 0 00-4 .85zM2 2L1 3l2.55 2.4A13.89 13.89 0 000 10s3 7 10 7a9.67 9.67 0 004.64-1.16L18 19l1-1zm8 12.5A4.5 4.5 0 015.5 10a4.45 4.45 0 01.6-2.2l1.53 1.44a2.47 2.47 0 00-.13.76 2.49 2.49 0 003.41 2.32l1.54 1.45a4.47 4.47 0 01-2.45.73z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-eyeClosed,
.mw-ui-icon-eyeClosed-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=eyeClosed&variant=invert&format=rasterized&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eeye closed%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M12.49 9.94A2.5 2.5 0 0010 7.5z%22/%3E%3Cpath d=%22M8.2 5.9a4.38 4.38 0 011.8-.4 4.5 4.5 0 014.5 4.5 4.34 4.34 0 01-.29 1.55L17 14.14A14 14 0 0020 10s-3-7-10-7a9.63 9.63 0 00-4 .85zM2 2L1 3l2.55 2.4A13.89 13.89 0 000 10s3 7 10 7a9.67 9.67 0 004.64-1.16L18 19l1-1zm8 12.5A4.5 4.5 0 015.5 10a4.45 4.45 0 01.6-2.2l1.53 1.44a2.47 2.47 0 00-.13.76 2.49 2.49 0 003.41 2.32l1.54 1.45a4.47 4.47 0 01-2.45.73z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-eyeClosed,
.mw-ui-icon-eyeClosed-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=eyeClosed&variant=progressive&format=rasterized&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eeye closed%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M12.49 9.94A2.5 2.5 0 0010 7.5z%22/%3E%3Cpath d=%22M8.2 5.9a4.38 4.38 0 011.8-.4 4.5 4.5 0 014.5 4.5 4.34 4.34 0 01-.29 1.55L17 14.14A14 14 0 0020 10s-3-7-10-7a9.63 9.63 0 00-4 .85zM2 2L1 3l2.55 2.4A13.89 13.89 0 000 10s3 7 10 7a9.67 9.67 0 004.64-1.16L18 19l1-1zm8 12.5A4.5 4.5 0 015.5 10a4.45 4.45 0 01.6-2.2l1.53 1.44a2.47 2.47 0 00-.13.76 2.49 2.49 0 003.41 2.32l1.54 1.45a4.47 4.47 0 01-2.45.73z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-moon,
.mw-ui-icon-moon:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=moon&format=rasterized&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Emoon%3C/title%3E%3Cpath d=%22M17.39 15.14A7.33 7.33 0 0111.75 1.6c.23-.11.56-.23.79-.34a8.19 8.19 0 00-5.41.45 9 9 0 107 16.58 8.42 8.42 0 004.29-3.84 5.3 5.3 0 01-1.03.69z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-moon,
.mw-ui-icon-moon-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=moon&variant=invert&format=rasterized&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Emoon%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M17.39 15.14A7.33 7.33 0 0111.75 1.6c.23-.11.56-.23.79-.34a8.19 8.19 0 00-5.41.45 9 9 0 107 16.58 8.42 8.42 0 004.29-3.84 5.3 5.3 0 01-1.03.69z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-moon,
.mw-ui-icon-moon-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=moon&variant=progressive&format=rasterized&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Emoon%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M17.39 15.14A7.33 7.33 0 0111.75 1.6c.23-.11.56-.23.79-.34a8.19 8.19 0 00-5.41.45 9 9 0 107 16.58 8.42 8.42 0 004.29-3.84 5.3 5.3 0 01-1.03.69z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-largerText,
.mw-ui-icon-largerText:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=largerText&format=rasterized&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Elarger text%3C/title%3E%3Cpath d=%22M17.66 18h-2a.85.85 0 01-.56-.17 1.11 1.11 0 01-.32-.43l-1.33-3.53h-6.9L5.22 17.4a1.06 1.06 0 01-.31.41.83.83 0 01-.56.19h-2L8.68 2h2.63zm-4.92-6l-2.2-5.84A16.17 16.17 0 0110 4.43q-.12.52-.27 1t-.27.77L7.26 12z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-largerText,
.mw-ui-icon-largerText-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=largerText&variant=invert&format=rasterized&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Elarger text%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M17.66 18h-2a.85.85 0 01-.56-.17 1.11 1.11 0 01-.32-.43l-1.33-3.53h-6.9L5.22 17.4a1.06 1.06 0 01-.31.41.83.83 0 01-.56.19h-2L8.68 2h2.63zm-4.92-6l-2.2-5.84A16.17 16.17 0 0110 4.43q-.12.52-.27 1t-.27.77L7.26 12z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-largerText,
.mw-ui-icon-largerText-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=largerText&variant=progressive&format=rasterized&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Elarger text%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M17.66 18h-2a.85.85 0 01-.56-.17 1.11 1.11 0 01-.32-.43l-1.33-3.53h-6.9L5.22 17.4a1.06 1.06 0 01-.31.41.83.83 0 01-.56.19h-2L8.68 2h2.63zm-4.92-6l-2.2-5.84A16.17 16.17 0 0110 4.43q-.12.52-.27 1t-.27.77L7.26 12z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-smallerText,
.mw-ui-icon-smallerText:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=smallerText&format=rasterized&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Esmaller text%3C/title%3E%3Cpath d=%22M15.75 18h-1.51a.64.64 0 01-.42-.13.83.83 0 01-.24-.32l-1-2.65H7.41l-1 2.65a.79.79 0 01-.23.31.62.62 0 01-.42.14H4.25L9 6h2zm-3.69-4.5L10.4 9.12a12.13 12.13 0 01-.4-1.3q-.09.39-.2.72t-.2.58L7.95 13.5z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-smallerText,
.mw-ui-icon-smallerText-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=smallerText&variant=invert&format=rasterized&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Esmaller text%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M15.75 18h-1.51a.64.64 0 01-.42-.13.83.83 0 01-.24-.32l-1-2.65H7.41l-1 2.65a.79.79 0 01-.23.31.62.62 0 01-.42.14H4.25L9 6h2zm-3.69-4.5L10.4 9.12a12.13 12.13 0 01-.4-1.3q-.09.39-.2.72t-.2.58L7.95 13.5z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-smallerText,
.mw-ui-icon-smallerText-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=smallerText&variant=progressive&format=rasterized&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Esmaller text%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M15.75 18h-1.51a.64.64 0 01-.42-.13.83.83 0 01-.24-.32l-1-2.65H7.41l-1 2.65a.79.79 0 01-.23.31.62.62 0 01-.42.14H4.25L9 6h2zm-3.69-4.5L10.4 9.12a12.13 12.13 0 01-.4-1.3q-.09.39-.2.72t-.2.58L7.95 13.5z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-visionSimulator,
.mw-ui-icon-visionSimulator:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=visionSimulator&format=rasterized&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Evision simulator%3C/title%3E%3Cpath d=%22M17.5 11.83a.79.79 0 01-.83.83h-3.34A1.49 1.49 0 0111.67 11V9.33a.79.79 0 01.83-.83h4.17a.79.79 0 01.83.83zM8.33 11a1.49 1.49 0 01-1.67 1.67H3.33a.79.79 0 01-.83-.83V9.33a.79.79 0 01.83-.83H7.5a.79.79 0 01.83.83zM0 6.2v6.28a.2.2 0 00.2.2h1.72a1.61 1.61 0 001.42.83h3.33A2.46 2.46 0 009.13 12a.19.19 0 01.18-.13h1.39a.19.19 0 01.18.13 2.46 2.46 0 002.46 1.53h3.33c.55 0 1.1 0 1.37-.7a.2.2 0 01.18-.13h1.58a.2.2 0 00.2-.2V6.2a.2.2 0 00-.2-.2H.2a.2.2 0 00-.2.2z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-visionSimulator,
.mw-ui-icon-visionSimulator-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=visionSimulator&variant=invert&format=rasterized&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Evision simulator%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M17.5 11.83a.79.79 0 01-.83.83h-3.34A1.49 1.49 0 0111.67 11V9.33a.79.79 0 01.83-.83h4.17a.79.79 0 01.83.83zM8.33 11a1.49 1.49 0 01-1.67 1.67H3.33a.79.79 0 01-.83-.83V9.33a.79.79 0 01.83-.83H7.5a.79.79 0 01.83.83zM0 6.2v6.28a.2.2 0 00.2.2h1.72a1.61 1.61 0 001.42.83h3.33A2.46 2.46 0 009.13 12a.19.19 0 01.18-.13h1.39a.19.19 0 01.18.13 2.46 2.46 0 002.46 1.53h3.33c.55 0 1.1 0 1.37-.7a.2.2 0 01.18-.13h1.58a.2.2 0 00.2-.2V6.2a.2.2 0 00-.2-.2H.2a.2.2 0 00-.2.2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-visionSimulator,
.mw-ui-icon-visionSimulator-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-accessibility&image=visionSimulator&variant=progressive&format=rasterized&skin=vector&version=z9itd);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Evision simulator%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M17.5 11.83a.79.79 0 01-.83.83h-3.34A1.49 1.49 0 0111.67 11V9.33a.79.79 0 01.83-.83h4.17a.79.79 0 01.83.83zM8.33 11a1.49 1.49 0 01-1.67 1.67H3.33a.79.79 0 01-.83-.83V9.33a.79.79 0 01.83-.83H7.5a.79.79 0 01.83.83zM0 6.2v6.28a.2.2 0 00.2.2h1.72a1.61 1.61 0 001.42.83h3.33A2.46 2.46 0 009.13 12a.19.19 0 01.18-.13h1.39a.19.19 0 01.18.13 2.46 2.46 0 002.46 1.53h3.33c.55 0 1.1 0 1.37-.7a.2.2 0 01.18-.13h1.58a.2.2 0 00.2-.2V6.2a.2.2 0 00-.2-.2H.2a.2.2 0 00-.2.2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-alert,
.mw-ui-icon-alert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=alert&format=rasterized&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ealert%3C/title%3E%3Cpath d=%22M11.53 2.3A1.85 1.85 0 0010 1.21 1.85 1.85 0 008.48 2.3L.36 16.36C-.48 17.81.21 19 1.88 19h16.24c1.67 0 2.36-1.19 1.52-2.64zM11 16H9v-2h2zm0-4H9V6h2z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-alert,
.mw-ui-icon-alert-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=alert&variant=invert&format=rasterized&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ealert%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M11.53 2.3A1.85 1.85 0 0010 1.21 1.85 1.85 0 008.48 2.3L.36 16.36C-.48 17.81.21 19 1.88 19h16.24c1.67 0 2.36-1.19 1.52-2.64zM11 16H9v-2h2zm0-4H9V6h2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-alert,
.mw-ui-icon-alert-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=alert&variant=progressive&format=rasterized&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ealert%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M11.53 2.3A1.85 1.85 0 0010 1.21 1.85 1.85 0 008.48 2.3L.36 16.36C-.48 17.81.21 19 1.88 19h16.24c1.67 0 2.36-1.19 1.52-2.64zM11 16H9v-2h2zm0-4H9V6h2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-warning.oo-ui-icon-alert,
.mw-ui-icon-alert-warning:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=alert&variant=warning&format=rasterized&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ealert%3C/title%3E%3Cg fill=%22%23fc3%22%3E%3Cpath d=%22M11.53 2.3A1.85 1.85 0 0010 1.21 1.85 1.85 0 008.48 2.3L.36 16.36C-.48 17.81.21 19 1.88 19h16.24c1.67 0 2.36-1.19 1.52-2.64zM11 16H9v-2h2zm0-4H9V6h2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-bell,
.mw-ui-icon-bell:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=bell&format=rasterized&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ebell%3C/title%3E%3Cpath d=%22M16 7a5.38 5.38 0 00-4.46-4.85C11.6 1.46 11.53 0 10 0S8.4 1.46 8.46 2.15A5.38 5.38 0 004 7v6l-2 2v1h16v-1l-2-2zm-6 13a3 3 0 003-3H7a3 3 0 003 3z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-bell,
.mw-ui-icon-bell-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=bell&variant=invert&format=rasterized&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ebell%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M16 7a5.38 5.38 0 00-4.46-4.85C11.6 1.46 11.53 0 10 0S8.4 1.46 8.46 2.15A5.38 5.38 0 004 7v6l-2 2v1h16v-1l-2-2zm-6 13a3 3 0 003-3H7a3 3 0 003 3z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-bell,
.mw-ui-icon-bell-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=bell&variant=progressive&format=rasterized&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ebell%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M16 7a5.38 5.38 0 00-4.46-4.85C11.6 1.46 11.53 0 10 0S8.4 1.46 8.46 2.15A5.38 5.38 0 004 7v6l-2 2v1h16v-1l-2-2zm-6 13a3 3 0 003-3H7a3 3 0 003 3z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-bellOutline,
.mw-ui-icon-bellOutline:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=bellOutline&format=rasterized&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ebell%3C/title%3E%3Cpath d=%22M11.5 2.19C14.09 2.86 16 5.2 16 8v6l2 2v1H2v-1l2-2V8c0-2.8 1.91-5.14 4.5-5.81V1.5C8.5.67 9.17 0 10 0s1.5.67 1.5 1.5v.69zM10 4C7.79 4 6 5.79 6 8v7h8V8c0-2.21-1.79-4-4-4zM8 18h4c0 1.1-.9 2-2 2s-2-.9-2-2z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-bellOutline,
.mw-ui-icon-bellOutline-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=bellOutline&variant=invert&format=rasterized&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ebell%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M11.5 2.19C14.09 2.86 16 5.2 16 8v6l2 2v1H2v-1l2-2V8c0-2.8 1.91-5.14 4.5-5.81V1.5C8.5.67 9.17 0 10 0s1.5.67 1.5 1.5v.69zM10 4C7.79 4 6 5.79 6 8v7h8V8c0-2.21-1.79-4-4-4zM8 18h4c0 1.1-.9 2-2 2s-2-.9-2-2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-bellOutline,
.mw-ui-icon-bellOutline-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=bellOutline&variant=progressive&format=rasterized&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ebell%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M11.5 2.19C14.09 2.86 16 5.2 16 8v6l2 2v1H2v-1l2-2V8c0-2.8 1.91-5.14 4.5-5.81V1.5C8.5.67 9.17 0 10 0s1.5.67 1.5 1.5v.69zM10 4C7.79 4 6 5.79 6 8v7h8V8c0-2.21-1.79-4-4-4zM8 18h4c0 1.1-.9 2-2 2s-2-.9-2-2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-error,
.mw-ui-icon-error:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=error&format=rasterized&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eerror%3C/title%3E%3Cpath d=%22M13.728 1H6.272L1 6.272v7.456L6.272 19h7.456L19 13.728V6.272zM11 15H9v-2h2zm0-4H9V5h2z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-error,
.mw-ui-icon-error-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=error&variant=invert&format=rasterized&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eerror%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M13.728 1H6.272L1 6.272v7.456L6.272 19h7.456L19 13.728V6.272zM11 15H9v-2h2zm0-4H9V5h2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-error,
.mw-ui-icon-error-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=error&variant=progressive&format=rasterized&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eerror%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M13.728 1H6.272L1 6.272v7.456L6.272 19h7.456L19 13.728V6.272zM11 15H9v-2h2zm0-4H9V5h2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-error.oo-ui-icon-error,
.mw-ui-icon-error-error:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=error&variant=error&format=rasterized&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eerror%3C/title%3E%3Cg fill=%22%23d33%22%3E%3Cpath d=%22M13.728 1H6.272L1 6.272v7.456L6.272 19h7.456L19 13.728V6.272zM11 15H9v-2h2zm0-4H9V5h2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-message,
.mw-ui-icon-message:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=message&format=rasterized&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Emessage%3C/title%3E%3Cpath d=%22M0 8v8a2 2 0 002 2h16a2 2 0 002-2V8l-10 4z%22/%3E%3Cpath d=%22M2 2a2 2 0 00-2 2v2l10 4 10-4V4a2 2 0 00-2-2z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-message,
.mw-ui-icon-message-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=message&variant=invert&format=rasterized&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Emessage%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M0 8v8a2 2 0 002 2h16a2 2 0 002-2V8l-10 4z%22/%3E%3Cpath d=%22M2 2a2 2 0 00-2 2v2l10 4 10-4V4a2 2 0 00-2-2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-message,
.mw-ui-icon-message-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=message&variant=progressive&format=rasterized&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Emessage%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M0 8v8a2 2 0 002 2h16a2 2 0 002-2V8l-10 4z%22/%3E%3Cpath d=%22M2 2a2 2 0 00-2 2v2l10 4 10-4V4a2 2 0 00-2-2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-notice,
.mw-ui-icon-notice:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=notice&format=rasterized&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Enotice%3C/title%3E%3Cpath d=%22M10 0a10 10 0 1010 10A10 10 0 0010 0zm1 16H9v-2h2zm0-4H9V4h2z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-notice,
.mw-ui-icon-notice-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=notice&variant=invert&format=rasterized&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Enotice%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M10 0a10 10 0 1010 10A10 10 0 0010 0zm1 16H9v-2h2zm0-4H9V4h2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-notice,
.mw-ui-icon-notice-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=notice&variant=progressive&format=rasterized&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Enotice%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M10 0a10 10 0 1010 10A10 10 0 0010 0zm1 16H9v-2h2zm0-4H9V4h2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-speechBubble,
.mw-ui-icon-speechBubble:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=speechBubble&format=rasterized&lang=fr&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Espeech bubble%3C/title%3E%3Cpath d=%22M6 14H0v6z%22/%3E%3Crect width=%2220%22 height=%2216%22 rx=%222%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-speechBubble,
.mw-ui-icon-speechBubble-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=speechBubble&variant=invert&format=rasterized&lang=fr&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Espeech bubble%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M6 14H0v6z%22/%3E%3Crect width=%2220%22 height=%2216%22 rx=%222%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-speechBubble,
.mw-ui-icon-speechBubble-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=speechBubble&variant=progressive&format=rasterized&lang=fr&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Espeech bubble%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M6 14H0v6z%22/%3E%3Crect width=%2220%22 height=%2216%22 rx=%222%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-speechBubbleAdd,
.mw-ui-icon-speechBubbleAdd:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=speechBubbleAdd&format=rasterized&lang=fr&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eadd speech bubble%3C/title%3E%3Cpath d=%22M3 1a2 2 0 00-2 2v16l4-4h12a2 2 0 002-2V3a2 2 0 00-2-2zm12 8h-4v4H9V9H5V7h4V3h2v4h4z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-speechBubbleAdd,
.mw-ui-icon-speechBubbleAdd-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=speechBubbleAdd&variant=invert&format=rasterized&lang=fr&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eadd speech bubble%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M3 1a2 2 0 00-2 2v16l4-4h12a2 2 0 002-2V3a2 2 0 00-2-2zm12 8h-4v4H9V9H5V7h4V3h2v4h4z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-speechBubbleAdd,
.mw-ui-icon-speechBubbleAdd-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=speechBubbleAdd&variant=progressive&format=rasterized&lang=fr&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eadd speech bubble%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M3 1a2 2 0 00-2 2v16l4-4h12a2 2 0 002-2V3a2 2 0 00-2-2zm12 8h-4v4H9V9H5V7h4V3h2v4h4z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-speechBubbles,
.mw-ui-icon-speechBubbles:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=speechBubbles&format=rasterized&lang=fr&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Espeech bubbles%3C/title%3E%3Cpath d=%22M17 4v7a2 2 0 01-2 2H4v1a2 2 0 002 2h10l4 4V6a2 2 0 00-2-2zM6 10H0v6z%22/%3E%3Crect width=%2216%22 height=%2212%22 rx=%222%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-speechBubbles,
.mw-ui-icon-speechBubbles-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=speechBubbles&variant=invert&format=rasterized&lang=fr&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Espeech bubbles%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M17 4v7a2 2 0 01-2 2H4v1a2 2 0 002 2h10l4 4V6a2 2 0 00-2-2zM6 10H0v6z%22/%3E%3Crect width=%2216%22 height=%2212%22 rx=%222%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-speechBubbles,
.mw-ui-icon-speechBubbles-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=speechBubbles&variant=progressive&format=rasterized&lang=fr&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Espeech bubbles%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M17 4v7a2 2 0 01-2 2H4v1a2 2 0 002 2h10l4 4V6a2 2 0 00-2-2zM6 10H0v6z%22/%3E%3Crect width=%2216%22 height=%2212%22 rx=%222%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-tray,
.mw-ui-icon-tray:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=tray&format=rasterized&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etray%3C/title%3E%3Cpath d=%22M3 1a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2V3a2 2 0 00-2-2zm14 12h-4l-1 2H8l-1-2H3V3h14z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-tray,
.mw-ui-icon-tray-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=tray&variant=invert&format=rasterized&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etray%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M3 1a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2V3a2 2 0 00-2-2zm14 12h-4l-1 2H8l-1-2H3V3h14z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-tray,
.mw-ui-icon-tray-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-alerts&image=tray&variant=progressive&format=rasterized&skin=vector&version=1b2qj);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etray%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M3 1a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2V3a2 2 0 00-2-2zm14 12h-4l-1 2H8l-1-2H3V3h14z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-alignCenter,
.mw-ui-icon-alignCenter:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=alignCenter&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ealign center%3C/title%3E%3Cpath d=%22M1 15h18v2H1zM1 3h18v2H1z%22/%3E%3Crect width=%228%22 height=%226%22 x=%226%22 y=%227%22 rx=%221%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-alignCenter,
.mw-ui-icon-alignCenter-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=alignCenter&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ealign center%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M1 15h18v2H1zM1 3h18v2H1z%22/%3E%3Crect width=%228%22 height=%226%22 x=%226%22 y=%227%22 rx=%221%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-alignCenter,
.mw-ui-icon-alignCenter-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=alignCenter&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ealign center%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M1 15h18v2H1zM1 3h18v2H1z%22/%3E%3Crect width=%228%22 height=%226%22 x=%226%22 y=%227%22 rx=%221%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-alignLeft,
.mw-ui-icon-alignLeft:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=alignLeft&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ealign left%3C/title%3E%3Cpath d=%22M1 15h18v2H1zm11-8h7v2h-7zm0 4h7v2h-7zM1 3h18v2H1z%22/%3E%3Crect width=%228%22 height=%226%22 x=%221%22 y=%227%22 rx=%221%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-alignLeft,
.mw-ui-icon-alignLeft-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=alignLeft&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ealign left%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M1 15h18v2H1zm11-8h7v2h-7zm0 4h7v2h-7zM1 3h18v2H1z%22/%3E%3Crect width=%228%22 height=%226%22 x=%221%22 y=%227%22 rx=%221%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-alignLeft,
.mw-ui-icon-alignLeft-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=alignLeft&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ealign left%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M1 15h18v2H1zm11-8h7v2h-7zm0 4h7v2h-7zM1 3h18v2H1z%22/%3E%3Crect width=%228%22 height=%226%22 x=%221%22 y=%227%22 rx=%221%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-alignRight,
.mw-ui-icon-alignRight:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=alignRight&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ealign right%3C/title%3E%3Cpath d=%22M1 15h18v2H1zm0-8h7v2H1zm0 4h7v2H1zm0-8h18v2H1z%22/%3E%3Crect width=%228%22 height=%226%22 x=%2211%22 y=%227%22 rx=%221%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-alignRight,
.mw-ui-icon-alignRight-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=alignRight&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ealign right%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M1 15h18v2H1zm0-8h7v2H1zm0 4h7v2H1zm0-8h18v2H1z%22/%3E%3Crect width=%228%22 height=%226%22 x=%2211%22 y=%227%22 rx=%221%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-alignRight,
.mw-ui-icon-alignRight-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=alignRight&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ealign right%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M1 15h18v2H1zm0-8h7v2H1zm0 4h7v2H1zm0-8h18v2H1z%22/%3E%3Crect width=%228%22 height=%226%22 x=%2211%22 y=%227%22 rx=%221%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-attachment,
.mw-ui-icon-attachment:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=attachment&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eattachment%3C/title%3E%3Cpath d=%22M9.5 19.75a4.25 4.25 0 01-4.25-4.25V9a2.75 2.75 0 015.5 0v6h-1.5V9a1.25 1.25 0 00-2.5 0v6.5a2.75 2.75 0 005.5 0V4a2.25 2.25 0 00-4.5 0v1h-1.5V4a3.75 3.75 0 017.5 0v11.5a4.25 4.25 0 01-4.25 4.25z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-attachment,
.mw-ui-icon-attachment-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=attachment&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eattachment%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M9.5 19.75a4.25 4.25 0 01-4.25-4.25V9a2.75 2.75 0 015.5 0v6h-1.5V9a1.25 1.25 0 00-2.5 0v6.5a2.75 2.75 0 005.5 0V4a2.25 2.25 0 00-4.5 0v1h-1.5V4a3.75 3.75 0 017.5 0v11.5a4.25 4.25 0 01-4.25 4.25z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-attachment,
.mw-ui-icon-attachment-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=attachment&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eattachment%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M9.5 19.75a4.25 4.25 0 01-4.25-4.25V9a2.75 2.75 0 015.5 0v6h-1.5V9a1.25 1.25 0 00-2.5 0v6.5a2.75 2.75 0 005.5 0V4a2.25 2.25 0 00-4.5 0v1h-1.5V4a3.75 3.75 0 017.5 0v11.5a4.25 4.25 0 01-4.25 4.25z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-calendar,
.mw-ui-icon-calendar:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=calendar&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ecalendar%3C/title%3E%3Cpath d=%22M15 3V1h-2v2H7V1H5v2H2a2 2 0 00-2 2v12a2 2 0 002 2h16a2 2 0 002-2V5a2 2 0 00-2-2zm3 14H2V8h16zm-2-6h-4v4h4z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-calendar,
.mw-ui-icon-calendar-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=calendar&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ecalendar%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M15 3V1h-2v2H7V1H5v2H2a2 2 0 00-2 2v12a2 2 0 002 2h16a2 2 0 002-2V5a2 2 0 00-2-2zm3 14H2V8h16zm-2-6h-4v4h4z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-calendar,
.mw-ui-icon-calendar-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=calendar&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ecalendar%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M15 3V1h-2v2H7V1H5v2H2a2 2 0 00-2 2v12a2 2 0 002 2h16a2 2 0 002-2V5a2 2 0 00-2-2zm3 14H2V8h16zm-2-6h-4v4h4z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-code,
.mw-ui-icon-code:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=code&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 xmlns:xlink=%22http://www.w3.org/1999/xlink%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ecode%3C/title%3E%3Cpath id=%22a%22 d=%22M1 10.08V8.92h1.15c1.15 0 1.15 0 1.15-1.15V5a7.42 7.42 0 01.09-1.3 2 2 0 01.3-.7 1.84 1.84 0 01.93-.68A6.44 6.44 0 016.74 2h1.18v1.15h-.86A1.32 1.32 0 006 3.62a1.71 1.71 0 00-.36 1.23V7a3.22 3.22 0 01-.28 1.72 2 2 0 01-1.26.77 2.15 2.15 0 011.26.79A3.26 3.26 0 015.62 12v3.15A1.67 1.67 0 006 16.37a1.31 1.31 0 001.08.47h.87V18H6.74a6.3 6.3 0 01-2.12-.29 1.82 1.82 0 01-.93-.71 1.94 1.94 0 01-.3-.72A7.46 7.46 0 013.31 15v-3.77c0-1.15 0-1.15-1.15-1.15zm18 0V8.92h-1.15c-1.15 0-1.15 0-1.15-1.15V5a7.42 7.42 0 00-.08-1.32 2 2 0 00-.3-.73 1.84 1.84 0 00-.93-.68A6.44 6.44 0 0013.26 2h-1.18v1.15h.87a1.32 1.32 0 011.05.47 1.71 1.71 0 01.36 1.23V7a3.22 3.22 0 00.28 1.72 2 2 0 001.26.77 2.15 2.15 0 00-1.26.79 3.26 3.26 0 00-.26 1.72v3.15a1.67 1.67 0 01-.38 1.22 1.31 1.31 0 01-1.08.47h-.87V18h1.19a6.3 6.3 0 002.12-.29 1.82 1.82 0 00.93-.68 1.94 1.94 0 00.3-.72 7.46 7.46 0 00.1-1.31v-3.77c0-1.15 0-1.15 1.15-1.15z%22/%3E%3Cuse transform=%22matrix%28-1 0 0 1 20 0%29%22 xlink:href=%22%23a%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-code,
.mw-ui-icon-code-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=code&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 xmlns:xlink=%22http://www.w3.org/1999/xlink%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ecode%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath id=%22a%22 d=%22M1 10.08V8.92h1.15c1.15 0 1.15 0 1.15-1.15V5a7.42 7.42 0 01.09-1.3 2 2 0 01.3-.7 1.84 1.84 0 01.93-.68A6.44 6.44 0 016.74 2h1.18v1.15h-.86A1.32 1.32 0 006 3.62a1.71 1.71 0 00-.36 1.23V7a3.22 3.22 0 01-.28 1.72 2 2 0 01-1.26.77 2.15 2.15 0 011.26.79A3.26 3.26 0 015.62 12v3.15A1.67 1.67 0 006 16.37a1.31 1.31 0 001.08.47h.87V18H6.74a6.3 6.3 0 01-2.12-.29 1.82 1.82 0 01-.93-.71 1.94 1.94 0 01-.3-.72A7.46 7.46 0 013.31 15v-3.77c0-1.15 0-1.15-1.15-1.15zm18 0V8.92h-1.15c-1.15 0-1.15 0-1.15-1.15V5a7.42 7.42 0 00-.08-1.32 2 2 0 00-.3-.73 1.84 1.84 0 00-.93-.68A6.44 6.44 0 0013.26 2h-1.18v1.15h.87a1.32 1.32 0 011.05.47 1.71 1.71 0 01.36 1.23V7a3.22 3.22 0 00.28 1.72 2 2 0 001.26.77 2.15 2.15 0 00-1.26.79 3.26 3.26 0 00-.26 1.72v3.15a1.67 1.67 0 01-.38 1.22 1.31 1.31 0 01-1.08.47h-.87V18h1.19a6.3 6.3 0 002.12-.29 1.82 1.82 0 00.93-.68 1.94 1.94 0 00.3-.72 7.46 7.46 0 00.1-1.31v-3.77c0-1.15 0-1.15 1.15-1.15z%22/%3E%3Cuse xmlns:xlink=%22http://www.w3.org/1999/xlink%22 transform=%22matrix%28-1 0 0 1 20 0%29%22 xlink:href=%22%23a%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-code,
.mw-ui-icon-code-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=code&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 xmlns:xlink=%22http://www.w3.org/1999/xlink%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ecode%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath id=%22a%22 d=%22M1 10.08V8.92h1.15c1.15 0 1.15 0 1.15-1.15V5a7.42 7.42 0 01.09-1.3 2 2 0 01.3-.7 1.84 1.84 0 01.93-.68A6.44 6.44 0 016.74 2h1.18v1.15h-.86A1.32 1.32 0 006 3.62a1.71 1.71 0 00-.36 1.23V7a3.22 3.22 0 01-.28 1.72 2 2 0 01-1.26.77 2.15 2.15 0 011.26.79A3.26 3.26 0 015.62 12v3.15A1.67 1.67 0 006 16.37a1.31 1.31 0 001.08.47h.87V18H6.74a6.3 6.3 0 01-2.12-.29 1.82 1.82 0 01-.93-.71 1.94 1.94 0 01-.3-.72A7.46 7.46 0 013.31 15v-3.77c0-1.15 0-1.15-1.15-1.15zm18 0V8.92h-1.15c-1.15 0-1.15 0-1.15-1.15V5a7.42 7.42 0 00-.08-1.32 2 2 0 00-.3-.73 1.84 1.84 0 00-.93-.68A6.44 6.44 0 0013.26 2h-1.18v1.15h.87a1.32 1.32 0 011.05.47 1.71 1.71 0 01.36 1.23V7a3.22 3.22 0 00.28 1.72 2 2 0 001.26.77 2.15 2.15 0 00-1.26.79 3.26 3.26 0 00-.26 1.72v3.15a1.67 1.67 0 01-.38 1.22 1.31 1.31 0 01-1.08.47h-.87V18h1.19a6.3 6.3 0 002.12-.29 1.82 1.82 0 00.93-.68 1.94 1.94 0 00.3-.72 7.46 7.46 0 00.1-1.31v-3.77c0-1.15 0-1.15 1.15-1.15z%22/%3E%3Cuse xmlns:xlink=%22http://www.w3.org/1999/xlink%22 transform=%22matrix%28-1 0 0 1 20 0%29%22 xlink:href=%22%23a%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-hieroglyph,
.mw-ui-icon-hieroglyph:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=hieroglyph&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ehieroglyph%3C/title%3E%3Cpath d=%22M15 11h-3.75l2.55-3.4a4.75 4.75 0 10-7.6 0L8.75 11H5v2h4v7h2v-7h4zM7.54 3.52A2.75 2.75 0 1112.2 6.4L10 9.33 7.8 6.4a2.69 2.69 0 01-.26-2.88z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-hieroglyph,
.mw-ui-icon-hieroglyph-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=hieroglyph&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ehieroglyph%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M15 11h-3.75l2.55-3.4a4.75 4.75 0 10-7.6 0L8.75 11H5v2h4v7h2v-7h4zM7.54 3.52A2.75 2.75 0 1112.2 6.4L10 9.33 7.8 6.4a2.69 2.69 0 01-.26-2.88z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-hieroglyph,
.mw-ui-icon-hieroglyph-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=hieroglyph&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Ehieroglyph%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M15 11h-3.75l2.55-3.4a4.75 4.75 0 10-7.6 0L8.75 11H5v2h4v7h2v-7h4zM7.54 3.52A2.75 2.75 0 1112.2 6.4L10 9.33 7.8 6.4a2.69 2.69 0 01-.26-2.88z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-imageLayoutBasic,
.mw-ui-icon-imageLayoutBasic:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=imageLayoutBasic&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eimage layout basic%3C/title%3E%3Cpath d=%22M1 3v14h18V3zm17 13H2V4h16z%22/%3E%3Cpath d=%22M8.58 14h.81l3.11-4 3 4H17l-4.5-6L9 12.51 6.5 9.5 3 14h1.56l1.94-2.5z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-imageLayoutBasic,
.mw-ui-icon-imageLayoutBasic-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=imageLayoutBasic&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eimage layout basic%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M1 3v14h18V3zm17 13H2V4h16z%22/%3E%3Cpath d=%22M8.58 14h.81l3.11-4 3 4H17l-4.5-6L9 12.51 6.5 9.5 3 14h1.56l1.94-2.5z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-imageLayoutBasic,
.mw-ui-icon-imageLayoutBasic-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=imageLayoutBasic&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eimage layout basic%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M1 3v14h18V3zm17 13H2V4h16z%22/%3E%3Cpath d=%22M8.58 14h.81l3.11-4 3 4H17l-4.5-6L9 12.51 6.5 9.5 3 14h1.56l1.94-2.5z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-imageLayoutFrame,
.mw-ui-icon-imageLayoutFrame:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=imageLayoutFrame&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eimage layout frame%3C/title%3E%3Cpath d=%22M3 2a2 2 0 00-2 2v12a2 2 0 002 2h14a2 2 0 002-2V4a2 2 0 00-2-2zm0 15a1 1 0 01-1-1V4a1 1 0 011-1h14a1 1 0 011 1v12a1 1 0 01-1 1z%22/%3E%3Cpath d=%22M17 4H3v12h14zM5 13l2.5-3 2 2L12 9l3 4z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-imageLayoutFrame,
.mw-ui-icon-imageLayoutFrame-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=imageLayoutFrame&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eimage layout frame%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M3 2a2 2 0 00-2 2v12a2 2 0 002 2h14a2 2 0 002-2V4a2 2 0 00-2-2zm0 15a1 1 0 01-1-1V4a1 1 0 011-1h14a1 1 0 011 1v12a1 1 0 01-1 1z%22/%3E%3Cpath d=%22M17 4H3v12h14zM5 13l2.5-3 2 2L12 9l3 4z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-imageLayoutFrame,
.mw-ui-icon-imageLayoutFrame-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=imageLayoutFrame&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eimage layout frame%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M3 2a2 2 0 00-2 2v12a2 2 0 002 2h14a2 2 0 002-2V4a2 2 0 00-2-2zm0 15a1 1 0 01-1-1V4a1 1 0 011-1h14a1 1 0 011 1v12a1 1 0 01-1 1z%22/%3E%3Cpath d=%22M17 4H3v12h14zM5 13l2.5-3 2 2L12 9l3 4z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-imageLayoutFrameless,
.mw-ui-icon-imageLayoutFrameless:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=imageLayoutFrameless&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eimage layout frameless%3C/title%3E%3Cpath d=%22M19 3H1v14h18zM3 14l3.5-4.5 2.5 3L12.5 8l4.5 6z%22/%3E%3Cpath d=%22M19 5H1V3h18zm0 12H1v-2h18z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-imageLayoutFrameless,
.mw-ui-icon-imageLayoutFrameless-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=imageLayoutFrameless&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eimage layout frameless%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M19 3H1v14h18zM3 14l3.5-4.5 2.5 3L12.5 8l4.5 6z%22/%3E%3Cpath d=%22M19 5H1V3h18zm0 12H1v-2h18z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-imageLayoutFrameless,
.mw-ui-icon-imageLayoutFrameless-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=imageLayoutFrameless&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eimage layout frameless%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M19 3H1v14h18zM3 14l3.5-4.5 2.5 3L12.5 8l4.5 6z%22/%3E%3Cpath d=%22M19 5H1V3h18zm0 12H1v-2h18z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-imageLayoutThumbnail,
.mw-ui-icon-imageLayoutThumbnail:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=imageLayoutThumbnail&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eimage layout thumbnail%3C/title%3E%3Cpath d=%22M3 2a2 2 0 00-2 2v12a2 2 0 002 2h14a2 2 0 002-2V4a2 2 0 00-2-2zm0 15a1 1 0 01-1-1V4a1 1 0 011-1h14a1 1 0 011 1v12a1 1 0 01-1 1z%22/%3E%3Cpath d=%22M17 4H3v10h14zM5 12l2.5-3 2 2L12 8l3 4zm-1 3h12v1H4z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-imageLayoutThumbnail,
.mw-ui-icon-imageLayoutThumbnail-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=imageLayoutThumbnail&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eimage layout thumbnail%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M3 2a2 2 0 00-2 2v12a2 2 0 002 2h14a2 2 0 002-2V4a2 2 0 00-2-2zm0 15a1 1 0 01-1-1V4a1 1 0 011-1h14a1 1 0 011 1v12a1 1 0 01-1 1z%22/%3E%3Cpath d=%22M17 4H3v10h14zM5 12l2.5-3 2 2L12 8l3 4zm-1 3h12v1H4z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-imageLayoutThumbnail,
.mw-ui-icon-imageLayoutThumbnail-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=imageLayoutThumbnail&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eimage layout thumbnail%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M3 2a2 2 0 00-2 2v12a2 2 0 002 2h14a2 2 0 002-2V4a2 2 0 00-2-2zm0 15a1 1 0 01-1-1V4a1 1 0 011-1h14a1 1 0 011 1v12a1 1 0 01-1 1z%22/%3E%3Cpath d=%22M17 4H3v10h14zM5 12l2.5-3 2 2L12 8l3 4zm-1 3h12v1H4z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-labFlask,
.mw-ui-icon-labFlask:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=labFlask&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Elaboratory flask%3C/title%3E%3Cpath d=%22M13 7.61V3h1V1H6v2h1v4.61l-5.86 9.88A1 1 0 002 19h16a1 1 0 00.86-1.51zm-4.2.88a1 1 0 00.2-.6V3h2v4.89a1 1 0 00.14.51l2.14 3.6H6.72z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-labFlask,
.mw-ui-icon-labFlask-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=labFlask&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Elaboratory flask%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M13 7.61V3h1V1H6v2h1v4.61l-5.86 9.88A1 1 0 002 19h16a1 1 0 00.86-1.51zm-4.2.88a1 1 0 00.2-.6V3h2v4.89a1 1 0 00.14.51l2.14 3.6H6.72z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-labFlask,
.mw-ui-icon-labFlask-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=labFlask&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Elaboratory flask%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M13 7.61V3h1V1H6v2h1v4.61l-5.86 9.88A1 1 0 002 19h16a1 1 0 00.86-1.51zm-4.2.88a1 1 0 00.2-.6V3h2v4.89a1 1 0 00.14.51l2.14 3.6H6.72z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-language,
.mw-ui-icon-language:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=language&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Elanguage%3C/title%3E%3Cpath d=%22M20 18h-1.44a.61.61 0 01-.4-.12.81.81 0 01-.23-.31L17 15h-5l-1 2.54a.77.77 0 01-.22.3.59.59 0 01-.4.14H9l4.55-11.47h1.89zm-3.53-4.31L14.89 9.5a11.62 11.62 0 01-.39-1.24q-.09.37-.19.69l-.19.56-1.58 4.19zm-6.3-1.58a13.43 13.43 0 01-2.91-1.41 11.46 11.46 0 002.81-5.37H12V4H7.31a4 4 0 00-.2-.56C6.87 2.79 6.6 2 6.6 2l-1.47.5s.4.89.6 1.5H0v1.33h2.15A11.23 11.23 0 005 10.7a17.19 17.19 0 01-5 2.1q.56.82.87 1.38a23.28 23.28 0 005.22-2.51 15.64 15.64 0 003.56 1.77zM3.63 5.33h4.91a8.11 8.11 0 01-2.45 4.45 9.11 9.11 0 01-2.46-4.45z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-language,
.mw-ui-icon-language-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=language&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Elanguage%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M20 18h-1.44a.61.61 0 01-.4-.12.81.81 0 01-.23-.31L17 15h-5l-1 2.54a.77.77 0 01-.22.3.59.59 0 01-.4.14H9l4.55-11.47h1.89zm-3.53-4.31L14.89 9.5a11.62 11.62 0 01-.39-1.24q-.09.37-.19.69l-.19.56-1.58 4.19zm-6.3-1.58a13.43 13.43 0 01-2.91-1.41 11.46 11.46 0 002.81-5.37H12V4H7.31a4 4 0 00-.2-.56C6.87 2.79 6.6 2 6.6 2l-1.47.5s.4.89.6 1.5H0v1.33h2.15A11.23 11.23 0 005 10.7a17.19 17.19 0 01-5 2.1q.56.82.87 1.38a23.28 23.28 0 005.22-2.51 15.64 15.64 0 003.56 1.77zM3.63 5.33h4.91a8.11 8.11 0 01-2.45 4.45 9.11 9.11 0 01-2.46-4.45z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-language,
.mw-ui-icon-language-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=language&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Elanguage%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M20 18h-1.44a.61.61 0 01-.4-.12.81.81 0 01-.23-.31L17 15h-5l-1 2.54a.77.77 0 01-.22.3.59.59 0 01-.4.14H9l4.55-11.47h1.89zm-3.53-4.31L14.89 9.5a11.62 11.62 0 01-.39-1.24q-.09.37-.19.69l-.19.56-1.58 4.19zm-6.3-1.58a13.43 13.43 0 01-2.91-1.41 11.46 11.46 0 002.81-5.37H12V4H7.31a4 4 0 00-.2-.56C6.87 2.79 6.6 2 6.6 2l-1.47.5s.4.89.6 1.5H0v1.33h2.15A11.23 11.23 0 005 10.7a17.19 17.19 0 01-5 2.1q.56.82.87 1.38a23.28 23.28 0 005.22-2.51 15.64 15.64 0 003.56 1.77zM3.63 5.33h4.91a8.11 8.11 0 01-2.45 4.45 9.11 9.11 0 01-2.46-4.45z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-layout,
.mw-ui-icon-layout:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=layout&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Elayout%3C/title%3E%3Cpath d=%22M8 12V1H1v18h18v-7z%22/%3E%3Cpath d=%22M11 1v8h8V1zm6 6h-4V3h4z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-layout,
.mw-ui-icon-layout-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=layout&variant=invert&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Elayout%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M8 12V1H1v18h18v-7z%22/%3E%3Cpath d=%22M11 1v8h8V1zm6 6h-4V3h4z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-layout,
.mw-ui-icon-layout-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=layout&variant=progressive&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Elayout%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M8 12V1H1v18h18v-7z%22/%3E%3Cpath d=%22M11 1v8h8V1zm6 6h-4V3h4z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-markup,
.mw-ui-icon-markup:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=markup&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Emarkup%3C/title%3E%3Cpath d=%22M6.5 3.5L0 10l1.5 1.5 5 5L8 15l-5-5 5-5zm7 0L12 5l5 5-5 5 1.5 1.5L20 10z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-markup,
.mw-ui-icon-markup-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=markup&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Emarkup%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M6.5 3.5L0 10l1.5 1.5 5 5L8 15l-5-5 5-5zm7 0L12 5l5 5-5 5 1.5 1.5L20 10z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-markup,
.mw-ui-icon-markup-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=markup&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Emarkup%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M6.5 3.5L0 10l1.5 1.5 5 5L8 15l-5-5 5-5zm7 0L12 5l5 5-5 5 1.5 1.5L20 10z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-mathematics,
.mw-ui-icon-mathematics:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=mathematics&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Emathematics formula%3C/title%3E%3Cpath d=%22M14 2H4l5 8-5 8h12v-4h-2v2H8.25L12 10 8.25 4H14v2h2V2z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-mathematics,
.mw-ui-icon-mathematics-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=mathematics&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Emathematics formula%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M14 2H4l5 8-5 8h12v-4h-2v2H8.25L12 10 8.25 4H14v2h2V2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-mathematics,
.mw-ui-icon-mathematics-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=mathematics&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Emathematics formula%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M14 2H4l5 8-5 8h12v-4h-2v2H8.25L12 10 8.25 4H14v2h2V2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-mathematicsDisplayBlock,
.mw-ui-icon-mathematicsDisplayBlock:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=mathematicsDisplayBlock&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Emathematics formula displayed block%3C/title%3E%3Cpath d=%22M13 5H5l3 5-3 5h10v-3h-2v1H9.2l1.8-3-1.8-3H13v1h2V5zM2 1h16v2H2zm0 16h16v2H2z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-mathematicsDisplayBlock,
.mw-ui-icon-mathematicsDisplayBlock-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=mathematicsDisplayBlock&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Emathematics formula displayed block%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M13 5H5l3 5-3 5h10v-3h-2v1H9.2l1.8-3-1.8-3H13v1h2V5zM2 1h16v2H2zm0 16h16v2H2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-mathematicsDisplayBlock,
.mw-ui-icon-mathematicsDisplayBlock-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=mathematicsDisplayBlock&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Emathematics formula displayed block%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M13 5H5l3 5-3 5h10v-3h-2v1H9.2l1.8-3-1.8-3H13v1h2V5zM2 1h16v2H2zm0 16h16v2H2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-mathematicsDisplayDefault,
.mw-ui-icon-mathematicsDisplayDefault:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=mathematicsDisplayDefault&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Emathematics formula displayed default%3C/title%3E%3Cpath d=%22M12 5H4l3 5-3 5h10v-3h-2v1H8.2l1.8-3-1.8-3H12v1h2V5zM1 9h3v2H1zm15 0h3v2h-3z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-mathematicsDisplayDefault,
.mw-ui-icon-mathematicsDisplayDefault-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=mathematicsDisplayDefault&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Emathematics formula displayed default%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M12 5H4l3 5-3 5h10v-3h-2v1H8.2l1.8-3-1.8-3H12v1h2V5zM1 9h3v2H1zm15 0h3v2h-3z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-mathematicsDisplayDefault,
.mw-ui-icon-mathematicsDisplayDefault-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=mathematicsDisplayDefault&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Emathematics formula displayed default%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M12 5H4l3 5-3 5h10v-3h-2v1H8.2l1.8-3-1.8-3H12v1h2V5zM1 9h3v2H1zm15 0h3v2h-3z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-mathematicsDisplayInline,
.mw-ui-icon-mathematicsDisplayInline:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=mathematicsDisplayInline&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Emathematics formula displayed inline%3C/title%3E%3Cpath d=%22M4 13H0V7h4zm12-6h4v6h-4zM6 6l3 4-3 4h8v-3h-2v1H9.5l1.5-2-1.5-2H12v1h2V6z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-mathematicsDisplayInline,
.mw-ui-icon-mathematicsDisplayInline-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=mathematicsDisplayInline&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Emathematics formula displayed inline%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M4 13H0V7h4zm12-6h4v6h-4zM6 6l3 4-3 4h8v-3h-2v1H9.5l1.5-2-1.5-2H12v1h2V6z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-mathematicsDisplayInline,
.mw-ui-icon-mathematicsDisplayInline-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=mathematicsDisplayInline&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Emathematics formula displayed inline%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M4 13H0V7h4zm12-6h4v6h-4zM6 6l3 4-3 4h8v-3h-2v1H9.5l1.5-2-1.5-2H12v1h2V6z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-newline,
.mw-ui-icon-newline:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=newline&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Enewline%3C/title%3E%3Cpath d=%22M17 4v6H7V6l-6 5 6 5v-4h12V4z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-newline,
.mw-ui-icon-newline-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=newline&variant=invert&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Enewline%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M17 4v6H7V6l-6 5 6 5v-4h12V4z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-newline,
.mw-ui-icon-newline-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=newline&variant=progressive&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Enewline%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M17 4v6H7V6l-6 5 6 5v-4h12V4z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-noWikiText,
.mw-ui-icon-noWikiText:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=noWikiText&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eno WikiText%3C/title%3E%3Cpath d=%22M16 3v2h1v10l2 2V3zM9 5V3H5l2 2zM1 1L0 2l1 1v14h3v-2H3V5l2 2v10h4v-2H7V9l6 6h-2v2h4l3 3 1-1zm12 10l2 2V3h-4v2h2z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-noWikiText,
.mw-ui-icon-noWikiText-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=noWikiText&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eno WikiText%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M16 3v2h1v10l2 2V3zM9 5V3H5l2 2zM1 1L0 2l1 1v14h3v-2H3V5l2 2v10h4v-2H7V9l6 6h-2v2h4l3 3 1-1zm12 10l2 2V3h-4v2h2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-noWikiText,
.mw-ui-icon-noWikiText-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=noWikiText&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eno WikiText%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M16 3v2h1v10l2 2V3zM9 5V3H5l2 2zM1 1L0 2l1 1v14h3v-2H3V5l2 2v10h4v-2H7V9l6 6h-2v2h4l3 3 1-1zm12 10l2 2V3h-4v2h2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-outline,
.mw-ui-icon-outline:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=outline&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eoutline%3C/title%3E%3Cpath d=%22M1 12h18v7H1zM1 1v8h8V1zm6 6H3V3h4z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-outline,
.mw-ui-icon-outline-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=outline&variant=invert&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eoutline%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M1 12h18v7H1zM1 1v8h8V1zm6 6H3V3h4z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-outline,
.mw-ui-icon-outline-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=outline&variant=progressive&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eoutline%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M1 12h18v7H1zM1 1v8h8V1zm6 6H3V3h4z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-puzzle,
.mw-ui-icon-puzzle:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=puzzle&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Epuzzle%3C/title%3E%3Ccircle cx=%2217%22 cy=%2210%22 r=%223%22/%3E%3Cpath d=%22M10.58 3A3 3 0 0111 4.5a3 3 0 01-6 0A3 3 0 015.42 3H1v12a2 2 0 002 2h12V3z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-puzzle,
.mw-ui-icon-puzzle-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=puzzle&variant=invert&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Epuzzle%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Ccircle cx=%2217%22 cy=%2210%22 r=%223%22/%3E%3Cpath d=%22M10.58 3A3 3 0 0111 4.5a3 3 0 01-6 0A3 3 0 015.42 3H1v12a2 2 0 002 2h12V3z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-puzzle,
.mw-ui-icon-puzzle-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=puzzle&variant=progressive&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Epuzzle%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Ccircle cx=%2217%22 cy=%2210%22 r=%223%22/%3E%3Cpath d=%22M10.58 3A3 3 0 0111 4.5a3 3 0 01-6 0A3 3 0 015.42 3H1v12a2 2 0 002 2h12V3z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-quotes,
.mw-ui-icon-quotes:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=quotes&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Equotes%3C/title%3E%3Cpath d=%22M7 6l1-2H6C3.79 4 2 6.79 2 9v7h7V9H5c0-3 2-3 2-3zm7 3c0-3 2-3 2-3l1-2h-2c-2.21 0-4 2.79-4 5v7h7V9z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-quotes,
.mw-ui-icon-quotes-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=quotes&variant=invert&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Equotes%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M7 6l1-2H6C3.79 4 2 6.79 2 9v7h7V9H5c0-3 2-3 2-3zm7 3c0-3 2-3 2-3l1-2h-2c-2.21 0-4 2.79-4 5v7h7V9z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-quotes,
.mw-ui-icon-quotes-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=quotes&variant=progressive&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Equotes%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M7 6l1-2H6C3.79 4 2 6.79 2 9v7h7V9H5c0-3 2-3 2-3zm7 3c0-3 2-3 2-3l1-2h-2c-2.21 0-4 2.79-4 5v7h7V9z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-searchCaseSensitive,
.mw-ui-icon-searchCaseSensitive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=searchCaseSensitive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Esearch case sensitive%3C/title%3E%3Cpath d=%22M11.59 15.87h-1.52a.64.64 0 01-.42-.13.84.84 0 01-.24-.32l-1-2.67H3.18l-1 2.67a.8.8 0 01-.23.31.63.63 0 01-.42.14H0L4.8 3.76h2zm-3.72-4.54L6.2 6.91a12.12 12.12 0 01-.41-1.3q-.09.4-.2.73c-.07.22-.14.42-.2.58l-1.67 4.41zm5.58-2.84a4.91 4.91 0 013.46-1.35 3.41 3.41 0 011.32.24 2.62 2.62 0 011 .68 3 3 0 01.6 1 4.08 4.08 0 01.17 1.36v5.45h-.81a.78.78 0 01-.39-.08.61.61 0 01-.23-.32l-.18-.7a7.87 7.87 0 01-.65.53 4.12 4.12 0 01-.66.39 3.3 3.3 0 01-.73.24 4.3 4.3 0 01-.86.08 3.18 3.18 0 01-1-.14 2.12 2.12 0 01-.78-.43 2 2 0 01-.52-.72 2.48 2.48 0 01-.19-1 2 2 0 01.26-1 2.42 2.42 0 01.87-.85 5.66 5.66 0 011.6-.62 11.7 11.7 0 012.51-.25v-.57A2.06 2.06 0 0017.85 9a1.46 1.46 0 00-1.16-.45 2.53 2.53 0 00-.87.13 3.9 3.9 0 00-.62.32l-.46.28a.77.77 0 01-.43.13.52.52 0 01-.32-.1.81.81 0 01-.21-.24zm4.79 3.63a11.49 11.49 0 00-1.63.15 4.61 4.61 0 00-1.08.31 1.42 1.42 0 00-.59.45 1 1 0 00-.18.57 1.25 1.25 0 00.1.52.94.94 0 00.27.35 1.08 1.08 0 00.4.2 1.93 1.93 0 00.51.06 2.59 2.59 0 001.21-.27 3.79 3.79 0 001-.77z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-searchCaseSensitive,
.mw-ui-icon-searchCaseSensitive-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=searchCaseSensitive&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Esearch case sensitive%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M11.59 15.87h-1.52a.64.64 0 01-.42-.13.84.84 0 01-.24-.32l-1-2.67H3.18l-1 2.67a.8.8 0 01-.23.31.63.63 0 01-.42.14H0L4.8 3.76h2zm-3.72-4.54L6.2 6.91a12.12 12.12 0 01-.41-1.3q-.09.4-.2.73c-.07.22-.14.42-.2.58l-1.67 4.41zm5.58-2.84a4.91 4.91 0 013.46-1.35 3.41 3.41 0 011.32.24 2.62 2.62 0 011 .68 3 3 0 01.6 1 4.08 4.08 0 01.17 1.36v5.45h-.81a.78.78 0 01-.39-.08.61.61 0 01-.23-.32l-.18-.7a7.87 7.87 0 01-.65.53 4.12 4.12 0 01-.66.39 3.3 3.3 0 01-.73.24 4.3 4.3 0 01-.86.08 3.18 3.18 0 01-1-.14 2.12 2.12 0 01-.78-.43 2 2 0 01-.52-.72 2.48 2.48 0 01-.19-1 2 2 0 01.26-1 2.42 2.42 0 01.87-.85 5.66 5.66 0 011.6-.62 11.7 11.7 0 012.51-.25v-.57A2.06 2.06 0 0017.85 9a1.46 1.46 0 00-1.16-.45 2.53 2.53 0 00-.87.13 3.9 3.9 0 00-.62.32l-.46.28a.77.77 0 01-.43.13.52.52 0 01-.32-.1.81.81 0 01-.21-.24zm4.79 3.63a11.49 11.49 0 00-1.63.15 4.61 4.61 0 00-1.08.31 1.42 1.42 0 00-.59.45 1 1 0 00-.18.57 1.25 1.25 0 00.1.52.94.94 0 00.27.35 1.08 1.08 0 00.4.2 1.93 1.93 0 00.51.06 2.59 2.59 0 001.21-.27 3.79 3.79 0 001-.77z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-searchCaseSensitive,
.mw-ui-icon-searchCaseSensitive-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=searchCaseSensitive&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Esearch case sensitive%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M11.59 15.87h-1.52a.64.64 0 01-.42-.13.84.84 0 01-.24-.32l-1-2.67H3.18l-1 2.67a.8.8 0 01-.23.31.63.63 0 01-.42.14H0L4.8 3.76h2zm-3.72-4.54L6.2 6.91a12.12 12.12 0 01-.41-1.3q-.09.4-.2.73c-.07.22-.14.42-.2.58l-1.67 4.41zm5.58-2.84a4.91 4.91 0 013.46-1.35 3.41 3.41 0 011.32.24 2.62 2.62 0 011 .68 3 3 0 01.6 1 4.08 4.08 0 01.17 1.36v5.45h-.81a.78.78 0 01-.39-.08.61.61 0 01-.23-.32l-.18-.7a7.87 7.87 0 01-.65.53 4.12 4.12 0 01-.66.39 3.3 3.3 0 01-.73.24 4.3 4.3 0 01-.86.08 3.18 3.18 0 01-1-.14 2.12 2.12 0 01-.78-.43 2 2 0 01-.52-.72 2.48 2.48 0 01-.19-1 2 2 0 01.26-1 2.42 2.42 0 01.87-.85 5.66 5.66 0 011.6-.62 11.7 11.7 0 012.51-.25v-.57A2.06 2.06 0 0017.85 9a1.46 1.46 0 00-1.16-.45 2.53 2.53 0 00-.87.13 3.9 3.9 0 00-.62.32l-.46.28a.77.77 0 01-.43.13.52.52 0 01-.32-.1.81.81 0 01-.21-.24zm4.79 3.63a11.49 11.49 0 00-1.63.15 4.61 4.61 0 00-1.08.31 1.42 1.42 0 00-.59.45 1 1 0 00-.18.57 1.25 1.25 0 00.1.52.94.94 0 00.27.35 1.08 1.08 0 00.4.2 1.93 1.93 0 00.51.06 2.59 2.59 0 001.21-.27 3.79 3.79 0 001-.77z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-searchDiacritics,
.mw-ui-icon-searchDiacritics:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=searchDiacritics&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Esearch diacritics%3C/title%3E%3Cpath d=%22M5.31 7.87a7.27 7.27 0 015.13-2 5.06 5.06 0 011.95.35 3.91 3.91 0 011.43 1 4.44 4.44 0 01.88 1.54 6.05 6.05 0 01.3 2v8.04h-1.2a1.18 1.18 0 01-.58-.12.91.91 0 01-.34-.48l-.26-1a11.5 11.5 0 01-1 .78 6 6 0 01-1 .58 4.81 4.81 0 01-1.08.35 6.39 6.39 0 01-1.21.09 4.72 4.72 0 01-1.44-.21 3.14 3.14 0 01-1.15-.64A3 3 0 015 17.08a3.67 3.67 0 01-.28-1.49 2.89 2.89 0 01.39-1.43 3.58 3.58 0 011.29-1.25A8.37 8.37 0 018.76 12a17.22 17.22 0 013.64-.41v-.85a3 3 0 00-.59-2A2.15 2.15 0 0010.1 8a3.77 3.77 0 00-1.29.19 5.87 5.87 0 00-.91.42L7.21 9a1.15 1.15 0 01-.63.19.76.76 0 01-.47-.14 1.17 1.17 0 01-.32-.36zm6.2-5.8a.83.83 0 00.62-.23 1.11 1.11 0 00.24-.77H14a3.75 3.75 0 01-.17 1.18 2.74 2.74 0 01-.49.91 2.19 2.19 0 01-.76.59 2.27 2.27 0 01-1 .2 2 2 0 01-.82-.17 6.55 6.55 0 01-.72-.37L9.43 3a1.16 1.16 0 00-.56-.17.8.8 0 00-.62.24A1.12 1.12 0 008 3.9H6.37a3.67 3.67 0 01.18-1.18A2.81 2.81 0 017 1.8a2.25 2.25 0 01.76-.59 2.22 2.22 0 011-.21 2.06 2.06 0 01.83.17 6.42 6.42 0 01.72.37l.69.36a1.12 1.12 0 00.51.17zm.9 11.18a17 17 0 00-2.42.23 6.87 6.87 0 00-1.59.46 2.1 2.1 0 00-.88.67 1.45 1.45 0 00-.27.85 1.85 1.85 0 00.14.77 1.39 1.39 0 00.4.52 1.6 1.6 0 00.6.3 2.85 2.85 0 00.75.09 3.84 3.84 0 001.8-.39 5.61 5.61 0 001.46-1.14z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-searchDiacritics,
.mw-ui-icon-searchDiacritics-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=searchDiacritics&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Esearch diacritics%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M5.31 7.87a7.27 7.27 0 015.13-2 5.06 5.06 0 011.95.35 3.91 3.91 0 011.43 1 4.44 4.44 0 01.88 1.54 6.05 6.05 0 01.3 2v8.04h-1.2a1.18 1.18 0 01-.58-.12.91.91 0 01-.34-.48l-.26-1a11.5 11.5 0 01-1 .78 6 6 0 01-1 .58 4.81 4.81 0 01-1.08.35 6.39 6.39 0 01-1.21.09 4.72 4.72 0 01-1.44-.21 3.14 3.14 0 01-1.15-.64A3 3 0 015 17.08a3.67 3.67 0 01-.28-1.49 2.89 2.89 0 01.39-1.43 3.58 3.58 0 011.29-1.25A8.37 8.37 0 018.76 12a17.22 17.22 0 013.64-.41v-.85a3 3 0 00-.59-2A2.15 2.15 0 0010.1 8a3.77 3.77 0 00-1.29.19 5.87 5.87 0 00-.91.42L7.21 9a1.15 1.15 0 01-.63.19.76.76 0 01-.47-.14 1.17 1.17 0 01-.32-.36zm6.2-5.8a.83.83 0 00.62-.23 1.11 1.11 0 00.24-.77H14a3.75 3.75 0 01-.17 1.18 2.74 2.74 0 01-.49.91 2.19 2.19 0 01-.76.59 2.27 2.27 0 01-1 .2 2 2 0 01-.82-.17 6.55 6.55 0 01-.72-.37L9.43 3a1.16 1.16 0 00-.56-.17.8.8 0 00-.62.24A1.12 1.12 0 008 3.9H6.37a3.67 3.67 0 01.18-1.18A2.81 2.81 0 017 1.8a2.25 2.25 0 01.76-.59 2.22 2.22 0 011-.21 2.06 2.06 0 01.83.17 6.42 6.42 0 01.72.37l.69.36a1.12 1.12 0 00.51.17zm.9 11.18a17 17 0 00-2.42.23 6.87 6.87 0 00-1.59.46 2.1 2.1 0 00-.88.67 1.45 1.45 0 00-.27.85 1.85 1.85 0 00.14.77 1.39 1.39 0 00.4.52 1.6 1.6 0 00.6.3 2.85 2.85 0 00.75.09 3.84 3.84 0 001.8-.39 5.61 5.61 0 001.46-1.14z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-searchDiacritics,
.mw-ui-icon-searchDiacritics-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=searchDiacritics&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Esearch diacritics%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M5.31 7.87a7.27 7.27 0 015.13-2 5.06 5.06 0 011.95.35 3.91 3.91 0 011.43 1 4.44 4.44 0 01.88 1.54 6.05 6.05 0 01.3 2v8.04h-1.2a1.18 1.18 0 01-.58-.12.91.91 0 01-.34-.48l-.26-1a11.5 11.5 0 01-1 .78 6 6 0 01-1 .58 4.81 4.81 0 01-1.08.35 6.39 6.39 0 01-1.21.09 4.72 4.72 0 01-1.44-.21 3.14 3.14 0 01-1.15-.64A3 3 0 015 17.08a3.67 3.67 0 01-.28-1.49 2.89 2.89 0 01.39-1.43 3.58 3.58 0 011.29-1.25A8.37 8.37 0 018.76 12a17.22 17.22 0 013.64-.41v-.85a3 3 0 00-.59-2A2.15 2.15 0 0010.1 8a3.77 3.77 0 00-1.29.19 5.87 5.87 0 00-.91.42L7.21 9a1.15 1.15 0 01-.63.19.76.76 0 01-.47-.14 1.17 1.17 0 01-.32-.36zm6.2-5.8a.83.83 0 00.62-.23 1.11 1.11 0 00.24-.77H14a3.75 3.75 0 01-.17 1.18 2.74 2.74 0 01-.49.91 2.19 2.19 0 01-.76.59 2.27 2.27 0 01-1 .2 2 2 0 01-.82-.17 6.55 6.55 0 01-.72-.37L9.43 3a1.16 1.16 0 00-.56-.17.8.8 0 00-.62.24A1.12 1.12 0 008 3.9H6.37a3.67 3.67 0 01.18-1.18A2.81 2.81 0 017 1.8a2.25 2.25 0 01.76-.59 2.22 2.22 0 011-.21 2.06 2.06 0 01.83.17 6.42 6.42 0 01.72.37l.69.36a1.12 1.12 0 00.51.17zm.9 11.18a17 17 0 00-2.42.23 6.87 6.87 0 00-1.59.46 2.1 2.1 0 00-.88.67 1.45 1.45 0 00-.27.85 1.85 1.85 0 00.14.77 1.39 1.39 0 00.4.52 1.6 1.6 0 00.6.3 2.85 2.85 0 00.75.09 3.84 3.84 0 001.8-.39 5.61 5.61 0 001.46-1.14z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-searchRegularExpression,
.mw-ui-icon-searchRegularExpression:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=searchRegularExpression&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Esearch regular expression%3C/title%3E%3Cpath d=%22M1.62 10a13.63 13.63 0 00.45 3.51A13.39 13.39 0 003.4 16.7a.91.91 0 01.1.27.41.41 0 010 .21.38.38 0 01-.1.15l-.14.11-.83.5a14.89 14.89 0 01-1.11-2 13.62 13.62 0 01-.74-2 13.22 13.22 0 01-.42-2 16.4 16.4 0 010-4.14 13.22 13.22 0 01.42-2 13.84 13.84 0 01.74-2A14.94 14.94 0 012.4 2l.83.51.14.11a.4.4 0 01.1.15.41.41 0 010 .21.93.93 0 01-.1.27A13.6 13.6 0 001.62 10zM15.8 8.79l-.54.94-1.75-1-.34-.23a1.38 1.38 0 01-.27-.26A1.84 1.84 0 0113 9v2h-1V9a2.16 2.16 0 01.12-.76 1.82 1.82 0 01-.58.48l-1.74 1-.54-.94 1.73-1a2.25 2.25 0 01.75-.29 1.77 1.77 0 01-.75-.28L9.2 6.2l.54-.94 1.75 1 .33.24a1.64 1.64 0 01.27.27A2 2 0 0112 6V4h1v2a2.93 2.93 0 010 .4 1.36 1.36 0 01-.1.36 2.24 2.24 0 01.59-.49l1.74-1 .54.94-1.73 1-.36.18a1.29 1.29 0 01-.36.1 2.11 2.11 0 01.36.1 2 2 0 01.36.19zM18.37 10a13.65 13.65 0 00-.45-3.51 13.81 13.81 0 00-1.32-3.27.93.93 0 01-.1-.27.45.45 0 010-.21.36.36 0 01.1-.15l.14-.11.86-.48a15.54 15.54 0 011.1 2 13.79 13.79 0 01.74 2 13.18 13.18 0 01.42 2 16.16 16.16 0 01.14 2 16.21 16.21 0 01-.13 2 13.18 13.18 0 01-.42 2 13.57 13.57 0 01-.74 2 15.49 15.49 0 01-1.1 2l-.84-.5-.14-.11a.35.35 0 01-.1-.15.44.44 0 010-.21.91.91 0 01.1-.27 13.62 13.62 0 001.31-3.23 13.69 13.69 0 00.43-3.53z%22/%3E%3Ccircle cx=%226.5%22 cy=%2213.5%22 r=%221.5%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-searchRegularExpression,
.mw-ui-icon-searchRegularExpression-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=searchRegularExpression&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Esearch regular expression%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M1.62 10a13.63 13.63 0 00.45 3.51A13.39 13.39 0 003.4 16.7a.91.91 0 01.1.27.41.41 0 010 .21.38.38 0 01-.1.15l-.14.11-.83.5a14.89 14.89 0 01-1.11-2 13.62 13.62 0 01-.74-2 13.22 13.22 0 01-.42-2 16.4 16.4 0 010-4.14 13.22 13.22 0 01.42-2 13.84 13.84 0 01.74-2A14.94 14.94 0 012.4 2l.83.51.14.11a.4.4 0 01.1.15.41.41 0 010 .21.93.93 0 01-.1.27A13.6 13.6 0 001.62 10zM15.8 8.79l-.54.94-1.75-1-.34-.23a1.38 1.38 0 01-.27-.26A1.84 1.84 0 0113 9v2h-1V9a2.16 2.16 0 01.12-.76 1.82 1.82 0 01-.58.48l-1.74 1-.54-.94 1.73-1a2.25 2.25 0 01.75-.29 1.77 1.77 0 01-.75-.28L9.2 6.2l.54-.94 1.75 1 .33.24a1.64 1.64 0 01.27.27A2 2 0 0112 6V4h1v2a2.93 2.93 0 010 .4 1.36 1.36 0 01-.1.36 2.24 2.24 0 01.59-.49l1.74-1 .54.94-1.73 1-.36.18a1.29 1.29 0 01-.36.1 2.11 2.11 0 01.36.1 2 2 0 01.36.19zM18.37 10a13.65 13.65 0 00-.45-3.51 13.81 13.81 0 00-1.32-3.27.93.93 0 01-.1-.27.45.45 0 010-.21.36.36 0 01.1-.15l.14-.11.86-.48a15.54 15.54 0 011.1 2 13.79 13.79 0 01.74 2 13.18 13.18 0 01.42 2 16.16 16.16 0 01.14 2 16.21 16.21 0 01-.13 2 13.18 13.18 0 01-.42 2 13.57 13.57 0 01-.74 2 15.49 15.49 0 01-1.1 2l-.84-.5-.14-.11a.35.35 0 01-.1-.15.44.44 0 010-.21.91.91 0 01.1-.27 13.62 13.62 0 001.31-3.23 13.69 13.69 0 00.43-3.53z%22/%3E%3Ccircle cx=%226.5%22 cy=%2213.5%22 r=%221.5%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-searchRegularExpression,
.mw-ui-icon-searchRegularExpression-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=searchRegularExpression&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Esearch regular expression%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M1.62 10a13.63 13.63 0 00.45 3.51A13.39 13.39 0 003.4 16.7a.91.91 0 01.1.27.41.41 0 010 .21.38.38 0 01-.1.15l-.14.11-.83.5a14.89 14.89 0 01-1.11-2 13.62 13.62 0 01-.74-2 13.22 13.22 0 01-.42-2 16.4 16.4 0 010-4.14 13.22 13.22 0 01.42-2 13.84 13.84 0 01.74-2A14.94 14.94 0 012.4 2l.83.51.14.11a.4.4 0 01.1.15.41.41 0 010 .21.93.93 0 01-.1.27A13.6 13.6 0 001.62 10zM15.8 8.79l-.54.94-1.75-1-.34-.23a1.38 1.38 0 01-.27-.26A1.84 1.84 0 0113 9v2h-1V9a2.16 2.16 0 01.12-.76 1.82 1.82 0 01-.58.48l-1.74 1-.54-.94 1.73-1a2.25 2.25 0 01.75-.29 1.77 1.77 0 01-.75-.28L9.2 6.2l.54-.94 1.75 1 .33.24a1.64 1.64 0 01.27.27A2 2 0 0112 6V4h1v2a2.93 2.93 0 010 .4 1.36 1.36 0 01-.1.36 2.24 2.24 0 01.59-.49l1.74-1 .54.94-1.73 1-.36.18a1.29 1.29 0 01-.36.1 2.11 2.11 0 01.36.1 2 2 0 01.36.19zM18.37 10a13.65 13.65 0 00-.45-3.51 13.81 13.81 0 00-1.32-3.27.93.93 0 01-.1-.27.45.45 0 010-.21.36.36 0 01.1-.15l.14-.11.86-.48a15.54 15.54 0 011.1 2 13.79 13.79 0 01.74 2 13.18 13.18 0 01.42 2 16.16 16.16 0 01.14 2 16.21 16.21 0 01-.13 2 13.18 13.18 0 01-.42 2 13.57 13.57 0 01-.74 2 15.49 15.49 0 01-1.1 2l-.84-.5-.14-.11a.35.35 0 01-.1-.15.44.44 0 010-.21.91.91 0 01.1-.27 13.62 13.62 0 001.31-3.23 13.69 13.69 0 00.43-3.53z%22/%3E%3Ccircle cx=%226.5%22 cy=%2213.5%22 r=%221.5%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-signature,
.mw-ui-icon-signature:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=signature&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Esignature%3C/title%3E%3Cpath d=%22M0 18h20v1H0zm-.003-6.155l1.06-1.06 4.363 4.362-1.06 1.06z%22/%3E%3Cpath d=%22M.004 15.147l4.363-4.363 1.06 1.061-4.362 4.363zM17 5c0 9-11 9-11 9v-1.5s8 .5 9.5-6.5C16 4 15 2.5 14 2.5S11 4 10.75 10c-.08 2 .75 4.5 3.25 4.5 1.5 0 2-1 3.5-1a2.07 2.07 0 012.25 2.5h-1.5s.13-1-.5-1C16 15 16 16 14 16c0 0-4.75 0-4.75-6S12 1 14 1c.5 0 3 0 3 4z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-signature,
.mw-ui-icon-signature-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=signature&variant=invert&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Esignature%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M0 18h20v1H0zm-.003-6.155l1.06-1.06 4.363 4.362-1.06 1.06z%22/%3E%3Cpath d=%22M.004 15.147l4.363-4.363 1.06 1.061-4.362 4.363zM17 5c0 9-11 9-11 9v-1.5s8 .5 9.5-6.5C16 4 15 2.5 14 2.5S11 4 10.75 10c-.08 2 .75 4.5 3.25 4.5 1.5 0 2-1 3.5-1a2.07 2.07 0 012.25 2.5h-1.5s.13-1-.5-1C16 15 16 16 14 16c0 0-4.75 0-4.75-6S12 1 14 1c.5 0 3 0 3 4z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-signature,
.mw-ui-icon-signature-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=signature&variant=progressive&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Esignature%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M0 18h20v1H0zm-.003-6.155l1.06-1.06 4.363 4.362-1.06 1.06z%22/%3E%3Cpath d=%22M.004 15.147l4.363-4.363 1.06 1.061-4.362 4.363zM17 5c0 9-11 9-11 9v-1.5s8 .5 9.5-6.5C16 4 15 2.5 14 2.5S11 4 10.75 10c-.08 2 .75 4.5 3.25 4.5 1.5 0 2-1 3.5-1a2.07 2.07 0 012.25 2.5h-1.5s.13-1-.5-1C16 15 16 16 14 16c0 0-4.75 0-4.75-6S12 1 14 1c.5 0 3 0 3 4z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-specialCharacter,
.mw-ui-icon-specialCharacter:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=specialCharacter&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Especial character%3C/title%3E%3Cpath d=%22M19 15.9v1.29a.77.77 0 01-.23.58.86.86 0 01-.63.23h-6.76v-2.87a4.41 4.41 0 001.74-.71 5.51 5.51 0 001.4-1.42 6.92 6.92 0 00.93-1.91 7.47 7.47 0 00.34-2.28 6.15 6.15 0 00-.47-2.48 5.1 5.1 0 00-1.26-1.78 5.2 5.2 0 00-1.85-1.07 7.15 7.15 0 00-4.43 0 5.08 5.08 0 00-3.11 2.87 6.08 6.08 0 00-.47 2.48 7.47 7.47 0 00.34 2.28A6.81 6.81 0 005.47 13a5.59 5.59 0 001.41 1.39 4.41 4.41 0 001.74.71V18H1.86a.86.86 0 01-.63-.23.77.77 0 01-.23-.58V15.9h4.76l1 .12a6.94 6.94 0 01-2-1.05 7.39 7.39 0 01-1.58-1.63 7.75 7.75 0 01-1-2.1 8 8 0 01-.38-2.47 7.61 7.61 0 01.65-3.17A7.48 7.48 0 014.1 3.17a8.14 8.14 0 012.65-1.6A9.19 9.19 0 0110 1a9.18 9.18 0 013.25.57 8.14 8.14 0 012.65 1.6 7.48 7.48 0 011.78 2.47 7.61 7.61 0 01.65 3.17 8 8 0 01-.33 2.48 7.74 7.74 0 01-1 2.1A7.37 7.37 0 0115.33 15a7 7 0 01-2 1.05l1-.12h1z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-specialCharacter,
.mw-ui-icon-specialCharacter-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=specialCharacter&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Especial character%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M19 15.9v1.29a.77.77 0 01-.23.58.86.86 0 01-.63.23h-6.76v-2.87a4.41 4.41 0 001.74-.71 5.51 5.51 0 001.4-1.42 6.92 6.92 0 00.93-1.91 7.47 7.47 0 00.34-2.28 6.15 6.15 0 00-.47-2.48 5.1 5.1 0 00-1.26-1.78 5.2 5.2 0 00-1.85-1.07 7.15 7.15 0 00-4.43 0 5.08 5.08 0 00-3.11 2.87 6.08 6.08 0 00-.47 2.48 7.47 7.47 0 00.34 2.28A6.81 6.81 0 005.47 13a5.59 5.59 0 001.41 1.39 4.41 4.41 0 001.74.71V18H1.86a.86.86 0 01-.63-.23.77.77 0 01-.23-.58V15.9h4.76l1 .12a6.94 6.94 0 01-2-1.05 7.39 7.39 0 01-1.58-1.63 7.75 7.75 0 01-1-2.1 8 8 0 01-.38-2.47 7.61 7.61 0 01.65-3.17A7.48 7.48 0 014.1 3.17a8.14 8.14 0 012.65-1.6A9.19 9.19 0 0110 1a9.18 9.18 0 013.25.57 8.14 8.14 0 012.65 1.6 7.48 7.48 0 011.78 2.47 7.61 7.61 0 01.65 3.17 8 8 0 01-.33 2.48 7.74 7.74 0 01-1 2.1A7.37 7.37 0 0115.33 15a7 7 0 01-2 1.05l1-.12h1z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-specialCharacter,
.mw-ui-icon-specialCharacter-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=specialCharacter&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Especial character%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M19 15.9v1.29a.77.77 0 01-.23.58.86.86 0 01-.63.23h-6.76v-2.87a4.41 4.41 0 001.74-.71 5.51 5.51 0 001.4-1.42 6.92 6.92 0 00.93-1.91 7.47 7.47 0 00.34-2.28 6.15 6.15 0 00-.47-2.48 5.1 5.1 0 00-1.26-1.78 5.2 5.2 0 00-1.85-1.07 7.15 7.15 0 00-4.43 0 5.08 5.08 0 00-3.11 2.87 6.08 6.08 0 00-.47 2.48 7.47 7.47 0 00.34 2.28A6.81 6.81 0 005.47 13a5.59 5.59 0 001.41 1.39 4.41 4.41 0 001.74.71V18H1.86a.86.86 0 01-.63-.23.77.77 0 01-.23-.58V15.9h4.76l1 .12a6.94 6.94 0 01-2-1.05 7.39 7.39 0 01-1.58-1.63 7.75 7.75 0 01-1-2.1 8 8 0 01-.38-2.47 7.61 7.61 0 01.65-3.17A7.48 7.48 0 014.1 3.17a8.14 8.14 0 012.65-1.6A9.19 9.19 0 0110 1a9.18 9.18 0 013.25.57 8.14 8.14 0 012.65 1.6 7.48 7.48 0 011.78 2.47 7.61 7.61 0 01.65 3.17 8 8 0 01-.33 2.48 7.74 7.74 0 01-1 2.1A7.37 7.37 0 0115.33 15a7 7 0 01-2 1.05l1-.12h1z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-table,
.mw-ui-icon-table:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=table&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable%3C/title%3E%3Cpath d=%22M2 2a2 2 0 00-2 2v12a2 2 0 002 2h16a2 2 0 002-2V4a2 2 0 00-2-2zm0 4h7v4H2zm0 10v-4h7v4zm16 0h-7v-4h7zm0-6h-7V6h7z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-table,
.mw-ui-icon-table-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=table&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M2 2a2 2 0 00-2 2v12a2 2 0 002 2h16a2 2 0 002-2V4a2 2 0 00-2-2zm0 4h7v4H2zm0 10v-4h7v4zm16 0h-7v-4h7zm0-6h-7V6h7z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-table,
.mw-ui-icon-table-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=table&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M2 2a2 2 0 00-2 2v12a2 2 0 002 2h16a2 2 0 002-2V4a2 2 0 00-2-2zm0 4h7v4H2zm0 10v-4h7v4zm16 0h-7v-4h7zm0-6h-7V6h7z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-tableAddColumnAfter,
.mw-ui-icon-tableAddColumnAfter:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableAddColumnAfter&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable add column after%3C/title%3E%3Cpath d=%22M0 3v14h8v1h12V2H8v1zm10 6h3V6h2v3h3v2h-3v3h-2v-3h-3zM6 5h2v10H6zM2 5h2v10H2z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-tableAddColumnAfter,
.mw-ui-icon-tableAddColumnAfter-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableAddColumnAfter&variant=invert&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable add column after%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M0 3v14h8v1h12V2H8v1zm10 6h3V6h2v3h3v2h-3v3h-2v-3h-3zM6 5h2v10H6zM2 5h2v10H2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-tableAddColumnAfter,
.mw-ui-icon-tableAddColumnAfter-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableAddColumnAfter&variant=progressive&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable add column after%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M0 3v14h8v1h12V2H8v1zm10 6h3V6h2v3h3v2h-3v3h-2v-3h-3zM6 5h2v10H6zM2 5h2v10H2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-tableAddColumnBefore,
.mw-ui-icon-tableAddColumnBefore:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableAddColumnBefore&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable add column before%3C/title%3E%3Cpath d=%22M18 3h-6V2H0v16h12v-1h8V3zm-8 8H7v3H5v-3H2V9h3V6h2v3h3zm4 4h-2V5h2zm4 0h-2V5h2z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-tableAddColumnBefore,
.mw-ui-icon-tableAddColumnBefore-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableAddColumnBefore&variant=invert&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable add column before%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M18 3h-6V2H0v16h12v-1h8V3zm-8 8H7v3H5v-3H2V9h3V6h2v3h3zm4 4h-2V5h2zm4 0h-2V5h2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-tableAddColumnBefore,
.mw-ui-icon-tableAddColumnBefore-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableAddColumnBefore&variant=progressive&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable add column before%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M18 3h-6V2H0v16h12v-1h8V3zm-8 8H7v3H5v-3H2V9h3V6h2v3h3zm4 4h-2V5h2zm4 0h-2V5h2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-tableAddRowAfter,
.mw-ui-icon-tableAddRowAfter:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableAddRowAfter&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable add row after%3C/title%3E%3Cpath d=%22M3 0v8H2v12h16V8h-1V0zm8 10v3h3v2h-3v3H9v-3H6v-2h3v-3zm4-4v2H5V6zm0-4v2H5V2z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-tableAddRowAfter,
.mw-ui-icon-tableAddRowAfter-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableAddRowAfter&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable add row after%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M3 0v8H2v12h16V8h-1V0zm8 10v3h3v2h-3v3H9v-3H6v-2h3v-3zm4-4v2H5V6zm0-4v2H5V2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-tableAddRowAfter,
.mw-ui-icon-tableAddRowAfter-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableAddRowAfter&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable add row after%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M3 0v8H2v12h16V8h-1V0zm8 10v3h3v2h-3v3H9v-3H6v-2h3v-3zm4-4v2H5V6zm0-4v2H5V2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-tableAddRowBefore,
.mw-ui-icon-tableAddRowBefore:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableAddRowBefore&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable add row before%3C/title%3E%3Cpath d=%22M17 20v-8h1V0H2v12h1v8zM9 10V7H6V5h3V2h2v3h3v2h-3v3zm-4 4v-2h10v2zm0 4v-2h10v2z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-tableAddRowBefore,
.mw-ui-icon-tableAddRowBefore-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableAddRowBefore&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable add row before%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M17 20v-8h1V0H2v12h1v8zM9 10V7H6V5h3V2h2v3h3v2h-3v3zm-4 4v-2h10v2zm0 4v-2h10v2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-tableAddRowBefore,
.mw-ui-icon-tableAddRowBefore-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableAddRowBefore&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable add row before%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M17 20v-8h1V0H2v12h1v8zM9 10V7H6V5h3V2h2v3h3v2h-3v3zm-4 4v-2h10v2zm0 4v-2h10v2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-tableCaption,
.mw-ui-icon-tableCaption:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableCaption&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable caption%3C/title%3E%3Cpath d=%22M2 8a2 2 0 00-2 2v6a2 2 0 002 2h16a2 2 0 002-2v-6a2 2 0 00-2-2zm0 2h7v2H2zm0 6v-2h7v2zm16 0h-7v-2h7zm0-4h-7v-2h7zM2 2h16v4H2z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-tableCaption,
.mw-ui-icon-tableCaption-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableCaption&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable caption%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M2 8a2 2 0 00-2 2v6a2 2 0 002 2h16a2 2 0 002-2v-6a2 2 0 00-2-2zm0 2h7v2H2zm0 6v-2h7v2zm16 0h-7v-2h7zm0-4h-7v-2h7zM2 2h16v4H2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-tableCaption,
.mw-ui-icon-tableCaption-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableCaption&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable caption%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M2 8a2 2 0 00-2 2v6a2 2 0 002 2h16a2 2 0 002-2v-6a2 2 0 00-2-2zm0 2h7v2H2zm0 6v-2h7v2zm16 0h-7v-2h7zm0-4h-7v-2h7zM2 2h16v4H2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-tableMergeCells,
.mw-ui-icon-tableMergeCells:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableMergeCells&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 xmlns:xlink=%22http://www.w3.org/1999/xlink%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Emerge cells%3C/title%3E%3Cpath id=%22a%22 d=%22M9 10L4 6v3H0v2h4v3zm-7 3H0v5h8v-2H2zM0 2v5h2V4h6V2z%22/%3E%3Cuse transform=%22matrix%28-1 0 0 1 20 0%29%22 xlink:href=%22%23a%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-tableMergeCells,
.mw-ui-icon-tableMergeCells-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableMergeCells&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 xmlns:xlink=%22http://www.w3.org/1999/xlink%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Emerge cells%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath id=%22a%22 d=%22M9 10L4 6v3H0v2h4v3zm-7 3H0v5h8v-2H2zM0 2v5h2V4h6V2z%22/%3E%3Cuse xmlns:xlink=%22http://www.w3.org/1999/xlink%22 transform=%22matrix%28-1 0 0 1 20 0%29%22 xlink:href=%22%23a%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-tableMergeCells,
.mw-ui-icon-tableMergeCells-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableMergeCells&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 xmlns:xlink=%22http://www.w3.org/1999/xlink%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Emerge cells%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath id=%22a%22 d=%22M9 10L4 6v3H0v2h4v3zm-7 3H0v5h8v-2H2zM0 2v5h2V4h6V2z%22/%3E%3Cuse xmlns:xlink=%22http://www.w3.org/1999/xlink%22 transform=%22matrix%28-1 0 0 1 20 0%29%22 xlink:href=%22%23a%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-tableMoveColumnAfter,
.mw-ui-icon-tableMoveColumnAfter:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableMoveColumnAfter&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable move column after%3C/title%3E%3Cpath d=%22M16 10l-5-4v3H6v2h5v3z%22/%3E%3Cpath d=%22M0 2h20v16H0zm5 6v4h5v4h8V4h-8v4z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-tableMoveColumnAfter,
.mw-ui-icon-tableMoveColumnAfter-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableMoveColumnAfter&variant=invert&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable move column after%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M16 10l-5-4v3H6v2h5v3z%22/%3E%3Cpath d=%22M0 2h20v16H0zm5 6v4h5v4h8V4h-8v4z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-tableMoveColumnAfter,
.mw-ui-icon-tableMoveColumnAfter-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableMoveColumnAfter&variant=progressive&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable move column after%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M16 10l-5-4v3H6v2h5v3z%22/%3E%3Cpath d=%22M0 2h20v16H0zm5 6v4h5v4h8V4h-8v4z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-tableMoveColumnBefore,
.mw-ui-icon-tableMoveColumnBefore:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableMoveColumnBefore&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable move column before%3C/title%3E%3Cpath d=%22M4 10l5-4v3h5v2H9v3z%22/%3E%3Cpath d=%22M0 2v16h20V2zm2 2h8v4h5v4h-5v4H2z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-tableMoveColumnBefore,
.mw-ui-icon-tableMoveColumnBefore-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableMoveColumnBefore&variant=invert&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable move column before%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M4 10l5-4v3h5v2H9v3z%22/%3E%3Cpath d=%22M0 2v16h20V2zm2 2h8v4h5v4h-5v4H2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-tableMoveColumnBefore,
.mw-ui-icon-tableMoveColumnBefore-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableMoveColumnBefore&variant=progressive&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable move column before%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M4 10l5-4v3h5v2H9v3z%22/%3E%3Cpath d=%22M0 2v16h20V2zm2 2h8v4h5v4h-5v4H2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-tableMoveRowAfter,
.mw-ui-icon-tableMoveRowAfter:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableMoveRowAfter&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable move row after%3C/title%3E%3Cpath d=%22M10 16l-4-5h3V6h2v5h3z%22/%3E%3Cpath d=%22M2 0v20h16V0zm2 10h4V5h4v5h4v8H4z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-tableMoveRowAfter,
.mw-ui-icon-tableMoveRowAfter-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableMoveRowAfter&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable move row after%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M10 16l-4-5h3V6h2v5h3z%22/%3E%3Cpath d=%22M2 0v20h16V0zm2 10h4V5h4v5h4v8H4z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-tableMoveRowAfter,
.mw-ui-icon-tableMoveRowAfter-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableMoveRowAfter&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable move row after%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M10 16l-4-5h3V6h2v5h3z%22/%3E%3Cpath d=%22M2 0v20h16V0zm2 10h4V5h4v5h4v8H4z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-tableMoveRowBefore,
.mw-ui-icon-tableMoveRowBefore:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableMoveRowBefore&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable move row before%3C/title%3E%3Cpath d=%22M9 9H6l4-5 4 5h-3v5H9z%22/%3E%3Cpath d=%22M2 0h16v20H2zm2 2v8h4v5h4v-5h4V2z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-tableMoveRowBefore,
.mw-ui-icon-tableMoveRowBefore-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableMoveRowBefore&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable move row before%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M9 9H6l4-5 4 5h-3v5H9z%22/%3E%3Cpath d=%22M2 0h16v20H2zm2 2v8h4v5h4v-5h4V2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-tableMoveRowBefore,
.mw-ui-icon-tableMoveRowBefore-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=tableMoveRowBefore&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Etable move row before%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M9 9H6l4-5 4 5h-3v5H9z%22/%3E%3Cpath d=%22M2 0h16v20H2zm2 2v8h4v5h4v-5h4V2z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-templateAdd,
.mw-ui-icon-templateAdd:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=templateAdd&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eadd template%3C/title%3E%3Cpath d=%22M16 5V1h-2v4h-4v2h4v4h2V7h4V5z%22/%3E%3Cpath d=%22M0 17V5h8v2H2v8h12v-2h2v4z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-templateAdd,
.mw-ui-icon-templateAdd-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=templateAdd&variant=invert&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eadd template%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M16 5V1h-2v4h-4v2h4v4h2V7h4V5z%22/%3E%3Cpath d=%22M0 17V5h8v2H2v8h12v-2h2v4z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-templateAdd,
.mw-ui-icon-templateAdd-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=templateAdd&variant=progressive&format=rasterized&lang=fr&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eadd template%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M16 5V1h-2v4h-4v2h4v4h2V7h4V5z%22/%3E%3Cpath d=%22M0 17V5h8v2H2v8h12v-2h2v4z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-translation,
.mw-ui-icon-translation:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=translation&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Elanguage%3C/title%3E%3Cpath d=%22M20 18h-1.44a.61.61 0 01-.4-.12.81.81 0 01-.23-.31L17 15h-5l-1 2.54a.77.77 0 01-.22.3.59.59 0 01-.4.14H9l4.55-11.47h1.89zm-3.53-4.31L14.89 9.5a11.62 11.62 0 01-.39-1.24q-.09.37-.19.69l-.19.56-1.58 4.19zm-6.3-1.58a13.43 13.43 0 01-2.91-1.41 11.46 11.46 0 002.81-5.37H12V4H7.31a4 4 0 00-.2-.56C6.87 2.79 6.6 2 6.6 2l-1.47.5s.4.89.6 1.5H0v1.33h2.15A11.23 11.23 0 005 10.7a17.19 17.19 0 01-5 2.1q.56.82.87 1.38a23.28 23.28 0 005.22-2.51 15.64 15.64 0 003.56 1.77zM3.63 5.33h4.91a8.11 8.11 0 01-2.45 4.45 9.11 9.11 0 01-2.46-4.45z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-translation,
.mw-ui-icon-translation-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=translation&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Elanguage%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M20 18h-1.44a.61.61 0 01-.4-.12.81.81 0 01-.23-.31L17 15h-5l-1 2.54a.77.77 0 01-.22.3.59.59 0 01-.4.14H9l4.55-11.47h1.89zm-3.53-4.31L14.89 9.5a11.62 11.62 0 01-.39-1.24q-.09.37-.19.69l-.19.56-1.58 4.19zm-6.3-1.58a13.43 13.43 0 01-2.91-1.41 11.46 11.46 0 002.81-5.37H12V4H7.31a4 4 0 00-.2-.56C6.87 2.79 6.6 2 6.6 2l-1.47.5s.4.89.6 1.5H0v1.33h2.15A11.23 11.23 0 005 10.7a17.19 17.19 0 01-5 2.1q.56.82.87 1.38a23.28 23.28 0 005.22-2.51 15.64 15.64 0 003.56 1.77zM3.63 5.33h4.91a8.11 8.11 0 01-2.45 4.45 9.11 9.11 0 01-2.46-4.45z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-translation,
.mw-ui-icon-translation-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=translation&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Elanguage%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M20 18h-1.44a.61.61 0 01-.4-.12.81.81 0 01-.23-.31L17 15h-5l-1 2.54a.77.77 0 01-.22.3.59.59 0 01-.4.14H9l4.55-11.47h1.89zm-3.53-4.31L14.89 9.5a11.62 11.62 0 01-.39-1.24q-.09.37-.19.69l-.19.56-1.58 4.19zm-6.3-1.58a13.43 13.43 0 01-2.91-1.41 11.46 11.46 0 002.81-5.37H12V4H7.31a4 4 0 00-.2-.56C6.87 2.79 6.6 2 6.6 2l-1.47.5s.4.89.6 1.5H0v1.33h2.15A11.23 11.23 0 005 10.7a17.19 17.19 0 01-5 2.1q.56.82.87 1.38a23.28 23.28 0 005.22-2.51 15.64 15.64 0 003.56 1.77zM3.63 5.33h4.91a8.11 8.11 0 01-2.45 4.45 9.11 9.11 0 01-2.46-4.45z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-icon-wikiText,
.mw-ui-icon-wikiText:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=wikiText&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3EWikitext%3C/title%3E%3Cpath d=%22M1 3v14h3v-2H3V5h1V3zm4 0v14h4v-2H7V5h2V3zm11 0v2h1v10h-1v2h3V3zm-5 0v2h2v10h-2v2h4V3z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-icon-wikiText,
.mw-ui-icon-wikiText-invert:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=wikiText&variant=invert&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3EWikitext%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M1 3v14h3v-2H3V5h1V3zm4 0v14h4v-2H7V5h2V3zm11 0v2h1v10h-1v2h3V3zm-5 0v2h2v10h-2v2h4V3z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-image-progressive.oo-ui-icon-wikiText,
.mw-ui-icon-wikiText-progressive:before {
 background-image:url(/w/load.php?modules=oojs-ui.styles.icons-editing-advanced&image=wikiText&variant=progressive&format=rasterized&skin=vector&version=trx8x);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3EWikitext%3C/title%3E%3Cg fill=%22%2336c%22%3E%3Cpath d=%22M1 3v14h3v-2H3V5h1V3zm4 0v14h4v-2H7V5h2V3zm11 0v2h1v10h-1v2h3V3zm-5 0v2h2v10h-2v2h4V3z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-indicator-clear {
 background-image:url(/w/load.php?modules=oojs-ui.styles.indicators&image=clear&format=rasterized&skin=vector&version=1a0zp);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eclear%3C/title%3E%3Cpath d=%22M10 0a10 10 0 1010 10A10 10 0 0010 0zm5.66 14.24l-1.41 1.41L10 11.41l-4.24 4.25-1.42-1.42L8.59 10 4.34 5.76l1.42-1.42L10 8.59l4.24-4.24 1.41 1.41L11.41 10z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-indicator-clear {
 background-image:url(/w/load.php?modules=oojs-ui.styles.indicators&image=clear&variant=invert&format=rasterized&skin=vector&version=1a0zp);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Eclear%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M10 0a10 10 0 1010 10A10 10 0 0010 0zm5.66 14.24l-1.41 1.41L10 11.41l-4.24 4.25-1.42-1.42L8.59 10 4.34 5.76l1.42-1.42L10 8.59l4.24-4.24 1.41 1.41L11.41 10z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-indicator-up {
 background-image:url(/w/load.php?modules=oojs-ui.styles.indicators&image=up&format=rasterized&skin=vector&version=1a0zp);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2212%22 height=%2212%22 viewBox=%220 0 12 12%22%3E%3Ctitle%3Eup%3C/title%3E%3Cpath d=%22M10.035 9.026L6 5.168 2.053 9.026 1 7.974l5-5 5 5z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-indicator-up {
 background-image:url(/w/load.php?modules=oojs-ui.styles.indicators&image=up&variant=invert&format=rasterized&skin=vector&version=1a0zp);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2212%22 height=%2212%22 viewBox=%220 0 12 12%22%3E%3Ctitle%3Eup%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M10.035 9.026L6 5.168 2.053 9.026 1 7.974l5-5 5 5z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-indicator-down {
 background-image:url(/w/load.php?modules=oojs-ui.styles.indicators&image=down&format=rasterized&skin=vector&version=1a0zp);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2212%22 height=%2212%22 viewBox=%220 0 12 12%22%3E%3Ctitle%3Edown%3C/title%3E%3Cpath d=%22M10.085 2.943L6.05 6.803l-3.947-3.86L1.05 3.996l5 5 5-5z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-indicator-down {
 background-image:url(/w/load.php?modules=oojs-ui.styles.indicators&image=down&variant=invert&format=rasterized&skin=vector&version=1a0zp);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2212%22 height=%2212%22 viewBox=%220 0 12 12%22%3E%3Ctitle%3Edown%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M10.085 2.943L6.05 6.803l-3.947-3.86L1.05 3.996l5 5 5-5z%22/%3E%3C/g%3E%3C/svg%3E")
}
.oo-ui-indicator-required {
 background-image:url(/w/load.php?modules=oojs-ui.styles.indicators&image=required&format=rasterized&skin=vector&version=1a0zp);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Erequired%3C/title%3E%3Cpath d=%22M8.5 0h3v20h-3z%22/%3E%3Cpath d=%22M19.41 13.701l-1.5 2.598L.59 6.3l1.5-2.598z%22/%3E%3Cpath d=%22M17.91 3.701l1.5 2.598-17.32 10-1.5-2.598z%22/%3E%3C/svg%3E")
}
.oo-ui-image-invert.oo-ui-indicator-required {
 background-image:url(/w/load.php?modules=oojs-ui.styles.indicators&image=required&variant=invert&format=rasterized&skin=vector&version=1a0zp);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3Erequired%3C/title%3E%3Cg fill=%22%23fff%22%3E%3Cpath d=%22M8.5 0h3v20h-3z%22/%3E%3Cpath d=%22M19.41 13.701l-1.5 2.598L.59 6.3l1.5-2.598z%22/%3E%3Cpath d=%22M17.91 3.701l1.5 2.598-17.32 10-1.5-2.598z%22/%3E%3C/g%3E%3C/svg%3E")
}
.messagebox,
.errorbox,
.warningbox,
.successbox {
 color:#000;
 -webkit-box-sizing:border-box;
 -moz-box-sizing:border-box;
 box-sizing:border-box;
 margin-bottom:16px;
 border:1px solid;
 padding:12px 24px;
 word-wrap:break-word;
 overflow-wrap:break-word;
 overflow:hidden
}
.messagebox :only-child,
.errorbox :only-child,
.warningbox :only-child,
.successbox :only-child {
 margin:0
}
.messagebox h2,
.errorbox h2,
.warningbox h2,
.successbox h2 {
 color:inherit;
 display:inline;
 margin:0 0.5em 0 0;
 border:0;
 font-size:1em;
 font-weight:bold
}
.messagebox {
 background-color:#eaecf0;
 border-color:#a2a9b1
}
.errorbox {
 background-color:#fee7e6;
 border-color:#d33
}
.warningbox {
 background-color:#fef6e7;
 border-color:#fc3
}
.successbox {
 background-color:#d5fdf4;
 border-color:#14866d
}
@media screen {
 html,
 body {
  height:100%
 }
 :focus {
  outline-color:#3366cc
 }
 body {
  background-color:#ffffff;
  color:#202122;
  overflow-y:scroll
 }
 .mw-body,
 .parsoid-body {
  direction:ltr;
  padding:1em
 }
 .mw-body {
  border:1px solid #a7d7f9;
  border-right-width:0;
  margin-top:-1px
 }
 .mw-body .firstHeading {
  overflow:visible
 }
 .mw-header {
  min-height:3.125em;
  margin:0.625em 0 0.3125em;
  padding:0.125em 1.76666667em;
  display:-webkit-flex;
  display:-moz-flex;
  display:-ms-flexbox;
  display:flex;
  flex-wrap:wrap;
  align-items:center;
  z-index:1
 }
 #p-search {
  float:left;
  margin:0.5em 0.5em 0 0.5em;
  min-width:5em;
  width:13.2em;
  width:20vw;
  max-width:20em
 }
 .mw-body,
 #mw-data-after-content,
 #left-navigation,
 .mw-footer {
  margin-left:11em
 }
 .mw-indicators {
  float:right;
  z-index:1
 }
 .mw-body-content {
  position:relative;
  z-index:0
 }
 #mw-navigation h2 {
  position:absolute;
  top:-9999px
 }
 .mw-article-toolbar-container:after {
  clear:both;
  content:'';
  display:block
 }
 #left-navigation {
  float:left
 }
 #right-navigation {
  float:right
 }
 #mw-sidebar-button {
  float:left;
  margin-left:-12px;
  margin-right:12px
 }
 #mw-panel {
  position:absolute;
  left:0;
  width:11em;
  -webkit-box-sizing:border-box;
  -moz-box-sizing:border-box;
  box-sizing:border-box;
  margin-top:0.5em;
  padding-left:0.5em;
  z-index:1
 }
 .skin-vector-max-width {
  background-color:#f8f9fa
 }
 .skin-vector-max-width .mw-body {
  border-left:0;
  border-bottom:0;
  padding:1.25em 0.5em 1.5em
 }
 .skin-vector-max-width .parsoid-body {
  padding:1.25em 0.5em 1.5em
 }
 .skin-vector-max-width .mw-header {
  padding-left:0;
  padding-right:0
 }
 .skin-vector-max-width .mw-body,
 .skin-vector-max-width #mw-data-after-content,
 .skin-vector-max-width #left-navigation,
 .skin-vector-max-width .mw-footer {
  margin-left:0
 }
 .skin-vector-max-width.skin-vector-search-header-legacy #mw-head {
  width:auto;
  left:0;
  right:0
 }
 .skin-vector-max-width.skin-vector-search-header-legacy #left-navigation {
  margin-top:0;
  margin-bottom:0
 }
 .skin-vector-max-width.skin-vector-search-header-legacy #right-navigation {
  margin-top:0
 }
 .skin-vector-max-width.skin-vector-search-header-legacy #p-personal {
  right:0
 }
 .skin-vector-max-width.skin-vector-search-header-legacy #p-search {
  margin-right:0
 }
 .skin-vector-max-width #p-namespaces {
  background-image:none;
  padding-left:0
 }
 .skin-vector-max-width #mw-panel {
  background-image:linear-gradient(to bottom,#ffffff 0%,#f8f9fa 10%,#f8f9fa 90%,#ffffff 100%);
  left:-30px;
  margin-top:0;
  padding-top:8px;
  padding-bottom:40px;
  padding-left:13px
 }
 .skin-vector-max-width .mw-footer {
  border-top:1px solid #a2a9b1;
  padding:32px 0 0 0
 }
 .skin-vector-max-width .mw-page-container {
  min-width:40.375em;
  max-width:1650px;
  min-height:100%;
  margin-left:auto;
  margin-right:auto;
  padding:0 30px;
  background-color:#ffffff
 }
 .skin-vector-max-width.skin-vector-search-header .mw-page-container {
  overflow-y:auto
 }
 .skin-vector-max-width .mw-page-container-inner {
  position:relative
 }
 .skin-vector-max-width .mw-workspace-container {
  max-width:1440px;
  margin-left:auto;
  margin-right:auto
 }
 .skin-vector-max-width.skin-vector-search-header .mw-workspace-container {
  position:relative
 }
 .skin-vector-max-width .mw-content-container {
  max-width:960px;
  margin-left:auto;
  margin-right:auto
 }
 .skin-vector-max-width.skin-vector-search-header-legacy .mw-article-toolbar-container {
  margin-top:4.3125em
 }
 .skin-vector-max-width.skin-vector-search-header .mw-article-toolbar-container {
  max-width:960px;
  margin-left:auto;
  margin-right:auto
 }
 .skin-vector-max-width .mw-sidebar-container {
  position:absolute;
  top:0;
  left:0;
  right:0
 }
 .skin-vector-max-width .mw-footer-container {
  padding-top:50px;
  padding-bottom:82px
 }
 .skin-vector-max-width.action-history .mw-content-container,
 .skin-vector-max-width.ns-special .mw-content-container {
  max-width:none
 }
 .skin-vector-max-width.action-history.skin-vector-search-header-legacy .mw-article-toolbar-container,
 .skin-vector-max-width.ns-special.skin-vector-search-header-legacy .mw-article-toolbar-container {
  max-width:960px
 }
 .skin-vector-max-width.action-history .mw-checkbox-hack-checkbox:checked ~ .mw-workspace-container .mw-content-container,
 .skin-vector-max-width.ns-special .mw-checkbox-hack-checkbox:checked ~ .mw-workspace-container .mw-content-container {
  margin-left:11.5em
 }
 .skin-vector-max-width.skin-vector-search-header-legacy #mw-sidebar-checkbox:not(:checked) ~ .mw-header .mw-sidebar,
 .skin-vector-max-width.skin-vector-search-header #mw-sidebar-checkbox:not(:checked) ~ .mw-workspace-container .mw-sidebar {
  -webkit-transform:translateX(-105px);
  -moz-transform:translateX(-105px);
  -ms-transform:translateX(-105px);
  transform:translateX(-105px)
 }
 .skin-vector-search-header #p-search {
  flex-grow:1;
  float:left;
  min-width:21.875em;
  max-width:100%;
  margin:0 0 0 3.5em
 }
 .skin-vector-search-header #p-search #searchform {
  margin-left:0;
  max-width:28.125em
 }
 .skin-vector-search-header #p-personal {
  flex-grow:1;
  flex-basis:18.75em;
  margin-left:3.5em;
  float:right
 }
 html {
  font-size:100%
 }
 html,
 body {
  font-family:sans-serif
 }
 ul {
  list-style-image:url(/w/skins/Vector/resources/skins.vector.styles/images/bullet-icon.svg?d4515)
 }
 pre,
 .mw-code {
  line-height:1.3
 }
 .mw-jump-link:not(:focus) {
  display:block;
  position:absolute !important;
  clip:rect(1px,1px,1px,1px);
  width:1px;
  height:1px;
  margin:-1px;
  border:0;
  padding:0;
  overflow:hidden
 }
 #p-personal li {
  font-size:0.75em
 }
 .mw-editsection,
 .mw-editsection-like {
  font-family:sans-serif
 }
 .mw-body h1,
 .mw-body-content h1,
 .mw-body-content h2 {
  margin-bottom:0.25em;
  padding:0;
  font-family:'Linux Libertine','Georgia','Times',serif;
  line-height:1.3
 }
 .mw-body h1:lang(ja),
 .mw-body-content h1:lang(ja),
 .mw-body-content h2:lang(ja),
 .mw-body h1:lang(he),
 .mw-body-content h1:lang(he),
 .mw-body-content h2:lang(he),
 .mw-body h1:lang(ko),
 .mw-body-content h1:lang(ko),
 .mw-body-content h2:lang(ko) {
  font-family:sans-serif
 }
 .mw-body h1:lang(my),
 .mw-body-content h1:lang(my),
 .mw-body-content h2:lang(my) {
  line-height:normal
 }
 .mw-body h1,
 .mw-body-content h1 {
  font-size:1.8em
 }
 .mw-body-content {
  font-size:0.875em;
  font-size:calc(1em * 0.875);
  line-height:1.6
 }
 .mw-body-content h1 {
  margin-top:1em
 }
 .mw-body-content h2 {
  margin-top:1em;
  font-size:1.5em
 }
 .mw-body-content h3,
 .mw-body-content h4,
 .mw-body-content h5,
 .mw-body-content h6 {
  margin-top:0.3em;
  margin-bottom:0;
  padding-bottom:0;
  line-height:1.6
 }
 .mw-body-content h3 {
  font-size:1.2em
 }
 .mw-body-content h3,
 .mw-body-content h4 {
  font-weight:bold
 }
 .mw-body-content h4,
 .mw-body-content h5,
 .mw-body-content h6 {
  font-size:100%
 }
 .mw-body-content .toc h2 {
  font-family:sans-serif;
  font-size:100%
 }
 .mw-body-content p {
  margin:0.5em 0
 }
 .mw-body-content blockquote {
  border-left:4px solid #eaecf0;
  padding:8px 32px
 }
 .mw-body-content blockquote > :first-child {
  margin-top:0
 }
 .mw-body-content blockquote > :last-child {
  margin-bottom:0
 }
 .mw-body-content blockquote > :only-child {
  margin-top:0;
  margin-bottom:0
 }
 .mw-parser-output .external {
  background-image:url(/w/skins/Vector/resources/skins.vector.styles/images/external-link-ltr-icon.svg?b4b84);
  background-position:center right;
  background-repeat:no-repeat;
  padding-right:13px
 }
 .mw-body .mw-indicators {
  font-size:0.875em;
  line-height:1.6;
  position:relative
 }
 .mw-body .mw-indicator {
  display:inline-block
 }
 #siteNotice {
  font-size:0.8em
 }
 #p-personal .vector-menu-content-list {
  display:flex;
  flex-wrap:wrap;
  flex-grow:1;
  justify-content:flex-end;
  align-items:baseline
 }
 .mw-portlet h3 {
  display:none
 }
 .mw-portlet ul {
  list-style:none none;
  margin:0
 }
 .mw-portlet li {
  margin-left:0.75em;
  padding-top:0.5em;
  line-height:1.16666667
 }
 #pt-anonuserpage,
 #pt-userpage a {
  background-image:url(/w/skins/Vector/resources/skins.vector.styles/images/user-avatar.svg?b7f58);
  background-position:left 0.33333333em;
  background-repeat:no-repeat;
  background-size:1.16666667em 1.16666667em;
  padding-top:0.5em !important;
  padding-left:16px !important
 }
 #pt-userpage {
  padding-top:0 !important
 }
 #pt-userpage a {
  display:inline-block
 }
 #pt-anonuserpage {
  color:#54595d
 }
 #p-search h3 {
  display:block;
  position:absolute !important;
  clip:rect(1px,1px,1px,1px);
  width:1px;
  height:1px;
  margin:-1px;
  border:0;
  padding:0;
  overflow:hidden
 }
 #simpleSearch {
  position:relative;
  height:100%
 }
 #simpleSearch input {
  margin:0;
  font-family:inherit;
  height:2.28571429em
 }
 #searchInput {
  background-color:rgba(255,255,255,0.5);
  color:#000000;
  width:100%;
  -webkit-box-sizing:border-box;
  -moz-box-sizing:border-box;
  box-sizing:border-box;
  border:1px solid #a2a9b1;
  border-radius:2px;
  padding:0.4em 1.84615385em 0.4em 0.4em;
  -webkit-box-shadow:inset 0 0 0 1px transparent;
  box-shadow:inset 0 0 0 1px transparent;
  font-size:0.8125em;
  direction:ltr;
  -webkit-transition:border-color 250ms,box-shadow 250ms;
  -moz-transition:border-color 250ms,box-shadow 250ms;
  transition:border-color 250ms,box-shadow 250ms;
  -webkit-appearance:none;
  -moz-appearance:textfield
 }
 #simpleSearch:hover #searchInput {
  border-color:#72777d
 }
 #searchInput:focus,
 #simpleSearch:hover #searchInput:focus {
  outline:0;
  border-color:#3366cc;
  -webkit-box-shadow:inset 0 0 0 1px #3366cc,inset 0 0 0 2px #ffffff;
  box-shadow:inset 0 0 0 1px #3366cc,inset 0 0 0 2px #ffffff
 }
 #searchInput::-webkit-input-placeholder {
  color:#72777d;
  opacity:1
 }
 #searchInput:-ms-input-placeholder {
  color:#72777d;
  opacity:1
 }
 #searchInput::-moz-placeholder {
  color:#72777d;
  opacity:1
 }
 #searchInput:-moz-placeholder {
  color:#72777d;
  opacity:1
 }
 #searchInput::placeholder {
  color:#72777d;
  opacity:1
 }
 #searchInput::-webkit-search-decoration,
 #searchInput::-webkit-search-cancel-button,
 #searchInput::-webkit-search-results-button,
 #searchInput::-webkit-search-results-decoration {
  display:none
 }
 #searchButton,
 #mw-searchButton {
  background-color:transparent;
  position:absolute;
  top:1px;
  bottom:1px;
  right:1px;
  min-width:24px;
  width:1.84615385em;
  border:0;
  padding:0;
  cursor:pointer;
  font-size:0.8125em;
  direction:ltr;
  text-indent:-99999px;
  white-space:nowrap;
  overflow:hidden;
  z-index:1
 }
 #searchButton {
  background-image:url(/w/skins/Vector/resources/skins.vector.styles/images/search.svg?4d50a);
  background-position:center center;
  background-repeat:no-repeat
 }
 #simpleSearch.search-form__loader:after {
  content:attr(data-loading-msg);
  display:block;
  position:absolute;
  top:100%;
  width:100%;
  box-sizing:border-box;
  border:1px solid #a2a9b1;
  border-top-width:0;
  border-radius:0 0 2px 2px;
  color:#72777d;
  font-size:0.8em;
  padding:0.4em;
  -webkit-box-shadow:inset 0 0 0 1px transparent;
  box-shadow:inset 0 0 0 1px transparent;
  overflow:hidden;
  white-space:nowrap;
  text-overflow:ellipsis;
  z-index:1;
  background:linear-gradient(90deg,#3366cc 0%,#3366cc 100%) -10% 0 / 0 2px no-repeat,#ffffff;
  animation:search-loader-progress-bar 1200ms linear 1000ms infinite alternate
 }
 @keyframes search-loader-progress-bar {
  0% {
   background-size:0 2px;
   background-position:-10% 0
  }
  30% {
   background-size:30% 2px;
   background-position:-10% 0
  }
  70% {
   background-size:30% 2px;
   background-position:110% 0
  }
  100% {
   background-size:0 2px;
   background-position:110% 0
  }
 }
 .vector-menu-tabs {
  background-position:left bottom;
  float:left;
  height:2.5em;
  padding-left:1px
 }
 .vector-menu-tabs h3 {
  display:none
 }
 .vector-menu-tabs ul {
  float:left;
  height:100%;
  list-style:none none;
  margin:0;
  padding:0
 }
 .vector-menu-tabs li {
  background-image:url(/w/skins/Vector/resources/skins.vector.styles/images/tab-normal-fade.png?1cc52);
  background-image:linear-gradient(to top,#77c1f6 0,#e8f2f8 1px,#ffffff 100%);
  background-position:left bottom;
  background-repeat:repeat-x;
  float:left;
  display:block;
  height:100%;
  margin:0;
  padding:0;
  line-height:1.125em;
  white-space:nowrap
 }
 .vector-menu-tabs li a {
  background-position:right bottom;
  color:#0645ad;
  -webkit-box-sizing:border-box;
  -moz-box-sizing:border-box;
  box-sizing:border-box;
  display:block;
  float:left;
  height:3.07692308em;
  position:relative;
  padding-top:1.25em;
  padding-left:8px;
  padding-right:8px;
  font-size:0.8125em;
  cursor:pointer
 }
 .vector-menu-tabs .new a,
 .vector-menu-tabs .new a:visited {
  color:#a55858
 }
 .vector-menu-tabs .selected {
  background:#ffffff
 }
 .vector-menu-tabs .selected a,
 .vector-menu-tabs .selected a:visited {
  color:#202122;
  text-decoration:none
 }
 .vector-menu-tabs .icon a {
  background-position:right bottom;
  background-repeat:no-repeat
 }
 @-webkit-keyframes rotate {
  from {
   -webkit-transform:rotate(0deg);
   -moz-transform:rotate(0deg);
   transform:rotate(0deg)
  }
  to {
   -webkit-transform:rotate(360deg);
   -moz-transform:rotate(360deg);
   transform:rotate(360deg)
  }
 }
 @-moz-keyframes rotate {
  from {
   -webkit-transform:rotate(0deg);
   -moz-transform:rotate(0deg);
   transform:rotate(0deg)
  }
  to {
   -webkit-transform:rotate(360deg);
   -moz-transform:rotate(360deg);
   transform:rotate(360deg)
  }
 }
 @keyframes rotate {
  from {
   -webkit-transform:rotate(0deg);
   -moz-transform:rotate(0deg);
   transform:rotate(0deg)
  }
  to {
   -webkit-transform:rotate(360deg);
   -moz-transform:rotate(360deg);
   transform:rotate(360deg)
  }
 }
 .vector-menu-tabs .mw-watchlink.icon a {
  width:2.15384615em;
  height:0;
  padding:3.07692308em 0 0 0;
  overflow:hidden
 }
 .vector-menu-tabs .mw-watchlink.icon a:before {
  background-repeat:no-repeat;
  background-position:50% 50%;
  content:'';
  display:block;
  position:absolute;
  top:1.07692308em;
  left:0.38461538em;
  width:1.23076923em;
  height:1.23076923em
 }
 .vector-menu-tabs #ca-unwatch.icon a:before {
  background-image:linear-gradient(transparent,transparent),url(/w/skins/Vector/resources/skins.vector.styles/images/unwatch-icon.svg?3de3e)
 }
 .vector-menu-tabs #ca-unwatch.mw-watchlink-temp.icon a:before {
  background-image:linear-gradient(transparent,transparent),url(/w/skins/Vector/resources/skins.vector.styles/images/unwatch-temp-icon.svg?b7b09)
 }
 .vector-menu-tabs #ca-watch.icon a:before {
  background-image:linear-gradient(transparent,transparent),url(/w/skins/Vector/resources/skins.vector.styles/images/watch-icon.svg?0e9fa)
 }
 .vector-menu-tabs #ca-unwatch.icon a:hover:before,
 .vector-menu-tabs #ca-unwatch.icon a:focus:before {
  background-image:linear-gradient(transparent,transparent),url(/w/skins/Vector/resources/skins.vector.styles/images/unwatch-icon-hl.svg?c58d6)
 }
 .vector-menu-tabs #ca-unwatch.mw-watchlink-temp.icon a:hover:before,
 .vector-menu-tabs #ca-unwatch.mw-watchlink-temp.icon a:focus:before {
  background-image:linear-gradient(transparent,transparent),url(/w/skins/Vector/resources/skins.vector.styles/images/unwatch-temp-icon-hl.svg?06c6c)
 }
 .vector-menu-tabs #ca-watch.icon a:hover:before,
 .vector-menu-tabs #ca-watch.icon a:focus:before {
  background-image:linear-gradient(transparent,transparent),url(/w/skins/Vector/resources/skins.vector.styles/images/watch-icon-hl.svg?84b7e)
 }
 .vector-menu-tabs #ca-unwatch.icon .loading:before,
 .vector-menu-tabs #ca-watch.icon .loading:before {
  -webkit-animation:rotate 700ms infinite linear;
  -moz-animation:rotate 700ms infinite linear;
  animation:rotate 700ms infinite linear;
  outline:0;
  cursor:default;
  pointer-events:none;
  -webkit-transform-origin:50% 50%;
  -moz-transform-origin:50% 50%;
  -ms-transform-origin:50% 50%;
  transform-origin:50% 50%
 }
 .vector-menu-dropdown {
  direction:ltr;
  float:left;
  cursor:pointer;
  position:relative;
  line-height:1.125em
 }
 .vector-menu-dropdown h3 {
  color:#54595d;
  position:relative;
  display:block;
  -webkit-box-sizing:border-box;
  -moz-box-sizing:border-box;
  box-sizing:border-box;
  padding-top:1.25em;
  padding-left:8px;
  padding-right:1.84615385em;
  font-size:0.8125em;
  font-weight:normal
 }
 .vector-menu-dropdown h3:after {
  content:'';
  background-image:url(/w/skins/Vector/resources/skins.vector.styles/images/arrow-down.svg?e7827);
  background-position:100% 50%;
  background-repeat:no-repeat;
  position:absolute;
  top:0.76923077em;
  right:8px;
  bottom:0;
  width:1.23076923em;
  opacity:0.84
 }
 .vector-menu-dropdown h3:hover,
 .vector-menu-dropdown h3:focus {
  color:#202122
 }
 .vector-menu-dropdown h3:hover:after,
 .vector-menu-dropdown h3:focus:after {
  opacity:1
 }
 .vector-menu-dropdown .vector-menu-content-list {
  background-color:#ffffff;
  list-style:none none;
  min-width:100%;
  position:absolute;
  top:2.5em;
  left:-1px;
  margin:0;
  border:1px solid #a2a9b1;
  border-top-width:0;
  padding:0;
  box-shadow:0 1px 1px 0 rgba(0,0,0,0.1);
  text-align:left;
  opacity:0;
  visibility:hidden;
  -webkit-transition:opacity 100ms;
  -moz-transition:opacity 100ms;
  transition:opacity 100ms;
  z-index:2
 }
 .vector-menu-dropdown:hover .vector-menu-content-list,
 .vector-menu-dropdown .vector-menu-checkbox:checked ~ .vector-menu-content .vector-menu-content-list {
  opacity:1;
  visibility:visible
 }
 .vector-menu-dropdown li {
  padding:0;
  margin:0;
  text-align:left;
  line-height:1em
 }
 .vector-menu-dropdown li a {
  color:#0645ad;
  display:block;
  padding:0.625em;
  white-space:nowrap;
  cursor:pointer;
  font-size:0.8125em
 }
 .vector-menu-dropdown .selected a,
 .vector-menu-dropdown .selected a:visited {
  color:#202122;
  text-decoration:none
 }
 #mw-head .vector-menu-dropdown h3 {
  background-position:right bottom;
  float:left;
  height:3.07692308em;
  margin:0 -1px 0 0;
  padding-right:1.84615385em
 }
 .vector-menu-tabs,
 .vector-menu-tabs a,
 #mw-head .vector-menu-dropdown h3 {
  background-image:url(/w/skins/Vector/resources/skins.vector.styles/images/tab-separator.png?09d4b);
  background-image:linear-gradient(to bottom,rgba(167,215,249,0) 0,#a7d7f9 100%);
  background-repeat:no-repeat;
  background-size:1px 100%
 }
 .vector-menu-checkbox {
  cursor:pointer;
  position:absolute;
  top:0;
  left:0;
  z-index:1;
  opacity:0;
  width:100%;
  height:100%;
  margin:0;
  padding:0;
  display:none
 }
 :not(:checked) > .vector-menu-checkbox {
  display:block
 }
 .vector-menu-checkbox:checked + h3:after {
  transform:scaleY(-1)
 }
 .vector-menu-checkbox:focus + h3 {
  outline:dotted 1px;
  outline:auto -webkit-focus-ring-color
 }
 .vector-menu-portal {
  margin:0 0.6em 0 0.7em;
  padding:0.25em 0;
  direction:ltr
 }
 .vector-menu-portal h3 {
  display:block;
  background-image:url(/w/skins/Vector/resources/skins.vector.styles/images/portal-separator.png?4ab04);
  background-image:linear-gradient(to right,rgba(200,204,209,0) 0,#c8ccd1 33%,#c8ccd1 66%,rgba(200,204,209,0) 100%);
  background-position:center bottom;
  background-repeat:no-repeat;
  background-size:100% 1px;
  color:#54595d;
  margin:0.5em 0 0 0.66666667em;
  border:0;
  padding:0.25em 0;
  font-size:0.75em;
  font-weight:normal;
  cursor:default
 }
 .vector-menu-portal .body,
 .vector-menu-portal .vector-menu-content {
  margin-left:0.5em;
  padding-top:0
 }
 .vector-menu-portal .body ul,
 .vector-menu-portal .vector-menu-content ul {
  list-style:none none;
  margin:0;
  padding-top:0.3em
 }
 .vector-menu-portal .body li,
 .vector-menu-portal .vector-menu-content li {
  margin:0;
  padding:0.25em 0;
  font-size:0.75em;
  line-height:1.125em;
  word-wrap:break-word
 }
 .vector-menu-portal .body li a,
 .vector-menu-portal .vector-menu-content li a {
  color:#0645ad
 }
 .vector-menu-portal .body li a:visited,
 .vector-menu-portal .vector-menu-content li a:visited {
  color:#0b0080
 }
 #mw-panel {
  font-size:inherit
 }
 #mw-panel .portal-first {
  background-image:none
 }
 #mw-panel .portal-first h3 {
  display:none
 }
 #mw-panel .portal-first .body,
 #mw-panel .portal-first .vector-menu-content {
  margin-left:0.5em
 }
 .mw-checkbox-hack-checkbox {
  display:none
 }
 .mw-checkbox-hack-button {
  display:inline-block;
  cursor:pointer
 }
 .mw-sidebar-action {
  margin:8px 0.6em 8px 1.2em
 }
 .mw-sidebar-action-link {
  font-size:0.75em;
  font-weight:bold
 }
 #mw-sidebar-button {
  min-width:2.75em;
  min-height:2.75em;
  width:2.75em;
  height:2.75em;
  border:1px solid transparent;
  border-radius:2px
 }
 #mw-sidebar-button:before {
  min-width:20px;
  min-height:20px;
  height:100%;
  margin:0 12px;
  opacity:0.67;
  background-image:url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E %3Ctitle%3E chevron %3C/title%3E %3Cpath d=%22M9 2l1.3 1.3L3.7 10l6.6 6.7L9 18l-8-8 8-8zm8.5 0L19 3.3 12.2 10l6.7 6.7-1.4 1.3-8-8 8-8z%22/%3E %3C/svg%3E")
 }
 #mw-sidebar-checkbox:not(:checked) ~ .mw-header #mw-sidebar-button:before {
  background-image:url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E %3Ctitle%3E menu %3C/title%3E %3Cpath d=%22M1 3v2h18V3zm0 8h18V9H1zm0 6h18v-2H1z%22/%3E %3C/svg%3E")
 }
 #mw-sidebar-button:hover {
  background-color:rgba(0,24,73,0.02745098)
 }
 #mw-sidebar-button:hover:before {
  opacity:1
 }
 #mw-sidebar-button:focus {
  outline:0;
  border-color:#3366cc;
  -webkit-box-shadow:inset 0 0 0 1px #3366cc;
  box-shadow:inset 0 0 0 1px #3366cc
 }
 .skin-vector-search-header-legacy #mw-sidebar-checkbox:not(:checked) ~ .mw-header .mw-sidebar,
 .skin-vector-search-header #mw-sidebar-checkbox:not(:checked) ~ .mw-workspace-container .mw-sidebar {
  visibility:hidden;
  opacity:0;
  -webkit-transform:translateX(-100%);
  -moz-transform:translateX(-100%);
  -ms-transform:translateX(-100%);
  transform:translateX(-100%)
 }
 .vector-animations-ready .mw-sidebar {
  -webkit-transition:transform 100ms ease-out,opacity 100ms ease-out,visibility 100ms ease-out;
  -moz-transition:transform 100ms ease-out,opacity 100ms ease-out,visibility 100ms ease-out;
  transition:transform 100ms ease-out,opacity 100ms ease-out,visibility 100ms ease-out
 }
 .vector-animations-ready #mw-sidebar-button {
  -webkit-transition:background-color 100ms,border-color 100ms,box-shadow 100ms;
  -moz-transition:background-color 100ms,border-color 100ms,box-shadow 100ms;
  transition:background-color 100ms,border-color 100ms,box-shadow 100ms
 }
 #p-logo {
  width:10em;
  height:160px;
  margin-bottom:1em
 }
 #p-logo a {
  background-position:center center;
  background-repeat:no-repeat;
  display:block;
  width:10em;
  height:160px;
  text-decoration:none
 }
 .mw-footer {
  padding:0.75em;
  direction:ltr
 }
 .mw-footer ul {
  list-style:none none;
  margin:0;
  padding:0
 }
 .mw-footer li {
  color:#202122;
  margin:0;
  padding:0.5em 0;
  font-size:0.75em
 }
 #footer-icons {
  float:right
 }
 #footer-icons li {
  float:left;
  margin-left:0.5em;
  line-height:2;
  text-align:right
 }
 #footer-info li {
  line-height:1.4
 }
 #footer-places li {
  float:left;
  margin-right:1em;
  line-height:2
 }
}
@media screen and (min-width:1710px) {
 .skin-vector-max-width .mw-page-container {
  border-left:1px solid #f8f9fa;
  border-right:1px solid #f8f9fa
 }
}
@media screen and (max-width:86.75em) {
 .skin-vector-max-width .mw-checkbox-hack-checkbox:checked ~ .mw-workspace-container .mw-content-container,
 .skin-vector-max-width.skin-vector-search-header-legacy .mw-checkbox-hack-checkbox:checked ~ #mw-navigation .mw-content-container,
 .skin-vector-max-width.skin-vector-search-header .mw-checkbox-hack-checkbox:checked ~ .mw-workspace-container .mw-article-toolbar-container {
  margin-left:11.5em
 }
 .skin-vector-max-width .mw-sidebar {
  -webkit-transition:none;
  -moz-transition:none;
  transition:none
 }
}
@media screen and (min-width:1500px) {
 .skin-vector-max-width #mw-panel {
  background:#ffffff;
  border-right:1px solid #f8f9fa
 }
}
@media screen and (max-width:72.375em) {
 .skin-vector-search-header #p-search #searchform {
  margin-left:auto
 }
}
@media all {
 .mw-logo {
  display:-webkit-flex;
  display:-moz-flex;
  display:-ms-flexbox;
  display:flex;
  height:100%;
  align-items:center
 }
 .mw-logo-icon {
  float:left;
  margin-right:10px
 }
 .mw-logo-container {
  float:left
 }
 .mw-logo-wordmark {
  display:block;
  margin:0 auto;
  font-size:1.4em
 }
 .mw-logo-tagline {
  display:block;
  margin:5px auto 0;
  font-size:0.7em
 }
}
@media print {
 .toc,
 body {
  padding:10px;
  font-family:'Linux Libertine','Georgia','Times',serif
 }
 .printfooter,
 .mw-footer,
 .thumb,
 table,
 ol,
 dl,
 ul,
 h3,
 h4,
 h5,
 h6 {
  font-family:sans-serif
 }
 img {
  font-family:'Linux Libertine','Georgia','Times',serif
 }
 .mw-body a:not(.image) {
  border-bottom:1px solid #aaa
 }
 .firstHeading {
  font-size:25pt;
  line-height:28pt;
  margin-bottom:20px;
  padding-bottom:5px
 }
 .firstHeading,
 h2 {
  overflow:hidden;
  border-bottom:2px solid #000000
 }
 h3,
 h4,
 h5,
 h6 {
  margin:30px 0 0
 }
 h2,
 h3,
 h4,
 h5,
 h6 {
  padding:0;
  position:relative
 }
 h2 {
  font-size:18pt;
  line-height:24pt;
  margin-bottom:0.25em
 }
 h3 {
  font-size:14pt;
  line-height:20pt
 }
 h4,
 h5,
 h6 {
  font-size:12pt;
  line-height:16pt
 }
 p {
  font-size:12pt;
  line-height:16pt;
  margin-top:5px;
  text-align:justify
 }
 p:before {
  content:'';
  display:block;
  width:120pt;
  overflow:hidden
 }
 blockquote {
  border-left:2px solid #000000;
  padding-left:20px
 }
 ol,
 ul {
  margin:10px 0 0 1.6em;
  padding:0
 }
 ol li,
 ul li {
  padding:2px 0;
  font-size:12pt
 }
 table ol li,
 table ul li {
  font-size:inherit
 }
 .toc {
  page-break-before:avoid;
  page-break-after:avoid;
  background:none;
  border:0;
  display:table
 }
 .toc a {
  border:0;
  font-weight:normal
 }
 .toc > ul > li {
  margin-bottom:4px;
  font-weight:bold
 }
 .toc ul {
  margin:0;
  list-style:none
 }
 .toc ul ul {
  padding-left:30px
 }
 .toc li.toclevel-1 > a {
  font-size:12pt;
  font-weight:bold
 }
 .mw-jump-link,
 .toc .tocnumber {
  display:none
 }
 .printfooter {
  margin-top:10px;
  border-top:3px solid #000000;
  padding-top:10px;
  font-size:10pt;
  clear:both
 }
 .mw-footer {
  margin-top:12px;
  border-top:1px solid #eeeeee;
  padding-top:5px
 }
 #footer-info {
  margin:0;
  padding:0
 }
 #footer-info li {
  color:#999;
  list-style:none;
  display:block;
  padding-bottom:10px;
  font-size:10pt
 }
 #footer-info li a {
  color:#999 !important
 }
 #footer-info-lastmod {
  color:#000000;
  font-size:12pt;
  font-weight:bold
 }
 .mw-page-container-inner {
  display:-webkit-flex;
  display:-moz-flex;
  display:-ms-flexbox;
  display:flex;
  flex-direction:column;
  align-items:flex-start
 }
 .mw-page-container-inner > * {
  width:100%
 }
 #mw-sidebar-checkbox,
 .mw-header > *:not(.mw-logo) {
  display:none
 }
 .mw-header {
  order:1
 }
 .mw-workspace-container {
  order:2
 }
}
@media screen {
 body {
  margin:0
 }
 main {
  display:block
 }
 hr {
  box-sizing:content-box;
  height:0;
  overflow:visible
 }
 abbr[title] {
  border-bottom:1px dotted;
  cursor:help
 }
 @supports (text-decoration:underline dotted) {
  abbr[title] {
   border-bottom:0;
   text-decoration:underline dotted
  }
 }
 pre,
 code,
 tt,
 kbd,
 samp {
  font-family:monospace,monospace
 }
 sub,
 sup {
  line-height:1
 }
 img {
  border:0
 }
 button::-moz-focus-inner,
 [type='button']::-moz-focus-inner,
 [type='reset']::-moz-focus-inner,
 [type='submit']::-moz-focus-inner {
  border-style:none;
  padding:0
 }
 legend {
  color:inherit;
  padding:0
 }
 a {
  text-decoration:none;
  color:#0645ad;
  background:none
 }
 a:not([href]) {
  cursor:pointer
 }
 a:visited {
  color:#0b0080
 }
 a:active {
  color:#faa700
 }
 a:hover,
 a:focus {
  text-decoration:underline
 }
 a:lang(ar),
 a:lang(kk-arab),
 a:lang(mzn),
 a:lang(ps),
 a:lang(ur) {
  text-decoration:none
 }
 a.stub {
  color:#723
 }
 a.new,
 #p-personal a.new {
  color:#d33
 }
 a.mw-selflink {
  color:inherit;
  font-weight:bold;
  text-decoration:inherit
 }
 a.mw-selflink:hover {
  cursor:inherit;
  text-decoration:inherit
 }
 a.mw-selflink:active,
 a.mw-selflink:visited {
  color:inherit
 }
 a.new:visited,
 #p-personal a.new:visited {
  color:#a55858
 }
 .mw-parser-output a.extiw,
 .mw-parser-output a.external {
  color:#36b
 }
 .mw-parser-output a.extiw:visited,
 .mw-parser-output a.external:visited {
  color:#636
 }
 .mw-parser-output a.extiw:active,
 .mw-parser-output a.external:active {
  color:#b63
 }
 .mw-parser-output a.external.free {
  word-wrap:break-word
 }
 img {
  border:0;
  vertical-align:middle
 }
 hr {
  height:1px;
  background-color:#a2a9b1;
  border:0;
  margin:0.2em 0
 }
 h1,
 h2,
 h3,
 h4,
 h5,
 h6 {
  color:#000;
  margin:0;
  padding-top:0.5em;
  padding-bottom:0.17em;
  overflow:hidden
 }
 h1,
 h2 {
  margin-bottom:0.6em;
  border-bottom:1px solid #a2a9b1
 }
 h3,
 h4,
 h5 {
  margin-bottom:0.3em
 }
 h1 {
  font-size:188%;
  font-weight:normal
 }
 h2 {
  font-size:150%;
  font-weight:normal
 }
 h3 {
  font-size:128%
 }
 h4 {
  font-size:116%
 }
 h5 {
  font-size:108%
 }
 h6 {
  font-size:100%
 }
 p {
  margin:0.4em 0 0.5em 0
 }
 p img {
  margin:0
 }
 ul {
  margin:0.3em 0 0 1.6em;
  padding:0
 }
 ol {
  margin:0.3em 0 0 3.2em;
  padding:0;
  list-style-image:none
 }
 li {
  margin-bottom:0.1em
 }
 dt {
  font-weight:bold;
  margin-bottom:0.1em
 }
 dl {
  margin-top:0.2em;
  margin-bottom:0.5em
 }
 dd {
  margin-left:1.6em;
  margin-bottom:0.1em
 }
 pre,
 code,
 tt,
 kbd,
 samp,
 .mw-code {
  font-family:monospace,monospace
 }
 code {
  color:#000;
  background-color:#f8f9fa;
  border:1px solid #eaecf0;
  border-radius:2px;
  padding:1px 4px
 }
 pre,
 .mw-code {
  color:#000;
  background-color:#f8f9fa;
  border:1px solid #eaecf0;
  padding:1em;
  white-space:pre-wrap;
  overflow-x:hidden;
  word-wrap:break-word
 }
 table {
  font-size:100%
 }
 fieldset {
  border:1px solid #2a4b8d;
  margin:1em 0 1em 0;
  padding:0 1em 1em
 }
 legend {
  padding:0.5em;
  font-size:95%
 }
 form {
  border:0;
  margin:0
 }
 textarea {
  width:100%;
  padding:0.1em;
  display:block;
  -moz-box-sizing:border-box;
  -webkit-box-sizing:border-box;
  box-sizing:border-box
 }
 .center {
  width:100%;
  text-align:center
 }
 *.center * {
  margin-left:auto;
  margin-right:auto
 }
 .small {
  font-size:94%
 }
 table.small {
  font-size:100%
 }
 .toc,
 .mw-warning,
 .toccolours {
  border:1px solid #a2a9b1;
  background-color:#f8f9fa;
  padding:5px;
  font-size:95%
 }
 .toc {
  display:table;
  padding:7px
 }
 table.toc {
  border-collapse:collapse
 }
 table.toc td {
  padding:0
 }
 .toc h2 {
  display:inline;
  border:0;
  padding:0;
  font-size:100%;
  font-weight:bold
 }
 .toc .toctitle {
  text-align:center
 }
 .toc ul {
  list-style-type:none;
  list-style-image:none;
  margin-left:0;
  padding:0;
  text-align:left
 }
 .toc ul ul {
  margin:0 0 0 2em
 }
 .tocnumber,
 .toctext {
  display:table-cell;
  text-decoration:inherit
 }
 .tocnumber {
  color:#202122;
  padding-left:0;
  padding-right:0.5em
 }
 .mw-content-ltr .tocnumber {
  padding-left:0;
  padding-right:0.5em
 }
 .mw-content-rtl .tocnumber {
  padding-left:0.5em;
  padding-right:0
 }
 .mw-warning {
  margin-left:50px;
  margin-right:50px;
  text-align:center
 }
 div.floatright,
 table.floatright {
  margin:0 0 0.5em 0.5em
 }
 div.floatleft,
 table.floatleft {
  margin:0 0.5em 0.5em 0
 }
 div.thumb {
  margin-bottom:0.5em;
  width:auto;
  background-color:transparent
 }
 div.thumbinner {
  border:1px solid #c8ccd1;
  padding:3px;
  background-color:#f8f9fa;
  font-size:94%;
  text-align:center;
  overflow:hidden
 }
 html .thumbimage {
  background-color:#fff;
  border:1px solid #c8ccd1
 }
 html .thumbcaption {
  border:0;
  line-height:1.4em;
  padding:3px;
  font-size:94%;
  text-align:left
 }
 .magnify {
  float:right;
  margin-left:3px
 }
 .magnify a {
  display:block;
  text-indent:15px;
  white-space:nowrap;
  overflow:hidden;
  width:15px;
  height:11px;
  background-image:url(/w/resources/src/mediawiki.skinning/images/magnify-clip-ltr.png?4f704);
  background-image:linear-gradient(transparent,transparent),url(/w/resources/src/mediawiki.skinning/images/magnify-clip-ltr.svg?8330e);
  -moz-user-select:none;
  -webkit-user-select:none;
  -ms-user-select:none;
  user-select:none
 }
 img.thumbborder {
  border:1px solid #eaecf0
 }
 .mw-content-ltr .thumbcaption {
  text-align:left
 }
 .mw-content-ltr .magnify {
  float:right;
  margin-left:3px;
  margin-right:0
 }
 .mw-content-ltr .magnify a {
  background-image:url(/w/resources/src/mediawiki.skinning/images/magnify-clip-ltr.png?4f704);
  background-image:linear-gradient(transparent,transparent),url(/w/resources/src/mediawiki.skinning/images/magnify-clip-ltr.svg?8330e)
 }
 .mw-content-rtl .thumbcaption {
  text-align:right
 }
 .mw-content-rtl .magnify {
  float:left;
  margin-left:0;
  margin-right:3px
 }
 .mw-content-rtl .magnify a {
  background-image:url(/w/resources/src/mediawiki.skinning/images/magnify-clip-rtl.png?a9fb3);
  background-image:linear-gradient(transparent,transparent),url(/w/resources/src/mediawiki.skinning/images/magnify-clip-rtl.svg?38fd5)
 }
 div.tright {
  margin:0.5em 0 1.3em 1.4em
 }
 div.tleft {
  margin:0.5em 1.4em 1.3em 0
 }
 body.mw-hide-empty-elt .mw-empty-elt {
  display:none
 }
 .catlinks {
  border:1px solid #a2a9b1;
  background-color:#f8f9fa;
  padding:5px;
  margin-top:1em;
  clear:both
 }
 textarea {
  border:1px solid #c8ccd1
 }
 .editOptions {
  background-color:#eaecf0;
  color:#202122;
  border:1px solid #c8ccd1;
  border-top:0;
  padding:1em 1em 1.5em 1em;
  margin-bottom:2em
 }
 .usermessage {
  background-color:#ffce7b;
  border:1px solid #ffa500;
  color:#000;
  font-weight:bold;
  margin:2em 0 1em;
  padding:0.5em 1em;
  vertical-align:middle
 }
 #siteNotice {
  position:relative;
  text-align:center;
  margin:0
 }
 #localNotice {
  margin-bottom:0.9em
 }
 #siteSub {
  display:none
 }
 #contentSub,
 #contentSub2 {
  font-size:84%;
  line-height:1.2em;
  margin:0 0 1.4em 1em;
  color:#54595d;
  width:auto
 }
 span.subpages {
  display:block
 }
 .emptyPortlet {
  display:none
 }
 .printfooter,
 .client-nojs #t-print {
  display:none
 }
 .mw-content-ltr {
  direction:ltr
 }
 .mw-content-rtl {
  direction:rtl
 }
 .sitedir-ltr textarea,
 .sitedir-ltr input,
 textarea[dir='ltr'][dir='ltr'],
 input[dir='ltr'][dir='ltr'] {
  direction:ltr
 }
 .sitedir-rtl textarea,
 .sitedir-rtl input,
 textarea[dir='rtl'][dir='rtl'],
 input[dir='rtl'][dir='rtl'] {
  direction:rtl
 }
 .mw-userlink {
  word-wrap:break-word;
  -webkit-hyphens:auto;
  -moz-hyphens:auto;
  -ms-hyphens:auto;
  hyphens:auto;
  unicode-bidi:embed
 }
 mark {
  background-color:#ff0;
  color:#000
 }
 wbr {
  display:inline-block
 }
 input[type='submit'],
 input[type='button'],
 input[type='reset'],
 input[type='file'] {
  direction:ltr
 }
 abbr[title],
 .explain[title] {
  border-bottom:1px dotted;
  cursor:help
 }
 @supports (text-decoration:underline dotted) {
  abbr[title],
  .explain[title] {
   border-bottom:0;
   text-decoration:underline dotted
  }
 }
 span.comment {
  font-style:italic;
  unicode-bidi:-moz-isolate;
  unicode-bidi:isolate
 }
 #editform,
 #toolbar,
 #wpTextbox1 {
  clear:both
 }
 #toolbar {
  height:22px
 }
 .mw-underline-always a {
  text-decoration:underline
 }
 .mw-underline-never a {
  text-decoration:none
 }
 li span.deleted,
 span.history-deleted {
  text-decoration:line-through;
  color:#72777d;
  font-style:italic
 }
 .not-patrolled {
  background-color:#ffa
 }
 .unpatrolled {
  font-weight:bold;
  color:#d33
 }
 div.patrollink {
  font-size:75%;
  text-align:right
 }
 td.mw-label {
  text-align:right;
  vertical-align:middle
 }
 td.mw-input {
  text-align:left
 }
 td.mw-submit {
  text-align:left;
  white-space:nowrap
 }
 .mw-input-with-label {
  white-space:nowrap;
  display:inline-block
 }
 .mw-content-ltr .thumbcaption {
  text-align:left
 }
 .mw-content-ltr .magnify {
  float:right
 }
 .mw-content-rtl .thumbcaption {
  text-align:right
 }
 .mw-content-rtl .magnify {
  float:left
 }
 #catlinks {
  text-align:left
 }
 .catlinks ul {
  display:inline;
  margin:0;
  padding:0;
  list-style:none none
 }
 .catlinks li {
  display:inline-block;
  line-height:1.25em;
  border-left:1px solid #a2a9b1;
  margin:0.125em 0;
  padding:0 0.5em
 }
 .catlinks li:first-child {
  padding-left:0.25em;
  border-left:0
 }
 .catlinks li a.mw-redirect {
  font-style:italic
 }
 .mw-hidden-cats-hidden {
  display:none
 }
 .catlinks-allhidden {
  display:none
 }
 p.mw-protect-editreasons,
 p.mw-filedelete-editreasons,
 p.mw-delete-editreasons {
  font-size:90%;
  text-align:right
 }
 .autocomment,
 .autocomment a,
 .autocomment a:visited {
  color:#72777d
 }
 .newpage,
 .minoredit,
 .botedit {
  font-weight:bold
 }
 .mw-warning-with-logexcerpt {
  clear:both
 }
 .mw-warning-with-logexcerpt ul li {
  font-size:90%
 }
 span.mw-revdelundel-link,
 strong.mw-revdelundel-link {
  font-size:90%
 }
 span.mw-revdelundel-hidden,
 input.mw-revdelundel-hidden {
  visibility:hidden
 }
 td.mw-revdel-checkbox,
 th.mw-revdel-checkbox {
  padding-right:10px;
  text-align:center
 }
 a.new {
  color:#ba0000
 }
 .plainlinks a.external {
  background:none !important;
  padding:0 !important
 }
 .rtl a.external.free,
 .rtl a.external.autonumber {
  direction:ltr;
  unicode-bidi:embed
 }
 .wikitable {
  background-color:#f8f9fa;
  color:#202122;
  margin:1em 0;
  border:1px solid #a2a9b1;
  border-collapse:collapse
 }
 .wikitable > tr > th,
 .wikitable > tr > td,
 .wikitable > * > tr > th,
 .wikitable > * > tr > td {
  border:1px solid #a2a9b1;
  padding:0.2em 0.4em
 }
 .wikitable > tr > th,
 .wikitable > * > tr > th {
  background-color:#eaecf0;
  text-align:center
 }
 .wikitable > caption {
  font-weight:bold
 }
 .error,
 .warning,
 .success {
  font-size:larger
 }
 .error {
  color:#d33
 }
 .warning {
  color:#ac6600
 }
 .success {
  color:#14866d
 }
 .mw-infobox {
  border:2px solid #fc3;
  margin:0.5em;
  clear:left;
  overflow:hidden
 }
 .mw-infobox-left {
  margin:7px;
  float:left;
  width:35px
 }
 .mw-infobox-right {
  margin:0.5em 0.5em 0.5em 49px
 }
 .previewnote {
  margin-bottom:1em
 }
 .visualClear {
  clear:both
 }
 .mw-datatable {
  border:1px solid #a2a9b1;
  border-collapse:collapse
 }
 .mw-datatable td,
 .mw-datatable th {
  border:1px solid #a2a9b1;
  padding:0.2em 0.4em
 }
 .mw-datatable th {
  background-color:#eaeeff
 }
 .mw-datatable td {
  background-color:#fff
 }
 .mw-datatable tr:hover td {
  background-color:#eaf3ff
 }
 .mw-ajax-loader {
  background-image:url(/w/resources/src/mediawiki.skinning/images/ajax-loader.gif?57f34);
  background-position:center center;
  background-repeat:no-repeat;
  padding:16px;
  position:relative;
  top:-16px
 }
 .mw-small-spinner {
  padding:10px !important;
  margin-right:0.6em;
  background-image:url(/w/resources/src/mediawiki.skinning/images/spinner.gif?ca65b);
  background-position:center center;
  background-repeat:no-repeat
 }
 .mw-content-ltr ul,
 .mw-content-rtl .mw-content-ltr ul {
  margin:0.3em 0 0 1.6em;
  padding:0
 }
 .mw-content-rtl ul,
 .mw-content-ltr .mw-content-rtl ul {
  margin:0.3em 1.6em 0 0;
  padding:0
 }
 .mw-content-ltr ol,
 .mw-content-rtl .mw-content-ltr ol {
  margin:0.3em 0 0 3.2em;
  padding:0
 }
 .mw-content-rtl ol,
 .mw-content-ltr .mw-content-rtl ol {
  margin:0.3em 3.2em 0 0;
  padding:0
 }
 .mw-content-ltr dd,
 .mw-content-rtl .mw-content-ltr dd {
  margin-left:1.6em;
  margin-right:0
 }
 .mw-content-rtl dd,
 .mw-content-ltr .mw-content-rtl dd {
  margin-right:1.6em;
  margin-left:0
 }
 h1:lang(anp),
 h1:lang(as),
 h1:lang(bh),
 h1:lang(bho),
 h1:lang(bn),
 h1:lang(gu),
 h1:lang(hi),
 h1:lang(kn),
 h1:lang(ks),
 h1:lang(ml),
 h1:lang(mr),
 h1:lang(my),
 h1:lang(mai),
 h1:lang(ne),
 h1:lang(new),
 h1:lang(or),
 h1:lang(pa),
 h1:lang(pi),
 h1:lang(sa),
 h1:lang(ta),
 h1:lang(te) {
  line-height:1.6em !important
 }
 h2:lang(anp),
 h3:lang(anp),
 h4:lang(anp),
 h5:lang(anp),
 h6:lang(anp),
 h2:lang(as),
 h3:lang(as),
 h4:lang(as),
 h5:lang(as),
 h6:lang(as),
 h2:lang(bho),
 h3:lang(bho),
 h4:lang(bho),
 h5:lang(bho),
 h6:lang(bho),
 h2:lang(bh),
 h3:lang(bh),
 h4:lang(bh),
 h5:lang(bh),
 h6:lang(bh),
 h2:lang(bn),
 h3:lang(bn),
 h4:lang(bn),
 h5:lang(bn),
 h6:lang(bn),
 h2:lang(gu),
 h3:lang(gu),
 h4:lang(gu),
 h5:lang(gu),
 h6:lang(gu),
 h2:lang(hi),
 h3:lang(hi),
 h4:lang(hi),
 h5:lang(hi),
 h6:lang(hi),
 h2:lang(kn),
 h3:lang(kn),
 h4:lang(kn),
 h5:lang(kn),
 h6:lang(kn),
 h2:lang(ks),
 h3:lang(ks),
 h4:lang(ks),
 h5:lang(ks),
 h6:lang(ks),
 h2:lang(ml),
 h3:lang(ml),
 h4:lang(ml),
 h5:lang(ml),
 h6:lang(ml),
 h2:lang(mr),
 h3:lang(mr),
 h4:lang(mr),
 h5:lang(mr),
 h6:lang(mr),
 h2:lang(my),
 h3:lang(my),
 h4:lang(my),
 h5:lang(my),
 h6:lang(my),
 h2:lang(mai),
 h3:lang(mai),
 h4:lang(mai),
 h5:lang(mai),
 h6:lang(mai),
 h2:lang(ne),
 h3:lang(ne),
 h4:lang(ne),
 h5:lang(ne),
 h6:lang(ne),
 h2:lang(new),
 h3:lang(new),
 h4:lang(new),
 h5:lang(new),
 h6:lang(new),
 h2:lang(or),
 h3:lang(or),
 h4:lang(or),
 h5:lang(or),
 h6:lang(or),
 h2:lang(pa),
 h3:lang(pa),
 h4:lang(pa),
 h5:lang(pa),
 h6:lang(pa),
 h2:lang(pi),
 h3:lang(pi),
 h4:lang(pi),
 h5:lang(pi),
 h6:lang(pi),
 h2:lang(sa),
 h3:lang(sa),
 h4:lang(sa),
 h5:lang(sa),
 h6:lang(sa),
 h2:lang(ta),
 h3:lang(ta),
 h4:lang(ta),
 h5:lang(ta),
 h6:lang(ta),
 h2:lang(te),
 h3:lang(te),
 h4:lang(te),
 h5:lang(te),
 h6:lang(te) {
  line-height:1.2em
 }
 ol:lang(azb) li,
 ol:lang(bcc) li,
 ol:lang(bgn) li,
 ol:lang(bqi) li,
 ol:lang(fa) li,
 ol:lang(glk) li,
 ol:lang(kk-arab) li,
 ol:lang(lrc) li,
 ol:lang(luz) li,
 ol:lang(mzn) li {
  list-style-type:persian
 }
 ol:lang(ckb) li,
 ol:lang(sdh) li {
  list-style-type:arabic-indic
 }
 ol:lang(hi) li,
 ol:lang(mai) li,
 ol:lang(mr) li,
 ol:lang(ne) li {
  list-style-type:devanagari
 }
 ol:lang(as) li,
 ol:lang(bn) li {
  list-style-type:bengali
 }
 ol:lang(or) li {
  list-style-type:oriya
 }
 .toc ul {
  margin:0.3em 0
 }
 .mw-content-ltr .toc ul,
 .mw-content-rtl .mw-content-ltr .toc ul {
  text-align:left
 }
 .mw-content-rtl .toc ul,
 .mw-content-ltr .mw-content-rtl .toc ul {
  text-align:right
 }
 .mw-content-ltr .toc ul ul,
 .mw-content-rtl .mw-content-ltr .toc ul ul {
  margin:0 0 0 2em
 }
 .mw-content-rtl .toc ul ul,
 .mw-content-ltr .mw-content-rtl .toc ul ul {
  margin:0 2em 0 0
 }
 .toc .toctitle {
  direction:ltr
 }
 #mw-clearyourcache,
 #mw-sitecsspreview,
 #mw-sitejspreview,
 #mw-usercsspreview,
 #mw-userjspreview {
  direction:ltr;
  unicode-bidi:embed
 }
 #mw-revision-info,
 #mw-revision-info-current,
 #mw-revision-nav {
  direction:ltr
 }
 div.tright,
 div.floatright,
 table.floatright {
  clear:right;
  float:right
 }
 div.tleft,
 div.floatleft,
 table.floatleft {
  float:left;
  clear:left
 }
 #mw-credits a {
  unicode-bidi:embed
 }
 .printfooter {
  display:none
 }
 .xdebug-error {
  position:absolute;
  z-index:99
 }
 .mw-editsection {
  -moz-user-select:none;
  -webkit-user-select:none;
  -ms-user-select:none;
  user-select:none
 }
 .mw-editsection,
 .mw-editsection-like {
  font-size:small;
  font-weight:normal;
  margin-left:1em;
  vertical-align:baseline;
  line-height:1em
 }
 .mw-content-ltr .mw-editsection,
 .mw-content-rtl .mw-content-ltr .mw-editsection {
  margin-left:1em
 }
 .mw-content-rtl .mw-editsection,
 .mw-content-ltr .mw-content-rtl .mw-editsection {
  margin-right:1em
 }
 sup,
 sub {
  line-height:1
 }
}
@media print {
 .noprint,
 .catlinks,
 .magnify,
 .mw-cite-backlink,
 .mw-editsection,
 .mw-editsection-like,
 .mw-hidden-catlinks,
 .mw-indicators,
 .mw-redirectedfrom,
 .patrollink,
 .usermessage,
 #column-one,
 #footer-places,
 #mw-navigation,
 #siteNotice,
 #f-poweredbyico,
 #f-copyrightico,
 li#about,
 li#disclaimer,
 li#mobileview,
 li#privacy {
  display:none
 }
 body {
  background:#fff;
  color:#000;
  margin:0;
  padding:0
 }
 a {
  background:none !important;
  padding:0 !important
 }
 a,
 a.external,
 a.new,
 a.stub {
  color:inherit !important;
  text-decoration:inherit !important
 }
 .mw-parser-output a.external.text:after,
 .mw-parser-output a.external.autonumber:after {
  content:' (' attr(href) ')';
  word-break:break-all;
  word-wrap:break-word
 }
 .mw-parser-output a.external.text[href^='//']:after,
 .mw-parser-output a.external.autonumber[href^='//']:after {
  content:' (https:' attr(href) ')'
 }
 dt {
  font-weight:bold
 }
 h1,
 h2,
 h3,
 h4,
 h5,
 h6 {
  font-weight:bold;
  page-break-after:avoid;
  page-break-before:avoid
 }
 p {
  margin:1em 0;
  line-height:1.2;
  orphans:3;
  widows:3
 }
 img,
 figure,
 .wikitable,
 .thumb {
  page-break-inside:avoid
 }
 img {
  border:0;
  vertical-align:middle
 }
 pre,
 .mw-code {
  background:#fff;
  color:#000;
  border:1pt dashed #000;
  padding:1em;
  font-size:8pt;
  white-space:pre-wrap;
  overflow-x:hidden;
  word-wrap:break-word
 }
 sup,
 sub {
  line-height:1
 }
 ul {
  list-style-type:square
 }
 #globalWrapper {
  width:100% !important;
  min-width:0 !important
 }
 .mw-body {
  background:#fff;
  color:#000;
  border:0 !important;
  padding:0 !important;
  margin:0 !important;
  direction:ltr
 }
 #column-content {
  margin:0 !important
 }
 #column-content .mw-body {
  padding:1em;
  margin:0 !important
 }
 .toc {
  background-color:#f9f9f9;
  border:1pt solid #aaa;
  padding:5px;
  display:table
 }
 .tocnumber,
 .toctext {
  display:table-cell
 }
 .tocnumber {
  padding-left:0;
  padding-right:0.5em
 }
 .mw-content-ltr .tocnumber {
  padding-left:0;
  padding-right:0.5em
 }
 .mw-content-rtl .tocnumber {
  padding-left:0.5em;
  padding-right:0
 }
 table.floatright,
 div.floatright,
 div.tright {
  float:right;
  clear:right
 }
 table.floatleft,
 div.floatleft,
 div.tleft {
  float:left;
  clear:left
 }
 div.tleft {
  margin:0.5em 1.4em 1.3em 0
 }
 div.tright {
  margin:0.5em 0 1.3em 1.4em
 }
 table.floatright,
 div.floatright {
  margin:0 0 0.5em 0.5em;
  border:0
 }
 table.floatleft,
 div.floatleft {
  margin:0 0.5em 0.5em 0;
  border:0
 }
 .center {
  text-align:center
 }
 div.thumb {
  background-color:transparent;
  width:auto
 }
 div.thumb a {
  border-bottom:0
 }
 div.thumbinner {
  background-color:#fff;
  border:0;
  border-radius:2px;
  padding:5px;
  font-size:10pt;
  color:#666;
  text-align:center;
  overflow:hidden;
  min-width:100px
 }
 html .thumbcaption {
  text-align:left;
  line-height:1.4;
  padding:3px
 }
 img.thumbborder {
  border:1pt solid #ddd
 }
 .wikitable,
 .mw_metadata {
  background:#fff;
  margin:1em 0;
  border:1pt solid #aaa;
  border-collapse:collapse;
  font-size:10pt
 }
 .wikitable > caption,
 .mw_metadata caption {
  padding:5px;
  font-size:10pt
 }
 .wikitable > tr > th,
 .wikitable > tr > td,
 .wikitable > * > tr > th,
 .wikitable > * > tr > td,
 .mw_metadata th,
 .mw_metadata td {
  background:#fff !important;
  color:#000 !important;
  border:1pt solid #aaa;
  padding:0.4em 0.6em
 }
 .wikitable > tr > th,
 .wikitable > * > tr > th,
 .mw_metadata th {
  text-align:center
 }
 table.listing,
 table.listing td {
  border:1pt solid #000;
  border-collapse:collapse
 }
 .catlinks ul {
  display:inline;
  padding:0;
  list-style:none none
 }
 .catlinks li {
  display:inline-block;
  line-height:1.15;
  margin:0.1em 0;
  border-left:1pt solid #aaa;
  padding:0 0.4em
 }
 .catlinks li:first-child {
  border-left:0;
  padding-left:0.2em
 }
 .printfooter {
  padding:1em 0
 }
 #footer {
  background:#fff;
  color:#000;
  margin-top:1em;
  border-top:1pt solid #aaa;
  padding-top:5px;
  direction:ltr
 }
}
.wb-langlinks-link {
 line-height:1.125em;
 font-size:0.75em;
 float:right
}
.wb-langlinks-link {
 list-style:none none;
 text-align:right;
 padding-right:0.5em !important
}
.wb-langlinks-link > a:before {
 content:'';
 background-image:url(/w/extensions/Wikibase/client/resources/images/edit.png?52328);
 background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2212%22 height=%2212%22 viewBox=%220 0 12 12%22%3E %3Cpath fill=%22%230645ad%22 d=%22M10.5 4.7l1.3-1.3c.3-.3.3-.7 0-.9L9.6.2c-.3-.3-.7-.3-.9 0L7.3 1.5l3.2 3.2zM6.6 2.2L0 8.8V12h3.2l6.6-6.6-3.2-3.2z%22/%3E %3C/svg%3E");
 background-position:left top;
 background-repeat:no-repeat;
 -webkit-background-size:10px 10px;
 background-size:10px 10px;
 display:inline-block;
 width:10px;
 height:10px;
 margin-right:2px;
 vertical-align:top
}
.wb-langlinks-link > a:link,
.wb-langlinks-link > a:visited {
 color:#54595d !important
}
.wb-langlinks-link > a:link:before,
.wb-langlinks-link > a:visited:before {
 -webkit-filter:grayscale(1);
 filter:grayscale(1);
 opacity:0.73
}
.wb-langlinks-link > a:hover {
 color:#0645ad !important
}
.wb-langlinks-link > a:hover:before {
 -webkit-filter:none;
 filter:none;
 opacity:1
}
div.after-portlet-lang:after {
 content:'';
 clear:both;
 display:block
}







</style>""")