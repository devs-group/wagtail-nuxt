let loading
export default (isLoading, countModifier, nuxtContext) => {
  loading += countModifier
  console.log(loading)
}
