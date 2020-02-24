<template>
  <div class="min-h-screen w-screen bg-custom-gold z-10 shadow-lg">
    <div class="relative pt-32">
      <div
        class="text-white text-center tracking-wider pb-6 flex items-center flex-col"
      >
        <Spinner :show="isLoading" animation="fade-scale"></Spinner>
        <div v-for="genre in getGenresWithInterests" :key="genre.id">
          <h2
            @click="openedGenreId = genre.id"
            class="font-moret text-2xl mb-4 cursor-pointer"
          >
            {{ genre.name }}
          </h2>
          <div v-if="openedGenreId === genre.id" class="my-4">
            <div
              v-for="interest in genre.InterestFk"
              :key="interest.id"
              class="mb-4"
            >
              <p
                @click="gotoInterest(interest.id)"
                class="font-signo text-sm cursor-pointer"
              >
                {{ interest.name }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import gql from 'graphql-tag'
import Spinner from '../../components/shared/spinner'

export default {
  components: { Spinner },
  data() {
    return {
      genres: [],
      isLoading: true,
      openedGenreId: null
    }
  },
  computed: {
    getGenresWithInterests() {
      return this.genres.filter((genre) => genre.InterestFk.length)
    }
  },
  async mounted() {
    this.isLoading = true
    const client = this.$apolloProvider.defaultClient
    const response = await client.query({
      query: gql`
        query getGenres {
          genres {
            id
            name
            InterestFk {
              id
              name
            }
          }
        }
      `
    })
    this.isLoading = false
    const { genres } = await response.data
    this.genres = genres
  },
  methods: {
    gotoInterest(interestId) {
      this.$router.push(this.localePath(`/choose/interest/${interestId}`))
    }
  }
}
</script>
