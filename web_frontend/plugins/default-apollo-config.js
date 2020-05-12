export default function(context) {
  let url = ''
  const isServer = process.server

  if (isServer) {
    url = 'http://cms:8000/'
  } else {
    url = 'http://localhost:8000/'
  }

  url = url + '/api/graphiql'
  return {
    httpEndpoint: url
  }
}
