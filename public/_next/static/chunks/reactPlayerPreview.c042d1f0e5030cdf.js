(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[7664],{83855:function(e,t,r){let a,n,l;var i=Object.create,s=Object.defineProperty,o=Object.getOwnPropertyDescriptor,p=Object.getOwnPropertyNames,u=Object.getPrototypeOf,d=Object.prototype.hasOwnProperty,c=(e,t,r)=>t in e?s(e,t,{enumerable:!0,configurable:!0,writable:!0,value:r}):e[t]=r,h=(e,t,r,a)=>{if(t&&"object"==typeof t||"function"==typeof t)for(let n of p(t))d.call(e,n)||n===r||s(e,n,{get:()=>t[n],enumerable:!(a=o(t,n))||a.enumerable});return e},m=(e,t,r)=>(c(e,"symbol"!=typeof t?t+"":t,r),r),f={};((e,t)=>{for(var r in t)s(e,r,{get:t[r],enumerable:!0})})(f,{default:()=>_}),e.exports=h(s({},"__esModule",{value:!0}),f);var b=(l=null!=(a=r(67294))?i(u(a)):{},h(!n&&a&&a.__esModule?l:s(l,"default",{value:a,enumerable:!0}),a));let g="64px",y={};class _ extends b.Component{constructor(){super(...arguments),m(this,"mounted",!1),m(this,"state",{image:null}),m(this,"handleKeyPress",e=>{("Enter"===e.key||" "===e.key)&&this.props.onClick()})}componentDidMount(){this.mounted=!0,this.fetchImage(this.props)}componentDidUpdate(e){let{url:t,light:r}=this.props;(e.url!==t||e.light!==r)&&this.fetchImage(this.props)}componentWillUnmount(){this.mounted=!1}fetchImage({url:e,light:t,oEmbedUrl:r}){if(!b.default.isValidElement(t)){if("string"==typeof t){this.setState({image:t});return}if(y[e]){this.setState({image:y[e]});return}return this.setState({image:null}),window.fetch(r.replace("{url}",e)).then(e=>e.json()).then(t=>{if(t.thumbnail_url&&this.mounted){let r=t.thumbnail_url.replace("height=100","height=480").replace("-d_295x166","-d_640");this.setState({image:r}),y[e]=r}})}}render(){let{light:e,onClick:t,playIcon:r,previewTabIndex:a,previewAriaLabel:n}=this.props,{image:l}=this.state,i=b.default.isValidElement(e),s={display:"flex",alignItems:"center",justifyContent:"center"},o={preview:{width:"100%",height:"100%",backgroundImage:l&&!i?`url(${l})`:void 0,backgroundSize:"cover",backgroundPosition:"center",cursor:"pointer",...s},shadow:{background:"radial-gradient(rgb(0, 0, 0, 0.3), rgba(0, 0, 0, 0) 60%)",borderRadius:g,width:g,height:g,position:i?"absolute":void 0,...s},playIcon:{borderStyle:"solid",borderWidth:"16px 0 16px 26px",borderColor:"transparent transparent transparent white",marginLeft:"7px"}},p=b.default.createElement("div",{style:o.shadow,className:"react-player__shadow"},b.default.createElement("div",{style:o.playIcon,className:"react-player__play-icon"}));return b.default.createElement("div",{style:o.preview,className:"react-player__preview",onClick:t,tabIndex:a,onKeyPress:this.handleKeyPress,...n?{"aria-label":n}:{}},i?e:null,r||p)}}}}]);