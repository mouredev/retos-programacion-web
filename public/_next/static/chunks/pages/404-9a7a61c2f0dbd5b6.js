(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[92197],{20394:function(t,e,n){(window.__NEXT_P=window.__NEXT_P||[]).push(["/404",function(){return n(66367)}])},66367:function(t,e,n){"use strict";n.r(e),n.d(e,{Div_bd4c022a8f796682aa6392e9d4c102e9:function(){return x},Fragment_9017984ada32ffa55f5d2870ebd3c887:function(){return w},Toaster_6e6ebf8d7ce589d59b7d382fb7576edf:function(){return b},default:function(){return v}});var o=n(82729),r=n(35944),i=n(67294),c=n(48039),s=n(59654),a=n(52377),u=n(70917),d=n(64712),f=n(73954),l=n(12918),h=n.n(l),m=n(11163);let p=()=>{let[t,e]=(0,i.useState)(!1),n=(0,i.useRef)(!1),o=(0,m.useRouter)();return(0,i.useEffect)(()=>{o.isReady&&!n.current&&(n.current=!0,o.replace({pathname:window.location.pathname,query:window.location.search.slice(1)}).then(()=>{"/404"===o.pathname&&e(!0)}).catch(t=>{e(!0)}))},[o.isReady]),t};var g=n(9008),_=n.n(g);function Z(){let t=(0,o._)(["\n    0% {\n        opacity: 0;\n    }\n    100% {\n        opacity: 1;\n    }\n"]);return Z=function(){return t},t}function x(){let[t,e]=(0,i.useContext)(c.EventLoopContext);return(0,r.tZ)("div",{css:{position:"fixed",width:"100vw",height:"0"},title:"Connection Error: "+(e.length>0?e[e.length-1].message:""),children:(0,r.tZ)(w,{})})}let C=(0,u.keyframes)(Z());function w(){let[t,e]=(0,i.useContext)(c.EventLoopContext);return(0,r.tZ)(i.Fragment,{children:(0,s.isTrue)(e.length>0)?(0,r.tZ)(i.Fragment,{children:(0,r.tZ)(a.Z,{css:{color:"crimson",zIndex:9999,position:"fixed",bottom:"33px",right:"33px",animation:C+" 1s infinite"},size:32})}):(0,r.tZ)(i.Fragment,{})})}function b(){let{resolvedColorMode:t}=(0,i.useContext)(c.ColorModeContext);s.refs.__toast=d.Am;let[e,n]=(0,i.useContext)(c.EventLoopContext),o={description:"Check if server is reachable at "+(0,s.getBackendURL)(f.Ks).href,closeButton:!0,duration:12e4,id:"websocket-error"},[a,u]=(0,i.useState)(!1);return(0,i.useEffect)(()=>{n.length>=2?a||d.Am.error("Cannot connect to server: ".concat(n.length>0?n[n.length-1].message:"","."),{...o,onDismiss:()=>u(!0)}):(d.Am.dismiss("websocket-error"),u(!1))},[n]),(0,r.tZ)(d.x7,{closeButton:!1,expand:!0,position:"bottom-right",richColors:!0,theme:t})}function v(){let t=p();return(0,r.BX)(i.Fragment,{children:[(0,r.BX)(i.Fragment,{children:[(0,r.tZ)(x,{}),(0,r.tZ)(b,{})]}),(0,r.tZ)(i.Fragment,{children:(0,s.isTrue)(t)?(0,r.tZ)(i.Fragment,{children:(0,r.tZ)(h(),{statusCode:404})}):(0,r.tZ)(i.Fragment,{})}),(0,r.BX)(_(),{children:[(0,r.tZ)("title",{children:"404 - Not Found"}),(0,r.tZ)("meta",{content:"The page was not found",name:"description"}),(0,r.tZ)("meta",{content:"favicon.ico",property:"og:image"})]})]})}},12918:function(t,e,n){t.exports=n(2111)}},function(t){t.O(0,[94346,92888,49774,40179],function(){return t(t.s=20394)}),_N_E=t.O()}]);