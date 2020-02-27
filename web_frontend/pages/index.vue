<template>
  <div>{{ homePage.body }}</div>
</template>

<script>
import gql from 'graphql-tag'

export default {
  components: {},
  data() {
    return {}
  },
  async asyncData({ app }) {
    const client = app.apolloProvider.defaultClient
    const homePageResponse = await client.query({
      query: gql`
        query getHomePage {
          homePage {
            body
          }
        }
      `
    })
    const homePageData = await homePageResponse.data
    return {
      ...homePageData
    }
  }
}
</script>
