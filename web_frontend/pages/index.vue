<template>
  <div>
    <ul>
      <li v-for="infoCard in infoCards" :key="infoCard.id">
        <nuxt-link :to="'/entry/' + infoCard.id">{{
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
    const infoCardData = await infoCardResponse.data
    console.log(infoCardData)
    return { ...infoCardData }
  }
}
</script>
