"use strict";(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[5299],{65447:function(e){function csp(e){!function(e){function value(e){return RegExp(/([ \t])/.source+"(?:"+e+")"+/(?=[\s;]|$)/.source,"i")}e.languages.csp={directive:{pattern:/(^|[\s;])(?:base-uri|block-all-mixed-content|(?:child|connect|default|font|frame|img|manifest|media|object|prefetch|script|style|worker)-src|disown-opener|form-action|frame-(?:ancestors|options)|input-protection(?:-(?:clip|selectors))?|navigate-to|plugin-types|policy-uri|referrer|reflected-xss|report-(?:to|uri)|require-sri-for|sandbox|(?:script|style)-src-(?:attr|elem)|upgrade-insecure-requests)(?=[\s;]|$)/i,lookbehind:!0,alias:"property"},scheme:{pattern:value(/[a-z][a-z0-9.+-]*:/.source),lookbehind:!0},none:{pattern:value(/'none'/.source),lookbehind:!0,alias:"keyword"},nonce:{pattern:value(/'nonce-[-+/\w=]+'/.source),lookbehind:!0,alias:"number"},hash:{pattern:value(/'sha(?:256|384|512)-[-+/\w=]+'/.source),lookbehind:!0,alias:"number"},host:{pattern:value(/[a-z][a-z0-9.+-]*:\/\/[^\s;,']*/.source+"|"+/\*[^\s;,']*/.source+"|"+/[a-z0-9-]+(?:\.[a-z0-9-]+)+(?::[\d*]+)?(?:\/[^\s;,']*)?/.source),lookbehind:!0,alias:"url",inside:{important:/\*/}},keyword:[{pattern:value(/'unsafe-[a-z-]+'/.source),lookbehind:!0,alias:"unsafe"},{pattern:value(/'[a-z-]+'/.source),lookbehind:!0,alias:"safe"}],punctuation:/;/}}(e)}e.exports=csp,csp.displayName="csp",csp.aliases=[]}}]);