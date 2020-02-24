export default function(context) {
  let url = ''
  const isServer = process.server
  const isDev = context.isDev

  if (isServer) {
    url = 'http://cms:8000/'
  } else {
    url = isDev
      ? 'http://localhost:8000/'
      : 'https://cms.youmezurich.devs-group.de/'
  }

  const lang = context.app.i18n.locale || context.app.i18n.fallbackLocale
  if (lang) {
    url = `${url}${lang}/api/graphiql`
  } else {
    url = `${url}en/api/graphiql`
  }

  return {
    httpEndpoint: url
  }
}
