(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[75773,68126,88119,63047],{75773:function(e,t,n){"use strict";var a=n(64836);Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var r=a(n(66055));t.default=r.default},66055:function(e,t,n){"use strict";var a=n(59803),r=n(93205);function o(e){e.register(a),e.register(r),e.languages.etlua={delimiter:{pattern:/^<%[-=]?|-?%>$/,alias:"punctuation"},"language-lua":{pattern:/[\s\S]+/,inside:e.languages.lua}},e.hooks.add("before-tokenize",function(t){e.languages["markup-templating"].buildPlaceholders(t,"etlua",/<%[\s\S]+?%>/g)}),e.hooks.add("after-tokenize",function(t){e.languages["markup-templating"].tokenizePlaceholders(t,"etlua")})}e.exports=o,o.displayName="etlua",o.aliases=[]},59803:function(e){"use strict";function t(e){e.languages.lua={comment:/^#!.+|--(?:\[(=*)\[[\s\S]*?\]\1\]|.*)/m,string:{pattern:/(["'])(?:(?!\1)[^\\\r\n]|\\z(?:\r\n|\s)|\\(?:\r\n|[^z]))*\1|\[(=*)\[[\s\S]*?\]\2\]/,greedy:!0},number:/\b0x[a-f\d]+(?:\.[a-f\d]*)?(?:p[+-]?\d+)?\b|\b\d+(?:\.\B|(?:\.\d*)?(?:e[+-]?\d+)?\b)|\B\.\d+(?:e[+-]?\d+)?\b/i,keyword:/\b(?:and|break|do|else|elseif|end|false|for|function|goto|if|in|local|nil|not|or|repeat|return|then|true|until|while)\b/,function:/(?!\d)\w+(?=\s*(?:[({]))/,operator:[/[-+*%^&|#]|\/\/?|<[<=]?|>[>=]?|[=~]=?/,{pattern:/(^|[^.])\.\.(?!\.)/,lookbehind:!0}],punctuation:/[\[\](){},;]|\.+|:+/}}e.exports=t,t.displayName="lua",t.aliases=[]},93205:function(e){"use strict";function t(e){!function(e){function t(e,t){return"___"+e.toUpperCase()+t+"___"}Object.defineProperties(e.languages["markup-templating"]={},{buildPlaceholders:{value:function(n,a,r,o){if(n.language===a){var u=n.tokenStack=[];n.code=n.code.replace(r,function(e){if("function"==typeof o&&!o(e))return e;for(var r,i=u.length;-1!==n.code.indexOf(r=t(a,i));)++i;return u[i]=e,r}),n.grammar=e.languages.markup}}},tokenizePlaceholders:{value:function(n,a){if(n.language===a&&n.tokenStack){n.grammar=e.languages[a];var r=0,o=Object.keys(n.tokenStack);!function u(i){for(var s=0;s<i.length&&!(r>=o.length);s++){var l=i[s];if("string"==typeof l||l.content&&"string"==typeof l.content){var c=o[r],f=n.tokenStack[c],p="string"==typeof l?l:l.content,g=t(a,c),d=p.indexOf(g);if(d>-1){++r;var k=p.substring(0,d),m=new e.Token(a,e.tokenize(f,n.grammar),"language-"+a,f),b=p.substring(d+g.length),h=[];k&&h.push.apply(h,u([k])),h.push(m),b&&h.push.apply(h,u([b])),"string"==typeof l?i.splice.apply(i,[s,1].concat(h)):l.content=h}}else l.content&&u(l.content)}return i}(n.tokens)}}}})}(e)}e.exports=t,t.displayName="markupTemplating",t.aliases=[]},64836:function(e){e.exports=function(e){return e&&e.__esModule?e:{default:e}},e.exports.__esModule=!0,e.exports.default=e.exports}}]);