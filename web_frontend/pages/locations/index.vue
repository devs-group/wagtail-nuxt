<template>
  <div class="bg-custom-turquoise text-white tracking-wider min-h-screen">
    <div class="bg-black pt-32 pb-12">
      <div class="ml-4">
        <h1 class="font-moret text-3xl">{{ $t('location.your_choice') }}</h1>
        <div class="font-signo text-md font-hairline text-white mt-6">
          <p v-for="choice in choicesArray">{{ choice }}</p>
        </div>
      </div>
    </div>
    <div class="flex flex-col items-center">
      <div
        class="flex-grid-container flex flex-row flex-wrap w-full max-w-md border border-transparent
        font-light justify-center last-bottom-border items-center"
      >
        <div
          v-for="location in locations"
          :key="location.id"
          @click.stop="setFlippedLocation(location.id)"
          class="w-1/2 max-w-full h-40"
        >
          <transition name="flip-horizontal" mode="out-in">
            <div
              v-if="flippedLocations.includes(location.id)"
              :key="location.id"
              :class="{
                'bg-custom-green-bright': location.id % 2 === 0,
                'bg-custom-brown': location.id % 2 === 1
              }"
              class="h-full flex justify-center items-center text-base py-4 px-2 outline-border relative"
            >
              <div class="overflow-ellipsis self-start flex flex-col">
                <a
                  @click.stop
                  :href="location.homepage"
                  target="_blank"
                  class="font-moret self-center"
                  >{{ location.name }}</a
                >

                <div
                  v-if="flippedLocations.includes(location.id)"
                  class="overflow-ellipsis font-signo text-xxxs mt-2"
                >
                  <div class="flex flex-row items-center">
                    <img class="h-2" src="@/assets/icons/location.svg" alt="" />
                    <span v-html="location.address" class="ml-1"></span>
                  </div>
                  <p>
                    Closes today at
                    {{ openUntil(location) }}
                  </p>
                  <div class="flex">
                    <span
                      v-for="locationType in location.LocationTypeFk
                        .LocationParameterCategoryFk"
                      :key="locationType.id"
                    >
                      {{ locationType.name }}
                    </span>
                  </div>
                </div>

                <div
                  v-if="flippedLocations.includes(location.id)"
                  class="font-signo text-xxxs mt-2"
                >
                  <nuxt-link
                    @click.stop
                    :to="
                      'profile/' +
                        location.LocationSubInterestRelationshipFk[0]
                          .ProfilePageFk.id
                    "
                    class="overflow-ellipsis"
                  >
                    <p>
                      Recommended by:
                    </p>
                    <p>
                      {{
                        location.LocationSubInterestRelationshipFk[0]
                          .ProfilePageFk.prename
                      }}
                      {{
                        location.LocationSubInterestRelationshipFk[0]
                          .ProfilePageFk.surname
                      }}
                    </p>
                  </nuxt-link>
                </div>
              </div>
            </div>
            <div
              v-else
              :style="
                `background-image: url('${getFirstLocationGalleryImage(
                  location
                )}')`
              "
              class="h-full flex text-base py-4 px-2 outline-border relative
              overflow-ellipsis self-start flex flex-col bg-cover bg-center bg-no-repeat cursor-pointer"
            >
              <div v-if="location.id % 3 === 0" class="background-dimmer"></div>
              <p class="font-moret self-center underline z-10">
                {{ location.name }}
              </p>
            </div>
          </transition>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import gql from 'graphql-tag'
import { getCurrentDayString } from '@/utils'
import DataMixin from '@/mixins/data'

export default {
  name: 'Locations',
  mixins: [DataMixin],
  data() {
    return { flippedLocations: [] }
  },
  computed: {
    openUntil() {
      return (location) =>
        location[this.untilKey] && location[this.untilKey].slice(0, -3)
    }
  },
  async asyncData({ app, query }) {
    const { filter, locationType, choices } = query
    const filterString = JSON.stringify(filter)
    const choicesArray = choices.split(',')
    const client = app.apolloProvider.defaultClient
    const currentDayString = getCurrentDayString()
    // We create the key for the query dynamically to get the current day time.
    const untilKey = currentDayString + 'Until'

    const response = await client.query({
      query: gql`
        query getLocations {
          locations(locationType: ${locationType}, filter: ${filterString}) {
            id
            name
            address
            LocationGalleryImageFk {
              imageFk {
                rendition(width: 300) {
                  url
                }
              }
            }
            ${untilKey},
            LocationTypeFk {
              id,
              name,
              LocationParameterCategoryFk {
                id,
                name
              }
            },
            LocationSubInterestRelationshipFk {
              ProfilePageFk {
                id,
                prename,
                surname
              },
            }
          }
        }
      `
    })
    const data = await response.data
    return {
      ...data,
      untilKey,
      choicesArray,
      choosenLocationParametersIds: Object.values(JSON.parse(filter))
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
    }
  }
}
</script>

<style lang="scss" scoped>
.outline-border {
  outline: 1px solid white;
}
.flex-grid-container {
  &:after {
    content: '';
    flex: auto;
  }
}
.background-dimmer {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(#00000044 50%, #000000aa);
}
.overflow-ellipsis {
  white-space: nowrap;
  overflow-x: hidden;
  p {
    overflow-x: hidden;
    text-overflow: ellipsis;
  }
}
</style>
