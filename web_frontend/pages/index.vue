<template>
  <div>
    <div
      @click.stop="hideLocations"
      class="bg-black pt-32 pb-10 min-h-screen relative"
    >
      <div class="mt-12 text-white pl-6 pr-6 tracking-wider">
        <div v-html="homePage.body" class="font-monotalic text-md"></div>
        <div class="mt-16">
          <nuxt-link
            :to="localePath('/interests')"
            tag="h2"
            class="font-moret cursor-pointer text-xl inline-flex"
          >
            {{ homePage.interestsPrompt }}
            <img class="ml-4" src="@/assets/arrow_forward-24px.svg" />
          </nuxt-link>
        </div>
        <div
          @click.stop="showLocations"
          @mouseover="showLocations"
          @mouseleave="hideLocations"
          class="mt-16 inline-block"
        >
          <div class="flex flex-row">
            <h2 class="font-moret cursor-pointer text-xl">
              {{ homePage.locationsPrompt }}
            </h2>
            <Spinner
              v-if="isLoading"
              :show="true"
              :size="24"
              class="ml-8"
            ></Spinner>
            <img
              v-if="!isLoading"
              :class="{ 'rotate-90-deg': locationsAreVisible }"
              class="ml-4 arrow"
              src="@/assets/arrow_forward-24px.svg"
            />
          </div>
          <div v-if="locationsAreVisible" class="mt-5">
            <nuxt-link
              :key="locationType.id"
              :to="localePath(`/choose/locationType/${locationType.id}`)"
              v-for="locationType in locationTypes"
              class="cursor-pointer mt-2"
              tag="div"
            >
              <span class="font-signo font-weight-100 text-base">
                {{ locationType.name }}
              </span>
            </nuxt-link>
          </div>
        </div>
      </div>
      <div class="absolute bottom-0 right-0 mr-3 mb-20">
        <SocialIcon
          :size="25"
          :href="$t('links.facebook')"
          platform="facebook"
          class="opacity-50 mb-3"
        ></SocialIcon>
        <SocialIcon
          :size="25"
          :href="$t('links.instagram')"
          platform="instagram"
          class="opacity-50"
        ></SocialIcon>
      </div>
      <div class="absolute bottom-0 right-0 mr-3 mb-4 text-white">
        <nuxt-link
          :to="localePath('/contact')"
          class="text-xs italic opacity-75 cursor-pointer"
          tag="p"
          >{{ $t('home.contact_us') }}</nuxt-link
        >
      </div>
    </div>
    <div id="locals" class="bg-custom-brown text-center pt-12">
      <h2 class="font-monotalic">{{ $t('home.living_in_zurich') }}</h2>
      <p class="font-moret">{{ $t('home.locals_will_inspire') }}</p>
      <div class="mt-12 relative">
        <div v-for="profile in profiles" :key="profile.id">
          <nuxt-link
            :to="localePath(`/profile/${profile.id}`)"
            tag="p"
            class="text-white cursor-pointer font-moret font-sstyle-italic font-bold italic text-1xl my-8"
          >
            {{ profile.prename }} {{ profile.surname }}
          </nuxt-link>
        </div>
        <div class="flex my-8 justify-center">
          <img class="rotate-90-deg" src="@/assets/arrow_forward-24px.svg" />
        </div>
        <div class="absolute bottom-0 right-0 mr-3">
          <SocialIcon
            :size="25"
            :href="$t('links.facebook')"
            platform="facebook"
            class="opacity-50 mb-3"
          ></SocialIcon>
          <SocialIcon
            :size="25"
            :href="$t('links.instagram')"
            platform="instagram"
            class="opacity-50"
          ></SocialIcon>
        </div>
      </div>
      <div class="p-12 flex justify-center items-center border-t border-white">
        <p class="text-white text-xs tracking-wide">
          {{ $t('home.curious') }}
          <nuxt-link
            :to="localePath('/inspiration')"
            class="cursor-pointer"
            tag="u"
            >{{ $t('home.more') }}</nuxt-link
          >.
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import gql from 'graphql-tag'
import SocialIcon from '@/components/SocialIcon/index'
import Spinner from '@/components/shared/spinner'

export default {
  components: {
    Spinner,
    SocialIcon
  },
  data() {
    return {
      isLoading: false,
      locationTypes: [],
      locationsAreVisible: false
    }
  },
  async asyncData({ app }) {
    const client = app.apolloProvider.defaultClient
    const homePageResponse = await client.query({
      query: gql`
        query getHomePage {
          homePage {
            body
            interestsPrompt
            locationsPrompt
          }
        }
      `
    })

    const profilesResponse = await client.query({
      query: gql`
        query getProfiles {
          profiles {
            id
            prename
            surname
            job
            age
            ProfileInterestRelationshipFk {
              InterestFk {
                name
              }
            }
          }
        }
      `
    })

    const profilesData = await profilesResponse.data
    const homePageData = await homePageResponse.data
    return {
      ...homePageData,
      ...profilesData
    }
  },
  methods: {
    async showLocations() {
      this.isLoading = true
      const client = this.$apolloProvider.defaultClient
      const response = await client.query({
        query: gql`
          query {
            locationTypes {
              id
              name
            }
          }
        `
      })
      this.isLoading = false
      const { locationTypes } = await response.data
      this.locationTypes = locationTypes
      this.locationsAreVisible = true
    },
    hideLocations() {
      this.locationsAreVisible = false
    }
  }
}
</script>
<style scoped>
.arrow {
  transform: rotate3d(0, 0, 1, 0deg);
  transition: all 0.35s ease-out;
}
.rotate-90-deg {
  transform: rotate3d(0, 0, 1, 90deg);
}
</style>
