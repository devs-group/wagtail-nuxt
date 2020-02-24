<template>
  <div class="bg-custom-turquoise min-h-screen">
    <div class="bg-black pt-32 pb-12">
      <div class="ml-4">
        <h1 class="text-white text-3xl font-moret">
          {{ $t('location.your_choice') }}
        </h1>
        <p class="font-signo text-sm font-hairline text-white mt-8">
          {{ interest.name }}
        </p>
      </div>
    </div>
    <div>
      <div v-if="!interest.ProfileInterestRelationshipFk.length" class="p-4">
        <p class="text-white text-sm">{{ $t('interest.no_matches') }}</p>
      </div>
      <div
        v-else
        v-for="profileRel in interest.ProfileInterestRelationshipFk"
        :key="profileRel.id"
      >
        <div class="flex flex-col items-center">
          <div
            class="flex flex-row justify-center items-center w-full max-w-md"
          >
            <nuxt-link
              :to="localePath(`/profile/${profileRel.ProfilePageFk.id}`)"
              class="w-40 h-40 flex-shrink-0 border border-transparent relative cursor-pointer"
              tag="div"
            >
              <img
                v-if="getFirstProfileImage(profileRel.ProfilePageFk)"
                :src="getFirstProfileImage(profileRel.ProfilePageFk)"
                class="w-full h-full outline-border object-cover object-center"
              />
              <div v-else class="w-full h-full outline-border"></div>
            </nuxt-link>
            <div class="text-white flex-1">
              <div class="text-center p-5">
                <p class="font-moret text-sm tracking-widest italic font-bold">
                  <nuxt-link
                    :to="localePath(`/profile/${profileRel.ProfilePageFk.id}`)"
                    class="cursor-pointer"
                    tag="p"
                  >
                    {{ profileRel.ProfilePageFk.prename }}
                    {{ profileRel.ProfilePageFk.surname }}
                  </nuxt-link>
                </p>
                <p class="font-signo text-xxs">
                  {{ profileRel.ProfilePageFk.job }}
                  {{
                    profileRel.ProfilePageFk.age
                      ? `, ${profileRel.ProfilePageFk.age}`
                      : ''
                  }}
                </p>
                <div class="flex flex-row flex-wrap justify-center">
                  <span
                    v-for="interestRel in profileRel.ProfilePageFk
                      .ProfileInterestRelationshipFk"
                    :key="interestRel.id"
                    class="text-xxs block font-signo ml-1"
                    >#{{ interestRel.InterestFk.name }}</span
                  >
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import gql from 'graphql-tag'
import { pageTitle } from '@/utils'

export default {
  head() {
    return {
      title: pageTitle(this.interest.name)
    }
  },
  async asyncData({ params, app }) {
    const client = app.apolloProvider.defaultClient
    const response = await client.query({
      query: gql`
        query getInterest {
          interest(id: ${params.id} ) {
            id
            name
            ProfileInterestRelationshipFk {
              id
              ProfilePageFk {
                id
                prename
                surname
                job
                age
                ProfilePageGalleryImageFk {
                  id
                  image {
                    id
                    rendition(width: 460) {
                      id
                      url
                    }
                  }
                }
                ProfileInterestRelationshipFk {
                  id
                  InterestFk {
                    id
                    name
                  }
                }
              }
            }
          }
        }
      `
    })
    const data = await response.data
    return {
      ...data
    }
  },
  methods: {
    getFirstProfileImage(profile) {
      if (profile.ProfilePageGalleryImageFk.length === 0) {
        return ''
      }
      return profile.ProfilePageGalleryImageFk[0].image.rendition.url
    }
  }
}
</script>

<style lang="scss" scoped>
.outline-border {
  outline: 1px solid white;
}
</style>
