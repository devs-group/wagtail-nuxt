<template>
  <div>
    <InfoCard
      :title="infoCard.title"
      :src="infoCard.image"
      :info="infoCard.info"
    ></InfoCard>
  </div>
</template>
<script>
import gql from 'graphql-tag'
import InfoCard from '@/components/InfoCard'

export default {
  components: {
    InfoCard
  },
  data() {
    return {
      selection: {}
    }
  },
  async asyncData({ params, app }) {
    const client = app.apolloProvider.defaultClient
    const response = await client.query({
      query: gql`
        query getInfoCard {
          infoCard(id: ${params.id}) {
            id
            title
            info
            image(width: 200)
          }
        }
      `
    })
    const data = await response.data
    return {
      ...data
    }
  }
}
</script>
