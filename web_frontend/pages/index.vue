<template>
  <div>
    <span v-html="homePage.body"></span>
    <ul>
      <li v-for="infoCard in infoCards" :key="infoCard.id">
        <nuxt-link :to="localePath(`/entry/${infoCard.id}`)">{{
          infoCard.title
        }}</nuxt-link>
      </li>
    </ul>
  </div>
</template>

<script>
import gql from 'graphql-tag'
// import InfoCard from '@/components/InfoCard'

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
    const infoCardResponse = await client.query({
      query: gql`
        query getInfoCards {
          infoCards {
            id
            title
          }
        }
      `
    })
    const homePageData = await homePageResponse.data
    const infoCardData = await infoCardResponse.data
    return {
      ...homePageData,
      ...infoCardData
    }
  }
}
</script>
