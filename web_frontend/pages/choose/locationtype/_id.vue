<template>
  <div class="bg-custom-green-brightest pt-32 pb-10 min-h-screen relative">
    <div class="flex flex-col font-moret tracking-wider mt-6 text-white px-2">
      <div>
        <h1 class="text-3xl">
          {{ locationType.name }} {{ $t('location.in_zurich') }}
        </h1>
        <h2 class="font-signo tracking-wide text-base">
          {{ $t('location.recommended_by') }}
        </h2>
      </div>

      <div class="mt-12">
        <div
          v-for="locationCategory in getLocationCategories"
          :key="locationCategory.id"
          class="flex flex-col justify-center mt-2"
        >
          <h3
            @click.stop="setOpenedLocationCategory(locationCategory.id)"
            class="text-2xl font-light cursor-pointer"
          >
            {{ locationCategory.name }}
          </h3>
          <div
            v-if="openedLocations.includes(locationCategory.id)"
            class="mt-3 ml-6"
          >
            <div
              v-for="locationParameter in locationCategory.LocationParameterFk"
              :key="locationParameter.id"
              @click.stop="
                setLocationParameter(
                  locationCategory.id,
                  locationParameter.id,
                  locationParameter.name
                )
              "
              class="font-signo text-sm tracking-wider py-1 flex flex-row items-center cursor-pointer"
            >
              <p>{{ locationParameter.name }}</p>
              <p
                :class="{
                  hidden:
                    selectedParameters[locationCategory.id] !==
                    locationParameter.id
                }"
                class="ml-4"
              >
                <b>x</b>
              </p>
            </div>
          </div>
        </div>
      </div>

      <div class="flex justify-center mt-4">
        <button
          @click="submit"
          :class="{ 'shake-animation': hasNoSelections }"
          class="font-signo bg-transparent font-light text-xl tracking-widest mt-4 focus:outline-none border-b border-gray-400"
        >
          {{ $t('location.go') }}
        </button>
      </div>
    </div>
  </div>
</template>
<script>
import gql from 'graphql-tag'

export default {
  data() {
    return {
      openedLocations: [],
      selectedParameters: {},
      selectedChoices: {},
      hasNoSelections: false
    }
  },
  computed: {
    getLocationCategories() {
      return this.locationType.LocationParameterCategoryFk.filter(
        (locationCategory) => locationCategory.LocationParameterFk.length
      )
    }
  },
  async asyncData({ params, app }) {
    const client = app.apolloProvider.defaultClient
    const response = await client.query({
      query: gql`
        query getLocationType {
          locationType(id: ${params.id}) {
            id
            name
            LocationParameterCategoryFk {
              id
              name
              LocationParameterFk {
                id
                name
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
    setOpenedLocationCategory(locationCategoryId) {
      if (this.openedLocations.includes(locationCategoryId)) {
        this.openedLocations = this.openedLocations.filter(
          (id) => id !== locationCategoryId
        )
      } else {
        this.openedLocations.push(locationCategoryId)
      }
    },
    setLocationParameter(
      locationCategoryId,
      locationParameterId,
      locationParameterName
    ) {
      // Delete existing selection so user can deselect parameters.
      if (this.selectedParameters[locationCategoryId] === locationParameterId) {
        delete this.selectedParameters[locationCategoryId]
        delete this.selectedChoices[locationCategoryId]
      } else {
        this.selectedParameters[locationCategoryId] = locationParameterId
        this.selectedChoices[locationCategoryId] = locationParameterName
      }
      this.selectedParameters = Object.assign({}, this.selectedParameters)
      this.selectedChoices = Object.assign({}, this.selectedChoices)
    },
    buildQueryParams() {
      return {
        filter: JSON.stringify(this.selectedParameters),
        locationType: this.$route.params.id,
        choices: Object.values(this.selectedChoices).join(',')
      }
    },
    submit() {
      if (!Object.keys(this.selectedParameters).length) {
        if (!this.hasNoSelections) {
          this.hasNoSelections = true
          setTimeout(() => {
            this.hasNoSelections = false
          }, 1000)
        }
        return
      }
      this.$router.push({
        path: this.localePath('/locations'),
        query: this.buildQueryParams()
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.shake-animation {
  animation: shake 0.82s cubic-bezier(0.36, 0.07, 0.19, 0.97) both;
}
@keyframes shake {
  10%,
  90% {
    transform: translate3d(-1px, 0, 0);
  }

  20%,
  80% {
    transform: translate3d(2px, 0, 0);
  }

  30%,
  50%,
  70% {
    transform: translate3d(-4px, 0, 0);
  }

  40%,
  60% {
    transform: translate3d(4px, 0, 0);
  }
}
</style>
