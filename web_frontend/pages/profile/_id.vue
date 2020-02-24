<template>
  <div
    class="bg-custom-green text-white pt-32 min-h-screen pb-8 tracking-widest"
  >
    <div class="ml-4">
      <div class="font-moret flex text-3xl italic font-bold lg:justify-center">
        <p class="z-10">{{ profile.prename }} {{ profile.surname }}</p>
      </div>
      <div class="font-signo flex tracking-wide text-lg lg:justify-center">
        <p class="z-10">{{ profile.job }}, {{ profile.age }}</p>
      </div>
      <div class="flex flex-row margin-children min-h-40px mt-2">
        <SocialIcon
          v-if="profile.instagram"
          :href="profile.instagram"
          :size="30"
          class="z-10"
          platform="instagram"
        />
        <SocialIcon
          v-if="profile.facebook"
          :href="profile.facebook"
          :size="30"
          class="z-10"
          platform="facebook"
        />
        <SocialIcon
          v-if="profile.twitter"
          :href="profile.twitter"
          :size="30"
          class="z-10"
          platform="twitter"
        />
        <SocialIcon
          v-if="profile.homePage"
          :href="profile.homePage"
          :size="30"
          class="z-10"
          platform="homepage"
        />
      </div>
    </div>

    <div class="-mt-5">
      <div class="flex justify-center items-center">
        <div class="flex justify-center items-center h-56">
          <img
            :src="getFirstProfileImage(profile)"
            :alt="`${profile.prename} ${profile.surname}`"
            class="w-56 h-56 object-cover object-center"
          />
        </div>
      </div>
      <div
        v-if="profile.intro"
        v-html="profile.intro"
        class="font-monotalic text-white px-4 text-sm font-bold -mt-10"
      ></div>
    </div>

    <div class="mt-8 flex flex-col items-center">
      <p
        v-for="subInterest in getProfileSubInterests"
        :key="subInterest.id"
        @click="activeInterest = subInterest"
        :class="{
          'font-bold italic':
            activeInterest && activeInterest.id === subInterest.id
        }"
        class="font-signo border-b w-1/2 max-w-xs mt-3 whitespace-no-wrap cursor-pointer"
      >
        {{ subInterest.name }}
      </p>
    </div>

    <transition name="fade" mode="out-in">
      <div
        v-if="activeInterest"
        :key="activeInterest.id"
        class="inline-flex flex-row flex-wrap w-full items-center justify-center border border-transparent font-light mt-10"
      >
        <div
          v-for="(locationSubinterest,
          n) in activeInterest.locationSubInterestRelation"
          :key="locationSubinterest.id"
          @click.stop="setFlippedLocation(locationSubinterest.id)"
          class="w-40 h-40 max-w-half"
        >
          <transition name="flip-horizontal" mode="out-in">
            <div
              v-if="flippedLocations.includes(locationSubinterest.id)"
              :key="n"
              :class="{
                'bg-custom-green-bright': n % 2 === 0,
                'bg-custom-brown': n % 2 === 1
              }"
              class="h-full flex justify-center items-center overflow-y-scroll overflow-x-hidden text-base py-4 px-2 outline-border relative"
            >
              <div class="self-start flex flex-col">
                <a
                  @click.stop
                  :href="locationSubinterest.LocationFk.homepage"
                  target="_blank"
                  class="font-moret self-center text-sm"
                  >{{ locationSubinterest.LocationFk.name }}</a
                >

                <div
                  v-html="locationSubinterest.description"
                  class="font-signo text-xxxs leading-none mt-2"
                ></div>
              </div>
            </div>
            <div
              v-else
              :style="
                `background-image: url('${getPerProfileLocationGalleryImage(
                  locationSubinterest.LocationFk
                )}')`
              "
              class="h-full flex flex-col text-center items-center justify-center py-4 px-2 outline-border relative self-start bg-cover bg-center bg-no-repeat cursor-pointer overflow-scroll"
            >
              <div
                v-if="
                  getPerProfileLocationGalleryImage(
                    locationSubinterest.LocationFk
                  )
                "
                class="background-dimmer"
              ></div>
              <p class="font-moret text-xl italic font-bold self-center z-10">
                {{ locationSubinterest.LocationFk.name }}
              </p>
            </div>
          </transition>
        </div>
        <div
          v-for="n in activeInterest.locationSubInterestRelation.length %
            colMobile"
          :key="n"
          :data-fill="n"
          class="w-40 h-40 max-w-half"
        ></div>
      </div>
    </transition>

    <div class="mt-10">
      <hr />
      <div
        class="mt-4 px-2 font-signo self-start text-xs mt-2 tracking-wider text-right"
      >
        <p>{{ $t('profile.photocredit') }} Name Surname</p>
      </div>
    </div>
  </div>
</template>
<script>
import gql from 'graphql-tag'
import SocialIcon from '@/components/SocialIcon'
import { pageTitle } from '@/utils'
import DataMixin from '@/mixins/data'

export default {
  components: {
    SocialIcon
  },
  mixins: [DataMixin],
  data() {
    return {
      activeInterest: null,
      flippedLocations: [],
      colMobile: 2
    }
  },
  computed: {
    getProfileSubInterests() {
      return this.profile.ProfileInterestRelationshipFk.map((profileInterest) =>
        profileInterest.InterestFk.InterestSubInterestRelationshipFk.map(
          (interestSubInterest) => interestSubInterest.SubInterestFk
        )
      )
        .flat()
        .filter(
          (subInterest) => subInterest.locationSubInterestRelation.length > 0
        )
    }
  },
  head() {
    return {
      title: pageTitle(`${this.profile.prename} ${this.profile.surname}`)
    }
  },
  async asyncData({ params, app }) {
    const client = app.apolloProvider.defaultClient
    const response = await client.query({
      query: gql`
        query getProfile {
          profile(id: ${params.id}) {
            id
            prename
            surname
            job
            age
            intro
            instagram
            facebook
            twitter
            homePage
            ProfilePageGalleryImageFk {
              id
              randomShape {
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
                InterestSubInterestRelationshipFk {
                  id
                  SubInterestFk {
                    id
                    name
                    longVersion
                    locationSubInterestRelation(profileId: ${params.id}) {
                      id
                      description
                      LocationFk {
                        id
                        name
                        homepage
                        locationImageRelation(profileId: ${params.id}) {
                          id
                          imageFk {
                            id
                            rendition(width: 200) {
                              id
                              url
                            }
                          }
                        }
                      }
                    }
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
    setFlippedLocation(locationId) {
      if (this.flippedLocations.includes(locationId)) {
        this.flippedLocations = this.flippedLocations.filter(
          (id) => id !== locationId
        )
      } else {
        this.flippedLocations.push(locationId)
      }
    },
    getFirstProfileImage(profile) {
      if (profile.ProfilePageGalleryImageFk.length === 0) {
        return ''
      }
      return profile.ProfilePageGalleryImageFk[0].randomShape.rendition.url
    }
  }
}
</script>

<style lang="scss" scoped>
.margin-children {
  div:nth-child(2n) {
    margin-left: 0.75rem;
  }
}
.outline-border {
  outline: 1px solid white;
}
.background-dimmer {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(#00000044 50%, #000000aa);
}
.min-h-40px {
  min-height: 40px;
}
</style>
