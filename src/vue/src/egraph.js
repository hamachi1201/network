export default () => {
  return window.egraph.init('https://unpkg.com/egraph@4.0.1-alpha.13/umd/egraph_bg.wasm').then(() => window.egraph)
}
